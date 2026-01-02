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
from db import init_db, get_all, search, add, delete, update
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
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableroGageWidget()
        self.ui.setupUi(self)

        self.gridLayout = self.ui.gridLayout
        self.searchInput = self.ui.searchInput
        self.searchButton = self.ui.searchButton
        self.addButton = self.ui.addButton
        self.restoreButton = self.ui.restoreButton

        self.matriz = {}
        self.group_map = {}
        self.label_map = {}
        self.row_map = {}
        self.original_border = {}

        self.initGrid()

        try:
            init_db()
            self.cargarTodo()
        except Exception as e:
            QMessageBox.critical(
                self, "Error crítico",
                f"No se pudo inicializar la base de datos:\n{e}\n\nLa aplicación se cerrará."
            )
            sys.exit(1)

        self.searchButton.clicked.connect(self.buscarParte)
        self.addButton.clicked.connect(self.agregarParte)
        self.restoreButton.clicked.connect(self.restaurarEstilos)
        self.searchInput.returnPressed.connect(self.buscarParte)

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

    def cargarTodo(self):
        self.limpiarGrid()
        for tipo, parte, i, j in get_all():
            self.addParteToCell(parte, tipo, i, j)

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
        btn_edit.setIcon(QIcon("./iconos/edit.svg"))
        btn_edit.setIconSize(QSize(20, 20))
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
        btn_del.setIcon(QIcon("./iconos/delete.svg"))
        btn_del.setIconSize(QSize(20, 20))
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
            if parte and add(tipo, parte, i, j):
                self.addParteToCell(parte, tipo, i, j)
            elif parte:
                QMessageBox.warning(self, "Duplicado", f"La parte '{parte}' ya existe.")

    def editarParte(self, old_parte, old_tipo, old_i, old_j):
        dlg = ParteDialog(self, old_parte, old_tipo, old_i, old_j)
        if dlg.exec():
            new_parte, new_tipo, new_i, new_j = dlg.values()
            if new_parte and update(old_parte, new_parte, new_tipo, new_i, new_j):
                if old_parte in self.row_map:
                    row = self.row_map[old_parte]
                    self.clearLayout(row)
                    row.deleteLater()
                    del self.row_map[old_parte]
                    del self.label_map[old_parte]
                self.addParteToCell(new_parte, new_tipo, new_i, new_j)
            elif new_parte:
                QMessageBox.warning(self, "Error", "No se pudo actualizar (posible duplicado).")

    def confirmarEliminacion(self, parte):
        reply = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar la parte:\n\n<b>{parte}</b>?\n\nEsta acción no se puede deshacer.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.eliminarParte(parte)

    def eliminarParte(self, parte):
        if delete(parte):
            if parte in self.row_map:
                row = self.row_map[parte]
                self.clearLayout(row)
                row.deleteLater()
                del self.row_map[parte]
                del self.label_map[parte]
        else:
            QMessageBox.critical(self, "Error", "No se pudo eliminar la parte de la base de datos.")

    def buscarParte(self):
        texto = self.searchInput.text().strip().lower()
        
        # Restaurar estilos sin limpiar el texto
        self.restaurarEstilosSinLimpiarTexto()

        if not texto:
            return

        # Resaltar coincidencias
        for tipo, parte, i, j in search(texto):
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


