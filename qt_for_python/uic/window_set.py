# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_set.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(486, 386)
        self.verticalLayout = QVBoxLayout(dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_app_id = QLineEdit(dialog)
        self.lineEdit_app_id.setObjectName(u"lineEdit_app_id")
        self.lineEdit_app_id.setMaximumSize(QSize(320, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_app_id)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.label_2 = QLabel(dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_api_key = QLineEdit(dialog)
        self.lineEdit_api_key.setObjectName(u"lineEdit_api_key")
        self.lineEdit_api_key.setMinimumSize(QSize(0, 0))
        self.lineEdit_api_key.setMaximumSize(QSize(320, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_api_key)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.label_3 = QLabel(dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_secret_key = QLineEdit(dialog)
        self.lineEdit_secret_key.setObjectName(u"lineEdit_secret_key")
        self.lineEdit_secret_key.setMaximumSize(QSize(320, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_secret_key)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 20, -1)
        self.commandLinkButton = QCommandLinkButton(dialog)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.horizontalLayout_4.addWidget(self.commandLinkButton)

        self.pushButton = QPushButton(dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u9ad8\u7ea7\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("dialog", u"APP_ID:", None))
        self.label_2.setText(QCoreApplication.translate("dialog", u"API_KEY:", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"SECRET_KEY:", None))
        self.commandLinkButton.setText(QCoreApplication.translate("dialog", u"\u8bbf\u95ee\u767e\u5ea6\u667a\u80fd\u4e91", None))
        self.pushButton.setText(QCoreApplication.translate("dialog", u"\u5e94\u7528\u8bbe\u7f6e", None))
    # retranslateUi

