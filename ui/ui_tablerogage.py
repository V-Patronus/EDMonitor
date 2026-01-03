# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gagesBoardtlmpur.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_TableroGageWidget(object):
    def setupUi(self, TableroGageWidget):
        if not TableroGageWidget.objectName():
            TableroGageWidget.setObjectName(u"TableroGageWidget")
        TableroGageWidget.resize(1135, 753)
        TableroGageWidget.setStyleSheet(u"\n"
"    QWidget { background-color: #1e1e1e; color: #ffffff; font-family: \"Segoe UI\"; }\n"
"    QGroupBox {\n"
"     background-color: #2a2a2a;\n"
"     border: 1px solid #444;\n"
"     border-radius: 8px;\n"
"     margin-top: 6px;\n"
"     font-weight: bold;\n"
"    }\n"
"    QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 4px; }\n"
"    QScrollArea { border: none; }\n"
"    QPushButton {\n"
"     background-color: #2563eb;\n"
"     color: white;\n"
"     border: none;\n"
"     padding: 6px 10px;\n"
"     border-radius: 4px;\n"
"     font-size: 11px;\n"
"    }\n"
"    QPushButton:hover { background-color: #3b82f6; }\n"
"    QPushButton:pressed { background-color: #1d4ed8; }\n"
"    QLineEdit {\n"
"     background-color: #2a2a2a;\n"
"     border: 1px solid #444;\n"
"     padding: 6px;\n"
"     border-radius: 4px;\n"
"     color: #ffffff;\n"
"    }\n"
"    QLineEdit[valid=\"false\"] { border: 1px solid #e74c3c; }\n"
"    QLabel { color: #ffffff; font-size: 12px; }\n"
"    QLabel.chip {\n"
""
                        "     background-color: #ffffff;\n"
"     color: #000000;\n"
"     border-radius: 4px;\n"
"     padding: 4px;\n"
"     font-size: 11px;\n"
"     min-width: 250px;\n"
"    }\n"
"    QLabel.chip.found { background-color: #22c55e; color: white; }\n"
"\n"
"QLabel#totalPartes {\n"
"        background-color: #2d2d2d;      /* Fondo gris oscuro */\n"
"        color: #e0e0e0;                 /* Texto blanco suave */\n"
"        border: 1px solid #3d3d3d;      /* Borde sutil */\n"
"        border-radius: 10px;            /* Esquinas redondeadas */\n"
"        padding: 5px 15px;              /* Espaciado interno */\n"
"        font-family: 'Segoe UI', Arial; /* Tipograf\u00eda moderna */\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"}\n"
"   ")
        self.mainLayout = QVBoxLayout(TableroGageWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.headerFrame = QFrame(TableroGageWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerLayout = QHBoxLayout(self.headerFrame)
        self.headerLayout.setObjectName(u"headerLayout")
        self.searchInput = QLineEdit(self.headerFrame)
        self.searchInput.setObjectName(u"searchInput")

        self.headerLayout.addWidget(self.searchInput)

        self.searchButton = QPushButton(self.headerFrame)
        self.searchButton.setObjectName(u"searchButton")

        self.headerLayout.addWidget(self.searchButton)

        self.addButton = QPushButton(self.headerFrame)
        self.addButton.setObjectName(u"addButton")

        self.headerLayout.addWidget(self.addButton)

        self.restoreButton = QPushButton(self.headerFrame)
        self.restoreButton.setObjectName(u"restoreButton")

        self.headerLayout.addWidget(self.restoreButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)

        self.totalPartes = QLabel(self.headerFrame)
        self.totalPartes.setObjectName(u"totalPartes")

        self.headerLayout.addWidget(self.totalPartes)


        self.mainLayout.addWidget(self.headerFrame)

        self.scrollArea = QScrollArea(TableroGageWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollWidget = QWidget()
        self.scrollWidget.setObjectName(u"scrollWidget")
        self.scrollWidget.setGeometry(QRect(0, 0, 1117, 679))
        self.gridLayout = QGridLayout(self.scrollWidget)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.scrollWidget)

        self.mainLayout.addWidget(self.scrollArea)


        self.retranslateUi(TableroGageWidget)

        QMetaObject.connectSlotsByName(TableroGageWidget)
    # setupUi

    def retranslateUi(self, TableroGageWidget):
        TableroGageWidget.setWindowTitle(QCoreApplication.translate("TableroGageWidget", u"Tablero de Partes - Gages", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("TableroGageWidget", u"Buscar n\u00famero de parte", None))
        self.searchButton.setText(QCoreApplication.translate("TableroGageWidget", u"Buscar", None))
        self.addButton.setText(QCoreApplication.translate("TableroGageWidget", u"A\u00f1adir", None))
        self.restoreButton.setText(QCoreApplication.translate("TableroGageWidget", u"Restaurar", None))
        self.totalPartes.setText(QCoreApplication.translate("TableroGageWidget", u"Total de Partes: 00", None))
    # retranslateUi

