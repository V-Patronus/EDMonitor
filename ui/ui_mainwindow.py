# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowEjbXdH.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(769, 566)
        MainWindow.setStyleSheet(u"/* ===== VENTANA PRINCIPAL ===== */\n"
"#centralwidget{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #0f172a, stop:1 #1e293b);\n"
"	border:none;\n"
"}\n"
"\n"
"#CentralStack QWidget {\n"
"	background: #0D1017;\n"
"}\n"
"\n"
"#labelNombreEmpresa {\n"
"    color: #ffffff;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   \n"
"    \n"
"    /* Fondo radial que ya te gustaba */\n"
"    background: qradialgradient(cx:0.5, cy:0.5, radius:1.5,\n"
"        fx:0.5, fy:0.5, stop:0 #1e293b, stop:1 #0f172a);\n"
"        \n"
"    /* Configuraci\u00f3n de esquinas: \n"
"       Superior-Derecha: 20px, Inferior-Derecha: 20px\n"
"       Superior-Izquierda: 0px, Inferior-Izquierda: 0px */\n"
"    border-top-right-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"\n"
"    /* Bordes: Solo habilitamos el superior, derecho e inferior con el gradiente.\n"
"       El izquierdo se deja en 'none' o transparen"
                        "te */\n"
"    border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #3b82f6, stop:1 #8b5cf6);\n"
"    border-left: none; /* Esto hace que el lado izquierdo sea abierto/transparente */\n"
"}\n"
"\n"
"#labelIconoEmpresa {\n"
"    color: #ffffff;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   \n"
"    \n"
"    /* Fondo radial que ya te gustaba */\n"
"    background: qradialgradient(cx:0.5, cy:0.5, radius:1.5,\n"
"        fx:0.5, fy:0.5, stop:0 #1e293b, stop:1 #0f172a);\n"
"        \n"
"    /* Configuraci\u00f3n de esquinas: \n"
"       Superior-Derecha: 20px, Inferior-Derecha: 20px\n"
"       Superior-Izquierda: 0px, Inferior-Izquierda: 0px */\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"\n"
"    /* Bordes: Solo habilitamos el superior, derecho e inferior con el gradiente.\n"
"       El izquierdo se deja en 'none' o transparente */\n"
"    border: 2px solid qlinea"
                        "rgradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #3b82f6, stop:1 #8b5cf6);\n"
"    border-right: none; /* Esto hace que el lado izquierdo sea abierto/transparente */\n"
"}\n"
"\n"
"/* ===== BOT\u00d3N CEGA NIC - ESTILO PREMIUM ===== */\n"
"/* Estado Normal */\n"
"#CegaNicButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #1e3a8a, stop:1 #581c87); /* Azules y p\u00farpuras profundos */\n"
"    color: #e2e8f0; /* Blanco azulado suave */\n"
"    border: 1px solid #334155;\n"
"    border-radius: 12px;\n"
"    padding: 12px 20px;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"    margin: 8px;\n"
"}\n"
"\n"
"/* Estado Hover (Pasar el rat\u00f3n) */\n"
"#CegaNicButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #2563eb, stop:1 #7c3aed); /* Brillo m\u00e1s intenso */\n"
"    border: 1px solid #475569;\n"
"}\n"
"\n"
"/* Estado Pressed (Al hacer clic) */\n"
"#CegaNicButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0,"
                        " x2:1, y2:0,\n"
"        stop:0 #172554, stop:1 #4c1d95); /* Color m\u00e1s oscuro que el normal */\n"
"    padding-top: 14px; /* Efecto visual de hundimiento */\n"
"    padding-bottom: 10px;\n"
"}\n"
"\n"
"\n"
"#SideBarGroup, #SideBarFrame {\n"
"border:transparent;\n"
"padding-top:15px;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ===== BOTONES DEL GRUPO LATERAL - ESTADOS MODERNOS ===== */\n"
"#SideBarGroup QPushButton{\n"
"    background: rgba(60, 63, 65, 0.5);\n"
"    color: #bbbbbb;\n"
"    border: 1px solid rgba(85, 85, 85, 0.3);\n"
"    border-radius: 10px;\n"
"    padding: 10px 16px;\n"
"    margin: 4px 8px;\n"
"    text-align: left;\n"
"    font-weight: 500;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* ESTADO HOVER - Elevaci\u00f3n e iluminaci\u00f3n */\n"
"#SideBarGroup QPushButton:hover{\n"
"    background: rgba(75, 79, 83, 0.7);\n"
"    color: #ffffff;\n"
"    border-color: rgba(119, 119, 119, 0.5);\n"
"}\n"
"\n"
"/* ESTADO PRESSED - Hundido */\n"
"#SideBarGroup QPushButton:pressed{\n"
"    background: rgba(45, 48, 50"
                        ", 0.8);\n"
"}\n"
"\n"
"/* ESTADO ACTIVE/CHECKED - Efecto NEON */\n"
"#SideBarGroup QPushButton:checked{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #0078d4, stop:1 #00a8f4);\n"
"    color: #ffffff;\n"
"    border: 2px solid rgba(0, 168, 244, 0.5);\n"
"    font-weight: 600;\n"
"    /* Indicador lateral brillante */\n"
"    border-left: 4px solid #00f2ff;\n"
"    padding-left: 12px;\n"
"}\n"
"\n"
"/* ESTADO INACTIVO/DESENFocado - Atenuado */\n"
"#SideBarGroup QPushButton:disabled{\n"
"    background: rgba(40, 43, 45, 0.3);\n"
"    color: #666666;\n"
"    border-color: rgba(85, 85, 85, 0.2);\n"
"    opacity: 0.6;\n"
"}\n"
"\n"
"/* ===== \u00c1REA QTD-SIGNER - ESTADO ACTIVO ===== */\n"
"#SignerFrame[active=\"true\"]{\n"
"    border: 2px solid #0078d4;\n"
"    border-radius: 12px;\n"
"    background: rgba(0, 66, 117, 0.3);\n"
"}\n"
"\n"
"/* ===== BARRA SUPERIOR - GLASS EFFECT ===== */\n"
"#TopBarFrame{\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #02"
                        "0c1b, stop:0.2 #0a1929, stop:0.5 #14213d, stop:0.8 #1e3a5f, stop:1 #2a4a70);;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== CAMPO DE B\u00daSQUEDA - MODERNO ===== */\n"
"\n"
"#SearchLine{\n"
"    background: rgba(0, 180, 216, 0.1);\n"
"    color: #e2e8f0;\n"
"    border: 2px solid rgba(0, 180, 216, 0.3);\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"#SearchLine:focus {\n"
"    background: rgba(0, 180, 216, 0.15);\n"
"    border-color: #00b4d8;\n"
"}\n"
"\n"
"#SearchLine:disabled {\n"
"    background: rgba(255, 255, 255, 0.05);\n"
"    color: #64748b;\n"
"    border-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"/* ===== BOTONES SUPERIORES - MINIMALISTAS ===== */\n"
"#TopBarGroup QPushButton{\n"
"   /* Fondo oscuro trasl\u00facido para que resalte el icono colorido */\n"
"    background-color: rgba(30, 30, 35, 200);\n"
"    border: 2px solid #1a6dff; /* Azul base del icono */\n"
"    border-radius: 10px;\n"
"    color: #ffffff;\n"
"    font-"
                        "family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 5px 7px;\n"
"}\n"
"#TopBarGroup QPushButton:hover{\n"
"    /* Cambia a un gradiente similar al del icono */\n"
"    border: 2px solid #c822ff;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                      stop:0 rgba(26, 109, 255, 40), \n"
"                                      stop:1 rgba(200, 34, 255, 40));\n"
"}\n"
"\n"
"#TopBarGroup QPushButton:pressed {\n"
"    background-color: rgba(200, 34, 255, 80);\n"
"    border-color: #e6abff;\n"
"}\n"
"\n"
"/* ===== \u00c1REA CENTRAL / SCROLL - OSCURO ===== */\n"
"#CentralStack QScrollArea{\n"
"    background: #1e1e1e;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== SCROLLBAR MODERNO - GLASSMORPHISM ===== */\n"
"\n"
"/* SCROLLBAR VERTICAL */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 14px;\n"
"    border: none;\n"
"    margin: 16px 0 16px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrol"
                        "lBar::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(0, 180, 216, 0.3), stop:1 rgba(0, 119, 182, 0.5));\n"
"    border: 2px solid rgba(0, 180, 216, 0.6);\n"
"    border-radius: 7px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(0, 212, 255, 0.5), stop:1 rgba(0, 153, 204, 0.7));\n"
"    border-color: rgba(0, 212, 255, 0.8);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(0, 153, 204, 0.6), stop:1 rgba(0, 119, 182, 0.8));\n"
"}\n"
"\n"
"/* Flechas del scrollbar - estilizadas */\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: rgba(0, 180, 216, 0.2);\n"
"    border: 1px solid rgba(0, 180, 216, 0.4);\n"
"    border-radius: 7px;\n"
"    height: 14px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:ver"
                        "tical {\n"
"    subcontrol-position: bottom;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    subcontrol-position: top;\n"
"    margin-top: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover {\n"
"    background: rgba(0, 212, 255, 0.3);\n"
"    border-color: rgba(0, 212, 255, 0.6);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* SCROLLBAR HORIZONTAL */\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 14px;\n"
"    border: none;\n"
"    margin: 0 16px 0 16px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(0, 180, 216, 0.3), stop:1 rgba(0, 119, 182, 0.5));\n"
"    border: 2px solid rgba(0, 180, 216, 0.6);\n"
"    border-radius: 7px;\n"
"    min-width: 30px;    \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"   "
                        " background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(0, 212, 255, 0.5), stop:1 rgba(0, 153, 204, 0.7));\n"
"    border-color: rgba(0, 212, 255, 0.8);    \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(0, 153, 204, 0.6), stop:1 rgba(0, 119, 182, 0.8));\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: rgba(0, 180, 216, 0.2);\n"
"    border: 1px solid rgba(0, 180, 216, 0.4);\n"
"    border-radius: 7px;\n"
"    width: 14px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    subcontrol-position: right;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    subcontrol-position: left;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::sub-line:horizontal:hover {\n"
"    background: rgba(0, 212, 255, 0.3);\n"
"    border-color: rgba(0, 212, 25"
                        "5, 0.6);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* CORNER (esquina entre scrollbars) */\n"
"QScrollBar::corner {\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QPushButton#btnAddCard{\n"
"    background: rgb(60, 63, 65);\n"
"    color: #bbbbbb;\n"
"    border: 1px solid rgba(85, 85, 85, 0.3);\n"
"    border-radius: 10px;\n"
"    padding: 10px 16px;\n"
"    margin: 4px 8px;\n"
"    text-align: center;\n"
"    font-weight: 500;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* ESTADO HOVER - Elevaci\u00f3n e iluminaci\u00f3n */\n"
"QPushButton#btnAddCard:hover{\n"
"    background: rgba(75, 79, 83, 0.7);\n"
"    color: #ffffff;\n"
"    border-color: rgba(119, 119, 119, 0.5);\n"
"}\n"
"\n"
"/* ESTADO PRESSED - Hundido */\n"
"QPushButton#btnAddCard:pressed{\n"
"    background: rgb(86, 86, 86);\n"
"}\n"
"\n"
"QLabel#labelNotificacion {\n"
"    /* Fondo oscuro trasl\u00facido o s\u00f3lido */\n"
"    background-color: #2b2b2b;\n"
""
                        "    \n"
"    /* Borde fino y elegante */\n"
"    border: 1px solid #3d3d3d;\n"
"    border-radius: 10px;\n"
"    \n"
"    /* Tipograf\u00eda clara */\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI\", \"SF Pro Display\", \"Arial\";\n"
"    font-size: 13px;\n"
"    \n"
"    /* Espaciado para que el texto no toque los bordes */\n"
"    padding: 12px 18px;\n"
"    \n"
"    /* Simulaci\u00f3n de relieve */\n"
"    border-bottom: 2px solid #1a1a1a;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MainLay = QHBoxLayout(self.centralwidget)
        self.MainLay.setSpacing(0)
        self.MainLay.setObjectName(u"MainLay")
        self.MainLay.setContentsMargins(0, 0, 0, 0)
        self.RightFrame = QFrame(self.centralwidget)
        self.RightFrame.setObjectName(u"RightFrame")
        self.RightFrame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.RightFrame.setAutoFillBackground(False)
        self.RightFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.RightFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.RightLay = QVBoxLayout(self.RightFrame)
        self.RightLay.setSpacing(0)
        self.RightLay.setObjectName(u"RightLay")
        self.RightLay.setContentsMargins(0, 0, 0, 0)
        self.TopBarFrame = QFrame(self.RightFrame)
        self.TopBarFrame.setObjectName(u"TopBarFrame")
        self.TopBarHorLay = QHBoxLayout(self.TopBarFrame)
        self.TopBarHorLay.setSpacing(0)
        self.TopBarHorLay.setObjectName(u"TopBarHorLay")
        self.TopBarHorLay.setContentsMargins(0, 0, 0, 0)
        self.CegaNicButton = QPushButton(self.TopBarFrame)
        self.CegaNicButton.setObjectName(u"CegaNicButton")
        self.CegaNicButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CegaNicButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.CegaNicButton.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/iconos/iconos/align-justify.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CegaNicButton.setIcon(icon)
        self.CegaNicButton.setIconSize(QSize(25, 25))
        self.CegaNicButton.setCheckable(True)
        self.CegaNicButton.setChecked(False)
        self.CegaNicButton.setAutoExclusive(False)

        self.TopBarHorLay.addWidget(self.CegaNicButton)

        self.TopBarGroup = QFrame(self.TopBarFrame)
        self.TopBarGroup.setObjectName(u"TopBarGroup")
        self.TopGroupLay = QHBoxLayout(self.TopBarGroup)
        self.TopGroupLay.setObjectName(u"TopGroupLay")
        self.SearchLine = QLineEdit(self.TopBarGroup)
        self.SearchLine.setObjectName(u"SearchLine")
        self.SearchLine.setMaximumSize(QSize(0, 16777215))

        self.TopGroupLay.addWidget(self.SearchLine)

        self.BtnSearch = QPushButton(self.TopBarGroup)
        self.BtnSearch.setObjectName(u"BtnSearch")
        self.BtnSearch.setMaximumSize(QSize(0, 16777215))
        self.BtnSearch.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconos/iconos/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnSearch.setIcon(icon1)
        self.BtnSearch.setIconSize(QSize(20, 20))

        self.TopGroupLay.addWidget(self.BtnSearch)

        self.frame_2 = QFrame(self.TopBarGroup)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelIconoEmpresa = QLabel(self.frame_2)
        self.labelIconoEmpresa.setObjectName(u"labelIconoEmpresa")
        self.labelIconoEmpresa.setMaximumSize(QSize(50, 50))
        self.labelIconoEmpresa.setPixmap(QPixmap(u":/iconos/iconos/tuerca.svg"))
        self.labelIconoEmpresa.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.labelIconoEmpresa)

        self.labelNombreEmpresa = QLabel(self.frame_2)
        self.labelNombreEmpresa.setObjectName(u"labelNombreEmpresa")

        self.horizontalLayout_7.addWidget(self.labelNombreEmpresa)


        self.TopGroupLay.addWidget(self.frame_2)

        self.HSpacer = QSpacerItem(131, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TopGroupLay.addItem(self.HSpacer)

        self.BtnDoc = QPushButton(self.TopBarGroup)
        self.BtnDoc.setObjectName(u"BtnDoc")
        self.BtnDoc.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconos/iconos/icons8-document.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnDoc.setIcon(icon2)
        self.BtnDoc.setIconSize(QSize(30, 30))

        self.TopGroupLay.addWidget(self.BtnDoc)


        self.TopBarHorLay.addWidget(self.TopBarGroup)


        self.RightLay.addWidget(self.TopBarFrame)

        self.RightCentralFrame = QFrame(self.RightFrame)
        self.RightCentralFrame.setObjectName(u"RightCentralFrame")
        self.CentralHorLay = QHBoxLayout(self.RightCentralFrame)
        self.CentralHorLay.setSpacing(0)
        self.CentralHorLay.setObjectName(u"CentralHorLay")
        self.CentralHorLay.setContentsMargins(0, 0, 0, 0)
        self.SideBarFrame = QFrame(self.RightCentralFrame)
        self.SideBarFrame.setObjectName(u"SideBarFrame")
        self.SideBarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SideBarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.SideBarFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SideBarGroup = QFrame(self.SideBarFrame)
        self.SideBarGroup.setObjectName(u"SideBarGroup")
        self.SideBarGroup.setFrameShape(QFrame.Shape.StyledPanel)
        self.SideBarGroup.setFrameShadow(QFrame.Shadow.Raised)
        self.SideGroupLay = QVBoxLayout(self.SideBarGroup)
        self.SideGroupLay.setObjectName(u"SideGroupLay")
        self.SideGroupLay.setContentsMargins(0, 0, 0, 0)
        self.btnHome = QPushButton(self.SideBarGroup)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconos/iconos/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHome.setIcon(icon3)
        self.btnHome.setIconSize(QSize(20, 20))
        self.btnHome.setCheckable(True)
        self.btnHome.setChecked(True)
        self.btnHome.setAutoExclusive(True)

        self.SideGroupLay.addWidget(self.btnHome)

        self.btnDocuments = QPushButton(self.SideBarGroup)
        self.btnDocuments.setObjectName(u"btnDocuments")
        self.btnDocuments.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/iconos/iconos/layers.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDocuments.setIcon(icon4)
        self.btnDocuments.setIconSize(QSize(20, 20))
        self.btnDocuments.setCheckable(True)
        self.btnDocuments.setAutoExclusive(True)

        self.SideGroupLay.addWidget(self.btnDocuments)

        self.btnCalculator = QPushButton(self.SideBarGroup)
        self.btnCalculator.setObjectName(u"btnCalculator")
        self.btnCalculator.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/iconos/iconos/cpu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCalculator.setIcon(icon5)
        self.btnCalculator.setIconSize(QSize(20, 20))
        self.btnCalculator.setCheckable(True)
        self.btnCalculator.setAutoExclusive(True)

        self.SideGroupLay.addWidget(self.btnCalculator)

        self.btnJapon = QPushButton(self.SideBarGroup)
        self.btnJapon.setObjectName(u"btnJapon")
        self.btnJapon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/iconos/iconos/codesandbox.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnJapon.setIcon(icon6)
        self.btnJapon.setIconSize(QSize(20, 20))
        self.btnJapon.setCheckable(True)
        self.btnJapon.setAutoExclusive(True)

        self.SideGroupLay.addWidget(self.btnJapon)

        self.BtnAyuda = QPushButton(self.SideBarGroup)
        self.BtnAyuda.setObjectName(u"BtnAyuda")
        self.BtnAyuda.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/iconos/iconos/download-cloud.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnAyuda.setIcon(icon7)
        self.BtnAyuda.setIconSize(QSize(20, 20))
        self.BtnAyuda.setCheckable(True)
        self.BtnAyuda.setAutoExclusive(True)

        self.SideGroupLay.addWidget(self.BtnAyuda)

        self.VSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SideGroupLay.addItem(self.VSpacer)

        self.BtnSalir = QPushButton(self.SideBarGroup)
        self.BtnSalir.setObjectName(u"BtnSalir")
        self.BtnSalir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/iconos/iconos/external-link.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnSalir.setIcon(icon8)
        self.BtnSalir.setIconSize(QSize(20, 20))

        self.SideGroupLay.addWidget(self.BtnSalir)


        self.verticalLayout_2.addWidget(self.SideBarGroup)


        self.CentralHorLay.addWidget(self.SideBarFrame)

        self.CentralStack = QStackedWidget(self.RightCentralFrame)
        self.CentralStack.setObjectName(u"CentralStack")
        self.PageHome = QWidget()
        self.PageHome.setObjectName(u"PageHome")
        self.PageHome.setStyleSheet(u"")
        self.ViewerLay = QHBoxLayout(self.PageHome)
        self.ViewerLay.setObjectName(u"ViewerLay")
        self.ViewerLay.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.PageHome)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.heroFrame = QFrame(self.frame)
        self.heroFrame.setObjectName(u"heroFrame")
        self.heroFrame.setStyleSheet(u"")
        self.vboxLayout = QVBoxLayout(self.heroFrame)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.titulos = QFrame(self.heroFrame)
        self.titulos.setObjectName(u"titulos")
        self.titulos.setStyleSheet(u"\n"
"/* HERO (solo este frame) */\n"
"QFrame{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 #2563eb,\n"
"                                stop:1 #06b6d4);\n"
"  border-radius: 24px;\n"
"\n"
"}\n"
"      ")
        self.titulos.setFrameShape(QFrame.Shape.StyledPanel)
        self.titulos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.titulos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.heroTitle = QLabel(self.titulos)
        self.heroTitle.setObjectName(u"heroTitle")
        self.heroTitle.setStyleSheet(u"\n"
"#heroTitle {\n"
"    background-color: transparent;\n"
"    font-size: 25px;\n"
"    font-weight: 900;\n"
"    letter-spacing: 5px;\n"
"    padding: 2px;\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"         ")
        self.heroTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.heroTitle)

        self.heroSubtitle = QLabel(self.titulos)
        self.heroSubtitle.setObjectName(u"heroSubtitle")
        self.heroSubtitle.setStyleSheet(u"\n"
"#heroSubtitle {\n"
"    background-color: transparent;\n"
"    border-radius:5px;\n"
"    font-size: 16px;\n"
"    color: #e0f2fe;\n"
"}\n"
"         ")
        self.heroSubtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.heroSubtitle)


        self.vboxLayout.addWidget(self.titulos)

        self.mediaPlaceholder = QFrame(self.heroFrame)
        self.mediaPlaceholder.setObjectName(u"mediaPlaceholder")
        self.mediaPlaceholder.setStyleSheet(u"\n"
"#mediaPlaceholder {\n"
"    border: 3px dashed #38bdf8;\n"
"    border-radius: 24px;\n"
"    font-size: 18px;\n"
"    color: #38bdf8;\n"
"}\n"
"          ")
        self.mediaPlaceholder.setFrameShape(QFrame.Shape.StyledPanel)
        self.mediaPlaceholder.setFrameShadow(QFrame.Shadow.Raised)

        self.vboxLayout.addWidget(self.mediaPlaceholder)


        self.verticalLayout_3.addWidget(self.heroFrame)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QWidget()
        self.scrollContent.setObjectName(u"scrollContent")
        self.scrollContent.setGeometry(QRect(0, -160, 785, 618))
        self._2 = QVBoxLayout(self.scrollContent)
        self._2.setObjectName(u"_2")
        self.lay_2 = QHBoxLayout()
        self.lay_2.setObjectName(u"lay_2")
        self.cardPrecision = QFrame(self.scrollContent)
        self.cardPrecision.setObjectName(u"cardPrecision")
        self.cardPrecision.setStyleSheet(u"\n"
"#cardPrecision {\n"
"    border-radius: 22px;\n"
"    background-color: rgba(14,165,233,0.3);\n"
"    border: 1px solid rgba(148, 163, 184, 0.25);\n"
"    padding: 6px;\n"
"}\n"
"#cardPrecision:hover {\n"
"    border: 1px solid rgba(56, 189, 248, 1);\n"
"    background-color: rgba(2, 6, 23, 0.85);\n"
"}\n"
"            ")
        self._3 = QVBoxLayout(self.cardPrecision)
        self._3.setObjectName(u"_3")
        self.cardPrecisionInner = QFrame(self.cardPrecision)
        self.cardPrecisionInner.setObjectName(u"cardPrecisionInner")
        self.cardPrecisionInner.setStyleSheet(u"\n"
"#cardPrecisionInner {\n"
"    border-radius: 18px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgba(255,255,255,0.15),\n"
"                                stop:1 rgba(255,255,255,0.03));\n"
"    padding: 16px;\n"
"}\n"
"               ")
        self._4 = QVBoxLayout(self.cardPrecisionInner)
        self._4.setObjectName(u"_4")
        self.cardPrecisionTitle = QLabel(self.cardPrecisionInner)
        self.cardPrecisionTitle.setObjectName(u"cardPrecisionTitle")
        self.cardPrecisionTitle.setStyleSheet(u"\n"
"#cardPrecisionTitle {\n"
"    background: transparent;\n"
"    color: #94a3b8;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"                  ")
        self.cardPrecisionTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._4.addWidget(self.cardPrecisionTitle)

        self.cardPrecisionValue = QLabel(self.cardPrecisionInner)
        self.cardPrecisionValue.setObjectName(u"cardPrecisionValue")
        self.cardPrecisionValue.setStyleSheet(u"\n"
"#cardPrecisionValue {\n"
"    background: transparent;\n"
"    color: #f8fafc;\n"
"    font-size: 22px;\n"
"    font-weight: 800;\n"
"}\n"
"                  ")
        self.cardPrecisionValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._4.addWidget(self.cardPrecisionValue)


        self._3.addWidget(self.cardPrecisionInner)


        self.lay_2.addWidget(self.cardPrecision)

        self.cardMaterial = QFrame(self.scrollContent)
        self.cardMaterial.setObjectName(u"cardMaterial")
        self.cardMaterial.setStyleSheet(u"\n"
"#cardMaterial {\n"
"    border-radius: 22px;\n"
"    background-color: rgba(34,197,94,0.3);\n"
"    border: 1px solid rgba(148, 163, 184, 0.25);\n"
"    padding: 6px;\n"
"}\n"
"#cardMaterial:hover {\n"
"    border: 1px solid rgba(56, 189, 248, 1);\n"
"    background-color: rgba(2, 6, 23, 0.85);\n"
"}\n"
"            ")
        self._5 = QVBoxLayout(self.cardMaterial)
        self._5.setObjectName(u"_5")
        self.cardMaterialInner = QFrame(self.cardMaterial)
        self.cardMaterialInner.setObjectName(u"cardMaterialInner")
        self.cardMaterialInner.setStyleSheet(u"\n"
"#cardMaterialInner {\n"
"    border-radius: 18px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgba(255,255,255,0.15),\n"
"                                stop:1 rgba(255,255,255,0.03));\n"
"    padding: 16px;\n"
"}\n"
"               ")
        self._6 = QVBoxLayout(self.cardMaterialInner)
        self._6.setObjectName(u"_6")
        self.cardMaterialTitle = QLabel(self.cardMaterialInner)
        self.cardMaterialTitle.setObjectName(u"cardMaterialTitle")
        self.cardMaterialTitle.setStyleSheet(u"\n"
"#cardMaterialTitle {\n"
"    background: transparent;\n"
"    color: #94a3b8;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"                  ")
        self.cardMaterialTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._6.addWidget(self.cardMaterialTitle)

        self.cardMaterialValue = QLabel(self.cardMaterialInner)
        self.cardMaterialValue.setObjectName(u"cardMaterialValue")
        self.cardMaterialValue.setStyleSheet(u"\n"
"#cardMaterialValue {\n"
"    background: transparent;\n"
"    color: #f8fafc;\n"
"    font-size: 22px;\n"
"    font-weight: 800;\n"
"}\n"
"                  ")
        self.cardMaterialValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._6.addWidget(self.cardMaterialValue)


        self._5.addWidget(self.cardMaterialInner)


        self.lay_2.addWidget(self.cardMaterial)

        self.cardProcess = QFrame(self.scrollContent)
        self.cardProcess.setObjectName(u"cardProcess")
        self.cardProcess.setStyleSheet(u"\n"
"#cardProcess {\n"
"    border-radius: 22px;\n"
"    background-color: rgba(245,158,11,0.3);\n"
"    border: 1px solid rgba(148, 163, 184, 0.25);\n"
"    padding: 6px;\n"
"}\n"
"#cardProcess:hover {\n"
"    border: 1px solid rgba(56, 189, 248, 1);\n"
"    background-color: rgba(2, 6, 23, 0.85);\n"
"}\n"
"            ")
        self._7 = QVBoxLayout(self.cardProcess)
        self._7.setObjectName(u"_7")
        self.cardProcessInner = QFrame(self.cardProcess)
        self.cardProcessInner.setObjectName(u"cardProcessInner")
        self.cardProcessInner.setStyleSheet(u"\n"
"#cardProcessInner {\n"
"    border-radius: 18px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgba(255,255,255,0.15),\n"
"                                stop:1 rgba(255,255,255,0.03));\n"
"    padding: 16px;\n"
"}\n"
"               ")
        self._8 = QVBoxLayout(self.cardProcessInner)
        self._8.setObjectName(u"_8")
        self.cardProcessTitle = QLabel(self.cardProcessInner)
        self.cardProcessTitle.setObjectName(u"cardProcessTitle")
        self.cardProcessTitle.setStyleSheet(u"\n"
"#cardProcessTitle {\n"
"    background: transparent;\n"
"    color: #94a3b8;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"                  ")
        self.cardProcessTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._8.addWidget(self.cardProcessTitle)

        self.cardProcessValue = QLabel(self.cardProcessInner)
        self.cardProcessValue.setObjectName(u"cardProcessValue")
        self.cardProcessValue.setStyleSheet(u"\n"
"#cardProcessValue {\n"
"    background: transparent;\n"
"    color: #f8fafc;\n"
"    font-size: 22px;\n"
"    font-weight: 800;\n"
"}\n"
"                  ")
        self.cardProcessValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._8.addWidget(self.cardProcessValue)


        self._7.addWidget(self.cardProcessInner)


        self.lay_2.addWidget(self.cardProcess)


        self._2.addLayout(self.lay_2)

        self.sectionWhat = QFrame(self.scrollContent)
        self.sectionWhat.setObjectName(u"sectionWhat")
        self.sectionWhat.setStyleSheet(u"\n"
"#sectionWhat {\n"
"	\n"
"	background-color: #200136;\n"
"    border-radius: 24px;\n"
"    padding: 24px;\n"
"    border: 1px solid rgba(148, 163, 184, 0.25);\n"
"}\n"
"          ")
        self._9 = QVBoxLayout(self.sectionWhat)
        self._9.setObjectName(u"_9")
        self.sectionWhatTitle = QLabel(self.sectionWhat)
        self.sectionWhatTitle.setObjectName(u"sectionWhatTitle")
        self.sectionWhatTitle.setStyleSheet(u"\n"
"#sectionWhatTitle {\n"
"	\n"
"	background-color: transparent;\n"
"    font-size: 22px;\n"
"    font-weight: 700;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"             ")
        self.sectionWhatTitle.setTextFormat(Qt.TextFormat.PlainText)
        self.sectionWhatTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sectionWhatTitle.setWordWrap(True)

        self._9.addWidget(self.sectionWhatTitle)

        self.label_2 = QLabel(self.sectionWhat)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"#label_2 {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"}")
        self.label_2.setTextFormat(Qt.TextFormat.PlainText)
        self.label_2.setWordWrap(True)

        self._9.addWidget(self.label_2)


        self._2.addWidget(self.sectionWhat)

        self.lay_1 = QHBoxLayout()
        self.lay_1.setObjectName(u"lay_1")
        self.fact1 = QFrame(self.scrollContent)
        self.fact1.setObjectName(u"fact1")
        self.fact1.setStyleSheet(u"\n"
"#fact1 {\n"
"    border-radius: 22px;\n"
"    background-color: rgba(124,58,237,0.4);\n"
"    border: 1px solid rgba(148, 163, 184, 0.25);\n"
"    padding: 6px;\n"
"}\n"
"#fact1:hover {\n"
"    border: 1px solid rgba(56, 189, 248, 1);\n"
"    background-color: rgba(2, 6, 23, 0.85);\n"
"}\n"
"            ")
        self._10 = QVBoxLayout(self.fact1)
        self._10.setObjectName(u"_10")
        self.fact1Inner = QFrame(self.fact1)
        self.fact1Inner.setObjectName(u"fact1Inner")
        font1 = QFont()
        font1.setPointSize(10)
        self.fact1Inner.setFont(font1)
        self.fact1Inner.setStyleSheet(u"\n"
"#fact1Inner {\n"
"    border-radius: 18px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgba(255,255,255,0.15),\n"
"                                stop:1 rgba(255,255,255,0.03));\n"
"    padding: 16px;\n"
"}\n"
"               ")
        self._11 = QVBoxLayout(self.fact1Inner)
        self._11.setObjectName(u"_11")
        self.label = QLabel(self.fact1Inner)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setWeight(QFont.DemiBold)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"\n"
"#label {\n"
"    background: transparent;\n"
"    color: #f8fafc;\n"
"    font-weight: 600;\n"
"}\n"
"                  ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._11.addWidget(self.label)


        self._10.addWidget(self.fact1Inner)


        self.lay_1.addWidget(self.fact1)

        self.fact2 = QFrame(self.scrollContent)
        self.fact2.setObjectName(u"fact2")
        self.fact2.setStyleSheet(u"\n"
"#fact2 {\n"
"    border-radius: 22px;\n"
"    background-color: rgba(236,72,153,0.4);\n"
"    border: 1px solid rgba(148, 163, 184, 0.25);\n"
"    padding: 6px;\n"
"}\n"
"#fact2:hover {\n"
"    border: 1px solid rgba(56, 189, 248, 1);\n"
"    background-color: rgba(2, 6, 23, 0.85);\n"
"}\n"
"            ")
        self._12 = QVBoxLayout(self.fact2)
        self._12.setObjectName(u"_12")
        self.fact2Inner = QFrame(self.fact2)
        self.fact2Inner.setObjectName(u"fact2Inner")
        self.fact2Inner.setStyleSheet(u"\n"
"#fact2Inner {\n"
"    border-radius: 18px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgba(255,255,255,0.15),\n"
"                                stop:1 rgba(255,255,255,0.03));\n"
"    padding: 16px;\n"
"}\n"
"               ")
        self._13 = QVBoxLayout(self.fact2Inner)
        self._13.setObjectName(u"_13")
        self.label_3 = QLabel(self.fact2Inner)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"\n"
"#label_3 {\n"
"    background: transparent;\n"
"    color: #f8fafc;\n"
"    font-weight: 600;\n"
"}\n"
"                  ")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._13.addWidget(self.label_3)


        self._12.addWidget(self.fact2Inner)


        self.lay_1.addWidget(self.fact2)

        self.fact3 = QFrame(self.scrollContent)
        self.fact3.setObjectName(u"fact3")
        self.fact3.setStyleSheet(u"\n"
"#fact3 {\n"
"    border-radius: 22px;\n"
"    background-color: rgba(16,185,129,0.4);\n"
"    border: 1px solid rgba(148, 163, 184, 0.25);\n"
"    padding: 6px;\n"
"}\n"
"#fact3:hover {\n"
"    border: 1px solid rgba(56, 189, 248, 1);\n"
"    background-color: rgba(2, 6, 23, 0.85);\n"
"}\n"
"            ")
        self._14 = QVBoxLayout(self.fact3)
        self._14.setObjectName(u"_14")
        self.fact3Inner = QFrame(self.fact3)
        self.fact3Inner.setObjectName(u"fact3Inner")
        font3 = QFont()
        font3.setPointSize(12)
        self.fact3Inner.setFont(font3)
        self.fact3Inner.setStyleSheet(u"\n"
"#fact3Inner {\n"
"    border-radius: 18px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgba(255,255,255,0.15),\n"
"                                stop:1 rgba(255,255,255,0.03));\n"
"    padding: 16px;\n"
"}\n"
"               ")
        self._15 = QVBoxLayout(self.fact3Inner)
        self._15.setObjectName(u"_15")
        self.label_4 = QLabel(self.fact3Inner)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"\n"
"#label_4 {\n"
"    background: transparent;\n"
"    color: #f8fafc;\n"
"    font-weight: 600;\n"
"}\n"
"                  ")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._15.addWidget(self.label_4)


        self._14.addWidget(self.fact3Inner)


        self.lay_1.addWidget(self.fact3)


        self._2.addLayout(self.lay_1)

        self.scrollArea.setWidget(self.scrollContent)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.ViewerLay.addWidget(self.frame)

        self.CentralStack.addWidget(self.PageHome)
        self.PageCalculator = QWidget()
        self.PageCalculator.setObjectName(u"PageCalculator")
        self.horizontalLayout = QHBoxLayout(self.PageCalculator)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollCalculator = QScrollArea(self.PageCalculator)
        self.scrollCalculator.setObjectName(u"scrollCalculator")
        self.scrollCalculator.setWidgetResizable(True)
        self.scrollAreaWidgetCalculator = QWidget()
        self.scrollAreaWidgetCalculator.setObjectName(u"scrollAreaWidgetCalculator")
        self.scrollAreaWidgetCalculator.setGeometry(QRect(0, 0, 68, 18))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetCalculator)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollCalculator.setWidget(self.scrollAreaWidgetCalculator)

        self.horizontalLayout.addWidget(self.scrollCalculator)

        self.CentralStack.addWidget(self.PageCalculator)
        self.PageDocuments = QWidget()
        self.PageDocuments.setObjectName(u"PageDocuments")
        self.horizontalLayout_2 = QHBoxLayout(self.PageDocuments)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollDocuments = QScrollArea(self.PageDocuments)
        self.scrollDocuments.setObjectName(u"scrollDocuments")
        self.scrollDocuments.setWidgetResizable(True)
        self.scrollAreaWidgetDocuments = QWidget()
        self.scrollAreaWidgetDocuments.setObjectName(u"scrollAreaWidgetDocuments")
        self.scrollAreaWidgetDocuments.setGeometry(QRect(0, 0, 208, 119))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetDocuments)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AddCardGroup = QFrame(self.scrollAreaWidgetDocuments)
        self.AddCardGroup.setObjectName(u"AddCardGroup")
        self.AddCardGroup.setFrameShape(QFrame.Shape.StyledPanel)
        self.AddCardGroup.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.AddCardGroup)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnAddCard = QPushButton(self.AddCardGroup)
        self.btnAddCard.setObjectName(u"btnAddCard")
        self.btnAddCard.setMaximumSize(QSize(250, 16777215))
        font4 = QFont()
        font4.setWeight(QFont.Medium)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.btnAddCard.setFont(font4)
        self.btnAddCard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddCard.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u":/iconos/iconos/plus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddCard.setIcon(icon9)
        self.btnAddCard.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.btnAddCard)


        self.verticalLayout.addWidget(self.AddCardGroup, 0, Qt.AlignmentFlag.AlignTop)

        self.ViewAddCard = QFrame(self.scrollAreaWidgetDocuments)
        self.ViewAddCard.setObjectName(u"ViewAddCard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ViewAddCard.sizePolicy().hasHeightForWidth())
        self.ViewAddCard.setSizePolicy(sizePolicy)
        self.ViewAddCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.ViewAddCard.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.ViewAddCard)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ViewCards = QFrame(self.ViewAddCard)
        self.ViewCards.setObjectName(u"ViewCards")
        self.ViewCards.setFrameShape(QFrame.Shape.StyledPanel)
        self.ViewCards.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.ViewCards)

        self.AddCardWidget = QFrame(self.ViewAddCard)
        self.AddCardWidget.setObjectName(u"AddCardWidget")
        self.AddCardWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.AddCardWidget.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.AddCardWidget)


        self.verticalLayout.addWidget(self.ViewAddCard)

        self.scrollDocuments.setWidget(self.scrollAreaWidgetDocuments)

        self.horizontalLayout_2.addWidget(self.scrollDocuments)

        self.CentralStack.addWidget(self.PageDocuments)
        self.PageSettings = QWidget()
        self.PageSettings.setObjectName(u"PageSettings")
        self.horizontalLayout_4 = QHBoxLayout(self.PageSettings)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollSettings = QScrollArea(self.PageSettings)
        self.scrollSettings.setObjectName(u"scrollSettings")
        self.scrollSettings.setWidgetResizable(True)
        self.scrollAreaWidgetSettings = QWidget()
        self.scrollAreaWidgetSettings.setObjectName(u"scrollAreaWidgetSettings")
        self.scrollAreaWidgetSettings.setGeometry(QRect(0, 0, 744, 480))
        self.horizontalLayout_9 = QHBoxLayout(self.scrollAreaWidgetSettings)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frameBackup = QFrame(self.scrollAreaWidgetSettings)
        self.frameBackup.setObjectName(u"frameBackup")
        self.frameBackup.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameBackup.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frameBackup)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupCards = QGroupBox(self.frameBackup)
        self.groupCards.setObjectName(u"groupCards")
        self.groupCards.setStyleSheet(u"\n"
"     QGroupBox {\n"
"      border: 1px solid #555;\n"
"      margin-top: 10px;\n"
"      font-weight: bold;\n"
"	border-radius:10px;\n"
"     }\n"
"     QGroupBox::title {\n"
"      subcontrol-origin: margin;\n"
"      left: 10px;\n"
"      padding: 0 5px 0 5px;\n"
"	color: rgb(255, 255, 255);\n"
"     }\n"
"    ")
        self.horizontalLayout_11 = QHBoxLayout(self.groupCards)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.leCards_1 = QLineEdit(self.groupCards)
        self.leCards_1.setObjectName(u"leCards_1")
        self.leCards_1.setStyleSheet(u"\n"
"      QLineEdit {\n"
"       background-color: #2a2a2a;\n"
"       color: #ffffff;\n"
"       border: 1px solid #555;\n"
"       border-radius: 4px;\n"
"       padding: 4px;\n"
"      }\n"
"     ")

        self.horizontalLayout_11.addWidget(self.leCards_1)

        self.btnBrowseCards_1 = QPushButton(self.groupCards)
        self.btnBrowseCards_1.setObjectName(u"btnBrowseCards_1")
        self.btnBrowseCards_1.setStyleSheet(u"\n"
"      QPushButton {\n"
"       background-color: #3c3c3c;\n"
"       color: #ffffff;\n"
"       border: 1px solid #555;\n"
"       border-radius: 4px;\n"
"		padding: 6px;\n"
"      }\n"
"      QPushButton:hover { background-color: #505050; }\n"
"      QPushButton:pressed { background-color: #2a2a2a; }\n"
"     ")

        self.horizontalLayout_11.addWidget(self.btnBrowseCards_1)

        self.btnExcelCards_1 = QPushButton(self.groupCards)
        self.btnExcelCards_1.setObjectName(u"btnExcelCards_1")
        self.btnExcelCards_1.setStyleSheet(u"\n"
"      QPushButton {\n"
"       background-color: #2a4d6b;\n"
"       color: #ffffff;\n"
"       border: 1px solid #4a6b8a;\n"
"       border-radius: 4px;\n"
"		padding: 6px;\n"
"      }\n"
"      QPushButton:hover { background-color: #3a5d7b; }\n"
"      QPushButton:pressed { background-color: #1a3d5b; }\n"
"     ")

        self.horizontalLayout_11.addWidget(self.btnExcelCards_1)


        self.verticalLayout_5.addWidget(self.groupCards)

        self.groupPartes = QGroupBox(self.frameBackup)
        self.groupPartes.setObjectName(u"groupPartes")
        self.groupPartes.setStyleSheet(u"\n"
"     QGroupBox {\n"
"      border: 1px solid #555;\n"
"      margin-top: 10px;\n"
"      font-weight: bold;\n"
"	border-radius:10px;\n"
"     }\n"
"     QGroupBox::title {\n"
"      subcontrol-origin: margin;\n"
"      left: 10px;\n"
"      padding: 0 5px 0 5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"     }\n"
"    ")
        self.horizontalLayout_10 = QHBoxLayout(self.groupPartes)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lePartes_2 = QLineEdit(self.groupPartes)
        self.lePartes_2.setObjectName(u"lePartes_2")
        self.lePartes_2.setStyleSheet(u"\n"
"      QLineEdit {\n"
"       background-color: #2a2a2a;\n"
"       color: #ffffff;\n"
"       border: 1px solid #555;\n"
"       border-radius: 4px;\n"
"       padding: 4px;\n"
"      }\n"
"     ")

        self.horizontalLayout_10.addWidget(self.lePartes_2)

        self.btnBrowsePartes_2 = QPushButton(self.groupPartes)
        self.btnBrowsePartes_2.setObjectName(u"btnBrowsePartes_2")
        self.btnBrowsePartes_2.setStyleSheet(u"\n"
"      QPushButton {\n"
"       background-color: #3c3c3c;\n"
"       color: #ffffff;\n"
"       border: 1px solid #555;\n"
"       border-radius: 4px;\n"
"		padding: 6px;\n"
"      }\n"
"      QPushButton:hover { background-color: #505050; }\n"
"      QPushButton:pressed { background-color: #2a2a2a; }\n"
"     ")

        self.horizontalLayout_10.addWidget(self.btnBrowsePartes_2)

        self.btnExcelPartes_2 = QPushButton(self.groupPartes)
        self.btnExcelPartes_2.setObjectName(u"btnExcelPartes_2")
        self.btnExcelPartes_2.setStyleSheet(u"\n"
"      QPushButton {\n"
"       background-color: #2a4d6b;\n"
"       color: #ffffff;\n"
"       border: 1px solid #4a6b8a;\n"
"       border-radius: 4px;\n"
"		padding: 6px;\n"
"      }\n"
"      QPushButton:hover { background-color: #3a5d7b; }\n"
"      QPushButton:pressed { background-color: #1a3d5b; }\n"
"     ")

        self.horizontalLayout_10.addWidget(self.btnExcelPartes_2)

        self.btnPDFPartes_2 = QPushButton(self.groupPartes)
        self.btnPDFPartes_2.setObjectName(u"btnPDFPartes_2")
        self.btnPDFPartes_2.setStyleSheet(u"\n"
"      QPushButton {\n"
"       background-color: #5a2a6b;\n"
"       color: #ffffff;\n"
"       border: 1px solid #7a4a8a;\n"
"       border-radius: 4px;\n"
"		padding: 6px;\n"
"      }\n"
"      QPushButton:hover { background-color: #6a3a7b; }\n"
"      QPushButton:pressed { background-color: #4a1a5b; }\n"
"     ")

        self.horizontalLayout_10.addWidget(self.btnPDFPartes_2)


        self.verticalLayout_5.addWidget(self.groupPartes)

        self.logOutput = QTextEdit(self.frameBackup)
        self.logOutput.setObjectName(u"logOutput")
        self.logOutput.setStyleSheet(u"\n"
"     QTextEdit {\n"
"      background-color: #0d0d0d;\n"
"      color: #00ff00;\n"
"      border: 1px solid #555;\n"
"      font-family: monospace;\n"
"      font-size: 9pt;\n"
"	border-radius:10px;\n"
"     }\n"
"    ")
        self.logOutput.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.logOutput)

        self.limpiarbtn = QPushButton(self.frameBackup)
        self.limpiarbtn.setObjectName(u"limpiarbtn")
        self.limpiarbtn.setStyleSheet(u"\n"
"      QPushButton {\n"
"       background-color: #2a4d6b;\n"
"       color: #ffffff;\n"
"       border: 1px solid #4a6b8a;\n"
"       border-radius: 4px;\n"
"		padding: 6px;\n"
"      }\n"
"      QPushButton:hover { background-color: #3a5d7b; }\n"
"      QPushButton:pressed { background-color: #1a3d5b; }\n"
"     ")

        self.verticalLayout_5.addWidget(self.limpiarbtn)


        self.horizontalLayout_9.addWidget(self.frameBackup)

        self.scrollSettings.setWidget(self.scrollAreaWidgetSettings)

        self.horizontalLayout_4.addWidget(self.scrollSettings)

        self.CentralStack.addWidget(self.PageSettings)
        self.PageJapon = QWidget()
        self.PageJapon.setObjectName(u"PageJapon")
        self.horizontalLayout_3 = QHBoxLayout(self.PageJapon)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CentralStack.addWidget(self.PageJapon)

        self.CentralHorLay.addWidget(self.CentralStack)


        self.RightLay.addWidget(self.RightCentralFrame)


        self.MainLay.addWidget(self.RightFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnHome.toggled.connect(self.CentralStack.setCurrentIndex)
        self.btnCalculator.toggled.connect(self.CentralStack.setCurrentIndex)
        self.btnJapon.toggled.connect(self.CentralStack.setCurrentIndex)
        self.btnDocuments.toggled.connect(self.CentralStack.setCurrentIndex)
        self.BtnAyuda.toggled.connect(self.CentralStack.setCurrentIndex)

        self.CentralStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EDMonitor \u2013 CEGA NIC", None))
        self.CegaNicButton.setText(QCoreApplication.translate("MainWindow", u"EDMonitor  ", None))
        self.BtnSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.labelIconoEmpresa.setText("")
        self.labelNombreEmpresa.setText(QCoreApplication.translate("MainWindow", u"CEGA Nicaragua S.A ", None))
        self.BtnDoc.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnDocuments.setText(QCoreApplication.translate("MainWindow", u"Cards", None))
        self.btnCalculator.setText(QCoreApplication.translate("MainWindow", u"Japon", None))
        self.btnJapon.setText(QCoreApplication.translate("MainWindow", u"Gages", None))
        self.BtnAyuda.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.BtnSalir.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.heroTitle.setText(QCoreApplication.translate("MainWindow", u"WIRE EDM", None))
        self.heroSubtitle.setText(QCoreApplication.translate("MainWindow", u"Electrical Discharge Machining de Alta Precisi\u00f3n", None))
        self.cardPrecision.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardRoot", None))
        self.cardPrecisionInner.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardInner", None))
        self.cardPrecisionTitle.setText(QCoreApplication.translate("MainWindow", u"Precisi\u00f3n", None))
        self.cardPrecisionValue.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.cardMaterial.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardRoot", None))
        self.cardMaterialInner.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardInner", None))
        self.cardMaterialTitle.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        self.cardMaterialValue.setText(QCoreApplication.translate("MainWindow", u"Conductores", None))
        self.cardProcess.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardRoot", None))
        self.cardProcessInner.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardInner", None))
        self.cardProcessTitle.setText(QCoreApplication.translate("MainWindow", u"Proceso de corte", None))
        self.cardProcessValue.setText(QCoreApplication.translate("MainWindow", u"Sin contacto", None))
        self.sectionWhatTitle.setText(QCoreApplication.translate("MainWindow", u"\u00bfQu\u00e9 es Wire EDM?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Una m\u00e1quina Wire EDM (Electro Discharge Machining por hilo) es una m\u00e1quina CNC de precisi\u00f3n que corta formas complejas en materiales conductores usando un fino hilo met\u00e1lico (electrodo) que genera chispas el\u00e9ctricas controladas para erosionar el material, logrando cortes extremadamente precisos, tolerancias ajustadas y geometr\u00edas dif\u00edciles de mecanizar con m\u00e9todos tradicionales, ideal para industrias como la aeroespacial y m\u00e9dica. \n"
"\n"
"C\u00f3mo funciona:\n"
"1. Electrodo de Hilo: Un hilo delgado (lat\u00f3n, cobre) act\u00faa como electrodo, movi\u00e9ndose a trav\u00e9s de la pieza de trabajo.\n"
"2. Descargas El\u00e9ctricas (Chispas): Se aplica un alto voltaje entre el hilo y la pieza, creando chispas que funden y vaporizan peque\u00f1as cantidades de material conductor.\n"
"3. Fluido Diel\u00e9ctrico: La m\u00e1quina sumerge la pieza en un fluido (agua desionizada) que enfr\u00eda, lubrica y ayuda a eliminar las part\u00edculas erosionadas, permitiendo el "
                        "corte y la recirculaci\u00f3n del proceso.\n"
"4. Movimiento CNC: Un control num\u00e9rico (CNC) gu\u00eda el hilo a lo largo de una trayectoria programada, permitiendo cortes rectos, c\u00f3nicos y formas tridimensionales.", None))
        self.fact1.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardRoot", None))
        self.fact1Inner.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardInner", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No usa fuerza mec\u00e1nica", None))
        self.fact2.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardRoot", None))
        self.fact2Inner.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardInner", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Corta aceros templados", None))
        self.fact3.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardRoot", None))
        self.fact3Inner.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cardInner", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Geometr\u00edas complejas", None))
        self.btnAddCard.setText(QCoreApplication.translate("MainWindow", u"Agregar Tarjeta", None))
        self.groupCards.setTitle(QCoreApplication.translate("MainWindow", u"Base de Datos - Tarjetas (Cards)", None))
        self.leCards_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ruta para guardar Excel de Cards...", None))
        self.btnBrowseCards_1.setText(QCoreApplication.translate("MainWindow", u"Examinar", None))
        self.btnExcelCards_1.setText(QCoreApplication.translate("MainWindow", u"Exportar Excel Cards", None))
        self.groupPartes.setTitle(QCoreApplication.translate("MainWindow", u"Base de Datos - Partes", None))
        self.lePartes_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ruta para guardar Excel de Partes...", None))
        self.btnBrowsePartes_2.setText(QCoreApplication.translate("MainWindow", u"Examinar", None))
        self.btnExcelPartes_2.setText(QCoreApplication.translate("MainWindow", u"Exportar Excel Partes", None))
        self.btnPDFPartes_2.setText(QCoreApplication.translate("MainWindow", u"Generar PDF Partes", None))
        self.logOutput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Estado de operaciones...", None))
        self.limpiarbtn.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
    # retranslateUi

