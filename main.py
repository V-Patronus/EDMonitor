import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QGraphicsOpacityEffect, QGridLayout
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QSize, QTimer, QThread
from ui.ui_mainwindow import Ui_MainWindow
from widgets.CalculatorWidget import CalculatorWidget
from widgets.CreateEditCardWidget import CreateEditCardWidget
from widgets.CardWidget import CardWidget
from widgets.FlowLayout import FlowLayout
from workers.DatabaseWorker import DatabaseWorker

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # --- Asynchronous Database Setup ---
        self.db_thread = QThread()
        self.db_worker = DatabaseWorker()
        self.db_worker.moveToThread(self.db_thread)
        
        # Connect Worker Signals to Main Slots
        self.db_worker.cards_loaded.connect(self.display_cards)
        self.db_worker.card_added.connect(self.on_card_saved_async)
        self.db_worker.card_updated.connect(self.on_card_saved_async)
        self.db_worker.card_deleted.connect(self.on_card_deleted_async)
        self.db_worker.error_occurred.connect(self.on_db_error)
        
        # Start Thread
        self.db_thread.start()
        # -----------------------------------

        self.setup_custom_widgets()
        
        # Initial Load via Worker
        self.db_worker.load_cards()

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

        # 3. View Cards Layout (Responsive Flow)
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
            btn.clicked.connect(lambda checked=False, p=page: self.CentralStack.setCurrentWidget(p))
            
        self.scrollCalculator.setWidgetResizable(True)
        self.setup_sidebar_animation()

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
        # Clear existing
        while self.card_flow_layout.count():
            item = self.card_flow_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for card_data in cards:
            c_id, name, desc, icon, style, path = card_data
            
            # Create Card Widget
            card = CardWidget(c_id, name, desc, icon, style, path)
            
            # Connect Delete Signal directly to Worker
            card.delete_requested.connect(self.db_worker.delete_card)
            
            # Connect Edit Signal
            card.edit_requested.connect(self.open_edit_card)
            
            self.card_flow_layout.addWidget(card)

    def on_card_saved_async(self, card_id):
        """Called when worker successfully adds or updates a card."""
        # Notify the editor widget to show success and clear
        self.create_card_widget.on_card_saved_success()
        # Reload cards
        self.db_worker.load_cards()
        self.switch_to_view_mode()

    def on_card_deleted_async(self, card_id):
        """Called when worker successfully deletes a card."""
        # Reload cards
        self.db_worker.load_cards()

    def on_db_error(self, error_message):
        """Handle database errors."""
        print(f"Database Error: {error_message}")
        # Optionally show a message box here if needed

    def open_edit_card(self, card_id, name, desc, icon, style, path):
        # Switch to Editor Mode
        self.switch_to_editor_mode(is_edit=True)
        # Pre-fill data
        self.create_card_widget.set_card_data(card_id, name, desc, icon, style, path)

    def load_cards(self):
        # Legacy/Refresh wrapper
        self.db_worker.load_cards()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    
    exit_code = app.exec()
    
    # Clean up thread
    if hasattr(window, 'db_thread') and window.db_thread.isRunning():
        window.db_thread.quit()
        window.db_thread.wait()
        
    sys.exit(exit_code)
