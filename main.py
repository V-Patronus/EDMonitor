import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QSize
from ui.ui_mainwindow import Ui_MainWindow
from widgets.CalculatorWidget import CalculatorWidget

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setup_custom_widgets()

    def setup_custom_widgets(self):
        # 1. Instanciar tu widget personalizado
        self.calculator_widget_instance = CalculatorWidget(self)
        # 2. Integrar el widget personalizado en el QScrollArea de la página Calculator
        # No añadimos otra página al CentralStack; ponemos la calculadora dentro
        # del contenedor del scroll existente: 'scrollAreaWidgetCalculator'.
        if not self.scrollAreaWidgetCalculator.layout():
            self.scrollAreaWidgetCalculator.setLayout(QVBoxLayout())
        # Add the calculator widget centered both horizontally and vertically
        self.scrollAreaWidgetCalculator.layout().addWidget(
            self.calculator_widget_instance, 0, Qt.AlignCenter
        )

        # 3. Conectar los botones de la barra lateral para cambiar páginas del CentralStack
        # Mapear botones a índices del CentralStack según el orden en ui_mainwindow.py
        try:
            self.btnHome.clicked.connect(lambda: self.CentralStack.setCurrentIndex(0))
            self.btnCalculator.clicked.connect(lambda: self.CentralStack.setCurrentIndex(1))
            self.btnDocuments.clicked.connect(lambda: self.CentralStack.setCurrentIndex(2))
            self.BtnAyuda.clicked.connect(lambda: self.CentralStack.setCurrentIndex(3))
            self.btnJapon.clicked.connect(lambda: self.CentralStack.setCurrentIndex(4))
        except Exception:
            pass
        
        # Opcional: Asegurar que el área de scroll se redimensione correctamente
        self.scrollCalculator.setWidgetResizable(True)

        # --- Sidebar responsive + animación ---
        try:
            # determine sensible widths
            try:
                expanded = max(150, self.SideBarFrame.sizeHint().width())
            except Exception:
                expanded = 150
            collapsed = 100

            self._sidebar_expanded_width = expanded
            self._sidebar_collapsed_width = collapsed

            # ensure initial max width allows animation
            self.SideBarFrame.setMaximumWidth(self._sidebar_expanded_width)

            # create animation group placeholder to keep reference
            self._sidebar_anim = None
            # store original texts for buttons so we can hide/show them
            self._sidebar_button_texts = {}
            # store original icon sizes so collapsing doesn't deform icons
            self._sidebar_button_icon_sizes = {}

            # connect the CegaNicButton (checkable) to animate
            try:
                self.CegaNicButton.toggled.connect(self._on_sidebar_toggled)
                # start with sidebar expanded by default
                try:
                    self.CegaNicButton.setChecked(True)
                except Exception:
                    pass
            except Exception:
                pass

            # apply initial state according to button
            try:
                checked = bool(self.CegaNicButton.isChecked())
                # if checked, show expanded; if not, collapse
                if checked:
                    self.SideBarFrame.setMaximumWidth(self._sidebar_expanded_width)
                else:
                    self.SideBarFrame.setMaximumWidth(self._sidebar_collapsed_width)
            except Exception:
                pass
        except Exception:
            pass

    def _on_sidebar_toggled(self, checked: bool):
        """Animate sidebar expanding/collapsing when `CegaNicButton` is toggled."""
        try:
            start = self.SideBarFrame.maximumWidth()
            end = self._sidebar_expanded_width if checked else self._sidebar_collapsed_width

            # create a parallel animation group to animate width + fade for smoothness
            group = QParallelAnimationGroup(self)

            widthAnim = QPropertyAnimation(self.SideBarFrame, b"maximumWidth")
            widthAnim.setDuration(420)
            widthAnim.setStartValue(start)
            widthAnim.setEndValue(end)
            widthAnim.setEasingCurve(QEasingCurve.InOutCubic)
            group.addAnimation(widthAnim)

            # ensure we have an opacity effect on the SideBarGroup to fade contents
            try:
                effect = getattr(self, "_sidebar_opacity_effect", None)
                if effect is None:
                    effect = QGraphicsOpacityEffect(self.SideBarGroup)
                    self.SideBarGroup.setGraphicsEffect(effect)
                    self._sidebar_opacity_effect = effect
            except Exception:
                effect = None

            if effect is not None:
                # Only animate opacity when expanding to avoid hiding icons when collapsed.
                if checked:
                    opacityAnim = QPropertyAnimation(effect, b"opacity")
                    opacityAnim.setDuration(300)
                    opacityAnim.setStartValue(0.0)
                    opacityAnim.setEndValue(1.0)
                    opacityAnim.setEasingCurve(QEasingCurve.InOutCubic)
                    group.addAnimation(opacityAnim)
                else:
                    # ensure effect remains fully visible when collapsed
                    try:
                        effect.setOpacity(1.0)
                    except Exception:
                        pass

            # keep reference to avoid GC until finished
            self._sidebar_anim = group

            # Buttons behavior: when collapsing hide text (leave icon only),
            # when expanding restore text after animation for a smooth effect.
            try:
                buttons = self.SideBarGroup.findChildren(QPushButton)
                if not checked:
                    # collapsing: store and hide
                    for b in buttons:
                        try:
                            txt = b.text()
                            if txt:
                                self._sidebar_button_texts[b.objectName()] = txt
                                b.setToolTip(txt)
                                b.setText("")
                                b.setStyleSheet("text-align:center;")
                                # ensure icon keeps its original size (avoid deforming)
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
                    # expanding: prepare to restore text after animation
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
                    # ensure final width applied
                    self.SideBarFrame.setMaximumWidth(end)
                except Exception:
                    pass

                # ensure opacity restored (avoid invisible buttons)
                try:
                    effect = getattr(self, "_sidebar_opacity_effect", None)
                    if effect is not None:
                        effect.setOpacity(1.0)
                except Exception:
                    pass

                # restore texts if expanded
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
            # fallback immediate
            try:
                self.SideBarFrame.setMaximumWidth(self._sidebar_expanded_width if checked else self._sidebar_collapsed_width)
            except Exception:
                pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec()) # En PySide6, app.exec() es preferido sobre app.exec_()
