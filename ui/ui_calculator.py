# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatorwidgetsCprHV.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_CalculatorWidget(object):
    def setupUi(self, CalculatorWidget):
        if not CalculatorWidget.objectName():
            CalculatorWidget.setObjectName(u"CalculatorWidget")
        CalculatorWidget.resize(650, 1858)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CalculatorWidget.sizePolicy().hasHeightForWidth())
        CalculatorWidget.setSizePolicy(sizePolicy)
        CalculatorWidget.setMinimumSize(QSize(0, 0))
        CalculatorWidget.setMaximumSize(QSize(1000, 16777215))
        CalculatorWidget.setStyleSheet(u"/* ===== CALCULADORA MODERNA CON ENTRADA MANUAL ===== */\n"
"\n"
"#CalculatorWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #0f172a, stop:1 #1e293b);\n"
"}\n"
"\n"
"QFrame[state=\"true\"] {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #0f172a, stop:1 #1e293b);\n"
"	border: 2px solid #55ffff;\n"
" 	border-radius: 20px;\n"
"}\n"
"\n"
"QFrame[state=\"false\"] {\n"
"	border: none;\n"
" 	border-radius: 0;\n"
"}\n"
"\n"
"/* ===== DISPLAY CON ENTRADA MANUAL ===== */\n"
"#displayFrame {\n"
"    background: rgba(30, 41, 59, 0.8);\n"
"    border: 2px solid rgba(59, 130, 246, 0.3);\n"
"    border-radius: 20px;\n"
"    padding: 2%  3%;\n"
"    margin: 2%;\n"
"}\n"
"\n"
"#historyLabel {\n"
"    background: transparent;\n"
"    color: #94a3b8;\n"
"    font-size: clamp(10px, 2vw, 14px);\n"
"    font-weight: 400;\n"
"    border: none;\n"
"    padding: 1%;\n"
"    text-align: right;\n"
"}\n"
"\n"
"#displayLineEdit {\n"
"    background: transparent;\n"
"   "
                        " color: #f8fafc;\n"
"    border: none;\n"
"    font-size: 25px;\n"
"    font-weight: 300;\n"
"    font-family: 'Segoe UI', Arial, sans-serif;\n"
"    padding: 2%;\n"
"    text-align: right;\n"
"    selection-background-color: #3b82f6;\n"
"    selection-color: #ffffff;\n"
"    \n"
"    /* Cursor personalizado */\n"
"    qproperty-cursorPosition: 0;\n"
"}\n"
"\n"
"#displayLineEdit:focus {\n"
"    border-radius: 12px;\n"
"    outline: none;\n"
"\n"
"}\n"
"\n"
"#displayLineEdit::placeholder {\n"
"    color: #64748b;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"/* ===== BOTONES CON BORDER RADIUS ADAPTATIVO ===== */\n"
"\n"
"QPushButton[type=\"number\"] {\n"
"    background: rgba(30, 41, 59, 0.6);\n"
"    color: #e2e8f0;\n"
"    border: 1px solid rgba(59, 130, 246, 0.2);\n"
"    border-radius: 12px;\n"
"    font-size: 22px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QPushButton[type=\"number\"]:hover {\n"
"    background: rgba(51, 65, 85, 0.7);\n"
"}\n"
"\n"
"\n"
"\n"
"/* ===== BOTONES DE OPERACIONES ===== */\n"
"QPushB"
                        "utton[type=\"operator\"] {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #3b82f6, stop:1 #2563eb);\n"
"    color: white;\n"
"	border: 1px solid rgba(59, 130, 246, 0.2);\n"
"    border-radius: 12px;\n"
"    min-height: 40px;\n"
"	min-width:50px\n"
"}\n"
"\n"
"QPushButton[type=\"operator\"]:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #60a5fa, stop:1 #3b82f6);\n"
"}\n"
"\n"
"\n"
"/* ===== BOT\u00d3N IGUAL DESTACADO ===== */\n"
"QPushButton#btnEquals {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #10b981, stop:1 #059669);\n"
"    color: #ffffff;\n"
"   border: 1px solid rgba(59, 130, 246, 0.2);\n"
"    border-radius: 12px; \n"
"    padding: 0;\n"
"    font-size: clamp(18px, 4vw, 32px);\n"
"    font-weight: 700;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QPushButton#btnEquals:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #34d399, stop:1 #10b981);\n"
"}\n"
"\n"
"/* ===="
                        "= BOTONES ESPECIALES ===== */\n"
"QPushButton[type=\"special\"] {\n"
"    background: #aca412;\n"
"    color: #272727;\n"
"   border: 1px solid rgba(59, 130, 246, 0.2);\n"
"    border-radius: 12px; \n"
"    padding: 0;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    min-height: 40px; \n"
"}\n"
"\n"
"QPushButton[type=\"special\"]:hover {\n"
"    background: #e5e825;\n"
"    border-color: rgba(148, 163, 184, 0.5);\n"
"}\n"
"\n"
"QPushButton:pressed {}\n"
"\n"
"QPushButton[pressed=\"true\"] {\n"
"    border: 1px solid #55ffff;\n"
"}\n"
"\n"
"QPushButton[pressed=\"false\"] {\n"
"    border: 1px solid rgba(59, 130, 246, 0.2);\n"
"}\n"
"\n"
"QFrame[invalid=\"true\"]#displayFrame {\n"
"	border: 2px solid #ff5555;\n"
"}\n"
"\n"
"QFrame[invalid=\"false\"]#displayFrame {\n"
"	border: 2px solid rgba(59, 130, 246, 0.3);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#lbl_Type, #lbl_digit, #Conversiones, #lblFJapon, #labelRadio {\n"
"    /* Color de texto y tipograf\u00eda */\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe"
                        " UI Variable\", \"Inter\", sans-serif;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"\n"
"    /* Fondo: Gradiente sutil que nace del color de acento */\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, \n"
"                                stop:0 rgba(74, 144, 226, 0.15), \n"
"                                stop:0.6 rgba(45, 45, 45, 0.4), \n"
"                                stop:1 transparent);\n"
"\n"
"    /* Bordes redondeados y borde de acento */\n"
"    border-left: 4px solid #4a90e2; /* El resalte lateral */\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    border-top-left-radius: 8px;    /* Un radio peque\u00f1o para no romper la l\u00ednea vertical */\n"
"    border-bottom-left-radius: 8px;\n"
"\n"
"    /* Espaciado para que no se vea apretado */\n"
"    padding: 6px 15px 6px 12px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"/* Estilo base del QComboBox */\n"
"QComboBox[type=\"combo-box\"] {\n"
"    border: 2px solid #3d3d3d;\n"
"    border-radius: "
                        "8px;\n"
"    padding: 5px 35px 5px 15px; /* El padding derecho reserva espacio para el SVG */\n"
"    color: #ffffff;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #2e2e2e, stop:1 #1a1a1a);\n"
"    selection-background-color: #4a90e2;\n"
"}\n"
"\n"
"QComboBox[type=\"combo-box\"]:hover {\n"
"    border: 2px solid #5c5c5c;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #383838, stop:1 #242424);\n"
"}\n"
"\n"
"QComboBox[type=\"combo-box\"]:focus {\n"
"    border: 2px solid #4a90e2;\n"
"    background: #1a1a1a;\n"
"}\n"
"\n"
"/* Contenedor del bot\u00f3n de despliegue */\n"
"QComboBox[type=\"combo-box\"]::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left: none;\n"
"}\n"
"\n"
"/* LA FLECHA SVG */\n"
"QComboBox[type=\"combo-box\"]::down-arrow {\n"
"    /* Aseg\u00farate de que la ruta sea correcta seg\u00fan tu archivo .qrc *"
                        "/\n"
"    image: url(:/iconos/iconos/chevron-down.svg); \n"
"    width: 14px;  /* Tama\u00f1o del icono */\n"
"    height: 14px;\n"
"}\n"
"\n"
"/* Efecto opcional: Cambiar la flecha cuando el men\u00fa est\u00e1 desplegado */\n"
"QComboBox[type=\"combo-box\"]::down-arrow:on {\n"
"    top: 1px; /* Peque\u00f1o desplazamiento al hacer click */\n"
"}\n"
"\n"
"/* Flecha para estado desactivado (opcional) */\n"
"QComboBox[type=\"combo-box\"]::down-arrow:disabled {\n"
"    image: url(:/icons/chevron-down-gray.svg);\n"
"}\n"
"\n"
"/* Estilo del men\u00fa desplegable (la lista) */\n"
"QComboBox[type=\"combo-box\"] QAbstractItemView {\n"
"    border: 2px solid #4a90e2;\n"
"    background-color: #1a1a1a;\n"
"    color: #ffffff;\n"
"    selection-background-color: #4a90e2;\n"
"    selection-color: #ffffff;\n"
"    outline: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox[type=\"combo-box\"] QAbstractItemView::item {\n"
"    min-height: 30px;\n"
"    padding-left: 10px;\n"
"    border-radius"
                        ": 4px;\n"
"}\n"
"\n"
"QComboBox[type=\"combo-box\"] QAbstractItemView::item:selected {\n"
"    background-color: #4a90e2;\n"
"}\n"
"\n"
"\n"
"/* Estilo base para todas las tarjetas (QFrame) */\n"
"#card1, #card2, #card3, #card4 {\n"
"    background-color: white;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"/* Colores espec\u00edficos usando propiedades din\u00e1micas */\n"
"QFrame[clase=\"azul\"] { border-top: 6px solid #3498db; }\n"
"QFrame[clase=\"rojo\"] { border-top: 6px solid #e74c3c; }\n"
"QFrame[clase=\"amarillo\"] { border-top: 6px solid #f1c40f; }\n"
"QFrame[clase=\"morado\"] { border-top: 6px solid #9b59b6; }\n"
"\n"
"\n"
"\n"
"#buttonsFrame, #guiasFrame, #frameOnlyCalculator {\n"
"	 background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #0f172a, stop:1 #1e293b);\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"\n"
"/* Estilo para los t\u00edtulos (Labels) */\n"
"QLabel[conversor=\"unidad\"] {\n"
"	background-color: white;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    color: #2c3e"
                        "50;\n"
"    margin-bottom: 5px;\n"
"}\n"
"\n"
"/* Estilo para la caja de la f\u00f3rmula */\n"
"#formula_1, #formula_2, \n"
"#formula_3, #formula_4 {\n"
"    background-color: #f8f9fa;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-family: 'Courier New';\n"
"    font-weight: bold;\n"
"    color: #d35400;\n"
"}\n"
"\n"
"/* Estilo para el ejemplo */\n"
"#ejemplo_1, #ejemplo_2,\n"
"#ejemplo_3, #ejemplo_4 {\n"
"	background-color: rgb(255, 255, 255);\n"
"    color: #383838;\n"
"    font-size: 12px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"/* Resalte del resultado en verde */\n"
"#resultado_1, #resultado_2,\n"
"#resultado_3, #resultado_4 {\n"
"    color: #27ae60;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"/* \n"
"   ESTILO: CYBER-GLASS UI 2025\n"
"   Enfoque: Minimalismo tecnol\u00f3gico, Glassmorphism y jerarqu\u00eda visual.\n"
"*/\n"
"\n"
"/* ---------- VENTANA PRINCIPAL ---------- */\n"
"QFrame#frameJapon {\n"
"   background: qlineargradient(x1:0, y1:0, x2:1"
                        ", y2:1,\n"
"        stop:0 #0f172a, stop:1 #1e293b);\n"
"	border-radius:15px;\n"
"	font-family: \"Segoe UI Variable\", \"Inter\", sans-serif;\n"
"}\n"
"\n"
"/* --- AHORA ES UN QLineEdit --- */\n"
"QLineEdit#lineEditRadio {\n"
"    background: rgba(255, 255, 255, 0.05);\n"
"    color: #00e5ff; /* Color cian para el n\u00famero ingresado */\n"
"    border: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-radius: 15px;\n"
"    \n"
"    min-height: 40px;      /* Alto generoso estilo moderno */\n"
"    font-size: 15px;       /* Fuente grande y legible */\n"
"    font-weight: 700;\n"
"    padding-left: 15px;    /* Espacio a la izquierda */\n"
"    padding-right: 15px;   /* Espacio a la derecha */\n"
"    \n"
"    selection-background-color: #00e5ff; /* Color de selecci\u00f3n */\n"
"    selection-color: #05050a;            /* Color del texto seleccionado */\n"
"}\n"
"\n"
"QLineEdit#lineEditRadio:hover {\n"
"    border: 1px solid rgba(0, 229, 255, 0.5);\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"}\n"
"\n"
""
                        "QLineEdit#lineEditRadio:focus {\n"
"    border: 1px solid #00e5ff; /* Borde brillante al escribir */\n"
"    background: rgba(0, 229, 255, 0.05);\n"
"}\n"
"\n"
"/* ---------- BOT\u00d3N CALCULAR (EFECTO NE\u00d3N) ---------- */\n"
"QPushButton#pushButtonCalcular, QPushButton#clear_fj  {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, \n"
"                                stop:0 #246c35, stop:1 #35a24f);\n"
"    color:#eaeaea;\n"
"    font-size: 12px;\n"
"    font-weight: 900;\n"
"    border: none;\n"
"    border-radius: 14px;\n"
"    padding: 12px 30px;\n"
"    text-transform: uppercase;\n"
"    letter-spacing: 1px;\n"
"}\n"
"\n"
"QPushButton#pushButtonCalcular:hover, QPushButton#clear_fj:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, \n"
"                                stop:0 #005d44, stop:1 #007352);\n"
"}\n"
"\n"
"QPushButton#pushButtonCalcular:pressed, QPushButton#clear_fj:pressed {\n"
"    background: #006100;\n"
"}\n"
"\n"
"/* ---------- TARJETAS (GLASSMORPHISM AVANZADO) "
                        "---------- */\n"
"QFrame[class=\"tarjeta-angle\"] {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 rgba(255, 255, 255, 0.06), \n"
"                                stop:1 rgba(255, 255, 255, 0.02));\n"
"    border: 1px solid rgba(255, 255, 255, 0.08);\n"
"    border-top: 1px solid rgba(255, 255, 255, 0.15); /* Brillo en el borde superior */\n"
"    border-radius: 24px;\n"
"    padding: 20px;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QFrame[class=\"tarjeta-angle\"]:hover {\n"
"    background: rgba(255, 255, 255, 0.08);\n"
"    border: 1px solid rgba(0, 229, 255, 0.4);\n"
"}\n"
"\n"
"/* ---------- TEXTOS DE TARJETA ---------- */\n"
"\n"
"/* El nombre del \u00e1ngulo (Badge Style) */\n"
"QLabel[name=\"number-angle\"] {\n"
"    color: #00e5ff;\n"
"    font-size: 15px;\n"
"    font-weight: 800;\n"
"    text-transform: uppercase;\n"
"    letter-spacing: 1.5px;\n"
"    background: rgba(0, 229, 255, 0.12);\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    "
                        "max-height: 20px;\n"
"}\n"
"\n"
"/* El valor num\u00e9rico (Thin Modern Style) */\n"
"QLabel[valor=\"angle-c\"] {\n"
"    color: #ffffff;\n"
"    font-size: 38px;\n"
"    font-weight: 200;\n"
"    background: transparent;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(CalculatorWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedorPrincipal = QFrame(CalculatorWidget)
        self.contenedorPrincipal.setObjectName(u"contenedorPrincipal")
        self.contenedorPrincipal.setMinimumSize(QSize(650, 0))
        self.contenedorPrincipal.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenedorPrincipal.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.contenedorPrincipal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frameOptions = QFrame(self.contenedorPrincipal)
        self.frameOptions.setObjectName(u"frameOptions")
        self.frameOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frameOptions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameType = QFrame(self.frameOptions)
        self.frameType.setObjectName(u"frameType")
        self.frameType.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameType.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frameType)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(8)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_Type = QLabel(self.frameType)
        self.lbl_Type.setObjectName(u"lbl_Type")
        self.lbl_Type.setWordWrap(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_Type)

        self.lbl_digit = QLabel(self.frameType)
        self.lbl_digit.setObjectName(u"lbl_digit")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_digit)

        self.comboBoxDigit = QComboBox(self.frameType)
        self.comboBoxDigit.addItem("")
        self.comboBoxDigit.addItem("")
        self.comboBoxDigit.addItem("")
        self.comboBoxDigit.addItem("")
        self.comboBoxDigit.addItem("")
        self.comboBoxDigit.setObjectName(u"comboBoxDigit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBoxDigit)

        self.comboBoxType = QComboBox(self.frameType)
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.comboBoxType.setObjectName(u"comboBoxType")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxType)


        self.verticalLayout.addWidget(self.frameType)


        self.verticalLayout_4.addWidget(self.frameOptions)

        self.contendorWidgetCalculators = QFrame(self.contenedorPrincipal)
        self.contendorWidgetCalculators.setObjectName(u"contendorWidgetCalculators")
        self.contendorWidgetCalculators.setFrameShape(QFrame.Shape.StyledPanel)
        self.contendorWidgetCalculators.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.contendorWidgetCalculators)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameCalculator = QFrame(self.contendorWidgetCalculators)
        self.frameCalculator.setObjectName(u"frameCalculator")
        self.frameCalculator.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameCalculator.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameCalculator)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frameOnlyCalculator = QFrame(self.frameCalculator)
        self.frameOnlyCalculator.setObjectName(u"frameOnlyCalculator")
        self.frameOnlyCalculator.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameOnlyCalculator.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameOnlyCalculator)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.displayFrame = QFrame(self.frameOnlyCalculator)
        self.displayFrame.setObjectName(u"displayFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.displayFrame.sizePolicy().hasHeightForWidth())
        self.displayFrame.setSizePolicy(sizePolicy1)
        self.displayLayout = QVBoxLayout(self.displayFrame)
        self.displayLayout.setSpacing(2)
        self.displayLayout.setObjectName(u"displayLayout")
        self.displayLayout.setContentsMargins(15, 15, 15, 15)
        self.displayLineEdit = QLineEdit(self.displayFrame)
        self.displayLineEdit.setObjectName(u"displayLineEdit")
        sizePolicy1.setHeightForWidth(self.displayLineEdit.sizePolicy().hasHeightForWidth())
        self.displayLineEdit.setSizePolicy(sizePolicy1)
        self.displayLineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.displayLineEdit.setReadOnly(False)
        self.displayLineEdit.setClearButtonEnabled(False)

        self.displayLayout.addWidget(self.displayLineEdit)


        self.verticalLayout_6.addWidget(self.displayFrame)

        self.buttonsFrame = QFrame(self.frameOnlyCalculator)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buttonsFrame.sizePolicy().hasHeightForWidth())
        self.buttonsFrame.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.buttonsFrame)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.btn_clear = QPushButton(self.buttonsFrame)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy1.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_CE = QPushButton(self.buttonsFrame)
        self.btn_CE.setObjectName(u"btn_CE")
        sizePolicy1.setHeightForWidth(self.btn_CE.sizePolicy().hasHeightForWidth())
        self.btn_CE.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_CE, 0, 1, 1, 1)

        self.btn_back = QPushButton(self.buttonsFrame)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy1.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_back, 0, 2, 1, 1)

        self.btn_div = QPushButton(self.buttonsFrame)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy1.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_7 = QPushButton(self.buttonsFrame)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QPushButton(self.buttonsFrame)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.buttonsFrame)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_mul = QPushButton(self.buttonsFrame)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy1.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_4 = QPushButton(self.buttonsFrame)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(self.buttonsFrame)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(self.buttonsFrame)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_minus = QPushButton(self.buttonsFrame)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy1.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_1 = QPushButton(self.buttonsFrame)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_2 = QPushButton(self.buttonsFrame)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(self.buttonsFrame)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_plus = QPushButton(self.buttonsFrame)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy1.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_0 = QPushButton(self.buttonsFrame)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy1.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 1)

        self.btn_dot = QPushButton(self.buttonsFrame)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy1.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_dot, 4, 1, 1, 1)

        self.btn_neg_plus = QPushButton(self.buttonsFrame)
        self.btn_neg_plus.setObjectName(u"btn_neg_plus")
        sizePolicy1.setHeightForWidth(self.btn_neg_plus.sizePolicy().hasHeightForWidth())
        self.btn_neg_plus.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_neg_plus, 4, 2, 1, 1)

        self.btnEquals = QPushButton(self.buttonsFrame)
        self.btnEquals.setObjectName(u"btnEquals")
        sizePolicy1.setHeightForWidth(self.btnEquals.sizePolicy().hasHeightForWidth())
        self.btnEquals.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btnEquals, 4, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.buttonsFrame)


        self.horizontalLayout_2.addWidget(self.frameOnlyCalculator)

        self.guiasFrame = QFrame(self.frameCalculator)
        self.guiasFrame.setObjectName(u"guiasFrame")
        self.guiasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.guiasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.guiasFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Conversiones = QLabel(self.guiasFrame)
        self.Conversiones.setObjectName(u"Conversiones")

        self.verticalLayout_5.addWidget(self.Conversiones)

        self.card2 = QFrame(self.guiasFrame)
        self.card2.setObjectName(u"card2")
        self.vboxLayout = QVBoxLayout(self.card2)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.titulo_2 = QLabel(self.card2)
        self.titulo_2.setObjectName(u"titulo_2")

        self.vboxLayout.addWidget(self.titulo_2)

        self.formula_2 = QLabel(self.card2)
        self.formula_2.setObjectName(u"formula_2")
        self.formula_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.formula_2)

        self.ejemplo_2 = QLabel(self.card2)
        self.ejemplo_2.setObjectName(u"ejemplo_2")

        self.vboxLayout.addWidget(self.ejemplo_2)


        self.verticalLayout_5.addWidget(self.card2)

        self.card1 = QFrame(self.guiasFrame)
        self.card1.setObjectName(u"card1")
        self._2 = QVBoxLayout(self.card1)
        self._2.setObjectName(u"_2")
        self.titulo_1 = QLabel(self.card1)
        self.titulo_1.setObjectName(u"titulo_1")

        self._2.addWidget(self.titulo_1)

        self.formula_1 = QLabel(self.card1)
        self.formula_1.setObjectName(u"formula_1")
        self.formula_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._2.addWidget(self.formula_1)

        self.ejemplo_1 = QLabel(self.card1)
        self.ejemplo_1.setObjectName(u"ejemplo_1")

        self._2.addWidget(self.ejemplo_1)


        self.verticalLayout_5.addWidget(self.card1)

        self.card4 = QFrame(self.guiasFrame)
        self.card4.setObjectName(u"card4")
        self._3 = QVBoxLayout(self.card4)
        self._3.setObjectName(u"_3")
        self.titulo_4 = QLabel(self.card4)
        self.titulo_4.setObjectName(u"titulo_4")

        self._3.addWidget(self.titulo_4)

        self.formula_4 = QLabel(self.card4)
        self.formula_4.setObjectName(u"formula_4")
        self.formula_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._3.addWidget(self.formula_4)

        self.ejemplo_4 = QLabel(self.card4)
        self.ejemplo_4.setObjectName(u"ejemplo_4")

        self._3.addWidget(self.ejemplo_4)


        self.verticalLayout_5.addWidget(self.card4)

        self.card3 = QFrame(self.guiasFrame)
        self.card3.setObjectName(u"card3")
        self._4 = QVBoxLayout(self.card3)
        self._4.setObjectName(u"_4")
        self.titulo_3 = QLabel(self.card3)
        self.titulo_3.setObjectName(u"titulo_3")

        self._4.addWidget(self.titulo_3)

        self.formula_3 = QLabel(self.card3)
        self.formula_3.setObjectName(u"formula_3")
        self.formula_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._4.addWidget(self.formula_3)

        self.ejemplo_3 = QLabel(self.card3)
        self.ejemplo_3.setObjectName(u"ejemplo_3")

        self._4.addWidget(self.ejemplo_3)


        self.verticalLayout_5.addWidget(self.card3)


        self.horizontalLayout_2.addWidget(self.guiasFrame)


        self.verticalLayout_3.addWidget(self.frameCalculator)

        self.frameAngle = QFrame(self.contendorWidgetCalculators)
        self.frameAngle.setObjectName(u"frameAngle")
        self.frameAngle.setMaximumSize(QSize(0, 0))
        self.frameAngle.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAngle.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.frameAngle)

        self.frameJapon = QFrame(self.contendorWidgetCalculators)
        self.frameJapon.setObjectName(u"frameJapon")
        self.frameJapon.setMaximumSize(QSize(16777215, 16777215))
        self.frameJapon.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameJapon.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frameJapon)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.topBar = QHBoxLayout()
        self.topBar.setObjectName(u"topBar")
        self.labelRadio = QLabel(self.frameJapon)
        self.labelRadio.setObjectName(u"labelRadio")

        self.topBar.addWidget(self.labelRadio)

        self.lineEditRadio = QLineEdit(self.frameJapon)
        self.lineEditRadio.setObjectName(u"lineEditRadio")

        self.topBar.addWidget(self.lineEditRadio)

        self.pushButtonCalcular = QPushButton(self.frameJapon)
        self.pushButtonCalcular.setObjectName(u"pushButtonCalcular")
        icon = QIcon()
        icon.addFile(u":/iconos/iconos/codesandbox.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonCalcular.setIcon(icon)
        self.pushButtonCalcular.setIconSize(QSize(20, 20))

        self.topBar.addWidget(self.pushButtonCalcular)

        self.clear_fj = QPushButton(self.frameJapon)
        self.clear_fj.setObjectName(u"clear_fj")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/iconos/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_fj.setIcon(icon1)
        self.clear_fj.setIconSize(QSize(20, 20))

        self.topBar.addWidget(self.clear_fj)


        self.verticalLayout_12.addLayout(self.topBar)

        self.lblFJapon = QLabel(self.frameJapon)
        self.lblFJapon.setObjectName(u"lblFJapon")
        self.lblFJapon.setMinimumSize(QSize(450, 40))
        self.lblFJapon.setMaximumSize(QSize(450, 50))
        self.lblFJapon.setPixmap(QPixmap(u":/iconos/iconos/formula-japon.svg"))
        self.lblFJapon.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.lblFJapon, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tarjeta_angulo_1 = QFrame(self.frameJapon)
        self.tarjeta_angulo_1.setObjectName(u"tarjeta_angulo_1")
        self.tarjeta_angulo_1.setMinimumSize(QSize(0, 0))
        self.tarjeta_angulo_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_2 = QVBoxLayout(self.tarjeta_angulo_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_titulo_1 = QLabel(self.tarjeta_angulo_1)
        self.label_titulo_1.setObjectName(u"label_titulo_1")
        self.label_titulo_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_titulo_1)

        self.label_valor_1 = QLabel(self.tarjeta_angulo_1)
        self.label_valor_1.setObjectName(u"label_valor_1")
        self.label_valor_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_valor_1)


        self.verticalLayout_12.addWidget(self.tarjeta_angulo_1)

        self.tarjeta_angulo_2 = QFrame(self.frameJapon)
        self.tarjeta_angulo_2.setObjectName(u"tarjeta_angulo_2")
        self.tarjeta_angulo_2.setMinimumSize(QSize(0, 0))
        self.tarjeta_angulo_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_11 = QVBoxLayout(self.tarjeta_angulo_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_titulo_2 = QLabel(self.tarjeta_angulo_2)
        self.label_titulo_2.setObjectName(u"label_titulo_2")
        self.label_titulo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_titulo_2)

        self.label_valor_2 = QLabel(self.tarjeta_angulo_2)
        self.label_valor_2.setObjectName(u"label_valor_2")
        self.label_valor_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_valor_2)


        self.verticalLayout_12.addWidget(self.tarjeta_angulo_2)

        self.tarjeta_angulo_3 = QFrame(self.frameJapon)
        self.tarjeta_angulo_3.setObjectName(u"tarjeta_angulo_3")
        self.tarjeta_angulo_3.setMinimumSize(QSize(0, 0))
        self.tarjeta_angulo_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_9 = QVBoxLayout(self.tarjeta_angulo_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_titulo_3 = QLabel(self.tarjeta_angulo_3)
        self.label_titulo_3.setObjectName(u"label_titulo_3")
        self.label_titulo_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_titulo_3)

        self.label_valor_3 = QLabel(self.tarjeta_angulo_3)
        self.label_valor_3.setObjectName(u"label_valor_3")
        self.label_valor_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_valor_3)


        self.verticalLayout_12.addWidget(self.tarjeta_angulo_3)

        self.tarjeta_angulo_4 = QFrame(self.frameJapon)
        self.tarjeta_angulo_4.setObjectName(u"tarjeta_angulo_4")
        self.tarjeta_angulo_4.setMinimumSize(QSize(0, 0))
        self.tarjeta_angulo_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_8 = QVBoxLayout(self.tarjeta_angulo_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_titulo_4 = QLabel(self.tarjeta_angulo_4)
        self.label_titulo_4.setObjectName(u"label_titulo_4")
        self.label_titulo_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_titulo_4)

        self.label_valor_4 = QLabel(self.tarjeta_angulo_4)
        self.label_valor_4.setObjectName(u"label_valor_4")
        self.label_valor_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_valor_4)


        self.verticalLayout_12.addWidget(self.tarjeta_angulo_4)

        self.tarjeta_angulo_5 = QFrame(self.frameJapon)
        self.tarjeta_angulo_5.setObjectName(u"tarjeta_angulo_5")
        self.tarjeta_angulo_5.setMinimumSize(QSize(0, 0))
        self.tarjeta_angulo_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_7 = QVBoxLayout(self.tarjeta_angulo_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_titulo_5 = QLabel(self.tarjeta_angulo_5)
        self.label_titulo_5.setObjectName(u"label_titulo_5")
        self.label_titulo_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_titulo_5)

        self.label_valor_5 = QLabel(self.tarjeta_angulo_5)
        self.label_valor_5.setObjectName(u"label_valor_5")
        self.label_valor_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_valor_5)


        self.verticalLayout_12.addWidget(self.tarjeta_angulo_5)

        self.tarjeta_angulo_6 = QFrame(self.frameJapon)
        self.tarjeta_angulo_6.setObjectName(u"tarjeta_angulo_6")
        self.tarjeta_angulo_6.setMinimumSize(QSize(0, 0))
        self.tarjeta_angulo_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_10 = QVBoxLayout(self.tarjeta_angulo_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_titulo_6 = QLabel(self.tarjeta_angulo_6)
        self.label_titulo_6.setObjectName(u"label_titulo_6")
        self.label_titulo_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_titulo_6)

        self.label_valor_6 = QLabel(self.tarjeta_angulo_6)
        self.label_valor_6.setObjectName(u"label_valor_6")
        self.label_valor_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_valor_6)


        self.verticalLayout_12.addWidget(self.tarjeta_angulo_6)


        self.verticalLayout_3.addWidget(self.frameJapon)


        self.verticalLayout_4.addWidget(self.contendorWidgetCalculators)


        self.horizontalLayout.addWidget(self.contenedorPrincipal, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(CalculatorWidget)

        QMetaObject.connectSlotsByName(CalculatorWidget)
    # setupUi

    def retranslateUi(self, CalculatorWidget):
        CalculatorWidget.setWindowTitle(QCoreApplication.translate("CalculatorWidget", u"Calculadora Moderna", None))
        self.lbl_Type.setText(QCoreApplication.translate("CalculatorWidget", u"Tipo de Calculadora", None))
        self.lbl_digit.setText(QCoreApplication.translate("CalculatorWidget", u"N\u00famero de D\u00edgitos Decimales:", None))
        self.comboBoxDigit.setItemText(0, QCoreApplication.translate("CalculatorWidget", u"0.1", None))
        self.comboBoxDigit.setItemText(1, QCoreApplication.translate("CalculatorWidget", u"0.12", None))
        self.comboBoxDigit.setItemText(2, QCoreApplication.translate("CalculatorWidget", u"0.123", None))
        self.comboBoxDigit.setItemText(3, QCoreApplication.translate("CalculatorWidget", u"0.1234", None))
        self.comboBoxDigit.setItemText(4, QCoreApplication.translate("CalculatorWidget", u"0.12345", None))

        self.comboBoxDigit.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"combo-box", None))
        self.comboBoxType.setItemText(0, QCoreApplication.translate("CalculatorWidget", u"Est\u00e1ndar", None))
        self.comboBoxType.setItemText(1, QCoreApplication.translate("CalculatorWidget", u"Formula De Japon", None))

        self.comboBoxType.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"combo-box", None))
        self.frameCalculator.setProperty(u"state", QCoreApplication.translate("CalculatorWidget", u"true", None))
        self.displayFrame.setProperty(u"invalid", QCoreApplication.translate("CalculatorWidget", u"true", None))
        self.displayLineEdit.setPlaceholderText(QCoreApplication.translate("CalculatorWidget", u"0", None))
        self.buttonsFrame.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btn_clear.setText(QCoreApplication.translate("CalculatorWidget", u"C", None))
        self.btn_clear.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btn_clear.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"clear", None))
        self.btn_clear.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btn_clear.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_CE.setText(QCoreApplication.translate("CalculatorWidget", u"CE", None))
        self.btn_CE.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btn_CE.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btn_CE.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"ce", None))
        self.btn_CE.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_back.setText(QCoreApplication.translate("CalculatorWidget", u"\u232b", None))
        self.btn_back.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btn_back.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btn_back.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"back", None))
        self.btn_back.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_div.setText(QCoreApplication.translate("CalculatorWidget", u"\u00f7", None))
        self.btn_div.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_div.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_div.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"/", None))
        self.btn_div.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_7.setText(QCoreApplication.translate("CalculatorWidget", u"7", None))
        self.btn_7.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_7.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_7.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"7", None))
        self.btn_7.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_8.setText(QCoreApplication.translate("CalculatorWidget", u"8", None))
        self.btn_8.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_8.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_8.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"8", None))
        self.btn_8.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_9.setText(QCoreApplication.translate("CalculatorWidget", u"9", None))
        self.btn_9.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_9.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_9.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"9", None))
        self.btn_9.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_mul.setText(QCoreApplication.translate("CalculatorWidget", u"\u00d7", None))
        self.btn_mul.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_mul.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_mul.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"*", None))
        self.btn_mul.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_4.setText(QCoreApplication.translate("CalculatorWidget", u"4", None))
        self.btn_4.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_4.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_4.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"4", None))
        self.btn_4.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_5.setText(QCoreApplication.translate("CalculatorWidget", u"5", None))
        self.btn_5.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_5.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_5.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"5", None))
        self.btn_5.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_6.setText(QCoreApplication.translate("CalculatorWidget", u"6", None))
        self.btn_6.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_6.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_6.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"6", None))
        self.btn_6.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_minus.setText(QCoreApplication.translate("CalculatorWidget", u"-", None))
        self.btn_minus.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_minus.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_minus.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"-", None))
        self.btn_minus.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_1.setText(QCoreApplication.translate("CalculatorWidget", u"1", None))
        self.btn_1.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_1.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_1.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"1", None))
        self.btn_1.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_2.setText(QCoreApplication.translate("CalculatorWidget", u"2", None))
        self.btn_2.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_2.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_2.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"2", None))
        self.btn_2.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_3.setText(QCoreApplication.translate("CalculatorWidget", u"3", None))
        self.btn_3.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_3.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_3.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"3", None))
        self.btn_3.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_plus.setText(QCoreApplication.translate("CalculatorWidget", u"+", None))
        self.btn_plus.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_plus.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_plus.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"+", None))
        self.btn_plus.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_0.setText(QCoreApplication.translate("CalculatorWidget", u"0", None))
        self.btn_0.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_0.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"number", None))
        self.btn_0.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"0", None))
        self.btn_0.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_dot.setText(QCoreApplication.translate("CalculatorWidget", u".", None))
        self.btn_dot.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btn_dot.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btn_dot.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"dot", None))
        self.btn_dot.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btn_neg_plus.setText(QCoreApplication.translate("CalculatorWidget", u"\u00b1", None))
        self.btn_neg_plus.setProperty(u"type", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_neg_plus.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"operator", None))
        self.btn_neg_plus.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.btnEquals.setText(QCoreApplication.translate("CalculatorWidget", u"=", None))
        self.btnEquals.setProperty(u"role", QCoreApplication.translate("CalculatorWidget", u"special", None))
        self.btnEquals.setProperty(u"value", QCoreApplication.translate("CalculatorWidget", u"equals", None))
        self.btnEquals.setProperty(u"pressed", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.Conversiones.setText(QCoreApplication.translate("CalculatorWidget", u"Formulario de Conversiones", None))
        self.card2.setProperty(u"clase", QCoreApplication.translate("CalculatorWidget", u"rojo", None))
        self.titulo_2.setText(QCoreApplication.translate("CalculatorWidget", u"Pulgadas a mm", None))
        self.titulo_2.setProperty(u"conversor", QCoreApplication.translate("CalculatorWidget", u"unidad", None))
        self.formula_2.setText(QCoreApplication.translate("CalculatorWidget", u"(VALOR en pulg) \u00d7 25.4", None))
        self.ejemplo_2.setText(QCoreApplication.translate("CalculatorWidget", u"Ejemplo: 2 in = 50.8 mm", None))
        self.card1.setProperty(u"clase", QCoreApplication.translate("CalculatorWidget", u"azul", None))
        self.titulo_1.setText(QCoreApplication.translate("CalculatorWidget", u"mm a Pulgadas", None))
        self.titulo_1.setProperty(u"conversor", QCoreApplication.translate("CalculatorWidget", u"unidad", None))
        self.formula_1.setText(QCoreApplication.translate("CalculatorWidget", u"(VALOR en mm) \u00f7 25.4", None))
        self.ejemplo_1.setText(QCoreApplication.translate("CalculatorWidget", u"Ejemplo: 25.4 mm = 1 in", None))
        self.card4.setProperty(u"clase", QCoreApplication.translate("CalculatorWidget", u"morado", None))
        self.titulo_4.setText(QCoreApplication.translate("CalculatorWidget", u"Grados a Minutos", None))
        self.titulo_4.setProperty(u"conversor", QCoreApplication.translate("CalculatorWidget", u"unidad", None))
        self.formula_4.setText(QCoreApplication.translate("CalculatorWidget", u"(VALOR en grados) \u00d7 60", None))
        self.ejemplo_4.setText(QCoreApplication.translate("CalculatorWidget", u"Ejemplo: 1\u00b0 = 60'", None))
        self.card3.setProperty(u"clase", QCoreApplication.translate("CalculatorWidget", u"amarillo", None))
        self.titulo_3.setText(QCoreApplication.translate("CalculatorWidget", u"cm a mm", None))
        self.titulo_3.setProperty(u"conversor", QCoreApplication.translate("CalculatorWidget", u"unidad", None))
        self.formula_3.setText(QCoreApplication.translate("CalculatorWidget", u"(VALOR en cm \u00d7 10)", None))
        self.ejemplo_3.setText(QCoreApplication.translate("CalculatorWidget", u"Ejemplo: 5 cm = 50 mm", None))
        self.frameAngle.setProperty(u"state", QCoreApplication.translate("CalculatorWidget", u"false", None))
        self.frameJapon.setProperty(u"state", QCoreApplication.translate("CalculatorWidget", u"true", None))
        self.labelRadio.setText(QCoreApplication.translate("CalculatorWidget", u"Radio (R):", None))
        self.lineEditRadio.setPlaceholderText(QCoreApplication.translate("CalculatorWidget", u"Introduzca el radio aqu\u00ed", None))
        self.pushButtonCalcular.setText(QCoreApplication.translate("CalculatorWidget", u"Calcular", None))
        self.clear_fj.setText("")
        self.lblFJapon.setText("")
        self.tarjeta_angulo_1.setProperty(u"class", QCoreApplication.translate("CalculatorWidget", u"tarjeta-angle", None))
        self.label_titulo_1.setText(QCoreApplication.translate("CalculatorWidget", u"\u00c1ngulo 1", None))
        self.label_titulo_1.setProperty(u"name", QCoreApplication.translate("CalculatorWidget", u"number-angle", None))
        self.label_valor_1.setText("")
        self.label_valor_1.setProperty(u"valor", QCoreApplication.translate("CalculatorWidget", u"angle-c", None))
        self.tarjeta_angulo_2.setProperty(u"class", QCoreApplication.translate("CalculatorWidget", u"tarjeta-angle", None))
        self.label_titulo_2.setText(QCoreApplication.translate("CalculatorWidget", u"\u00c1ngulo 2", None))
        self.label_titulo_2.setProperty(u"name", QCoreApplication.translate("CalculatorWidget", u"number-angle", None))
        self.label_valor_2.setText("")
        self.label_valor_2.setProperty(u"valor", QCoreApplication.translate("CalculatorWidget", u"angle-c", None))
        self.tarjeta_angulo_3.setProperty(u"class", QCoreApplication.translate("CalculatorWidget", u"tarjeta-angle", None))
        self.label_titulo_3.setText(QCoreApplication.translate("CalculatorWidget", u"\u00c1ngulo 3", None))
        self.label_titulo_3.setProperty(u"name", QCoreApplication.translate("CalculatorWidget", u"number-angle", None))
        self.label_valor_3.setText("")
        self.label_valor_3.setProperty(u"valor", QCoreApplication.translate("CalculatorWidget", u"angle-c", None))
        self.tarjeta_angulo_4.setProperty(u"class", QCoreApplication.translate("CalculatorWidget", u"tarjeta-angle", None))
        self.label_titulo_4.setText(QCoreApplication.translate("CalculatorWidget", u"\u00c1ngulo 4", None))
        self.label_titulo_4.setProperty(u"name", QCoreApplication.translate("CalculatorWidget", u"number-angle", None))
        self.label_valor_4.setText("")
        self.label_valor_4.setProperty(u"valor", QCoreApplication.translate("CalculatorWidget", u"angle-c", None))
        self.tarjeta_angulo_5.setProperty(u"class", QCoreApplication.translate("CalculatorWidget", u"tarjeta-angle", None))
        self.label_titulo_5.setText(QCoreApplication.translate("CalculatorWidget", u"\u00c1ngulo 5", None))
        self.label_titulo_5.setProperty(u"name", QCoreApplication.translate("CalculatorWidget", u"number-angle", None))
        self.label_valor_5.setText("")
        self.label_valor_5.setProperty(u"valor", QCoreApplication.translate("CalculatorWidget", u"angle-c", None))
        self.tarjeta_angulo_6.setProperty(u"class", QCoreApplication.translate("CalculatorWidget", u"tarjeta-angle", None))
        self.label_titulo_6.setText(QCoreApplication.translate("CalculatorWidget", u"\u00c1ngulo 6", None))
        self.label_titulo_6.setProperty(u"name", QCoreApplication.translate("CalculatorWidget", u"number-angle", None))
        self.label_valor_6.setText("")
        self.label_valor_6.setProperty(u"valor", QCoreApplication.translate("CalculatorWidget", u"angle-c", None))
    # retranslateUi

