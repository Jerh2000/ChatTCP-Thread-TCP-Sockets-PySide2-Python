# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ChatForm(object):
    def setupUi(self, chatForm):
        if not chatForm.objectName():
            chatForm.setObjectName(u"chatForm")
        chatForm.resize(500, 550)
        iconW = QIcon()
        iconW.addFile(u"assets/icons8-email-send-96.png", QSize(), QIcon.Normal, QIcon.Off)
        chatForm.setWindowIcon(iconW)
        chatForm.setMinimumSize(QSize(500, 550));
        chatForm.setMaximumSize(QSize(500, 550));
        self.frame = QFrame(chatForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 500, 51))
        self.frame.setStyleSheet(u"background-color:white")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 241, 31))
        self.label.setStyleSheet(u"color: black;")
        self.logoutButton = QPushButton(self.frame)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(420, 0, 41, 51))
        self.logoutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutButton.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u"assets/icons8-exit-200.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutButton.setIcon(icon)
        self.logoutButton.setIconSize(QSize(32, 32))
        self.logoutButton.setFlat(True)
        self.chatTextEdit = QTextEdit(chatForm)
        self.chatTextEdit.setObjectName(u"chatTextEdit")
        self.chatTextEdit.setGeometry(QRect(0, 50, 500, 421))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Arial")
        self.chatTextEdit.setFont(font)
        self.chatTextEdit.setStyleSheet(u"background-color: #c9d2e3; \n"
        "color: black")
        self.chatTextEdit.setReadOnly(True)
        self.frame_2 = QFrame(chatForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 490, 461, 41))
        self.frame_2.setStyleSheet(u"background-color: white;\n"
        "border-radius: 10px;\n"
        "border: 1px solid #EDEDED;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.messageLineEdit = QLineEdit(self.frame_2)
        self.messageLineEdit.setObjectName(u"messageLineEdit")
        self.messageLineEdit.setGeometry(QRect(10, 5, 331, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.messageLineEdit.setFont(font1)
        self.messageLineEdit.setStyleSheet(u"border: none;")
        self.sendButton = QPushButton(self.frame_2)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(410, 1, 50, 38))
        self.sendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendButton.setStyleSheet(u"border:none;");
        icon1 = QIcon()
        icon1.addFile(u"assets/icons8-email-send-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendButton.setIcon(icon1)
        self.sendButton.setIconSize(QSize(30, 30))
        self.sendButton.setFlat(True)

        self.retranslateUi(chatForm)

        QMetaObject.connectSlotsByName(chatForm)
    # setupUi

    def retranslateUi(self, chatForm):
        chatForm.setWindowTitle(QCoreApplication.translate("chatForm", u"Ventana de chat", None))
        self.label.setText(QCoreApplication.translate("chatForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Ventana de chat</span></p></body></html>", None))
        self.logoutButton.setText("")
        # self.label_2.setText(QCoreApplication.translate("chatForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">LOGOUT</span></p></body></html>", None))
        self.messageLineEdit.setPlaceholderText(QCoreApplication.translate("chatForm", u"Escribe un mensaje...", None))
        self.sendButton.setText("")
    # retranslateUi

