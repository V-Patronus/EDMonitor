# main.py
from PySide6.QtWidgets import (
    QApplication, QWidget, QGroupBox, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QLineEdit, QSpinBox,
    QDialog, QDialogButtonBox, QFormLayout, QSizePolicy,
    QMessageBox
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from ui.ui_tablerogage import Ui_TableroGageWidget
from PySide6.QtCore import QThread, Signal, Slot
from ui.ui_tablerogage import Ui_TableroGageWidget
from workers.PartesWorker import PartesWorker
import sys


class ParteDialog(QDialog):
    def __init__(self, parent=None, parte="", tipo="", fila=1, columna=1):
        super().__init__(parent)
        self.setWindowTitle("Editar Parte" if parte else "Añadir Parte")

        self.parte_edit = QLineEdit(parte)
        self.tipo_edit = QLineEdit(tipo)
        self.fila_spin = QSpinBox()
        self.fila_spin.setRange(1, 5)
        self.fila_spin.setValue(fila)
        self.col_spin = QSpinBox()
        self.col_spin.setRange(1, 6)
        self.col_spin.setValue(columna)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        form = QFormLayout()
        form.addRow("Número de parte:", self.parte_edit)
        form.addRow("Tipo:", self.tipo_edit)
        form.addRow("Fila:", self.fila_spin)
        form.addRow("Columna:", self.col_spin)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.buttons)

    def values(self):
        return (
            self.parte_edit.text().strip(),
            self.tipo_edit.text().strip(),
            self.fila_spin.value(),
            self.col_spin.value()
        )


class TableroGageWidget(QWidget):
    initial_load_complete = Signal()

    def __init__(self, db_path="database/partes.db"):
        super().__init__()
        self.ui = Ui_TableroGageWidget()
        self.ui.setupUi(self)

        self.gridLayout = self.ui.gridLayout
        self.searchInput = self.ui.searchInput
        self.searchButton = self.ui.searchButton
        self.addButton = self.ui.addButton
        self.restoreButton = self.ui.restoreButton
        self.totalPartes = self.ui.totalPartes

        self.matriz = {}
        self.group_map = {}
        self.label_map = {}
        self.row_map = {}
        self.original_border = {}

        # Defer heavy grid initialization until start_worker() is called
        # (this allows the splash to show and animations to run)

        # --- Async Worker Setup (deferred start) ---
        self.worker_thread = QThread()
        self._first_load_parts = True # Track first load
        self.worker = PartesWorker(db_path)
        self.worker.moveToThread(self.worker_thread)

        # Connect Main -> Worker Signals (Slots) and thread start initialization
        self.worker_thread.started.connect(self.worker.init_db)

        # Connect Worker -> Main Signals
        self.worker.db_ready.connect(self.worker.load_parts) # Load parts once DB ready
        self.worker.parts_loaded.connect(self.on_parts_loaded)
        self.worker.part_added.connect(self.on_part_added)
        self.worker.part_updated.connect(self.on_part_updated)
        self.worker.part_deleted.connect(self.on_part_deleted)
        self.worker.search_results.connect(self.on_search_results)
        self.worker.error_occurred.connect(self.on_worker_error)

        # NOTE: do NOT start the thread here. Call start_worker() when ready so
        # callers can connect signals before the worker emits.
        # --------------------------

    def start_worker(self):
        """Start the partes worker thread. Call after external signal connections."""
        from PySide6.QtCore import QTimer
        import logging
        _logger = logging.getLogger(__name__)

        # Schedule grid initialization on next event loop turn so spinner can start
        QTimer.singleShot(0, self.initGrid)

        # Start the worker thread shortly after grid is built
        def _start_thread():
            try:
                if not self.worker_thread.isRunning():
                    _logger.debug("TableroGageWidget starting worker_thread")
                    self.worker_thread.start()
            except Exception as e:
                _logger.debug("TableroGageWidget error starting thread: %s", e)

        QTimer.singleShot(60, _start_thread)

        self.searchButton.clicked.connect(self.buscarParte)
        self.addButton.clicked.connect(self.agregarParte)
        self.restoreButton.clicked.connect(self.restaurarEstilos)
        self.searchInput.returnPressed.connect(self.buscarParte)
        
    def closeEvent(self, event):
        # Cleanup thread
        if self.worker_thread.isRunning():
            self.worker_thread.quit()
            self.worker_thread.wait()
        super().closeEvent(event)

    def initGrid(self):
        for i in range(1, 6):
            for j in range(1, 7):
                key = f"{i}-{j}"
                group = QGroupBox(f"({i}, {j})")
                group.setFixedSize(460, 300)

                scroll = QScrollArea()
                scroll.setWidgetResizable(True)
                inner = QWidget()
                layout = QVBoxLayout(inner)
                layout.setAlignment(Qt.AlignTop)
                scroll.setWidget(inner)

                vbox = QVBoxLayout(group)
                vbox.addWidget(scroll)

                self.matriz[key] = layout
                self.group_map[key] = group
                self.original_border[group] = group.styleSheet()

                self.gridLayout.addWidget(group, i - 1, j - 1)

    def limpiarGrid(self):
        for layout in self.matriz.values():
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                elif child.layout():
                    self.clearLayout(child.layout())
        self.label_map.clear()
        self.row_map.clear()

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clearLayout(child.layout())

    # --- Slots for Worker Responses ---
    
    def on_parts_loaded(self, parts):
        # Clear existing and prepare batch processing to keep UI responsive
        self.limpiarGrid()
        try:
            import logging
            logging.getLogger(__name__).debug("TableroGageWidget.on_parts_loaded called; total=%d", len(parts))
            total = len(parts)
            # show total early
            try:
                self.totalPartes.setText(f"Total de partes: {total}")
            except Exception:
                pass

            # prepare pending list for batch processing
            self._pending_parts = list(parts)
            self._parts_batch_index = 0
            self._parts_batch_size = max(4, int(total / 10) or 4)
            from PySide6.QtCore import QTimer
            QTimer.singleShot(0, self._process_parts_batch)
        except Exception:
            # fallback: immediate insertion
            total = 0
            for tipo, parte, i, j in parts:
                self.addParteToCell(parte, tipo, i, j)
                total += 1
            try:
                self.totalPartes.setText(str(total))
            except Exception:
                pass

                if self._first_load_parts:
                    self._first_load_parts = False
                    logging.getLogger(__name__).debug("TableroGageWidget initial load complete: emitting initial_load_complete")
                    self.initial_load_complete.emit()

    def on_part_added(self, parte, tipo, i, j):
        # Restore styles and clear search input immediately
        try:
            self.restaurarEstilos()
        except Exception:
            pass
        try:
            self.searchInput.clear()
        except Exception:
            pass

        # If we are batch-processing parts, append to pending to keep order
        if getattr(self, "_pending_parts", None) is not None and getattr(self, "_parts_batch_index", 0) < len(self._pending_parts):
            # simply append so it will appear in next batches
            try:
                self._pending_parts.append((tipo, parte, i, j))
            except Exception:
                # fallback immediate
                self.addParteToCell(parte, tipo, i, j)
        else:
            self.addParteToCell(parte, tipo, i, j)

        # increment total
        try:
            cur = int(self.totalPartes.text() or "0")
            self.totalPartes.setText(str(cur + 1))
        except Exception:
            pass
        
    def on_part_updated(self, old_parte, new_parte, new_tipo, new_i, new_j):
        if old_parte in self.row_map:
            row = self.row_map[old_parte]
            self.clearLayout(row)
            row.deleteLater()
            del self.row_map[old_parte]
            del self.label_map[old_parte]
        # After update, restore styles and clear search input
        try:
            self.restaurarEstilos()
        except Exception:
            pass
        try:
            self.searchInput.clear()
        except Exception:
            pass

        self.addParteToCell(new_parte, new_tipo, new_i, new_j)
        
    def on_part_deleted(self, parte):
        if parte in self.row_map:
            row = self.row_map[parte]
            self.clearLayout(row)
            row.deleteLater()
            del self.row_map[parte]
            del self.label_map[parte]
        # After deletion update total and restore styles + clear search
        try:
            cur = int(self.totalPartes.text() or "0")
            self.totalPartes.setText(str(max(0, cur - 1)))
        except Exception:
            pass
        try:
            self.restaurarEstilos()
        except Exception:
            pass
        try:
            self.searchInput.clear()
        except Exception:
            pass

        # If batching is active, nothing else to do; if not, ensure consistent state
        try:
            if getattr(self, "_pending_parts", None) is not None:
                # remove from pending if exists
                try:
                    self._pending_parts = [p for p in self._pending_parts if p[1] != parte]
                except Exception:
                    pass
        except Exception:
            pass
            
    def on_search_results(self, results):
        # First restore styles
        self.restaurarEstilosSinLimpiarTexto()
        
        if not results:
            return

        for tipo, parte, i, j in results:
            label = self.label_map.get(parte)
            group = self.group_map.get(f"{i}-{j}")
            if label and group:
                label.setStyleSheet("""
                    QLabel {
                        background-color: #22c55e;
                        color: white;
                        border-radius: 10px;
                        padding: 10px;
                        font-size: 13px;
                        font-weight: bold;
                    }
                """)
                group.setStyleSheet(self.original_border[group] + """
                    QGroupBox {
                        border: 3px solid #22c55e;
                        border-radius: 8px;
                    }
                """)

    def _process_parts_batch(self):
        try:
            total = len(self._pending_parts)
            start = self._parts_batch_index
            end = min(total, start + self._parts_batch_size)
            for i in range(start, end):
                tipo, parte, ii, jj = self._pending_parts[i]
                self.addParteToCell(parte, tipo, ii, jj)

            self._parts_batch_index = end

            # update partial UI (no need to update totalPartes here, it's set early)
            if self._parts_batch_index < total:
                from PySide6.QtCore import QTimer
                QTimer.singleShot(30, self._process_parts_batch)
            else:
                # finished
                self._pending_parts = []
                if self._first_load_parts:
                    self._first_load_parts = False
                    self.initial_load_complete.emit()
        except Exception:
            # fallback to signal completion
            try:
                if self._first_load_parts:
                    self._first_load_parts = False
                    self.initial_load_complete.emit()
            except Exception:
                pass

    def on_worker_error(self, message):
         QMessageBox.warning(self, "Error", message)

    def cargarTodo(self):
        # Triggered by worker.db_ready typically, or manual refresh
        self.worker.load_parts()

    def addParteToCell(self, parte, tipo, i, j):
        key = f"{i}-{j}"
        layout = self.matriz.get(key)
        if not layout:
            return

        row = QHBoxLayout()
        row.setAlignment(Qt.AlignLeft)
        row.setSpacing(10)

        btn_edit = QPushButton()
        btn_edit.setFixedSize(32, 32)
        btn_edit.setIcon(QIcon(":/iconos/iconos/edit.svg"))
        btn_edit.setIconSize(QSize(15, 15))
        btn_edit.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: 2px solid #4a5568;
                border-radius: 8px;
                padding: 4px;
            }
            QPushButton:hover {
                background: rgba(0, 255, 255, 60);
                border: 2px solid #00ffff;
            }
            QPushButton:pressed {
                background: rgba(0, 255, 255, 100);
            }
        """)

        btn_del = QPushButton()
        btn_del.setFixedSize(32, 32)
        btn_del.setIcon(QIcon(u":/iconos/iconos/delete-btn.svg"))
        btn_del.setIconSize(QSize(15, 15))
        btn_del.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: 2px solid #4a5568;
                border-radius: 8px;
                padding: 4px;
            }
            QPushButton:hover {
                background: rgba(255, 0, 0, 60);
                border: 2px solid #ff0000;
            }
            QPushButton:pressed {
                background: rgba(255, 0, 0, 100);
            }
        """)

        label = QLabel(parte)
        label.setObjectName("chip")
        label.setFixedSize(280, 42)
        label.setAlignment(Qt.AlignCenter)
        label.setWordWrap(True)
        label.setStyleSheet("""
            QLabel {
                background-color: #ffffff;
                color: #000000;
                border-radius: 10px;
                padding: 10px;
                font-size: 13px;
                font-weight: bold;
            }
        """)

        self.label_map[parte] = label
        self.row_map[parte] = row

        btn_edit.clicked.connect(
            lambda checked=False, p=parte, t=tipo, fi=i, fj=j: self.editarParte(p, t, fi, fj)
        )
        btn_del.clicked.connect(
            lambda checked=False, p=parte: self.confirmarEliminacion(p)
        )

        row.addWidget(btn_edit)
        row.addWidget(btn_del)
        row.addWidget(label, 1)
        layout.addLayout(row)

    def agregarParte(self):
        dlg = ParteDialog(self)
        if dlg.exec():
            parte, tipo, i, j = dlg.values()
            if parte:
                # Trigger async add. Logic moved to on_part_added
                from PySide6.QtCore import QMetaObject, Q_ARG
                # Proper way to invoke slot across threads if not connected to a signal is QMetaObject.invokeMethod
                # But creating a temporary signal is easier or calling a wrapper slot.
                # However, since self.worker is in another thread, calling self.worker.add_part DIRECTLY is unsafe 
                # effectively running it in the main thread unless we use invokeMethod.
                # Since I didn't define signals in the class __init__ for requests, I'll use invokeMethod here or add signals.
                # Adding signals is cleaner design. Let's add them to the class definition on the fly or just use invokeMethod.
                QMetaObject.invokeMethod(self.worker, "add_part", Qt.QueuedConnection,
                                         Q_ARG(str, tipo), Q_ARG(str, parte), Q_ARG(int, i), Q_ARG(int, j))

    def editarParte(self, old_parte, old_tipo, old_i, old_j):
        dlg = ParteDialog(self, old_parte, old_tipo, old_i, old_j)
        if dlg.exec():
            new_parte, new_tipo, new_i, new_j = dlg.values()
            if new_parte:
                 from PySide6.QtCore import QMetaObject, Q_ARG
                 QMetaObject.invokeMethod(self.worker, "update_part", Qt.QueuedConnection,
                                          Q_ARG(str, old_parte), Q_ARG(str, new_parte), Q_ARG(str, new_tipo), 
                                          Q_ARG(int, new_i), Q_ARG(int, new_j))

    def confirmarEliminacion(self, parte):
        reply = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar la parte:\n\n {parte}?\n\nEsta acción no se puede deshacer.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            # Restore styles and clear search input immediately after confirmation
            try:
                self.restaurarEstilos()
            except Exception:
                try:
                    self.searchInput.clear()
                except Exception:
                    pass

            # Then perform asynchronous deletion
            self.eliminarParte(parte)

    def eliminarParte(self, parte):
        from PySide6.QtCore import QMetaObject, Q_ARG
        QMetaObject.invokeMethod(self.worker, "delete_part", Qt.QueuedConnection, Q_ARG(str, parte))

    def buscarParte(self):
        texto = self.searchInput.text().strip().lower()
        if not texto:
            self.restaurarEstilos()
            return
            
        from PySide6.QtCore import QMetaObject, Q_ARG
        QMetaObject.invokeMethod(self.worker, "search_parts", Qt.QueuedConnection, Q_ARG(str, texto))

    def restaurarEstilosSinLimpiarTexto(self):
        for label in self.label_map.values():
            label.setStyleSheet("""
                QLabel {
                    background-color: #ffffff;
                    color: #000000;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 13px;
                    font-weight: bold;
                }
            """)
        for group in self.group_map.values():
            group.setStyleSheet(self.original_border[group])

    def restaurarEstilos(self):
        self.searchInput.clear()
        self.restaurarEstilosSinLimpiarTexto()


