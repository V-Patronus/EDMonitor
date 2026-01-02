# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modalCreateCardWwQGEj.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_CardModal(object):
    def setupUi(self, CardModal):
        if not CardModal.objectName():
            CardModal.setObjectName(u"CardModal")
        CardModal.setWindowModality(Qt.WindowModality.WindowModal)
        CardModal.resize(358, 521)
        CardModal.setStyleSheet(u"/* ----------  VENTANA GENERAL  ---------- */\n"
"#CardModal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 #0f172a, stop:1 #1e293b);\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI Variable\", \"Inter\", sans-serif;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"/* ----------  T\u00cdTULO (estilo exacto que diste)  ---------- */\n"
"#titleLabel {\n"
"    /* Color de texto y tipograf\u00eda */\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI Variable\", \"Inter\", sans-serif;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"\n"
"    /* Fondo: Gradiente sutil que nace del color de acento */\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 rgba(74, 144, 226, 0.15),\n"
"                                stop:0.6 rgba(45, 45, 45, 0.4),\n"
"                                stop:1 transparent);\n"
"\n"
"    /* Bordes redondeados y borde de acento */\n"
"    border-left: 4px solid #4a90e2;\n"
""
                        "    border-right: 4px solid #4a90e2;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    border-top-left-radius: 8px;\n"
"    border-bottom-left-radius: 8px;\n"
"\n"
"    /* Espaciado */\n"
"    padding: 6px 15px 6px 12px;\n"
"    margin: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"/* ----------  T\u00cdTULO (estilo exacto que diste)  ---------- */\n"
"#lblStyle {\n"
"    /* Color de texto y tipograf\u00eda */\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI Variable\", \"Inter\", sans-serif;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"\n"
"    /* Fondo: Gradiente sutil que nace del color de acento */\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 rgba(74, 144, 226, 0.15),\n"
"                                stop:0.6 rgba(45, 45, 45, 0.4),\n"
"                                stop:1 transparent);\n"
"\n"
"    /* Bordes redondeados y borde de acento */\n"
"    border-left: 4px solid #4a90e2;\n"
"    border-top-right-"
                        "radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    border-top-left-radius: 8px;\n"
"    border-bottom-left-radius: 8px;\n"
"\n"
"    /* Espaciado */\n"
"    padding: 6px 15px 6px 12px;\n"
"    margin: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"/* ----------  SELECTOR DE ICONOS  ---------- */\n"
"#iconSelectorFrame {\n"
"    background-color: rgba(255, 255, 255, 0.05);\n"
"    border: 1px solid rgba(255, 255, 255, 0.1);\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"#iconFolder, #iconExcel, #iconPdf, #iconDefault {\n"
"    background-color: rgba(255, 255, 255, 0.07);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    font-size: 32px;\n"
"    min-width: 64px;\n"
"    min-height: 64px;\n"
"}\n"
"\n"
"#iconFolder:hover, #iconExcel:hover, #iconPdf:hover, #iconDefault:hover {\n"
"    background-color: rgba(255, 255, 255, 0.12);\n"
"}\n"
"\n"
"#iconFolder:pressed, #iconExcel:pressed, #iconPdf:pressed, #iconDefault:pressed {\n"
"    backgr"
                        "ound-color: #1e3a5b;\n"
"}\n"
"\n"
"#iconFolder:checked, #iconExcel:checked, #iconPdf:checked, #iconDefault:checked {\n"
"    background-color: #23446a;\n"
"    border: 2px solid #ffffff;\n"
"}\n"
"\n"
"/* ----------  CAMPOS DE ENTRADA  ---------- */\n"
"#nameEdit, #pathEdit {\n"
"    background-color: rgba(255, 255, 255, 0.07);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#descEdit {\n"
"    background-color: rgba(255, 255, 255, 0.07);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"    min-height: 80px;\n"
"}\n"
"\n"
"/* Focus */\n"
"#nameEdit:focus, #pathEdit:focus, #descEdit:focus {\n"
"    border: 2px solid #4a90e2;\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"/* ----------  BOT\u00d3N EXAMINAR  ---------- */\n"
"#browseButton {\n"
"    background-color: rgb"
                        "a(255, 255, 255, 0.1);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#browseButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.15);\n"
"}\n"
"\n"
"#browseButton:pressed {\n"
"    background-color: #4a90e2;\n"
"}\n"
"\n"
"/* ----------  BOTONES DE ACCI\u00d3N  ---------- */\n"
"#createButton, #editButton {\n"
"    background-color: #4a90e2;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#createButton:hover, #editButton:hover {\n"
"    background-color: #5aa0f2;\n"
"}\n"
"\n"
"#createButton:pressed, #editButton:pressed {\n"
"    background-color: #3a7bc8;\n"
"}\n"
"\n"
"#deleteButton {\n"
"    background-color: #e53935;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-"
                        "weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#deleteButton:hover {\n"
"    background-color: #f14643;\n"
"}\n"
"\n"
"#deleteButton:pressed {\n"
"    background-color: #c62828;\n"
"}\n"
"\n"
"/* Estilo base del QComboBox */\n"
"QComboBox[type=\"combo-box\"] {\n"
"    border: 2px solid #3d3d3d;\n"
"    border-radius: 8px;\n"
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
"QCombo"
                        "Box[type=\"combo-box\"]::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left: none;\n"
"}\n"
"\n"
"/* LA FLECHA SVG */\n"
"QComboBox[type=\"combo-box\"]::down-arrow {\n"
"    /* Aseg\u00farate de que la ruta sea correcta seg\u00fan tu archivo .qrc */\n"
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
"    background-color: #1a1"
                        "a1a;\n"
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
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox[type=\"combo-box\"] QAbstractItemView::item:selected {\n"
"    background-color: #4a90e2;\n"
"}")
        self.mainLayout = QVBoxLayout(CardModal)
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleLabel = QLabel(CardModal)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.titleLabel)

        self.iconSelectorFrame = QFrame(CardModal)
        self.iconSelectorFrame.setObjectName(u"iconSelectorFrame")
        self.iconSelectorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.iconGrid = QGridLayout(self.iconSelectorFrame)
        self.iconGrid.setObjectName(u"iconGrid")
        self.iconFolder = QToolButton(self.iconSelectorFrame)
        self.iconFolder.setObjectName(u"iconFolder")
        icon = QIcon()
        icon.addFile(u":/iconos/iconos/carpeta.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconFolder.setIcon(icon)
        self.iconFolder.setIconSize(QSize(40, 40))
        self.iconFolder.setCheckable(True)
        self.iconFolder.setAutoExclusive(True)

        self.iconGrid.addWidget(self.iconFolder, 0, 0, 1, 1)

        self.iconExcel = QToolButton(self.iconSelectorFrame)
        self.iconExcel.setObjectName(u"iconExcel")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/iconos/excel.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconExcel.setIcon(icon1)
        self.iconExcel.setIconSize(QSize(40, 40))
        self.iconExcel.setCheckable(True)
        self.iconExcel.setAutoExclusive(True)

        self.iconGrid.addWidget(self.iconExcel, 0, 1, 1, 1)

        self.iconPdf = QToolButton(self.iconSelectorFrame)
        self.iconPdf.setObjectName(u"iconPdf")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/iconos/pdf.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconPdf.setIcon(icon2)
        self.iconPdf.setIconSize(QSize(40, 40))
        self.iconPdf.setCheckable(True)
        self.iconPdf.setAutoExclusive(True)

        self.iconGrid.addWidget(self.iconPdf, 1, 0, 1, 1)

        self.iconDefault = QToolButton(self.iconSelectorFrame)
        self.iconDefault.setObjectName(u"iconDefault")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/iconos/default.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconDefault.setIcon(icon3)
        self.iconDefault.setIconSize(QSize(40, 40))
        self.iconDefault.setCheckable(True)
        self.iconDefault.setAutoExclusive(True)

        self.iconGrid.addWidget(self.iconDefault, 1, 1, 1, 1)


        self.mainLayout.addWidget(self.iconSelectorFrame)

        self.styleLayout = QHBoxLayout()
        self.styleLayout.setObjectName(u"styleLayout")
        self.lblStyle = QLabel(CardModal)
        self.lblStyle.setObjectName(u"lblStyle")

        self.styleLayout.addWidget(self.lblStyle)

        self.comboBoxStyles = QComboBox(CardModal)
        self.comboBoxStyles.addItem("")
        self.comboBoxStyles.addItem("")
        self.comboBoxStyles.addItem("")
        self.comboBoxStyles.addItem("")
        self.comboBoxStyles.setObjectName(u"comboBoxStyles")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxStyles.sizePolicy().hasHeightForWidth())
        self.comboBoxStyles.setSizePolicy(sizePolicy)

        self.styleLayout.addWidget(self.comboBoxStyles)


        self.mainLayout.addLayout(self.styleLayout)

        self.nameEdit = QLineEdit(CardModal)
        self.nameEdit.setObjectName(u"nameEdit")

        self.mainLayout.addWidget(self.nameEdit)

        self.descEdit = QTextEdit(CardModal)
        self.descEdit.setObjectName(u"descEdit")

        self.mainLayout.addWidget(self.descEdit)

        self.pathRowLayout = QHBoxLayout()
        self.pathRowLayout.setObjectName(u"pathRowLayout")
        self.pathEdit = QLineEdit(CardModal)
        self.pathEdit.setObjectName(u"pathEdit")

        self.pathRowLayout.addWidget(self.pathEdit)

        self.browseButton = QPushButton(CardModal)
        self.browseButton.setObjectName(u"browseButton")

        self.pathRowLayout.addWidget(self.browseButton)

        self.pathRowLayout.setStretch(0, 1)

        self.mainLayout.addLayout(self.pathRowLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.createButton = QPushButton(CardModal)
        self.createButton.setObjectName(u"createButton")

        self.buttonLayout.addWidget(self.createButton)

        self.editButton = QPushButton(CardModal)
        self.editButton.setObjectName(u"editButton")

        self.buttonLayout.addWidget(self.editButton)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(CardModal)

        QMetaObject.connectSlotsByName(CardModal)
    # setupUi

    def retranslateUi(self, CardModal):
        CardModal.setWindowTitle(QCoreApplication.translate("CardModal", u"Gesti\u00f3n de Tarjeta", None))
        self.titleLabel.setText(QCoreApplication.translate("CardModal", u"Tarjeta de Control", None))
        self.iconFolder.setText("")
        self.iconExcel.setText("")
        self.iconPdf.setText("")
        self.iconDefault.setText("")
        self.lblStyle.setText(QCoreApplication.translate("CardModal", u"Estilo", None))
        self.comboBoxStyles.setItemText(0, QCoreApplication.translate("CardModal", u"neon", None))
        self.comboBoxStyles.setItemText(1, QCoreApplication.translate("CardModal", u"sunset", None))
        self.comboBoxStyles.setItemText(2, QCoreApplication.translate("CardModal", u"lava", None))
        self.comboBoxStyles.setItemText(3, QCoreApplication.translate("CardModal", u"aurora", None))

        self.comboBoxStyles.setProperty(u"type", QCoreApplication.translate("CardModal", u"combo-box", None))
        self.nameEdit.setPlaceholderText(QCoreApplication.translate("CardModal", u"Nombre de la tarjeta", None))
        self.descEdit.setPlaceholderText(QCoreApplication.translate("CardModal", u"Descripci\u00f3n de la tarjeta", None))
        self.pathEdit.setPlaceholderText(QCoreApplication.translate("CardModal", u"Ruta (archivo o carpeta)", None))
        self.browseButton.setText(QCoreApplication.translate("CardModal", u"Examinar", None))
        self.createButton.setText(QCoreApplication.translate("CardModal", u"Crear Tarjeta", None))
        self.editButton.setText(QCoreApplication.translate("CardModal", u"Aplicar", None))
    # retranslateUi

