# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_pdfForm(object):
    def setupUi(self, pdfForm):
        if not pdfForm.objectName():
            pdfForm.setObjectName(u"pdfForm")
        pdfForm.resize(686, 531)
        icon1 = QIcon()
        icon1.addFile(u"Images/Message To Document 2 - Copie.png", QSize(), QIcon.Normal, QIcon.Off)
        pdfForm.setWindowIcon(icon1)
        self.verticalLayout = QVBoxLayout(pdfForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.navbar = QWidget(pdfForm)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setStyleSheet(u"background-color: rgb(244, 192, 79);")
        self.horizontalLayout_3 = QHBoxLayout(self.navbar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.icon = QPushButton(self.navbar)
        self.icon.setObjectName(u"icon")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QSize(62, 58))
        self.icon.setMaximumSize(QSize(91, 85))
        self.icon.setStyleSheet(u"border-image: url(:/newPrefix/Message To Document 21.png);\n"
"border-radius: 12px;")

        self.horizontalLayout_3.addWidget(self.icon)

        self.horizontalSpacer = QSpacerItem(122, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.navbarLayout = QHBoxLayout()
        self.navbarLayout.setSpacing(10)
        self.navbarLayout.setObjectName(u"navbarLayout")
        self.excel = QPushButton(self.navbar)
        self.excel.setObjectName(u"excel")
        font = QFont()
        font.setFamily(u"Inter")
        font.setPointSize(12)
        self.excel.setFont(font)
        self.excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel.setStyleSheet(u"border: none;")

        self.navbarLayout.addWidget(self.excel)

        self.word = QPushButton(self.navbar)
        self.word.setObjectName(u"word")
        self.word.setFont(font)
        self.word.setCursor(QCursor(Qt.PointingHandCursor))
        self.word.setStyleSheet(u"border: none;")

        self.navbarLayout.addWidget(self.word)

        self.pdf = QPushButton(self.navbar)
        self.pdf.setObjectName(u"pdf")
        self.pdf.setFont(font)
        self.pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.pdf.setStyleSheet(u"border: none;")

        self.navbarLayout.addWidget(self.pdf)


        self.horizontalLayout_3.addLayout(self.navbarLayout)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 6)

        self.verticalLayout.addWidget(self.navbar)

        self.body = QWidget(pdfForm)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.messageInput = QWidget(self.body)
        self.messageInput.setObjectName(u"messageInput")
        self.messageInput.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.verticalLayout_2 = QVBoxLayout(self.messageInput)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.messageBox = QWidget(self.messageInput)
        self.messageBox.setObjectName(u"messageBox")
        self.messageBox.setStyleSheet(u"background-color: rgb(79, 149, 190);")
        self.horizontalLayout = QHBoxLayout(self.messageBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.messageLabel = QLabel(self.messageBox)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setFont(font)
        self.messageLabel.setAlignment(Qt.AlignCenter)
        self.messageLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.messageLabel)


        self.verticalLayout_2.addWidget(self.messageBox)

        self.messageEdit = QPlainTextEdit(self.messageInput)
        self.messageEdit.setObjectName(u"messageEdit")
        font1 = QFont()
        font1.setPointSize(10)
        self.messageEdit.setFont(font1)
        self.messageEdit.setStyleSheet(u"border: none;\n"
"")

        self.verticalLayout_2.addWidget(self.messageEdit)

        self.takeFileTxt = QPushButton(self.messageInput)
        self.takeFileTxt.setObjectName(u"takeFileTxt")
        sizePolicy.setHeightForWidth(self.takeFileTxt.sizePolicy().hasHeightForWidth())
        self.takeFileTxt.setSizePolicy(sizePolicy)
        self.takeFileTxt.setFont(font)
        self.takeFileTxt.setCursor(QCursor(Qt.PointingHandCursor))
        self.takeFileTxt.setStyleSheet(u"background-color: rgb(79, 149, 190);\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.takeFileTxt)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout_2.addWidget(self.messageInput)

        self.centralPart = QWidget(self.body)
        self.centralPart.setObjectName(u"centralPart")
        self.centralPart.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.centralPart)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 20)
        self.inputBox = QWidget(self.centralPart)
        self.inputBox.setObjectName(u"inputBox")
        self.verticalLayout_3 = QVBoxLayout(self.inputBox)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.inputBox)
        self.title.setObjectName(u"title")
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.title)

        self.titleEdit = QLineEdit(self.inputBox)
        self.titleEdit.setObjectName(u"titleEdit")
        sizePolicy.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy)
        self.titleEdit.setFont(font1)
        self.titleEdit.setStyleSheet(u"border: 5px solid rgb(244, 192, 79);\n"
"border-radius: 16px;")

        self.verticalLayout_3.addWidget(self.titleEdit)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)

        self.verticalLayout_4.addWidget(self.inputBox)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.wordConvert = QCheckBox(self.centralPart)
        self.wordConvert.setObjectName(u"wordConvert")
        font2 = QFont()
        font2.setFamily(u"Inter")
        font2.setPointSize(10)
        self.wordConvert.setFont(font2)
        self.wordConvert.setCursor(QCursor(Qt.PointingHandCursor))
        self.wordConvert.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.wordConvert)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.info = QLabel(self.centralPart)
        self.info.setObjectName(u"info")
        self.info.setFont(font2)
        self.info.setWordWrap(True)
        self.info.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.info)

        self.compile = QPushButton(self.centralPart)
        self.compile.setObjectName(u"compile")
        sizePolicy.setHeightForWidth(self.compile.sizePolicy().hasHeightForWidth())
        self.compile.setSizePolicy(sizePolicy)
        self.compile.setFont(font)
        self.compile.setCursor(QCursor(Qt.PointingHandCursor))
        self.compile.setStyleSheet(u"background-color: rgb(244, 192, 79);\n"
"border-radius: 16px;\n"
"")

        self.verticalLayout_4.addWidget(self.compile)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(2, 9)
        self.verticalLayout_4.setStretch(3, 1)

        self.horizontalLayout_2.addWidget(self.centralPart)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.body)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)

        self.retranslateUi(pdfForm)
        self.titleEdit.returnPressed.connect(self.compile.animateClick)

        QMetaObject.connectSlotsByName(pdfForm)
    # setupUi

    def retranslateUi(self, pdfForm):
        pdfForm.setWindowTitle(QCoreApplication.translate("pdfForm", u"Compilez vers PDF - Message To Doc", None))
        self.icon.setText("")
        self.excel.setText(QCoreApplication.translate("pdfForm", u"Compiler vers Excel", None))
        self.word.setText(QCoreApplication.translate("pdfForm", u"Compiler vers Word", None))
        self.pdf.setText(QCoreApplication.translate("pdfForm", u"Compiler vers PDF", None))
        self.messageLabel.setText(QCoreApplication.translate("pdfForm", u"<html><head/><body><p>Message \u00e0 utiliser <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.takeFileTxt.setText(QCoreApplication.translate("pdfForm", u"Importer un fichier txt", None))
        self.title.setText(QCoreApplication.translate("pdfForm", u"<html><head/><body><p>Titre du document <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.wordConvert.setText(QCoreApplication.translate("pdfForm", u"Pr\u00e9convertir d'abord en Word", None))
        self.info.setText(QCoreApplication.translate("pdfForm", u"<html><head/><body><p>Pour faciliter la transformation en document structur\u00e9 PDF, assurez-vous d'utiliser une structure coh\u00e9rente dans votre message texte. Utilisez des num\u00e9ros ou des lettres pour identifier les diff\u00e9rentes parties de votre message et gardez la m\u00eame structure tout au long du document. Cela permettra \u00e0 l'application de cr\u00e9er un document PDF bien structur\u00e9 et facile \u00e0 lire.</p></body></html>", None))
        self.compile.setText(QCoreApplication.translate("pdfForm", u"Transformer en PDF", None))
    # retranslateUi

