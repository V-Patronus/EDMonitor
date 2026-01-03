# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cardsmihqqM.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_FuturisticCard(object):
    def setupUi(self, FuturisticCard):
        if not FuturisticCard.objectName():
            FuturisticCard.setObjectName(u"FuturisticCard")
        FuturisticCard.resize(498, 368)
        FuturisticCard.setStyleSheet(u"/* ---------- BASE ---------- */\n"
"#cardFrame{\n"
"    border-radius: 24px;\n"
"    padding: 24px;\n"
"    font-family: \"Orbitron\", sans-serif;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(10,15,30,220),\n"
"        stop:1 rgba(25,30,60,220));\n"
"    border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #00f5d4,\n"
"        stop:1 #ff00ff);\n"
"}\n"
"\n"
"#buttonWidget{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#iconLabel{\n"
"    max-width: 80px;\n"
"    max-height: 80px;\n"
"    border-radius: 5px;\n"
"    border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #00f5d4,\n"
"        stop:1 #ff00ff);\n"
"}\n"
"#nameLabel{\n"
"	background-color: transparent;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"    letter-spacing: 1px;\n"
"}\n"
"#descLabel{\n"
"    font-size: 14px;\n"
"    letter-spacing: 0.5px;\n"
"}\n"
"QPushButton{\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-weigh"
                        "t: bold;\n"
"    font-size: 13px;\n"
"    border: 1px solid rgba(255,255,255,60);\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"}\n"
"\n"
"/* ==========================================================\n"
"   TEMA NEON\n"
"   ========================================================== */\n"
"#cardFrame[value=\"neon\"] #nameLabel{ color: #00f5d4; }\n"
"#cardFrame[value=\"neon\"] #descLabel{ color: #b0b0ff; }\n"
"#cardFrame[value=\"neon\"] QPushButton{\n"
"    background: #00f5d4;\n"
"    color: #0a0f1e;\n"
"}\n"
"#cardFrame[value=\"neon\"] QPushButton:hover{ background: #ffffff; }\n"
"#cardFrame[value=\"neon\"] QPushButton:pressed{ background: #00c7ae; }\n"
"#cardFrame[value=\"neon\"] #descText{\n"
"    color: #b0b0ff;\n"
"    background: rgba(255,255,255,12);\n"
"    border: 1px solid rgba(0,245,212,80);\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-family: \"Orbitron\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* ==========================================================\n"
"   TEMA SUN"
                        "SET\n"
"   ========================================================== */\n"
"#cardFrame[value=\"sunset\"] #nameLabel{ color: #ffcc00; }\n"
"#cardFrame[value=\"sunset\"] #descLabel{ color: #ffb3d9; }\n"
"#cardFrame[value=\"sunset\"] QPushButton{\n"
"    background: #ffcc00;\n"
"    color: #2e0b18;\n"
"}\n"
"#cardFrame[value=\"sunset\"] QPushButton:hover{ background: #ffe066; }\n"
"#cardFrame[value=\"sunset\"] QPushButton:pressed{ background: #cc9900; }\n"
"#cardFrame[value=\"sunset\"] #descText{\n"
"    color: #ffb3d9;\n"
"    background: rgba(255,255,255,12);\n"
"    border: 1px solid rgba(255,204,0,80);\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-family: \"Orbitron\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* ==========================================================\n"
"   TEMA AURORA\n"
"   ========================================================== */\n"
"#cardFrame[value=\"aurora\"] #nameLabel{ color: #00ffaa; }\n"
"#cardFrame[value=\"aurora\"] #descLabel{ color: #a0ffd0; }\n"
"#cardFr"
                        "ame[value=\"aurora\"] QPushButton{\n"
"    background: #00ffaa;\n"
"    color: #002220;\n"
"}\n"
"#cardFrame[value=\"aurora\"] QPushButton:hover{ background: #80ffdd; }\n"
"#cardFrame[value=\"aurora\"] QPushButton:pressed{ background: #00cc88; }\n"
"#cardFrame[value=\"aurora\"] #descText{\n"
"    color: #a0ffd0;\n"
"    background: rgba(255,255,255,12);\n"
"    border: 1px solid rgba(0,255,170,80);\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-family: \"Orbitron\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* ==========================================================\n"
"   TEMA LAVA\n"
"   ========================================================== */\n"
"#cardFrame[value=\"lava\"] #nameLabel{ color: #ffaa00; }\n"
"#cardFrame[value=\"lava\"] #descLabel{ color: #ffccaa; }\n"
"#cardFrame[value=\"lava\"] QPushButton{\n"
"    background: #ffaa00;\n"
"    color: #1a0500;\n"
"}\n"
"#cardFrame[value=\"lava\"] QPushButton:hover{ background: #ffcc66; }\n"
"#cardFrame[value=\"lava\"] QPushButton:pressed{"
                        " background: #cc7700; }\n"
"#cardFrame[value=\"lava\"] #descText{\n"
"    color: #ffccaa;\n"
"    background: rgba(255,255,255,12);\n"
"    border: 1px solid rgba(255,170,0,80);\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-family: \"Orbitron\";\n"
"    font-size: 13px;\n"
"}")
        self.verticalLayout = QVBoxLayout(FuturisticCard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cardFrame = QFrame(FuturisticCard)
        self.cardFrame.setObjectName(u"cardFrame")
        self.cardFrame.setMinimumSize(QSize(480, 350))
        self.cardFrame.setMaximumSize(QSize(480, 350))
        self.cardFrame.setStyleSheet(u"")
        self.cardLayout = QVBoxLayout(self.cardFrame)
        self.cardLayout.setObjectName(u"cardLayout")
        self.iconLabel = QLabel(self.cardFrame)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setPixmap(QPixmap(u":/iconos/iconos/carpeta.svg"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardLayout.addWidget(self.iconLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.nameLabel = QLabel(self.cardFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nameLabel.setWordWrap(True)

        self.cardLayout.addWidget(self.nameLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.descText = QPlainTextEdit(self.cardFrame)
        self.descText.setObjectName(u"descText")
        self.descText.setReadOnly(True)

        self.cardLayout.addWidget(self.descText)

        self.buttonWidget = QWidget(self.cardFrame)
        self.buttonWidget.setObjectName(u"buttonWidget")
        self.buttonLayout = QHBoxLayout(self.buttonWidget)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.goButton = QPushButton(self.buttonWidget)
        self.goButton.setObjectName(u"goButton")

        self.buttonLayout.addWidget(self.goButton)

        self.editButton = QPushButton(self.buttonWidget)
        self.editButton.setObjectName(u"editButton")

        self.buttonLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.buttonWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.buttonLayout.addWidget(self.deleteButton)


        self.cardLayout.addWidget(self.buttonWidget)


        self.verticalLayout.addWidget(self.cardFrame)


        self.retranslateUi(FuturisticCard)

        QMetaObject.connectSlotsByName(FuturisticCard)
    # setupUi

    def retranslateUi(self, FuturisticCard):
        FuturisticCard.setWindowTitle(QCoreApplication.translate("FuturisticCard", u"FuturisticCard", None))
        self.cardFrame.setProperty(u"property", QCoreApplication.translate("FuturisticCard", u"value", None))
        self.cardFrame.setProperty(u"value", QCoreApplication.translate("FuturisticCard", u"neon", None))
        self.nameLabel.setText(QCoreApplication.translate("FuturisticCard", u"Nombre del Item", None))
        self.descText.setPlainText("")
        self.descText.setPlaceholderText(QCoreApplication.translate("FuturisticCard", u"Aqu\u00ed estar\u00e1 la descripci\u00f3n de la tarjeta", None))
        self.goButton.setText(QCoreApplication.translate("FuturisticCard", u"Ir", None))
        self.editButton.setText(QCoreApplication.translate("FuturisticCard", u"Editar", None))
        self.deleteButton.setText(QCoreApplication.translate("FuturisticCard", u"Eliminar", None))
    # retranslateUi

