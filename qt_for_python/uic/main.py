# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(542, 584)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.actionAdvanced_settings = QAction(MainWindow)
        self.actionAdvanced_settings.setObjectName(u"actionAdvanced_settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(219, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 542, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.actionhelp)
        self.menu_2.addAction(self.actionAdvanced_settings)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ocr_net", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"version", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.actionAdvanced_settings.setText(QCoreApplication.translate("MainWindow", u"Advanced settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u6a21\u5f0f\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u901a\u7528\u6587\u5b57\u8bc6\u522b\uff08\u6807\u51c6\u7248\uff09", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u901a\u7528\u6587\u5b57\u8bc6\u522b\uff08\u9ad8\u7cbe\u5ea6\u7248\uff09", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u56fe\u7247\u6587\u5b57\u8bc6\u522b", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u8868\u683c\u6587\u5b57\u8bc6\u522b\uff08\u5f02\u6b65\u63a5\u53e3\uff09", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u624b\u5199\u6587\u5b57\u8bc6\u522b", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58excel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

