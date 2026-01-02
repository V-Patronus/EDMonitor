from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Signal, Qt
from ui.ui_modalCreateCard import Ui_CardModal
from ui.ui_modalCreateCard import Ui_CardModal
from widgets.CustomMessageBox import CustomMessageBox
import os

class CreateEditCardWidget(QWidget, Ui_CardModal):
    card_saved = Signal()  # Legacy/Forwarding signal
    add_card_requested = Signal(str, str, str, str, str) # name, desc, icon, style, path
    update_card_requested = Signal(int, str, str, str, str, str) # id, name, desc, icon, style, path

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        # FIX: Ensure it behaves like a normal widget, not a modal window
        self.setWindowFlags(Qt.Widget) # Force it to be a widget, not a window/dialog
        self.setWindowModality(Qt.WindowModality.NonModal)
        
        # Ensure inputs are interactive
        self.nameEdit.setEnabled(True)
        self.nameEdit.setReadOnly(False)
        self.nameEdit.setFocusPolicy(Qt.StrongFocus)
        
        self.descEdit.setEnabled(True)
        self.descEdit.setReadOnly(False)
        self.descEdit.setFocusPolicy(Qt.StrongFocus)

        self.current_card_id = None
        self.selected_icon = ":/iconos/iconos/default.svg"
        
        # Connect UI elements
        self.browseButton.clicked.connect(self.browse_path)
        self.createButton.clicked.connect(self.create_card)
        self.editButton.clicked.connect(self.update_card)
        
        # Connect Icon Buttons
        self.iconFolder.clicked.connect(lambda: self.select_icon(":/iconos/iconos/carpeta.svg"))
        self.iconExcel.clicked.connect(lambda: self.select_icon(":/iconos/iconos/excel.svg"))
        self.iconPdf.clicked.connect(lambda: self.select_icon(":/iconos/iconos/pdf.svg"))
        self.iconDefault.clicked.connect(lambda: self.select_icon(":/iconos/iconos/default.svg"))
        
        # Initial state
        self.editButton.hide()
        self.select_icon(self.selected_icon)

    def select_icon(self, icon_path):
        self.selected_icon = icon_path
        # Visually select the button (logic is handled by autoExclusive but let's ensure variable update)
        if icon_path == ":/iconos/iconos/carpeta.svg":
            self.iconFolder.setChecked(True)
        elif icon_path == ":/iconos/iconos/excel.svg":
            self.iconExcel.setChecked(True)
        elif icon_path == ":/iconos/iconos/pdf.svg":
            self.iconPdf.setChecked(True)
        else:
            self.iconDefault.setChecked(True)

    def browse_path(self):
        # Dynamic dialog based on selected icon
        if self.selected_icon == ":/iconos/iconos/carpeta.svg":
            path = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta")
        else:
            path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo")
        
        if path:
            self.pathEdit.setText(path)

    def validate_path(self, path):
        if not path:
            return True # Let empty path pass if that's allowed, or check separately. 
                        # Requirement says "store ... info", usually implies required.
        
        is_folder_icon = (self.selected_icon == ":/iconos/iconos/carpeta.svg")
        
        if is_folder_icon:
            if not os.path.isdir(path):
                CustomMessageBox.warning(self, "Error de Validación", "El icono seleccionado es para una carpeta, pero la ruta no es un directorio válido.")
                return False
        else:
            # Assume file for other icons
            if not os.path.isfile(path):
                CustomMessageBox.warning(self, "Error de Validación", "El icono seleccionado es para un archivo, pero la ruta no es un archivo válido.")
                return False
        return True

    def create_card(self):
        name = self.nameEdit.text()
        description = self.descEdit.toPlainText()
        style = self.comboBoxStyles.currentText()
        path = self.pathEdit.text()
        
        if not name:
            CustomMessageBox.warning(self, "Error de Validación", "Se requiere un nombre.")
            return

        # Path validation logic
        if path and not self.validate_path(path):
             return

        # Emit request signal
        self.add_card_requested.emit(name, description, self.selected_icon, style, path)
        # Note: Form clearing and success message will be handled by on_card_saved_success slot

    def update_card(self):
        if not self.current_card_id:
            return

        name = self.nameEdit.text()
        description = self.descEdit.toPlainText()
        style = self.comboBoxStyles.currentText()
        path = self.pathEdit.text()
        
        if not name:
            CustomMessageBox.warning(self, "Error de Validación", "Se requiere un nombre.")
            return

        # Path validation logic
        if path and not self.validate_path(path):
             return

        # Emit request signal
        self.update_card_requested.emit(self.current_card_id, name, description, self.selected_icon, style, path)

    def set_card_data(self, card_id, name, description, icon_path, style, path):
        self.current_card_id = card_id
        self.nameEdit.setText(name)
        self.descEdit.setPlainText(description)
        self.pathEdit.setText(path)
        self.select_icon(icon_path)
        self.comboBoxStyles.setCurrentText(style)
        
        self.createButton.hide()
        self.editButton.show()

    def clear_form(self):
        self.nameEdit.clear()
        self.descEdit.clear()
        self.pathEdit.clear()
        self.select_icon(":/iconos/iconos/default.svg")
        self.comboBoxStyles.setCurrentIndex(0)
        self.createButton.show()
        self.editButton.hide()
        self.current_card_id = None

    def on_card_saved_success(self, message="Acción completada"):
        """Called when main window confirms async save is done."""
        self.clear_form()
        self.card_saved.emit() # Forward signal to main if needed
        CustomMessageBox.show_fading_message(self, "Éxito", message, duration=2500)
