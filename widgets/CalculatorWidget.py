from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QEvent, QTimer, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup
from PySide6.QtGui import QDoubleValidator
import math
from ui.ui_calculator import Ui_CalculatorWidget
import sys
import ast

class CalculatorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CalculatorWidget()
        self.ui.setupUi(self)

        # Keep the full expression as a string so users can type inline
        # arithmetic like `5+9-3*2`.
        self.expression = ""
        self.result_shown = False

        self._connect_buttons()
        self._setup_keyboard()
        self._update_display()

        # Validator: only allow non-negative floating numbers for radio
        try:
            validator = QDoubleValidator(0.0, 1e12, 6, self)
            self.ui.lineEditRadio.setValidator(validator)
        except Exception:
            pass

        # Connect calcular button for frameJapon
        try:
            self.ui.pushButtonCalcular.clicked.connect(self._calculate_japon)
        except Exception:
            pass

        # Connect clear button for frameJapon to clear labels and radio input
        try:
            self.ui.clear_fj.clicked.connect(self._clear_japon)
        except Exception:
            pass

        # Do not force focus to `displayLineEdit` here so `lineEditRadio`
        # (and other inputs) can receive focus independently.

        # Connect mode selector to show/hide frames and apply initial mode
        try:
            # connect to a handler that will animate the switch
            self.ui.comboBoxType.currentIndexChanged.connect(self._on_mode_changed)
            # set initial mode without animation
            self._apply_mode(self.ui.comboBoxType.currentIndex())
        except Exception:
            pass

        # Keep a reference to current animation to avoid GC
        self._current_animation = None

        # Connect Enter on lineEditRadio to trigger calculate with pressed style
        try:
            self.ui.lineEditRadio.returnPressed.connect(self._radio_return_pressed)
        except Exception:
            pass

    def _connect_buttons(self):
        buttons = self.findChildren(QPushButton)

        for btn in buttons:
            role = btn.property("role")
            value = btn.property("value")

            if role:
                btn.clicked.connect(
                    lambda checked=False, r=role, v=value: self._handle_input(r, v)
                )

            # Visual pressed property for actual clicks
            btn.pressed.connect(lambda b=btn: (b.setProperty("pressed", True), b.style().unpolish(b), b.style().polish(b)))
            btn.released.connect(lambda b=btn: (b.setProperty("pressed", False), b.style().unpolish(b), b.style().polish(b)))

    def _handle_input(self, role, value):
        if role == "number":
            self._input_number(value)
        elif role == "operator":
            self._input_operator(value)
        elif role == "special":
            self._input_special(value)

        self._update_display()

    def _input_number(self, num):
        if self.result_shown:
            # Start a new expression after a shown result
            self.expression = str(num)
            self.result_shown = False
        else:
            self.expression += str(num)

    def _input_operator(self, op):
        if not self.expression:
            # allow negative numbers to start
            if op == "-":
                self.expression = op
            return

        # replace trailing operator if user presses operator twice
        if self.expression[-1] in "+-*/":
            self.expression = self.expression[:-1] + op
        else:
            self.expression += op
        self.result_shown = False

    def _input_special(self, action):
        if action == "clear":
            self.expression = ""
            self.result_shown = False

        elif action == "ce":
            self.expression = ""

        elif action == "back":
            self.expression = self.expression[:-1]

        elif action == "dot":
            # append dot only if current number doesn't have one
            # if a result was just shown, start a new expression with 0.
            if self.result_shown:
                self.expression = "0."
                self.result_shown = False
                return

            last = self._last_number()
            if "." not in last:
                if not last:
                    self.expression += "0."
                else:
                    self.expression += "."

        elif action == "equals":
            result = self._evaluate_expression(self.expression)
            # apply rounding according to comboBoxDigit selection
            if result and result != "Error":
                try:
                    val = float(result)
                    decimals = self._get_decimals()
                    result = f"{round(val, decimals):.{decimals}f}"
                except Exception:
                    pass

            self.expression = result
            self.result_shown = True


    def _calculate(self):
        # legacy - not used in expression mode
        return

    def _last_number(self):
        # return the last numeric token in the expression
        if not self.expression:
            return ""
        toks = []
        cur = ""
        for ch in self.expression[::-1]:
            if ch.isdigit() or ch == '.':
                cur = ch + cur
            else:
                break
        return cur

    def _evaluate_expression(self, expr):
        if not expr:
            return ""

        # sanitize: disallow invalid characters
        allowed = set('0123456789+-*/.() ')
        if any(ch not in allowed for ch in expr):
            return "Error"

        try:
            node = ast.parse(expr, mode='eval')
        except Exception:
            return "Error"
        # safe AST evaluator moved here so `node` is in scope
        def _eval(n):
            if isinstance(n, ast.Expression):
                return _eval(n.body)
            if isinstance(n, ast.BinOp):
                left = _eval(n.left)
                right = _eval(n.right)
                if isinstance(n.op, ast.Add):
                    return left + right
                if isinstance(n.op, ast.Sub):
                    return left - right
                if isinstance(n.op, ast.Mult):
                    return left * right
                if isinstance(n.op, ast.Div):
                    return left / right
                return None
            if isinstance(n, ast.UnaryOp):
                operand = _eval(n.operand)
                if isinstance(n.op, ast.UAdd):
                    return +operand
                if isinstance(n.op, ast.USub):
                    return -operand
            if isinstance(n, ast.Num):
                return n.n
            if isinstance(n, ast.Constant):
                return n.value
            return None

        try:
            val = _eval(node)
            if val is None:
                return "Error"
            # strip .0 for integers
            if isinstance(val, float) and val.is_integer():
                return str(int(val))
            return str(val)
        except ZeroDivisionError:
            return "Error"
        except Exception:
            return "Error"

    def _validate_expression(self):
        """Validate current expression and set displayFrame.invalid accordingly."""
        allowed = set('0123456789+-*/.() ')
        valid = all(ch in allowed for ch in self.expression)
        try:
            # stylesheet expects string values "true"/"false"
            self.ui.displayFrame.setProperty("invalid", "false" if valid else "true")
            self.ui.displayFrame.style().unpolish(self.ui.displayFrame)
            self.ui.displayFrame.style().polish(self.ui.displayFrame)
            self.ui.displayFrame.update()
        except Exception:
            pass

    def _flash_invalid(self, message, duration=1200):
        """Show a temporary invalid message in the display and restore it."""
        try:
            prev = self.ui.displayLineEdit.text()
            # show message
            self.ui.displayLineEdit.setText(message)
            self.ui.displayLineEdit.setCursorPosition(len(message))
            # set invalid frame property
            try:
                self.ui.displayFrame.setProperty("invalid", "true")
                self.ui.displayFrame.style().unpolish(self.ui.displayFrame)
                self.ui.displayFrame.style().polish(self.ui.displayFrame)
                self.ui.displayFrame.update()
            except Exception:
                pass
        except Exception:
            prev = None

        def _restore():
            try:
                text = self.expression if self.expression else "0"
                self.ui.displayLineEdit.setText(text)
                self.ui.displayLineEdit.setCursorPosition(len(text))
                # re-run validation to clear/redraw frame
                self._validate_expression()
            except Exception:
                pass

        QTimer.singleShot(duration, _restore)


    def _setup_keyboard(self):
        # Install event filter on the application so key presses
        # from child widgets (like the display QLineEdit) are caught.
        app = QApplication.instance()
        if app:
            app.installEventFilter(self)

        # Make Enter in the QLineEdit trigger the equals action.
        try:
            self.ui.displayLineEdit.returnPressed.connect(
                lambda: self._press_virtual("special", "equals")
            )
        except Exception:
            pass

        # Prevent the QLineEdit from accepting direct keyboard input so
        # keys are handled only by our logic (avoids duplicate insertions).
        try:
            # keep read-only so keys are processed by eventFilter,
            # but allow it to receive focus and show the caret.
            self.ui.displayLineEdit.setReadOnly(True)
            self.ui.displayLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
            # disable complex input methods (IME) to avoid composed characters
            try:
                self.ui.displayLineEdit.setAttribute(Qt.WA_InputMethodEnabled, False)
            except Exception:
                pass
        except Exception:
            pass

        # Ensure no button starts with an unexpected 'pressed' property
        for btn in self.findChildren(QPushButton):
            btn.setProperty("pressed", False)
            btn.style().unpolish(btn)
            btn.style().polish(btn)

    def eventFilter(self, obj, event):
        # FIX: Only handle events if the calculator is actually visible. 
        # This prevents blocking input in other parts of the application (like CreateEditCardWidget).
        if not self.isVisible():
            return super().eventFilter(obj, event)

        # If the radio line edit has focus, allow normal key handling
        try:
            app = QApplication.instance()
            if app and app.focusWidget() is getattr(self.ui, 'lineEditRadio', None):
                return super().eventFilter(obj, event)
        except Exception:
            pass

        if event.type() == QEvent.KeyPress:
            key = event.key()
            text = event.text()
            # handle control keys first so they aren't mistaken for printable text
            if key == Qt.Key_Enter or key == Qt.Key_Return:
                # set visual pressed on the equals button while Enter is down
                for b in self.findChildren(QPushButton):
                    if b.objectName() == "btnEquals":
                        try:
                            b.setProperty("pressed", True)
                            b.style().unpolish(b)
                            b.style().polish(b)
                            b.update()
                        except Exception:
                            pass
                        break

                self._press_virtual("special", "equals")
                event.accept()
                return True

            if key == Qt.Key_Backspace:
                self._press_virtual("special", "back")
                # after deleting, re-validate to clear invalid state
                try:
                    self._validate_expression()
                except Exception:
                    pass
                event.accept()
                return True

            if key == Qt.Key_Delete:
                # treat Delete same as Backspace (remove last char)
                self._press_virtual("special", "back")
                try:
                    self._validate_expression()
                except Exception:
                    pass
                event.accept()
                return True

            # printable input handling
            if text.isdigit():
                self._press_virtual("number", text)
                event.accept()
                return True
            elif text in "+-*/":
                self._press_virtual("operator", text)
                event.accept()
                return True
            elif text == ".":
                # decimal point; handle before the generic invalid-char branch
                self._press_virtual("special", "dot")
                event.accept()
                return True
            elif text and not text.isspace():
                # any other printable character (letters, symbols) should
                # flash an invalid-message and be ignored
                try:
                    self._flash_invalid("Carácter inválido")
                except Exception:
                    pass
                return True

        # clear visual on key release for Enter so the button appears released
        if event.type() == QEvent.KeyRelease:
            key = event.key()
            if key == Qt.Key_Enter or key == Qt.Key_Return:
                for b in self.findChildren(QPushButton):
                    if b.objectName() == "btnEquals":
                        try:
                            b.setProperty("pressed", False)
                            b.style().unpolish(b)
                            b.style().polish(b)
                            b.update()
                        except Exception:
                            pass
                        break
                event.accept()

        return super().eventFilter(obj, event)
    
    def _press_virtual(self, role, value):
        for btn in self.findChildren(QPushButton):
            if btn.property("role") == role and str(btn.property("value")) == str(value):
                # set property for stylesheet-driven pressed appearance
                try:
                    btn.setProperty("pressed", True)
                    btn.style().unpolish(btn)
                    btn.style().polish(btn)
                except Exception:
                    pass

                # animateClick emulates a real click and will emit clicked()
                try:
                    btn.animateClick(120)
                except Exception:
                    # Fallback: invoke handler directly
                    self._handle_input(role, value)

                # clear the property shortly after
                def _clear(b=btn):
                    try:
                        b.setProperty("pressed", False)
                        b.style().unpolish(b)
                        b.style().polish(b)
                    except Exception:
                        pass

                QTimer.singleShot(160, _clear)
                break


    def _update_display(self):
        text = self.expression if self.expression else ""
        if not text:
            text = "0"
        try:
            self.ui.displayLineEdit.setText(text)
            # keep caret at the end so user sees position if it has focus
            try:
                self.ui.displayLineEdit.setCursorPosition(len(text))
            except Exception:
                pass
            # validate current expression and update displayFrame style
            self._validate_expression()
        except Exception:
            pass

    def _calculate_japon(self):
        """Leer el radio desde `lineEditRadio`, validar y calcular
        c = radio * (1 - sin((angle / 180) * PI)) para ángulos 1..6.
        Escribe cada resultado en `label_valor_1` .. `label_valor_6`.
        """
        try:
            txt = self.ui.lineEditRadio.text().strip()
            if not txt:
                self._flash_invalid("Radio inválido")
                return
            # Try float conversion (validator should already help)
            try:
                radio = float(txt)
            except Exception:
                self._flash_invalid("Radio inválido")
                return

            # determine decimal digits from comboBoxDigit (items indicate digits)
            try:
                idx = self.ui.comboBoxDigit.currentIndex()
                decimals = max(1, idx + 1)
            except Exception:
                decimals = 2

            for i in range(1, 7):
                angle = float(i)
                c = radio * (1 - math.sin(math.radians(angle)))
                try:
                    lbl = getattr(self.ui, f"label_valor_{i}")
                    lbl.setText(f"C:{c:.{decimals}f}, R:{radio}, Ángulo:{angle}°")
                except Exception:
                    pass

        except Exception:
            self._flash_invalid("Error al calcular")


    def _clear_japon(self):
        """Clear the `lineEditRadio` and all `label_valor_{i}` labels in frameJapon."""
        try:
            try:
                self.ui.lineEditRadio.clear()
            except Exception:
                pass

            for i in range(1, 7):
                try:
                    lbl = getattr(self.ui, f"label_valor_{i}")
                    lbl.setText("")
                except Exception:
                    pass
        except Exception:
            pass


    def _radio_return_pressed(self):
        """Handler for Enter pressed while `lineEditRadio` has focus.
        Shows pressed style on `pushButtonCalcular` and triggers click.
        """
        try:
            btn = self.ui.pushButtonCalcular
            try:
                btn.setProperty("pressed", True)
                btn.style().unpolish(btn)
                btn.style().polish(btn)
            except Exception:
                pass

            # Try to animate the click to fire clicked(), fallback to direct call
            try:
                btn.animateClick(120)
            except Exception:
                try:
                    self._calculate_japon()
                except Exception:
                    pass

            def _clear():
                try:
                    btn.setProperty("pressed", False)
                    btn.style().unpolish(btn)
                    btn.style().polish(btn)
                except Exception:
                    pass

            QTimer.singleShot(160, _clear)
        except Exception:
            pass


    def _get_decimals(self):
        """Return number of decimal places from `comboBoxDigit` selection.
        Items like '0.1', '0.12', '0.123' map to 1,2,3 decimals respectively.
        """
        try:
            idx = self.ui.comboBoxDigit.currentIndex()
            return max(1, idx + 1)
        except Exception:
            return 2


    def _apply_mode(self, index: int):
        """Show/enable the selected frame based on `comboBoxType`.
        index 0 -> frameCalculator (Estándar), index 1 -> frameJapon.
        """
        try:
            if index == 0:
                # show calculator, hide japon
                self.ui.frameCalculator.setVisible(True)
                self.ui.frameCalculator.setEnabled(True)
                self.ui.frameJapon.setVisible(False)
                self.ui.frameJapon.setEnabled(False)
            else:
                self.ui.frameCalculator.setVisible(False)
                self.ui.frameCalculator.setEnabled(False)
                self.ui.frameJapon.setVisible(True)
                self.ui.frameJapon.setEnabled(True)
        except Exception:
            pass


    def _on_mode_changed(self, index: int):
        """Animate transition between modes (fade out current, fade in target)."""
        try:
            # determine widgets
            from_w = self.ui.frameCalculator if index != 0 else self.ui.frameJapon
            to_w = self.ui.frameJapon if index != 0 else self.ui.frameCalculator

            # If target already visible and enabled, nothing to do
            if to_w.isVisible() and to_w.isEnabled():
                return

            # Ensure to_w is visible and above for animation
            try:
                to_w.setVisible(True)
                to_w.setEnabled(True)
            except Exception:
                pass

            self._animate_switch(from_w, to_w)
        except Exception:
            # fallback to immediate apply
            self._apply_mode(index)


    def _animate_switch(self, from_widget, to_widget, duration=700):
        """Fade out from_widget and fade in to_widget concurrently.
        Duration increased to make transition visibly smooth (default 700ms).
        """
        try:
            # Setup opacity effects
            try:
                from_effect = from_widget.graphicsEffect()
                if not isinstance(from_effect, QGraphicsOpacityEffect):
                    from_effect = QGraphicsOpacityEffect(from_widget)
                    from_widget.setGraphicsEffect(from_effect)
            except Exception:
                from_effect = QGraphicsOpacityEffect(from_widget)
                from_widget.setGraphicsEffect(from_effect)

            try:
                to_effect = to_widget.graphicsEffect()
                if not isinstance(to_effect, QGraphicsOpacityEffect):
                    to_effect = QGraphicsOpacityEffect(to_widget)
                    to_widget.setGraphicsEffect(to_effect)
            except Exception:
                to_effect = QGraphicsOpacityEffect(to_widget)
                to_widget.setGraphicsEffect(to_effect)

            # start values
            from_effect.setOpacity(1.0)
            to_effect.setOpacity(0.0)

            # create animations and run them in parallel to avoid GC issues
            anim_out = QPropertyAnimation(from_effect, b"opacity")
            anim_out.setDuration(duration)
            anim_out.setStartValue(1.0)
            anim_out.setEndValue(0.0)
            anim_out.setEasingCurve(QEasingCurve.InOutCubic)

            anim_in = QPropertyAnimation(to_effect, b"opacity")
            anim_in.setDuration(duration)
            anim_in.setStartValue(0.0)
            anim_in.setEndValue(1.0)
            anim_in.setEasingCurve(QEasingCurve.InOutCubic)

            group = QParallelAnimationGroup(self)
            group.addAnimation(anim_out)
            group.addAnimation(anim_in)

            # When animation finishes, hide the from_widget and cleanup
            def on_finished():
                try:
                    from_widget.setVisible(False)
                    from_widget.setEnabled(False)
                    try:
                        to_widget.graphicsEffect().setOpacity(1.0)
                    except Exception:
                        pass
                except Exception:
                    pass
                # clear stored animation
                try:
                    self._current_animation = None
                except Exception:
                    pass

            group.finished.connect(on_finished)
            # keep reference to avoid GC while running
            self._current_animation = group
            group.start()
        except Exception:
            # fallback immediate
            try:
                from_widget.setVisible(False)
                from_widget.setEnabled(False)
                to_widget.setVisible(True)
                to_widget.setEnabled(True)
            except Exception:
                pass




