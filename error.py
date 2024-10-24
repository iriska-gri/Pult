# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_error(object):
    def setupUi(self, error):
        error.setObjectName("error")
        error.resize(500, 158)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(error.sizePolicy().hasHeightForWidth())
        error.setSizePolicy(sizePolicy)
        error.setMaximumSize(QtCore.QSize(500, 158))
        error.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.okButton = QtWidgets.QPushButton(error)
        self.okButton.setGeometry(QtCore.QRect(200, 120, 111, 31))
        self.okButton.setObjectName("okButton")
        self.text = QtWidgets.QLabel(error)
        self.text.setGeometry(QtCore.QRect(10, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.textBrowser = QtWidgets.QTextBrowser(error)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 481, 91))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(error)
        QtCore.QMetaObject.connectSlotsByName(error)

    def retranslateUi(self, error):
        _translate = QtCore.QCoreApplication.translate
        error.setWindowTitle(_translate("error", "Центр! У нас проблемы!"))
        self.okButton.setText(_translate("error", "Понятно"))
        self.text.setText(_translate("error", "Что-то вызвало ошибку:"))
