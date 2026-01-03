# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wire_edm_widgetmOhtvx.ui'
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
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_WireEDMPremium(object):
    def setupUi(self, WireEDMPremium):
        if not WireEDMPremium.objectName():
            WireEDMPremium.setObjectName(u"WireEDMPremium")
        WireEDMPremium.resize(768, 623)
        WireEDMPremium.setStyleSheet(u"/* =========================\n"
"   GLOBAL\n"
"========================= */\n"
"QWidget {\n"
"    background-color: #020617;\n"
"    color: #e5e7eb;\n"
"    font-family: \"Segoe UI\";\n"
"}\n"
"\n"
"/* =========================\n"
"   HERO\n"
"========================= */\n"
"#heroFrame {\n"
"	border-radius:20px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #2563eb,\n"
"        stop:1 #06b6d4\n"
"    );\n"
"    padding: 40px;\n"
"}\n"
"\n"
"#heroTitle {\n"
"	border-radius:20px;\n"
" 	 background-color: transparent;\n"
"    font-size: 44px;\n"
"    font-weight: 900;\n"
"    letter-spacing: 5px;\n"
"	 padding: 6px;\n"
"}\n"
"\n"
"#heroSubtitle {\n"
"	 background-color: transparent;\n"
"	border-radius:5px;\n"
"    font-size: 16px;\n"
"    color: #e0f2fe;\n"
"	 padding: 6px;\n"
"}\n"
"\n"
"/* =========================\n"
"   CARD ROOT (GLASS + NEON)\n"
"========================= */\n"
"QFrame[role=\"cardRoot\"] {\n"
"    border-radius: 22px;\n"
"    background-color: "
                        "rgba(2, 6, 23, 0.65);\n"
"    border: 1px solid rgba(148, 163, 184, 0.25);\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QFrame[role=\"cardRoot\"]:hover {\n"
"    border: 1px solid rgba(56, 189, 248, 1);\n"
"    background-color: rgba(2, 6, 23, 0.85);\n"
"}\n"
"\n"
"/* =========================\n"
"   CARD INNER (GLASS)\n"
"========================= */\n"
"QFrame[role=\"cardInner\"] {\n"
"    border-radius: 18px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(255,255,255,0.15),\n"
"        stop:1 rgba(255,255,255,0.03)\n"
"    );\n"
"    padding: 16px;\n"
"}\n"
"\n"
"/* =========================\n"
"   TEXT\n"
"========================= */\n"
"QFrame[role=\"cardInner\"] QLabel {\n"
"    background: transparent;\n"
"    color: #f8fafc;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#cardPrecisionTitle,\n"
"#cardMaterialTitle,\n"
"#cardProcessTitle {\n"
"    color: #94a3b8;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#cardPrecisionValue,\n"
"#cardMaterialValue,\n"
"#cardProcessValu"
                        "e {\n"
"    font-size: 22px;\n"
"    font-weight: 800;\n"
"}\n"
"\n"
"/* =========================\n"
"   NEON COLORS\n"
"========================= */\n"
"#cardPrecision { background-color: rgba(14,165,233,0.3); }\n"
"#cardMaterial  { background-color: rgba(34,197,94,0.3); }\n"
"#cardProcess   { background-color: rgba(245,158,11,0.3); }\n"
"\n"
"#fact1 { background-color: rgba(124,58,237,0.4); }\n"
"#fact2 { background-color: rgba(236,72,153,0.4); }\n"
"#fact3 { background-color: rgba(16,185,129,0.4); }\n"
"\n"
"/* =========================\n"
"   NOTE SECTION\n"
"========================= */\n"
"#sectionWhat {\n"
"    border-radius: 24px;\n"
"    padding: 24px;\n"
"    border: 1px solid rgba(148, 163, 184, 0.25);\n"
"}\n"
"\n"
"#sectionWhatTitle {\n"
"    font-size: 22px;\n"
"    font-weight: 700;\n"
"    color: #38bdf8;\n"
"}\n"
"\n"
"#sectionWhatText {\n"
"    line-height: 1.6em;\n"
"}\n"
"\n"
"/* =========================\n"
"   MEDIA\n"
"========================= */\n"
"#mediaPlaceholder {\n"
"    border:"
                        " 3px dashed #38bdf8;\n"
"    border-radius: 24px;\n"
"    font-size: 18px;\n"
"    color: #38bdf8;\n"
"}\n"
"")
        self.mainLayout = QVBoxLayout(WireEDMPremium)
        self.mainLayout.setObjectName(u"mainLayout")
        self.heroFrame = QFrame(WireEDMPremium)
        self.heroFrame.setObjectName(u"heroFrame")
        self.vboxLayout = QVBoxLayout(self.heroFrame)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.heroTitle = QLabel(self.heroFrame)
        self.heroTitle.setObjectName(u"heroTitle")
        self.heroTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.heroTitle)

        self.heroSubtitle = QLabel(self.heroFrame)
        self.heroSubtitle.setObjectName(u"heroSubtitle")
        self.heroSubtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.heroSubtitle)


        self.mainLayout.addWidget(self.heroFrame)

        self.scrollArea = QScrollArea(WireEDMPremium)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QWidget()
        self.scrollContent.setObjectName(u"scrollContent")
        self.scrollContent.setGeometry(QRect(-393, 0, 1126, 775))
        self.vboxLayout1 = QVBoxLayout(self.scrollContent)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.lay_2 = QHBoxLayout()
        self.lay_2.setObjectName(u"lay_2")
        self.cardPrecision = QFrame(self.scrollContent)
        self.cardPrecision.setObjectName(u"cardPrecision")
        self.vboxLayout2 = QVBoxLayout(self.cardPrecision)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.cardPrecisionInner = QFrame(self.cardPrecision)
        self.cardPrecisionInner.setObjectName(u"cardPrecisionInner")
        self.vboxLayout3 = QVBoxLayout(self.cardPrecisionInner)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.cardPrecisionIcon = QLabel(self.cardPrecisionInner)
        self.cardPrecisionIcon.setObjectName(u"cardPrecisionIcon")
        self.cardPrecisionIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout3.addWidget(self.cardPrecisionIcon)

        self.cardPrecisionTitle = QLabel(self.cardPrecisionInner)
        self.cardPrecisionTitle.setObjectName(u"cardPrecisionTitle")
        self.cardPrecisionTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout3.addWidget(self.cardPrecisionTitle)

        self.cardPrecisionValue = QLabel(self.cardPrecisionInner)
        self.cardPrecisionValue.setObjectName(u"cardPrecisionValue")
        self.cardPrecisionValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout3.addWidget(self.cardPrecisionValue)


        self.vboxLayout2.addWidget(self.cardPrecisionInner)


        self.lay_2.addWidget(self.cardPrecision)

        self.cardMaterial = QFrame(self.scrollContent)
        self.cardMaterial.setObjectName(u"cardMaterial")
        self.vboxLayout4 = QVBoxLayout(self.cardMaterial)
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.cardMaterialInner = QFrame(self.cardMaterial)
        self.cardMaterialInner.setObjectName(u"cardMaterialInner")
        self.vboxLayout5 = QVBoxLayout(self.cardMaterialInner)
        self.vboxLayout5.setObjectName(u"vboxLayout5")
        self.cardMaterialIcon = QLabel(self.cardMaterialInner)
        self.cardMaterialIcon.setObjectName(u"cardMaterialIcon")
        self.cardMaterialIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout5.addWidget(self.cardMaterialIcon)

        self.cardMaterialTitle = QLabel(self.cardMaterialInner)
        self.cardMaterialTitle.setObjectName(u"cardMaterialTitle")
        self.cardMaterialTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout5.addWidget(self.cardMaterialTitle)

        self.cardMaterialValue = QLabel(self.cardMaterialInner)
        self.cardMaterialValue.setObjectName(u"cardMaterialValue")
        self.cardMaterialValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout5.addWidget(self.cardMaterialValue)


        self.vboxLayout4.addWidget(self.cardMaterialInner)


        self.lay_2.addWidget(self.cardMaterial)

        self.cardProcess = QFrame(self.scrollContent)
        self.cardProcess.setObjectName(u"cardProcess")
        self.vboxLayout6 = QVBoxLayout(self.cardProcess)
        self.vboxLayout6.setObjectName(u"vboxLayout6")
        self.cardProcessInner = QFrame(self.cardProcess)
        self.cardProcessInner.setObjectName(u"cardProcessInner")
        self.vboxLayout7 = QVBoxLayout(self.cardProcessInner)
        self.vboxLayout7.setObjectName(u"vboxLayout7")
        self.cardProcessIcon = QLabel(self.cardProcessInner)
        self.cardProcessIcon.setObjectName(u"cardProcessIcon")
        self.cardProcessIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout7.addWidget(self.cardProcessIcon)

        self.cardProcessTitle = QLabel(self.cardProcessInner)
        self.cardProcessTitle.setObjectName(u"cardProcessTitle")
        self.cardProcessTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout7.addWidget(self.cardProcessTitle)

        self.cardProcessValue = QLabel(self.cardProcessInner)
        self.cardProcessValue.setObjectName(u"cardProcessValue")
        self.cardProcessValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout7.addWidget(self.cardProcessValue)


        self.vboxLayout6.addWidget(self.cardProcessInner)


        self.lay_2.addWidget(self.cardProcess)


        self.vboxLayout1.addLayout(self.lay_2)

        self.sectionWhat = QFrame(self.scrollContent)
        self.sectionWhat.setObjectName(u"sectionWhat")
        self.vboxLayout8 = QVBoxLayout(self.sectionWhat)
        self.vboxLayout8.setObjectName(u"vboxLayout8")
        self.sectionWhatTitle = QLabel(self.sectionWhat)
        self.sectionWhatTitle.setObjectName(u"sectionWhatTitle")
        self.sectionWhatTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout8.addWidget(self.sectionWhatTitle)

        self.label_2 = QLabel(self.sectionWhat)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.TextFormat.RichText)

        self.vboxLayout8.addWidget(self.label_2)


        self.vboxLayout1.addWidget(self.sectionWhat)

        self.lay_1 = QHBoxLayout()
        self.lay_1.setObjectName(u"lay_1")
        self.fact1 = QFrame(self.scrollContent)
        self.fact1.setObjectName(u"fact1")
        self.vboxLayout9 = QVBoxLayout(self.fact1)
        self.vboxLayout9.setObjectName(u"vboxLayout9")
        self.fact1Inner = QFrame(self.fact1)
        self.fact1Inner.setObjectName(u"fact1Inner")
        self.vboxLayout10 = QVBoxLayout(self.fact1Inner)
        self.vboxLayout10.setObjectName(u"vboxLayout10")
        self.label = QLabel(self.fact1Inner)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout10.addWidget(self.label)

        self.label1 = QLabel(self.fact1Inner)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout10.addWidget(self.label1)


        self.vboxLayout9.addWidget(self.fact1Inner)


        self.lay_1.addWidget(self.fact1)

        self.fact2 = QFrame(self.scrollContent)
        self.fact2.setObjectName(u"fact2")
        self.vboxLayout11 = QVBoxLayout(self.fact2)
        self.vboxLayout11.setObjectName(u"vboxLayout11")
        self.fact2Inner = QFrame(self.fact2)
        self.fact2Inner.setObjectName(u"fact2Inner")
        self.vboxLayout12 = QVBoxLayout(self.fact2Inner)
        self.vboxLayout12.setObjectName(u"vboxLayout12")
        self.label2 = QLabel(self.fact2Inner)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout12.addWidget(self.label2)

        self.label3 = QLabel(self.fact2Inner)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout12.addWidget(self.label3)


        self.vboxLayout11.addWidget(self.fact2Inner)


        self.lay_1.addWidget(self.fact2)

        self.fact3 = QFrame(self.scrollContent)
        self.fact3.setObjectName(u"fact3")
        self.vboxLayout13 = QVBoxLayout(self.fact3)
        self.vboxLayout13.setObjectName(u"vboxLayout13")
        self.fact3Inner = QFrame(self.fact3)
        self.fact3Inner.setObjectName(u"fact3Inner")
        self.vboxLayout14 = QVBoxLayout(self.fact3Inner)
        self.vboxLayout14.setObjectName(u"vboxLayout14")
        self.label4 = QLabel(self.fact3Inner)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout14.addWidget(self.label4)

        self.label5 = QLabel(self.fact3Inner)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout14.addWidget(self.label5)


        self.vboxLayout13.addWidget(self.fact3Inner)


        self.lay_1.addWidget(self.fact3)


        self.vboxLayout1.addLayout(self.lay_1)

        self.mediaPlaceholder = QFrame(self.scrollContent)
        self.mediaPlaceholder.setObjectName(u"mediaPlaceholder")
        self.mediaPlaceholder.setFrameShape(QFrame.Shape.StyledPanel)
        self.mediaPlaceholder.setFrameShadow(QFrame.Shadow.Raised)

        self.vboxLayout1.addWidget(self.mediaPlaceholder)

        self.scrollArea.setWidget(self.scrollContent)

        self.mainLayout.addWidget(self.scrollArea)


        self.retranslateUi(WireEDMPremium)

        QMetaObject.connectSlotsByName(WireEDMPremium)
    # setupUi

    def retranslateUi(self, WireEDMPremium):
        self.heroTitle.setText(QCoreApplication.translate("WireEDMPremium", u"WIRE EDM", None))
        self.heroSubtitle.setText(QCoreApplication.translate("WireEDMPremium", u"Electrical Discharge Machining de Alta Precisi\u00f3n", None))
        self.cardPrecision.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardRoot", None))
        self.cardPrecisionInner.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardInner", None))
        self.cardPrecisionIcon.setText(QCoreApplication.translate("WireEDMPremium", u"\ud83c\udfaf", None))
        self.cardPrecisionTitle.setText(QCoreApplication.translate("WireEDMPremium", u"Precisi\u00f3n", None))
        self.cardPrecisionValue.setText(QCoreApplication.translate("WireEDMPremium", u"Alta", None))
        self.cardMaterial.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardRoot", None))
        self.cardMaterialInner.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardInner", None))
        self.cardMaterialIcon.setText(QCoreApplication.translate("WireEDMPremium", u"\ud83e\uddf2", None))
        self.cardMaterialTitle.setText(QCoreApplication.translate("WireEDMPremium", u"Materiales", None))
        self.cardMaterialValue.setText(QCoreApplication.translate("WireEDMPremium", u"Conductores", None))
        self.cardProcess.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardRoot", None))
        self.cardProcessInner.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardInner", None))
        self.cardProcessIcon.setText(QCoreApplication.translate("WireEDMPremium", u"\u2699\ufe0f", None))
        self.cardProcessTitle.setText(QCoreApplication.translate("WireEDMPremium", u"Proceso de corte", None))
        self.cardProcessValue.setText(QCoreApplication.translate("WireEDMPremium", u"Sin contacto", None))
        self.sectionWhatTitle.setText(QCoreApplication.translate("WireEDMPremium", u"\u00bfQu\u00e9 es Wire EDM?", None))
        self.label_2.setText(QCoreApplication.translate("WireEDMPremium", u"<html><head/><body><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#2e86c1;\">\u26a1 EDM Wire (Electroerosi\u00f3n por Hilo)</span></h2><p>El <span style=\" font-weight:700;\">EDM Wire</span> es un proceso de mecanizado de precisi\u00f3n que utiliza descargas el\u00e9ctricas controladas para cortar materiales conductores duros, creando geometr\u00edas complejas con acabados finos. \u2699\ufe0f </p><p><span style=\" font-weight:700;\">\ud83d\udd0d Significado:</span><br/><span style=\" font-style:italic;\">Electrical Discharge Machining</span> (Mecanizado por Descarga El\u00e9ctrica). </p><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700; color:#28b463;\">\ud83d\ude80 \u00bfC\u00f3mo funciona?</span></h3><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-l"
                        "eft: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u26a1 Chispas El\u00e9ctricas:</span> Corriente entre un hilo (lat\u00f3n/molibdeno) y la pieza. </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\ud83d\udd25 Erosi\u00f3n:</span> Las chispas vaporizan el material siguiendo la trayectoria. </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\ud83d\udca7 Fluido Diel\u00e9ctrico:</span> Agua desionizada que enfr\u00eda y limpia el residuo. </li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\ud83c\udfaf Corte Preciso:</span> Movimie"
                        "nto continuo guiado por <span style=\" font-weight:700;\">CNC</span>. </li></ul><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700; color:#e67e22;\">\ud83d\udee0\ufe0f Aplicaciones Comunes</span></h3><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ud83c\udfd7\ufe0f Fabricaci\u00f3n de <span style=\" font-weight:700;\">moldes y matrices</span>. </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2708\ufe0f Componentes <span style=\" font-weight:700;\">aeroespaciales y m\u00e9dicos</span>. </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2702\ufe0f Herramient"
                        "as de corte, punzones y troqueles. </li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ud83d\udc8e Piezas con <span style=\" font-weight:700;\">detalles ultra-finos</span>. </li></ul><p><span style=\" font-weight:700;\">\ud83d\udccc En resumen:</span> Tecnolog\u00eda avanzada para cortar metales con precisi\u00f3n extrema, sin contacto f\u00edsico, usando energ\u00eda de chispas. </p></body></html>", None))
        self.fact1.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardRoot", None))
        self.fact1Inner.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardInner", None))
        self.label.setText(QCoreApplication.translate("WireEDMPremium", u"\u26a1", None))
        self.label1.setText(QCoreApplication.translate("WireEDMPremium", u"No usa fuerza mec\u00e1nica", None))
        self.fact2.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardRoot", None))
        self.fact2Inner.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardInner", None))
        self.label2.setText(QCoreApplication.translate("WireEDMPremium", u"\ud83d\udd29", None))
        self.label3.setText(QCoreApplication.translate("WireEDMPremium", u"Corta aceros templados", None))
        self.fact3.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardRoot", None))
        self.fact3Inner.setProperty(u"role", QCoreApplication.translate("WireEDMPremium", u"cardInner", None))
        self.label4.setText(QCoreApplication.translate("WireEDMPremium", u"\ud83d\udcd0", None))
        self.label5.setText(QCoreApplication.translate("WireEDMPremium", u"Geometr\u00edas complejas", None))
        pass
    # retranslateUi

