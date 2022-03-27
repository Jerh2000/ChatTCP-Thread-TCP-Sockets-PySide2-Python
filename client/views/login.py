# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from pickle import FALSE
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LoginForm(object):
    def setupUi(self, loginForm):
        if not loginForm.objectName():
            loginForm.setObjectName(u"loginForm")
        loginForm.resize(316, 242)
        loginForm.setMinimumSize(QSize(316, 242));
        loginForm.setMaximumSize(QSize(316, 242));
        iconW = QIcon()
        iconW.addFile(u"assets/icons8-email-send-96.png", QSize(), QIcon.Normal, QIcon.Off)
        loginForm.setWindowIcon(iconW)
        self.frame = QFrame(loginForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 316, 70))
        self.frame.setStyleSheet(u"background-color: #0A5EF2")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 316, 80))
        self.label.setStyleSheet(u"color: white;\n""font: 11pt \"Arial\";");
        self.label_2 = QLabel(loginForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 110, 110, 16))
        self.label_2.setStyleSheet(u"font: 9pt \"Arial\";")
        self.usernameLineEdit = QLineEdit(loginForm)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(60, 130, 191, 30))
        self.joinButton = QPushButton(loginForm)
        self.joinButton.setObjectName(u"joinButton")
        self.joinButton.setGeometry(QRect(100, 180, 115, 26))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.joinButton.setFont(font)
        self.joinButton.setStyleSheet(u"color: white; \n"
        "font: 10pt \"Arial\";\n"
        "background-color: #198754;\n"
        "border-radius: 5px;");

        self.retranslateUi(loginForm)

        QMetaObject.connectSlotsByName(loginForm)
    # setupUi

    def retranslateUi(self, loginForm):
        loginForm.setWindowTitle(QCoreApplication.translate("loginForm", u"Login Chat TCP", None))
        self.label.setText(QCoreApplication.translate("loginForm", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Inicio de Sesión</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("loginForm", u"Nombre de Usuario", None))
        self.joinButton.setText(QCoreApplication.translate("loginForm", u"INICIAR SESIÓN", None))
    # retranslateUi

