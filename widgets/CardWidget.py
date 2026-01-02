from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import Signal, QUrl
from PySide6.QtGui import QDesktopServices, QPixmap, QColor
from ui.ui_cards import Ui_FuturisticCard
from widgets.CustomMessageBox import CustomMessageBox
import os

class CardWidget(QWidget, Ui_FuturisticCard):
    edit_requested = Signal(int, str, str, str, str, str) # id, name, desc, icon, style, path
    delete_requested = Signal(int)

    def __init__(self, card_id, name, description, icon_path, style, path, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.card_id = card_id
        self.path = path
        self.name = name
        self.description = description
        self.icon_path = icon_path
        self.style = style

        # Set UI Data
        self.nameLabel.setText(name)
        self.descText.setPlainText(description)
        # Glow Effect via CSS (Safer than QGraphicsEffect)
        # 00E5FF is Cyan
        self.cardFrame.setStyleSheet(f"""
            QFrame#cardFrame {{
                border: 2px solid #00E5FF;
                border-radius: 10px;
                background-color: rgba(0, 229, 255, 10);
            }}
            QFrame#cardFrame[value="style1"] {{ border-color: #00E5FF; }} 
            QFrame#cardFrame[value="style2"] {{ border-color: #FF00FF; }}
            QFrame#cardFrame[value="style3"] {{ border-color: #FFFF00; }}
        """)
        self.cardFrame.setProperty("value", style)
        self.cardFrame.style().unpolish(self.cardFrame)
        self.cardFrame.style().polish(self.cardFrame)
        
        # Glow Effect (Luminescent Shadow)
        # self.glow_effect = QGraphicsDropShadowEffect()
        # self.glow_effect.setBlurRadius(20)
        # self.glow_effect.setXOffset(0)
        # self.glow_effect.setYOffset(0)
        # # Choose color based on style or default to Cyan
        # # 00E5FF is a bright cyan neon
        # self.glow_effect.setColor(QColor(0, 229, 255, 120)) 
        # self.cardFrame.setGraphicsEffect(self.glow_effect)
        
        # Set Icon
        if icon_path:
             self.iconLabel.setPixmap(QPixmap(icon_path))

        # Connect Buttons
        self.goButton.clicked.connect(self.open_path)
        self.editButton.clicked.connect(self.request_edit)
        self.deleteButton.clicked.connect(self.request_delete)

    def open_path(self):
        if self.path:
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.path))
        else:
            CustomMessageBox.information(self, "Info", "No hay ruta definida para esta tarjeta.")

    def request_edit(self):
        self.edit_requested.emit(self.card_id, self.name, self.description, self.icon_path, self.style, self.path)

    def request_delete(self):
        if CustomMessageBox.question(self, "Confirmar eliminación", f"¿Estás seguro de que deseas eliminar '{self.name}'?"):
            self.delete_requested.emit(self.card_id)
