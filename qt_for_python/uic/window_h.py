# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_h.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(435, 449)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.commandLinkButton = QCommandLinkButton(Dialog)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.gridLayout.addWidget(self.commandLinkButton, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"help", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Dialog", u"Github", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">ocr_net</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">---------------</span><span style=\" font-size:12pt; font-weight:600;\">help</span><span style=\" font-weight:600;\">--------------"
                        "-</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">1\u3001\u70b9\u51fb'\u5f00\u59cb\u8bc6\u522b'\u6309\u94ae\uff0c\u622a\u5b8c\u56fe\u540e\u81ea\u52a8\u8bc6\u522b\u6587\u672c\u3002</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">2\u3001\u82e5\u8bc6\u522b\u622a\u56fe\u754c\u9762\u6309ESC\u9000\u51fa\u65e0\u6548\uff0c\u968f\u4fbf\u62c9\u4e2a\u7ea2\u6846\uff0c\u81ea\u52a8\u8fdb\u5165\u4e3b\u754c\u9762\u518d\u9000\u51fa\u5373\u53ef\u3002</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">3\u3001\u672c\u7a0b\u5e8f\u9700\u8054\u7f51\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; marg"
                        "in-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">4\u3001\u53ef\u4ee5\u6839\u636e\u9700\u8981\u9009\u62e9\u8bc6\u522b\u6a21\u5f0f\u3002\u7cbe\u5ea6\u8d8a\u9ad8\uff0c\u8bc6\u522b\u65f6\u95f4\u8d8a\u957f\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">5\u3001\u8868\u683c\u8bc6\u522b\u4f1a\u4fdd\u5b58\u4e00\u4e2aexcel\u6587\u4ef6\u3002\u4e5f\u53ef\u4ee5\u4e0b\u8f7d\u94fe\u63a5\u4e0a\u7684excel\u8868\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">6\u3001\u7531\u4e8e\u7a0b\u5e8f\u8c03\u7528\u767e\u5ea6API\uff0c\u6bcf\u6708\u4f7f\u7528\u6b21\u6570\u6709\u9650\u5236\uff0c\u4e00\u822c\u4e0d\u4f1a\u8d85\u4e0a\u9650\uff0c\u82e5\u51fa\u73b0\uff0c\u53ef\u4ee5\uff1a</span></p>\n"
"<p style=\" margi"
                        "n-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">1\uff09\u81ea\u5df1\u6ce8\u518c\u767e\u5ea6\u667a\u80fd\u4e91\uff0c\u9009\u53d6\u5bf9\u5e94\u63a5\u53e3\uff0c\u7533\u8bf7KEY\u6216ID\u3002\uff08\u5177\u4f53\u7533\u8bf7\u65b9\u6cd5\u53ef\u767e\u5ea6\uff09</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">2\uff09\u5728\u2018\u8bbe\u7f6e-</span>Advanced settings\u2019\u83dc\u5355<span style=\" font-family:'\u5b8b\u4f53';\">\u4e2d\u586b\u5199\u81ea\u5df1\u7684\u767e\u5ea6API\u4fe1\u606f\u3002</span></p></body></html>", None))
    # retranslateUi

