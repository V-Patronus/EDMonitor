import sys
import logging
import traceback
import faulthandler
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QGraphicsOpacityEffect, QGridLayout, QSplashScreen, QLabel, QFileDialog
import re
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QSize, QTimer, QThread, Signal, QCoreApplication, QObject, Slot, QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
import os
import sqlite3
from datetime import datetime
from ui.ui_mainwindow import Ui_MainWindow
from workers.backup_manager import BackupManager
from widgets.CalculatorWidget import CalculatorWidget
from widgets.CreateEditCardWidget import CreateEditCardWidget
from widgets.CardWidget import CardWidget
from widgets.FlowLayout import FlowLayout
from widgets.gageBoard import TableroGageWidget
from workers.DatabaseWorker import DatabaseWorker
from widgets.circular_splash import CircularSplash
from widgets.CustomMessageBox import CustomMessageBox

# default logging level: enable debug logs for troubleshooting startup
logging.basicConfig(level=logging.DEBUG)

# Ensure uncaught exceptions are printed to console for debugging
def _excepthook(type, value, tb):
    print("UNCAUGHT EXCEPTION:")
    traceback.print_exception(type, value, tb)

sys.excepthook = _excepthook

# Enable faulthandler to print C-level tracebacks on crashes
try:
    faulthandler.enable(all_threads=True)
except Exception:
    pass

class MyMainWindow(QMainWindow, Ui_MainWindow):
    initial_load_complete = Signal()
    splash_progress = Signal(int, str)

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        # Initialize UI normally. We removed the runtime proxies for
        # `QLabel.setText`/`QPushButton.setText` because the project will
        # not use enriched/HTML labels and these proxies interfered with
        # styles on some pages.
        try:
            self.setupUi(self)
        except Exception:
            # If setup fails, re-raise after logging the traceback for debugging.
            traceback.print_exc()
            raise
        # No aliasing: use `leCards_1` for cards and `lePartes_2` for partes
        # --- Asynchronous Database Setup (deferred start) ---
        # We prepare worker/thread and connect signals here but DO NOT start the thread yet.
        self.loading_status = {
            "ui": True,
            "cards": False,
            "parts": False
        }

        self.db_thread = QThread()
        self.db_worker = DatabaseWorker()
        self.db_worker.moveToThread(self.db_thread)

        # Setup Backup Manager in its own thread to keep logic out of main.py
        self.backup_thread = QThread()
        self.backup_manager = BackupManager()
        self.backup_manager.moveToThread(self.backup_thread)
        # Connect backup signals
        self.backup_manager.finished.connect(lambda ok, msg: self.append_log(msg, level="success" if ok else "error"))
        self.backup_manager.progress.connect(lambda p, msg: self.append_log(msg, level="info"))
        self.backup_manager.paths_loaded.connect(self._on_backup_paths_loaded)
        
        # Trigger path loading as soon as the thread starts
        self.backup_thread.started.connect(self.backup_manager.load_paths)
        self.backup_thread.start()

        

        # Connect Worker Signals to Main Slots (ready even if thread not started)
        self.db_worker.cards_loaded.connect(self.display_cards)
        self.db_worker.card_added.connect(self.on_card_saved_async)
        self.db_worker.card_updated.connect(self.on_card_saved_async)
        self.db_worker.card_deleted.connect(self.on_card_deleted_async)
        self.db_worker.error_occurred.connect(self.on_db_error)

        # Note: actual thread start and invoking of loading will be triggered
        # by `start_initial_load()` after the splash is connected.
        # ------------------------------------------------------
        self.setup_custom_widgets()
        
        # Initial flags
        self.first_load_cards = True

    def start_initial_load(self):
        """Start threads and initial loading after splash connections are in place."""
        # Update splash to initial state
        try:
            import threading
            logging.getLogger(__name__).debug("start_initial_load START (thread=%s)", threading.get_ident())
        except Exception:
            pass

        self.splash_progress.emit(10, "Iniciando aplicación...")

        # Start DB thread and request load in that thread via queued connection
        if not self.db_thread.isRunning():
            try:
                logging.getLogger(__name__).debug("starting db_thread")
            except Exception:
                pass
            # connect thread start to optional initialization if needed
            # but here we directly start and invoke load_cards in queued connection
            self.db_thread.start()

        from PySide6.QtCore import QMetaObject, Q_ARG, Qt as _Qt
        try:
            QMetaObject.invokeMethod(self.db_worker, "load_cards", _Qt.QueuedConnection)
            logging.getLogger(__name__).debug("invoked db_worker.load_cards via QueuedConnection")
        except Exception as e:
            logging.getLogger(__name__).debug("error invoking load_cards: %s", e)

        self.splash_progress.emit(40, "Cargando Tarjetas...")

    def check_loading_complete(self):
        """Checks if all components are loaded and updates splash."""
        progress = 40
        if self.loading_status["cards"]:
            progress += 30
        if self.loading_status["parts"]:
            progress += 30
            
        current_msg = "Cargando..."
        if not self.loading_status["cards"]:
            current_msg = "Cargando Tarjetas..."
        elif not self.loading_status["parts"]:
            current_msg = "Cargando Partes..."
        else:
             current_msg = "Finalizando..."
             
        logging.getLogger(__name__).debug("check_loading_complete: status=%s progress=%s msg=%s", self.loading_status, progress, current_msg)
        self.splash_progress.emit(progress, current_msg)

        if self.loading_status["cards"] and self.loading_status["parts"]:
            logging.getLogger(__name__).debug("All components loaded: emitting initial_load_complete")
            self.initial_load_complete.emit()

    def on_cards_loaded_flags(self):
        if self.first_load_cards:
            self.first_load_cards = False
            self.loading_status["cards"] = True
            self.check_loading_complete()

    def on_parts_loaded_flags(self):
        self.loading_status["parts"] = True
        self.check_loading_complete()


    def setup_custom_widgets(self):
        # 1. Calculator Widget
        self.calculator_widget_instance = CalculatorWidget(self.scrollAreaWidgetCalculator)
        if not self.scrollAreaWidgetCalculator.layout():
            self.scrollAreaWidgetCalculator.setLayout(QVBoxLayout())
        self.scrollAreaWidgetCalculator.layout().addWidget(
            self.calculator_widget_instance, 0, Qt.AlignCenter
        )

        # 2. Card Editor Widget
        self.create_card_widget = CreateEditCardWidget(self.AddCardWidget)
        
        # Connect CreateEditCardWidget requests to Worker Slots
        self.create_card_widget.add_card_requested.connect(self.db_worker.add_card)
        self.create_card_widget.update_card_requested.connect(self.db_worker.update_card)
        
        # Backward compatibility for view switching (if needed) or internal logic
        # self.create_card_widget.card_saved.connect(self.on_card_saved) 
        
        if not self.AddCardWidget.layout():
             self.AddCardWidget.setLayout(QVBoxLayout())
        self.AddCardWidget.layout().addWidget(self.create_card_widget)
        
        # Initial State: Hide Editor, Show View
        self.create_card_widget.hide()
        self.AddCardWidget.hide()
        self.ViewCards.show()
        
        # Init Notification Label (Hidden/Transparent) - keep hidden by default
        # Init Notification Label (Hidden/Transparent) - keep hidden by default
        # self.labelNotificacion.hide() # Causing AttributeError, removing as we use Tooltips now

        # Connect "Add Card" button header
        self.btnAddCard.clicked.connect(self.toggle_add_card_mode)

        # 3. Gage Board Widget (PageJapon)
        self.tablero_gage_widget = TableroGageWidget()
        if not self.PageJapon.layout():
            self.PageJapon.setLayout(QVBoxLayout())
        self.PageJapon.layout().addWidget(self.tablero_gage_widget)

        # 4. View Cards Layout (Responsive Flow)
        # Note: We replace the default layout if any, or set a new FlowLayout
        if self.ViewCards.layout():
             pass
        
        self.card_flow_layout = FlowLayout(self.ViewCards, margin=10, hSpacing=15, vSpacing=15)
        self.ViewCards.setLayout(self.card_flow_layout)

        # Fix Stack Backgrounds
        bg_style = "background-color: #0D1017;"
        self.PageHome.setStyleSheet(bg_style)
        self.PageCalculator.setStyleSheet(bg_style)
        self.PageDocuments.setStyleSheet(bg_style)
        self.PageSettings.setStyleSheet(bg_style)
        self.PageJapon.setStyleSheet(bg_style)

        # (Wire EDM UI not added) PageHome keeps its original layout and widgets

        

        # Sidebar Buttons
        buttons_pages = [
            (self.btnHome, self.PageHome),
            (self.btnCalculator, self.PageCalculator),
            (self.btnDocuments, self.PageDocuments),
            (self.BtnAyuda, self.PageSettings),
            (self.btnJapon, self.PageJapon)
        ]

        for btn, page in buttons_pages:
            try:
                btn.toggled.disconnect()
            except Exception:
                pass
            # For the Japan page, start its worker lazily on first click to avoid blocking startup
            try:
                if btn is self.btnJapon:
                    btn.clicked.connect(lambda checked=False, p=page: self._on_btn_japon_clicked(p))
                else:
                    btn.clicked.connect(lambda checked=False, p=page: self.CentralStack.setCurrentWidget(p))
            except Exception:
                btn.clicked.connect(lambda checked=False, p=page: self.CentralStack.setCurrentWidget(p))
            
        self.scrollCalculator.setWidgetResizable(True)
        self.setup_sidebar_animation()
        # Setup backup handlers (buttons in PageSettings -> frameBackup)
        try:
            self.setup_backup_handlers()
        except Exception:
            pass

        # 5. Setup Home Video Playback
        try:
            self.setup_home_video()
        except Exception:
            pass

        # 6. Exit Confirmation
        try:
            self.BtnSalir.clicked.connect(self.confirm_exit)
        except Exception:
            pass

    def toggle_add_card_mode(self):
        """Toggles between View Mode and Create Mode when the header button is clicked."""
        if self.AddCardWidget.isVisible():
            # Currently adding/editing -> Cancel and go back to View
            self.switch_to_view_mode()
        else:
            # Currently viewing -> Open create form
            self.create_card_widget.clear_form()
            self.switch_to_editor_mode(is_edit=False)

    def switch_to_editor_mode(self, is_edit=False):
        """Switches UI to Editor/Create mode with animation."""
        self.btnAddCard.setText("Cancelar")
        
        
        # Show widget logic
        self.create_card_widget.show()
        
        # Animation: Fade Out View, Fade In Editor
        self.animate_transition(self.ViewCards, self.AddCardWidget)

    def switch_to_view_mode(self):
        """Switches UI back to Card List mode with animation."""
        self.btnAddCard.setText("Agregar Tarjeta")
        
        self.create_card_widget.clear_form() # Cleanup
        
        # Animation: Fade Out Editor, Fade In View
        self.animate_transition(self.AddCardWidget, self.ViewCards)

    def animate_transition(self, from_widget, to_widget):
        """Cross-fade animation between two widgets."""
        if from_widget.isVisible() and not to_widget.isVisible():
            # Setup effects
            self._ensure_opacity_effect(from_widget)
            self._ensure_opacity_effect(to_widget)
            
            to_widget.setVisible(True)
            to_widget.setEnabled(True)
            
            group = QParallelAnimationGroup(self)
            
            anim_out = QPropertyAnimation(from_widget.graphicsEffect(), b"opacity")
            anim_out.setDuration(400)
            anim_out.setStartValue(1.0)
            anim_out.setEndValue(0.0)
            
            anim_in = QPropertyAnimation(to_widget.graphicsEffect(), b"opacity")
            anim_in.setDuration(400)
            anim_in.setStartValue(0.0)
            anim_in.setEndValue(1.0)
            
            group.addAnimation(anim_out)
            group.addAnimation(anim_in)
            
            def on_finished():
                from_widget.setVisible(False)
                from_widget.setEnabled(False)
                # Cleanup opacity to avoid interference?
                # from_widget.graphicsEffect().setOpacity(1.0) 
            
            group.finished.connect(on_finished)
            self._transition_anim = group # Keep reference
            group.start()
        else:
            # Fallback if state is weird
            from_widget.setVisible(False)
            to_widget.setVisible(True)

    def display_cards(self, cards):
        """Slot called when worker finishes loading cards."""
        # Batch-create card widgets to avoid blocking the event loop
        try:
            # Clear existing
            while self.card_flow_layout.count():
                item = self.card_flow_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

            self._pending_cards = list(cards)
            self._cards_batch_index = 0
            self._cards_batch_size = max(4, int(len(self._pending_cards) / 10) or 4)
            # start processing batches
            QTimer.singleShot(0, self._process_card_batch)
        except Exception:
            # Fallback: create all at once
            for card_data in cards:
                c_id, name, desc, icon, style, path = card_data
                card = CardWidget(c_id, name, desc, icon, style, path)
                card.delete_requested.connect(self.db_worker.delete_card)
                card.edit_requested.connect(self.open_edit_card)
                self.card_flow_layout.addWidget(card)
            self.on_cards_loaded_flags()

    def _process_card_batch(self):
        # Create next batch of card widgets and schedule next step
        try:
            total = len(self._pending_cards)
            start = self._cards_batch_index
            end = min(total, start + self._cards_batch_size)
            for i in range(start, end):
                c_id, name, desc, icon, style, path = self._pending_cards[i]
                card = CardWidget(c_id, name, desc, icon, style, path)
                card.delete_requested.connect(self.db_worker.delete_card)
                card.edit_requested.connect(self.open_edit_card)
                self.card_flow_layout.addWidget(card)

            self._cards_batch_index = end

            # Update splash progress roughly based on portion loaded
            try:
                percent = 40 + int(50 * (self._cards_batch_index / total))
                self.splash_progress.emit(percent, f"Cargando Tarjetas... ({self._cards_batch_index}/{total})")
            except Exception:
                pass

            if self._cards_batch_index < total:
                QTimer.singleShot(25, self._process_card_batch)
            else:
                # finished
                self._pending_cards = []
                self.on_cards_loaded_flags()
        except Exception:
            self.on_cards_loaded_flags()

    def on_card_saved_async(self, card_id):
        """Called when worker successfully adds or updates a card."""
        # Notify the editor widget to show success and clear
        self.create_card_widget.on_card_saved_success()
        # Reload cards
        from PySide6.QtCore import QMetaObject, Qt as _Qt
        QMetaObject.invokeMethod(self.db_worker, "load_cards", _Qt.QueuedConnection)
        self.switch_to_view_mode()

    def on_card_deleted_async(self, card_id):
        """Called when worker successfully deletes a card."""
        # Reload cards
        from PySide6.QtCore import QMetaObject, Qt as _Qt
        QMetaObject.invokeMethod(self.db_worker, "load_cards", _Qt.QueuedConnection)

    def on_db_error(self, error_message):
        """Handle database errors."""
        # print(f"Database Error: {error_message}")
        # Optionally show a message box here if needed

    def open_edit_card(self, card_id, name, desc, icon, style, path):
        # Switch to Editor Mode
        self.switch_to_editor_mode(is_edit=True)
        # Pre-fill data
        self.create_card_widget.set_card_data(card_id, name, desc, icon, style, path)

    def load_cards(self):
        # Legacy/Refresh wrapper
        from PySide6.QtCore import QMetaObject, Qt as _Qt
        QMetaObject.invokeMethod(self.db_worker, "load_cards", _Qt.QueuedConnection)

    def _ensure_opacity_effect(self, widget):
        if not widget.graphicsEffect():
            effect = QGraphicsOpacityEffect(widget)
            widget.setGraphicsEffect(effect)
        return widget.graphicsEffect()

    def setup_sidebar_animation(self):
        try:
            try:
                expanded = max(150, self.SideBarFrame.sizeHint().width())
            except Exception:
                expanded = 150
            collapsed = 100

            self._sidebar_expanded_width = expanded
            self._sidebar_collapsed_width = collapsed
            self.SideBarFrame.setMaximumWidth(self._sidebar_expanded_width)
            self._sidebar_anim = None
            self._sidebar_button_texts = {}
            self._sidebar_button_icon_sizes = {}

            try:
                self.CegaNicButton.toggled.connect(self._on_sidebar_toggled)
                try:
                    self.CegaNicButton.setChecked(True)
                except Exception:
                    pass
            except Exception:
                pass

            try:
                checked = bool(self.CegaNicButton.isChecked())
                if checked:
                    self.SideBarFrame.setMaximumWidth(self._sidebar_expanded_width)
                else:
                    self.SideBarFrame.setMaximumWidth(self._sidebar_collapsed_width)
            except Exception:
                pass
        except Exception:
            pass

    def _on_sidebar_toggled(self, checked: bool):
        try:
            start = self.SideBarFrame.maximumWidth()
            end = self._sidebar_expanded_width if checked else self._sidebar_collapsed_width

            group = QParallelAnimationGroup(self)

            widthAnim = QPropertyAnimation(self.SideBarFrame, b"maximumWidth")
            widthAnim.setDuration(420)
            widthAnim.setStartValue(start)
            widthAnim.setEndValue(end)
            widthAnim.setEasingCurve(QEasingCurve.InOutCubic)
            group.addAnimation(widthAnim)

            try:
                effect = getattr(self, "_sidebar_opacity_effect", None)
                if effect is None:
                    effect = QGraphicsOpacityEffect(self.SideBarGroup)
                    self.SideBarGroup.setGraphicsEffect(effect)
                    self._sidebar_opacity_effect = effect
            except Exception:
                effect = None

            if effect is not None:
                if checked:
                    opacityAnim = QPropertyAnimation(effect, b"opacity")
                    opacityAnim.setDuration(300)
                    opacityAnim.setStartValue(0.0)
                    opacityAnim.setEndValue(1.0)
                    opacityAnim.setEasingCurve(QEasingCurve.InOutCubic)
                    group.addAnimation(opacityAnim)
                else:
                    try:
                        effect.setOpacity(1.0)
                    except Exception:
                        pass

            self._sidebar_anim = group

            try:
                buttons = self.SideBarGroup.findChildren(QPushButton)
                if not checked:
                    for b in buttons:
                        try:
                            txt = b.text()
                            if txt:
                                self._sidebar_button_texts[b.objectName()] = txt
                                b.setToolTip(txt)
                                b.setText("")
                                b.setStyleSheet("text-align:center;")
                                try:
                                    original = self._sidebar_button_icon_sizes.get(b.objectName(), None)
                                    if original is None:
                                        original = b.iconSize()
                                        self._sidebar_button_icon_sizes[b.objectName()] = original
                                    b.setIconSize(original)
                                except Exception:
                                    pass
                        except Exception:
                            pass
                else:
                    for b in buttons:
                        try:
                            b.setStyleSheet("")
                            try:
                                original = self._sidebar_button_icon_sizes.get(b.objectName(), None)
                                if original is not None:
                                    b.setIconSize(original)
                            except Exception:
                                pass
                        except Exception:
                            pass
            except Exception:
                pass

            def on_finished():
                try:
                    self.SideBarFrame.setMaximumWidth(end)
                except Exception:
                    pass

                try:
                    effect = getattr(self, "_sidebar_opacity_effect", None)
                    if effect is not None:
                        effect.setOpacity(1.0)
                except Exception:
                    pass

                try:
                    if checked:
                        buttons = self.SideBarGroup.findChildren(QPushButton)
                        for b in buttons:
                            try:
                                name = b.objectName()
                                txt = self._sidebar_button_texts.get(name, None)
                                if txt:
                                    b.setText(txt)
                                    b.setToolTip("")
                            except Exception:
                                pass
                except Exception:
                    pass

                try:
                    self._sidebar_anim = None
                except Exception:
                    pass

            group.finished.connect(on_finished)
            group.start()
        except Exception:
            try:
                self.SideBarFrame.setMaximumWidth(self._sidebar_expanded_width if checked else self._sidebar_collapsed_width)
            except Exception:
                pass

    def _on_btn_japon_clicked(self, page):
        """Handler for first click on btnJapon: starts gage worker lazily and shows page."""
        try:
            if not getattr(self, "_japon_started", False):
                self._japon_started = True
                if hasattr(self, "tablero_gage_widget"):
                    try:
                        self.tablero_gage_widget.start_worker()
                    except Exception:
                        pass
        except Exception:
            pass

        try:
            self.CentralStack.setCurrentWidget(page)
        except Exception:
            pass

    def setup_home_video(self):
        """Initializes and starts video playback in mediaPlaceholder frame."""
        try:
            # 0. Setup container styling (rounded dashed borders)
            self.mediaPlaceholder.setStyleSheet("""
                QFrame#mediaPlaceholder {
                    background-color: transparent;
                }
            """)
            
            # 1. Setup Media Components
            self.media_player = QMediaPlayer(self)
            self.video_widget = QVideoWidget()
            self.audio_output = QAudioOutput(self)
            
            # 2. Configure Player
            self.video_widget.setAspectRatioMode(Qt.IgnoreAspectRatio)
            # Remove styling from video widget, keep it clean
            self.video_widget.setStyleSheet("background-color: transparent;")
            
            self.media_player.setVideoOutput(self.video_widget)
            self.media_player.setAudioOutput(self.audio_output)
            self.audio_output.setMuted(True) 
            
            # 3. Handle Looping and Resizing
            def handle_status_change(status):
                if status == QMediaPlayer.MediaStatus.EndOfMedia:
                    self.media_player.setPosition(0)
                    self.media_player.play()
                elif status == QMediaPlayer.MediaStatus.LoadedMedia:
                    # Adjust size to exact resolution from metadata
                    from PySide6.QtMultimedia import QMediaMetaData
                    res = self.media_player.metaData().value(QMediaMetaData.Key.Resolution)
                    if res and not res.isEmpty():
                        target_width = min(540, res.width())
                        target_height = int(res.height() * (target_width / res.width()))
                        self.video_widget.setFixedSize(target_width, target_height)
                        # Placeholder should be slightly larger to show the border if needed
                        # but here we set it to wrap content or match size
                        self.mediaPlaceholder.setMinimumSize(target_width, target_height)
            
            self.media_player.mediaStatusChanged.connect(handle_status_change)
            
            # 4. Integrate into UI (mediaPlaceholder)
            if not self.mediaPlaceholder.layout():
                layout = QVBoxLayout(self.mediaPlaceholder)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setAlignment(Qt.AlignCenter)
            
            self.mediaPlaceholder.layout().addWidget(self.video_widget)
            self.mediaPlaceholder.layout().setAlignment(self.video_widget, Qt.AlignCenter)
            
            # 5. Load and Play
            video_path = os.path.abspath(os.path.join("assets", "video", "edm.mp4"))
            if os.path.exists(video_path):
                self.media_player.setSource(QUrl.fromLocalFile(video_path))
                self.media_player.play()
            else:
                logging.getLogger(__name__).warning("Video file not found: %s", video_path)
                self.mediaPlaceholder.hide()
                
        except Exception as e:
            logging.getLogger(__name__).error("Error setting up video: %s", e)
            try:
                self.mediaPlaceholder.hide()
            except Exception:
                pass
    
    # ---------------- Backup / Export Helpers ----------------
    def setup_backup_handlers(self):
        # Connect buttons from UI (frameBackup) to handlers
        try:
            self.btnBrowseCards_1.clicked.connect(self.on_browse_cards)
        except Exception:
            pass
        try:
            self.btnExcelCards_1.clicked.connect(self.on_export_cards_excel)
        except Exception:
            pass
        # Older/alternate UI may expose *_2 variants; connect them too but keep logic
        try:
            self.btnBrowseCards_2.clicked.connect(self.on_browse_cards)
        except Exception:
            pass
        try:
            self.btnExcelCards_2.clicked.connect(self.on_export_cards_excel)
        except Exception:
            pass
        try:
            self.btnBrowsePartes_2.clicked.connect(self.on_browse_partes)
        except Exception:
            pass
        try:
            self.btnExcelPartes_2.clicked.connect(self.on_export_partes_excel)
        except Exception:
            pass
        try:
            self.btnPDFPartes_2.clicked.connect(self.on_export_partes_pdf)
        except Exception:
            pass

        # Connect the existing clear button named 'limpiarbtn' to clear the log
        try:
            if hasattr(self, 'limpiarbtn'):
                try:
                    self.limpiarbtn.clicked.connect(lambda: self.logOutput.clear())
                except Exception:
                    pass
        except Exception:
            pass

    def _on_backup_paths_loaded(self, paths: dict):
        try:
            cards = paths.get('cards', '')
            partes = paths.get('partes', '')
            if cards:
                try:
                    self.leCards_1.setText(cards)
                except Exception:
                    pass
            if partes:
                try:
                    self.lePartes_2.setText(partes)
                except Exception:
                    pass
            self.append_log('Rutas de backup cargadas.', level='info')
        except Exception:
            pass

    def on_browse_cards(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta para Cards")
        if folder:
            try:
                self.leCards_1.setText(folder)
            except Exception:
                pass
            try:
                # persist via backup manager
                self.backup_manager.set_cards_path.emit(folder)
            except Exception:
                pass

    def on_browse_partes(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta para Partes")
        if folder:
            try:
                self.lePartes_2.setText(folder)
            except Exception:
                pass
            try:
                self.backup_manager.set_partes_path.emit(folder)
            except Exception:
                pass

    def on_export_cards_excel(self):
        outdir = (self.leCards_1.text() or "").strip()
        if not outdir or not os.path.isdir(outdir):
            self.append_log("Ruta inválida para guardar Excel de Cards.", level="error")
            return
        fname = os.path.join(outdir, f"cards_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
        try:
            self.backup_manager.export_cards_requested.emit(fname)
            self.append_log(f"Exportando Cards a: {fname}", level="info")
        except Exception as e:
            self.append_log(str(e), level="error")

    def on_export_partes_excel(self):
        outdir = (self.lePartes_2.text() or "").strip()
        if not outdir or not os.path.isdir(outdir):
            self.append_log("Ruta inválida para guardar Excel de Partes.", level="error")
            return
        fname = os.path.join(outdir, f"partes_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
        try:
            self.backup_manager.export_partes_requested.emit(fname)
            self.append_log(f"Exportando Partes a: {fname}", level="info")
        except Exception as e:
            self.append_log(str(e), level="error")

    def on_export_partes_pdf(self):
        outdir = (self.lePartes_2.text() or "").strip()
        if not outdir or not os.path.isdir(outdir):
            self.append_log("Ruta inválida para generar PDF de Partes.", level="error")
            return
        fname = os.path.join(outdir, "partes_report.pdf")
        try:
            self.backup_manager.export_partes_pdf_requested.emit(fname)
            self.append_log(f"Generando PDF Partes: {fname}", level="info")
        except Exception as e:
            self.append_log(str(e), level="error")

    

    def append_log(self, text, level="info"):
        colors = {"info":"#FFFFFF","success":"#00FF00","error":"#FF3333"}
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color = colors.get(level, "#FFFFFF")
        html = f"<span style='color:{color}'>[{ts}] {text}</span>"
        try:
            self.logOutput.append(html)
            self.logOutput.ensureCursorVisible()
        except Exception:
            pass

    def on_app_quit(self):
        """Cleanup logic before application exits. Called via aboutToQuit signal."""
        try:
            if hasattr(self, 'backup_manager') and self.backup_manager is not None:
                try:
                    self.backup_manager.cancel()
                except Exception:
                    pass
        except Exception:
            pass

    def confirm_exit(self):
        """Shows a confirmation dialog before closing the application."""
        # Just call close(), it will trigger closeEvent
        self.close()

    def closeEvent(self, event):
        """Override close event to show confirmation dialog."""
        if CustomMessageBox.question(self, "Confirmar Salida", "¿Está seguro de que desea salir?"):
            event.accept()
        else:
            event.ignore()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle("Fusion")
    app.setQuitOnLastWindowClosed(False)

    # Circular Splash
    splash = CircularSplash()
    print("[debug] showing splash", flush=True)
    splash.show()
    app.processEvents()
    try:
        window = MyMainWindow()
        print("[debug] created MyMainWindow instance", flush=True)
    except Exception:
        print("[debug] exception while creating MyMainWindow:", flush=True)
        traceback.print_exc()
        raise

    # Connect Window Signals to Splash
    window.splash_progress.connect(splash.set_progress)
    window.initial_load_complete.connect(splash.finish)
    print("[debug] connected splash signals", flush=True)
    
    # Connect Gage Board initial load signal to update splash progress
    if hasattr(window, "tablero_gage_widget"):
        window.tablero_gage_widget.initial_load_complete.connect(window.on_parts_loaded_flags)
    
    # Now start the main window initial load (DB etc.) so splash receives progress
    try:
        print("[debug] starting initial load", flush=True)
        try:
            window.start_initial_load()
        except Exception:
            print("[debug] exception when starting initial load:", flush=True)
            traceback.print_exc()
    except Exception:
        print("[debug] exception when starting initial load:")
        traceback.print_exc()
    
    # Show window when splash finishes (splash.finish emits nothing, so we hook into window.initial_load_complete too)
    
    def on_loaded():
         print("[debug] on_loaded called: showing main window")
         window.show()
         app.setQuitOnLastWindowClosed(True)
       
    window.initial_load_complete.connect(on_loaded)

    # Ensure BackupManager receives a cancel request when the app is quitting
    try:
        app.aboutToQuit.connect(window.on_app_quit)
    except Exception:
        pass

    # Fallback
    def fallback_show():
        if not window.isVisible():
            print("[debug] fallback_show triggered: showing window and closing splash")
            window.show()
            splash.close()
            app.setQuitOnLastWindowClosed(True)

    QTimer.singleShot(8000, fallback_show) # Increased timeout for safety
    
    exit_code = app.exec()
    
    # --- Robust Thread Cleanup ---
    def cleanup_thread(thread):
        if thread and thread.isRunning():
            thread.quit()
            thread.wait()

    # Clean up Main DB Thread
    if hasattr(window, 'db_thread'):
        cleanup_thread(window.db_thread)
    
    # Clean up Backup Manager Thread
    if hasattr(window, 'backup_thread'):
        cleanup_thread(window.backup_thread)

    # Clean up Gage Board Thread
    if hasattr(window, 'tablero_gage_widget') and hasattr(window.tablero_gage_widget, 'worker_thread'):
        cleanup_thread(window.tablero_gage_widget.worker_thread)

    sys.exit(exit_code)
