from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QPoint
from PySide6.QtGui import QCursor

class ToastNotification(QWidget):
    def __init__(self, parent, text, duration=4000):
        super().__init__(None) # Always top-level window for correct z-order over everything
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        
        self.target_parent = parent # Store intended parent for positioning logic

        # Style: Compact Tooltip
        self.setStyleSheet("""
            QWidget {
                background-color: #333333;
                border: 1px solid #555;
                border-radius: 6px;
            }
            QLabel {
                color: #FFFFFF;
                border: none;
                font-size: 13px;
                padding: 4px;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 8, 15, 8)
        layout.setSpacing(10)
        
        # Small Icon
        lbl_icon = QLabel("✅")
        lbl_icon.setStyleSheet("color: #4CAF50; font-size: 16px; background: transparent; border: none;")
        lbl_icon.setAlignment(Qt.AlignCenter)
        
        self.lbl_text = QLabel(text)
        self.lbl_text.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        layout.addWidget(lbl_icon)
        layout.addWidget(self.lbl_text)
        
        self.adjustSize()
        
        # Position logic: 
        # 1. If parent is a specific widget (not window/None), center over it.
        # 2. Else if cursor exists, follow cursor.
        # 3. Else fallback to screen/window center.
        
        pos_set = False
        if self.target_parent and isinstance(self.target_parent, QWidget):
             try:
                 # Calculate global center of the target widget
                 target_geo = self.target_parent.geometry()
                 target_global_pos = self.target_parent.mapToGlobal(QPoint(0,0))
                 
                 x = target_global_pos.x() + (target_geo.width() - self.width()) // 2
                 y = target_global_pos.y() + (target_geo.height() - self.height()) // 2
                 self.move(x, y)
                 pos_set = True
             except Exception:
                 pos_set = False
        
        if not pos_set:
            cursor_pos = QCursor.pos()
            if cursor_pos:
                self.move(cursor_pos.x() + 15, cursor_pos.y() + 15)
        
        # Animation
        self.setWindowOpacity(0.0)
        
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(3000)
        
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.fade_out)
        self.duration = duration

    def show_toast(self):
        self.show()
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()
        self.timer.start(self.duration)

    def fade_out(self):
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setEasingCurve(QEasingCurve.InCubic)
        self.anim.finished.connect(self.close)
        self.anim.start()

    @staticmethod
    def show_message(parent, text, duration=4000):
        # We pass the parent (target widget) into __init__ for positioning logic,
        # but the QWidget parent in super().__init__ will be None (set inside __init__) 
        # to ensure it's a top-level tool window.
        toast = ToastNotification(parent, text, duration) 
        toast.show_toast()
