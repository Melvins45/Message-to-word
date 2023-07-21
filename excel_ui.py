# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'excel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_excelForm(object):
    def setupUi(self, excelForm):
        if not excelForm.objectName():
            excelForm.setObjectName(u"excelForm")
        excelForm.resize(686, 529)
        excelForm.setMinimumSize(QSize(0, 529))
        icon1 = QIcon()
        icon1.addFile(u"Images/Message To Document 2 - Copie.png", QSize(), QIcon.Normal, QIcon.Off)
        excelForm.setWindowIcon(icon1)
        self.verticalLayout = QVBoxLayout(excelForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.navbar = QWidget(excelForm)
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
        self.icon.setStyleSheet(u"border-image: url(:/newPrefix/Message To Document 2.png);\n"
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
        self.excel.setStyleSheet(u"border: none;")

        self.navbarLayout.addWidget(self.excel)

        self.word = QPushButton(self.navbar)
        self.word.setObjectName(u"word")
        self.word.setFont(font)
        self.word.setStyleSheet(u"border: none;")

        self.navbarLayout.addWidget(self.word)

        self.pdf = QPushButton(self.navbar)
        self.pdf.setObjectName(u"pdf")
        self.pdf.setFont(font)
        self.pdf.setStyleSheet(u"border: none;")

        self.navbarLayout.addWidget(self.pdf)


        self.horizontalLayout_3.addLayout(self.navbarLayout)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 6)

        self.verticalLayout.addWidget(self.navbar)

        self.body = QWidget(excelForm)
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

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)

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

        self.inputBox_2 = QWidget(self.centralPart)
        self.inputBox_2.setObjectName(u"inputBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.inputBox_2)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.delimiter = QLabel(self.inputBox_2)
        self.delimiter.setObjectName(u"delimiter")
        self.delimiter.setFont(font)
        self.delimiter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.delimiter)

        self.delimiterEdit = QLineEdit(self.inputBox_2)
        self.delimiterEdit.setObjectName(u"delimiterEdit")
        sizePolicy.setHeightForWidth(self.delimiterEdit.sizePolicy().hasHeightForWidth())
        self.delimiterEdit.setSizePolicy(sizePolicy)
        self.delimiterEdit.setFont(font1)
        self.delimiterEdit.setStyleSheet(u"border: 5px solid rgb(244, 192, 79);\n"
"border-radius: 16px;")

        self.verticalLayout_5.addWidget(self.delimiterEdit)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 3)

        self.verticalLayout_4.addWidget(self.inputBox_2)

        self.info = QLabel(self.centralPart)
        self.info.setObjectName(u"info")
        font2 = QFont()
        font2.setFamily(u"Inter")
        font2.setPointSize(10)
        self.info.setFont(font2)
        self.info.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.info)

        self.compile = QPushButton(self.centralPart)
        self.compile.setObjectName(u"compile")
        sizePolicy.setHeightForWidth(self.compile.sizePolicy().hasHeightForWidth())
        self.compile.setSizePolicy(sizePolicy)
        self.compile.setFont(font)
        self.compile.setStyleSheet(u"background-color: rgb(244, 192, 79);\n"
"border-radius: 16px;\n"
"")

        self.verticalLayout_4.addWidget(self.compile)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 3)
        self.verticalLayout_4.setStretch(2, 12)
        self.verticalLayout_4.setStretch(3, 2)

        self.horizontalLayout_2.addWidget(self.centralPart)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.body)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)

        self.retranslateUi(excelForm)
        self.titleEdit.returnPressed.connect(self.compile.animateClick)

        QMetaObject.connectSlotsByName(excelForm)
    # setupUi

    def retranslateUi(self, excelForm):
        excelForm.setWindowTitle(QCoreApplication.translate("excelForm", u"Compilez vers Excel - Message To Doc", None))
        self.icon.setText("")
        self.excel.setText(QCoreApplication.translate("excelForm", u"Compiler vers Excel", None))
        self.word.setText(QCoreApplication.translate("excelForm", u"Compiler vers Word", None))
        self.pdf.setText(QCoreApplication.translate("excelForm", u"Compiler vers PDF", None))
        self.messageLabel.setText(QCoreApplication.translate("excelForm", u"<html><head/><body><p>Message \u00e0 utiliser <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.title.setText(QCoreApplication.translate("excelForm", u"<html><head/><body><p>Titre du document <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.delimiter.setText(QCoreApplication.translate("excelForm", u"<html><head/><body><p><span style=\" color:#000000;\">D\u00e9limiteur de cellules</span><span style=\" color:#ff0000;\"> *</span></p></body></html>", None))
        self.delimiterEdit.setPlaceholderText(QCoreApplication.translate("excelForm", u"Virgule par d\u00e9faut", None))
        self.info.setText(QCoreApplication.translate("excelForm", u" Pour faciliter la transformation de votre message texte en document Excel, assurez-vous d'utiliser un d\u00e9limiteur de cellules coh\u00e9rent dans tout votre message. Indiquez clairement le d\u00e9limiteur que vous avez utilis\u00e9 dans le formulaire, pour que notre application puisse l'identifier facilement et cr\u00e9er un document Excel bien structur\u00e9.", None))
        self.compile.setText(QCoreApplication.translate("excelForm", u"Transformer en xlsx", None))
    # retranslateUi

