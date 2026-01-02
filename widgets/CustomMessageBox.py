from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QFont, QIcon

class CustomMessageBox(QDialog):
    Information = "Información"
    Warning = "Advertencia"
    Critical = "Error"
    Question = "Pregunta"

    def __init__(self, parent=None, title="", text="", icon_type=Information):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Ensures that the dialog is modal and blocks interaction with other windows
        self.setWindowModality(Qt.ApplicationModal)
        
        self.result_code = QDialog.Rejected

        # Main Layout & Container
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        self.container = QWidget()
        self.container.setStyleSheet("""
            QWidget {
                background-color: #1A1D24;
                border: 1px solid #333;
                border-radius: 12px;
            }
            QLabel {
                color: #E0E0E0;
                border: none;
            }
            QPushButton {
                 background-color: #2F343F;
                 color: white;
                 border: none;
                 border-radius: 6px;
                 padding: 8px 16px;
                 font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3E4552;
            }
            QPushButton:pressed {
                background-color: #252A33;
            }
            #btnYes, #btnOk {
                background-color: #007ACC;
            }
            #btnYes:hover, #btnOk:hover {
                background-color: #008AD8;
            }
            #btnClose {
                background-color: transparent;
                color: #888;
                font-size: 14px;
                padding: 4px;
            }
            #btnClose:hover {
                color: #FFF;
                background-color: #C42B1C;
            }
        """)
        
        # Shadow Effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.container.setGraphicsEffect(shadow)
        
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)

        #--- Header ---
        self.header_frame = QWidget()
        self.header_frame.setFixedHeight(40)
        self.header_frame.setStyleSheet("border-bottom: 1px solid #333; border-radius: 12px 12px 0 0;")
        header_layout = QHBoxLayout(self.header_frame)
        header_layout.setContentsMargins(15, 0, 5, 0)
        
        self.lbl_title = QLabel(title)
        self.lbl_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        
        self.btn_close = QPushButton("✕")
        self.btn_close.setObjectName("btnClose")
        self.btn_close.setFixedSize(30, 30)
        self.btn_close.clicked.connect(self.reject)
        
        header_layout.addWidget(self.lbl_title)
        header_layout.addStretch()
        header_layout.addWidget(self.btn_close)
        
        #--- Body ---
        self.body_frame = QWidget()
        body_layout = QHBoxLayout(self.body_frame)
        body_layout.setContentsMargins(20, 20, 20, 20)
        body_layout.setSpacing(15)
        
        # Icon (Text-based for simplicity, can replace with SVG)
        self.lbl_icon = QLabel()
        self.lbl_icon.setFixedSize(40, 40)
        self.lbl_icon.setAlignment(Qt.AlignCenter)
        self.lbl_icon.setStyleSheet("font-size: 24px; border-radius: 20px; background-color: #333;")
        self.set_icon(icon_type)
        
        self.lbl_text = QLabel(text)
        self.lbl_text.setWordWrap(True)
        self.lbl_text.setStyleSheet("font-size: 13px;")
        
        body_layout.addWidget(self.lbl_icon)
        body_layout.addWidget(self.lbl_text, 1)

        #--- Footer ---
        self.footer_frame = QWidget()
        footer_layout = QHBoxLayout(self.footer_frame)
        footer_layout.setContentsMargins(15, 10, 15, 15)
        footer_layout.setSpacing(10)
        footer_layout.addStretch()
        
        if icon_type == CustomMessageBox.Question:
            self.btn_yes = QPushButton("Sí")
            self.btn_yes.setObjectName("btnYes")
            self.btn_yes.clicked.connect(self.accept)
            
            self.btn_no = QPushButton("No")
            self.btn_no.clicked.connect(self.reject)
            
            footer_layout.addWidget(self.btn_no)
            footer_layout.addWidget(self.btn_yes)
        else:
            self.btn_ok = QPushButton("Aceptar")
            self.btn_ok.setObjectName("btnOk")
            self.btn_ok.clicked.connect(self.accept)
            footer_layout.addWidget(self.btn_ok)

        # Assemble
        self.container_layout.addWidget(self.header_frame)
        self.container_layout.addWidget(self.body_frame)
        self.container_layout.addWidget(self.footer_frame)
        
        self.layout.addWidget(self.container)
        
        self.resize(400, 180)

    def set_icon(self, icon_type):
        if icon_type == CustomMessageBox.Information:
            self.lbl_icon.setText("ℹ")
            self.lbl_icon.setStyleSheet("color: #007ACC; font-size: 24px; border-radius: 20px; background-color: rgba(0, 122, 204, 0.1);")
        elif icon_type == CustomMessageBox.Warning:
            self.lbl_icon.setText("⚠")
            self.lbl_icon.setStyleSheet("color: #FFD700; font-size: 24px; border-radius: 20px; background-color: rgba(255, 215, 0, 0.1);")
        elif icon_type == CustomMessageBox.Critical:
            self.lbl_icon.setText("✕")
            self.lbl_icon.setStyleSheet("color: #FF4444; font-size: 24px; border-radius: 20px; background-color: rgba(255, 68, 68, 0.1);")
        elif icon_type == CustomMessageBox.Question:
            self.lbl_icon.setText("?")
            self.lbl_icon.setStyleSheet("color: #A0A0A0; font-size: 24px; border-radius: 20px; background-color: rgba(255, 255, 255, 0.1);")

    @staticmethod
    def information(parent, title, text):
        dialog = CustomMessageBox(parent, title, text, CustomMessageBox.Information)
        dialog.exec()

    @staticmethod
    def warning(parent, title, text):
        dialog = CustomMessageBox(parent, title, text, CustomMessageBox.Warning)
        dialog.exec()

    @staticmethod
    def critical(parent, title, text):
        dialog = CustomMessageBox(parent, title, text, CustomMessageBox.Critical)
        dialog.exec()

    @staticmethod
    def show_fading_message(parent, title, text, duration=2000):
        """Shows a non-modal, buttonless dialog that fades out after a duration."""
        dialog = CustomMessageBox(parent, title, text, CustomMessageBox.Information)
        
        # Configure for transient/toast behavior
        dialog.setWindowModality(Qt.NonModal)
        dialog.footer_frame.hide() # Hide buttons
        dialog.btn_close.hide() # Hide close button
        
        # Adjust size after hiding footer
        dialog.adjustSize()
        
        # Determine duration
        dialog.duration = duration
        
        # Setup Animation
        from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer
        dialog.anim = QPropertyAnimation(dialog, b"windowOpacity")
        dialog.anim.setDuration(500)
        
        dialog.timer = QTimer(dialog)
        dialog.timer.setSingleShot(True)
        
        def start_fade_out():
            dialog.anim.setStartValue(1.0)
            dialog.anim.setEndValue(0.0)
            dialog.anim.setEasingCurve(QEasingCurve.InCubic)
            dialog.anim.finished.connect(dialog.close)
            dialog.anim.start()
            
        dialog.timer.timeout.connect(start_fade_out)
        
        dialog.show()
        
        # Start timer
        dialog.timer.start(duration)

    @staticmethod
    def question(parent, title, text):
        dialog = CustomMessageBox(parent, title, text, CustomMessageBox.Question)
        return dialog.exec() == QDialog.Accepted
