# circular_splash.py
import sys
from PySide6.QtCore import (Qt, QPropertyAnimation, QRectF, Property,
                            QTimer, QThread, Signal, Slot, QAbstractAnimation)
import logging
_logger = logging.getLogger(__name__)
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QRegion, QBitmap
from PySide6.QtWidgets import QWidget, QApplication


class CircularSplash(QWidget):
    """
    Splash circular genérico:
        set_progress(percent, text)  -> actualiza UI
        finish()                     -> cierra splash
    """
    def __init__(self,
                 parent=None,
                 size=240,
                 line_width=10,
                 bg_ring="#202020",
                 progress_color="#00B4FF",
                 text_color="#00B4FF",
                 glow_color="#00B4FF",
                 glow_width=16,
                 process_name="Iniciando…"):
        super().__init__(parent)
        self._value = 0
        self._process = process_name
        self._line_width = line_width
        self._bg_ring = QColor(bg_ring)
        self._progress_color = QColor(progress_color)
        self._text_color = QColor(text_color)
        self._glow_color = QColor(glow_color)
        self._glow_width = glow_width

        # Ventana sin decoración y redonda
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(size, size)
        self.make_round()

        # Animación de rotación para el spinner indeterminado
        self._rotation = 0.0
        self.rotation_anim = QPropertyAnimation(self, b"rotation")
        self.rotation_anim.setDuration(1200)
        self.rotation_anim.setStartValue(0.0)
        self.rotation_anim.setEndValue(360.0)
        try:
            self.rotation_anim.setLoopCount(QAbstractAnimation.Infinite)
        except Exception:
            try:
                self.rotation_anim.setLoopCount(-1)
            except Exception:
                pass
        self.rotation_anim.valueChanged.connect(self.update)

        # Centrar en pantalla
        self.center()

    # ---------- Properties ----------
    def getValue(self):
        return self._value

    def setValue(self, v):
        self._value = max(0, min(100, int(v)))
        self.update()

    value = Property(int, getValue, setValue)

    def getRotation(self):
        return float(self._rotation)

    def setRotation(self, v: float):
        try:
            self._rotation = float(v) % 360.0
        except Exception:
            self._rotation = 0.0
        self.update()

    rotation = Property(float, getRotation, setRotation)

    # ---------- Round ----------
    def make_round(self):
        bmp = QBitmap(self.size())
        bmp.fill(Qt.color0)
        painter = QPainter(bmp)
        painter.setBrush(Qt.color1)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawEllipse(bmp.rect())
        painter.end()
        self.setMask(QRegion(bmp))

    def center(self):
        if QApplication.instance():
            desktop = QApplication.instance().primaryScreen().availableGeometry()
            self.move((desktop.width() - self.width()) // 2,
                      (desktop.height() - self.height()) // 2)

    # ---------- Public API ----------
    @Slot(int, str)
    def set_progress(self, percent: int, text: str):
        """Actualiza texto desde cualquier hilo (es Slot)."""
        self._process = text.strip()
        try:
            _logger.debug("CircularSplash.set_progress: percent=%s text=%s", percent, text)
        except Exception:
            pass
        # Aseguramos que la animación del spinner esté corriendo
        try:
            self.rotation_anim.start()
        except Exception:
            pass

    @Slot()
    def finish(self):
        try:
            _logger.debug("CircularSplash.finish called; stopping animation and closing")
            self.rotation_anim.stop()
        except Exception:
            pass
        self.close()

    def showEvent(self, event):
        try:
            _logger.debug("CircularSplash.showEvent")
            self.rotation_anim.start()
        except Exception:
            pass
        super().showEvent(event)

    # ---------- Paint ----------
    def paintEvent(self, _):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        outer = self.rect()
        center = outer.center()
        radius = (min(outer.width(), outer.height()) - self._glow_width) / 2

        # Glow (efecto de brillo suave)
        glow_pen = QPen(self._glow_color, self._line_width + self._glow_width,
                        Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        glow_color = QColor(self._glow_color)
        glow_color.setAlphaF(0.35)
        glow_pen.setColor(glow_color)
        painter.setPen(glow_pen)
        painter.drawEllipse(center, radius, radius)

        # Anillo de fondo
        base_pen = QPen(self._bg_ring, self._line_width,
                        Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(base_pen)
        painter.drawEllipse(center, radius, radius)

        # Arco de progreso (determinado, si se usa porcentaje)
        span = -int(self._value * 360 / 100)
        prog_pen = QPen(self._progress_color, self._line_width,
                        Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(prog_pen)
        painter.drawArc(QRectF(center.x() - radius, center.y() - radius,
                              2 * radius, 2 * radius),
                        90 * 16, span * 16)

        # Spinner indeterminado (arco giratorio)
        span_deg = 120
        start_angle = int((90 - self._rotation) * 16)
        span_spinner = -int(span_deg * 16)
        painter.setPen(prog_pen)
        painter.drawArc(QRectF(center.x() - radius, center.y() - radius,
                              2 * radius, 2 * radius),
                        start_angle, span_spinner)

        # Texto centrado perfectamente en el medio
        if self._process:
            painter.setPen(self._text_color)
            font = painter.font()
            font.setPixelSize(int(radius * 0.20))   # Tamaño adaptable al radio
            font.setBold(True)                       # Más legible
            painter.setFont(font)

            # Qt.AlignCenter centra tanto horizontal como verticalmente en todo el rectángulo
            painter.drawText(outer, Qt.AlignCenter, self._process)


# --------------- EJEMPLO DE USO (se puede borrar / mover a otro archivo) ---------------
class HeavyWorker(QThread):
    """Simula tareas pesadas y emite progreso."""
    progress = Signal(int, str)  # percent, text

    def run(self):
        tasks = (
            (30, "Obteniendo recursos…"),
            (60, "Inicializando interfaz…"),
            (90, "Cargando plugins…"),
            (100, "Finalizado"),
        )
        for percent, text in tasks:
            self.msleep(800)  # trabajo pesado simulado
            self.progress.emit(percent, text)
        self.msleep(500)


def main():
    app = QApplication(sys.argv)
    splash = CircularSplash()
    splash.show()

    # Worker en segundo plano
    worker = HeavyWorker()
    worker.progress.connect(splash.set_progress)
    worker.finished.connect(splash.finish)
    worker.start()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()