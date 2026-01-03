# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowZWWQSU.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(736, 497)
        MainWindow.setStyleSheet(u"/* ===== VENTANA PRINCIPAL ===== */\n"
"#centralwidget{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #0f172a, stop:1 #1e293b);\n"
"}\n"
"\n"
"#CentralStack QWidget {\n"
"	background: #0D1017;\n"
"}\n"
"\n"
"/* ===== LATERAL IZQUIERDO - GLASSMORPHISM ===== */\n"
"\n"
"\n"
"/* ===== BOT\u00d3N CEGA NIC - ESTILO PREMIUM ===== */\n"
"#CegaNicButton{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #3b82f6, stop:1 #8b5cf6);\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 12px 20px;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"    margin: 8px;\n"
"    \n"
"}\n"
"#CegaNicButton:hover{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #2563eb, stop:1 #7c3aed);\n"
"}\n"
"\n"
"#SideBarGroup, #SideBarFrame {\n"
"border:transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ===== BOTONES DEL GRUPO LATERAL - ESTADOS MODERNOS ===== */\n"
"#SideBarGroup QPushButton{\n"
"    background: rgba(60,"
                        " 63, 65, 0.5);\n"
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
"    background: rgba(45, 48, 50, 0.8);\n"
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
"/*"
                        " ESTADO INACTIVO/DESENFocado - Atenuado */\n"
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
"        stop:0 #020c1b, stop:0.2 #0a1929, stop:0.5 #14213d, stop:0.8 #1e3a5f, stop:1 #2a4a70);;\n"
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
"#SearchLi"
                        "ne:focus {\n"
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
"  background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #006b8f, stop:1 #0099cc);\n"
"    color: #ffffff;\n"
"    border: 1px solid rgba(85, 85, 85, 0.3);\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 12px;\n"
"    font-weight: 500;\n"
"}\n"
"#TopBarGroup QPushButton:hover{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #00708c, stop:1 #00a8f4);\n"
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
"QScr"
                        "ollBar:vertical {\n"
"    background: transparent;\n"
"    width: 14px;\n"
"    border: none;\n"
"    margin: 16px 0 16px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
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
""
                        "    border: 1px solid rgba(0, 180, 216, 0.4);\n"
"    border-radius: 7px;\n"
"    height: 14px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
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
"        stop:0 rgba(0, 180, 216, 0.3), stop:1 rgba(0, 119, 182, 0.5)"
                        ");\n"
"    border: 2px solid rgba(0, 180, 216, 0.6);\n"
"    border-radius: 7px;\n"
"    min-width: 30px;    \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
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
"}"
                        "\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::sub-line:horizontal:hover {\n"
"    background: rgba(0, 212, 255, 0.3);\n"
"    border-color: rgba(0, 212, 255, 0.6);\n"
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
""
                        "    background: rgb(86, 86, 86);\n"
"}\n"
"\n"
"QLabel#labelNotificacion {\n"
"    /* Fondo oscuro trasl\u00facido o s\u00f3lido */\n"
"    background-color: #2b2b2b;\n"
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
"}")
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
        self.TopBarHorLay.setObjectName(u"TopBarHorLay")
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

        self.HSpacer = QSpacerItem(131, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TopBarHorLay.addItem(self.HSpacer)

        self.TopBarGroup = QFrame(self.TopBarFrame)
        self.TopBarGroup.setObjectName(u"TopBarGroup")
        self.TopGroupLay = QHBoxLayout(self.TopBarGroup)
        self.TopGroupLay.setObjectName(u"TopGroupLay")
        self.SearchLine = QLineEdit(self.TopBarGroup)
        self.SearchLine.setObjectName(u"SearchLine")

        self.TopGroupLay.addWidget(self.SearchLine)

        self.BtnSearch = QPushButton(self.TopBarGroup)
        self.BtnSearch.setObjectName(u"BtnSearch")
        self.BtnSearch.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconos/iconos/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnSearch.setIcon(icon1)
        self.BtnSearch.setIconSize(QSize(20, 20))

        self.TopGroupLay.addWidget(self.BtnSearch)

        self.BtnClear = QPushButton(self.TopBarGroup)
        self.BtnClear.setObjectName(u"BtnClear")
        self.BtnClear.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconos/iconos/gitlab.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnClear.setIcon(icon2)
        self.BtnClear.setIconSize(QSize(20, 20))

        self.TopGroupLay.addWidget(self.BtnClear)


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
        icon4.addFile(u":/iconos/iconos/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon7.addFile(u":/iconos/iconos/slack.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.ViewerLay = QHBoxLayout(self.PageHome)
        self.ViewerLay.setObjectName(u"ViewerLay")
        self.ViewerLay.setContentsMargins(0, 0, 0, 0)
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
        self.scrollAreaWidgetCalculator.setGeometry(QRect(0, 0, 100, 30))
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
        self.scrollAreaWidgetDocuments.setGeometry(QRect(0, 0, 586, 396))
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
        font = QFont()
        font.setWeight(QFont.Medium)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btnAddCard.setFont(font)
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
        self.scrollAreaWidgetSettings.setGeometry(QRect(0, 0, 100, 30))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QtSigner \u2013 CEGA NIC", None))
        self.CegaNicButton.setText(QCoreApplication.translate("MainWindow", u"EDMonitor", None))
        self.BtnSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.BtnClear.setText(QCoreApplication.translate("MainWindow", u"  UniqueUser", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnDocuments.setText(QCoreApplication.translate("MainWindow", u"Cards", None))
        self.btnCalculator.setText(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.btnJapon.setText(QCoreApplication.translate("MainWindow", u"Gages", None))
        self.BtnAyuda.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.BtnSalir.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btnAddCard.setText(QCoreApplication.translate("MainWindow", u"Agregar Tarjeta", None))
    # retranslateUi

