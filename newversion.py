# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newversion.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newversiondialog(object):
    def setupUi(self, newversiondialog):
        newversiondialog.setObjectName("newversiondialog")
        newversiondialog.setWindowModality(QtCore.Qt.ApplicationModal)
        newversiondialog.resize(900, 533)
        newversiondialog.setMinimumSize(QtCore.QSize(900, 533))
        newversiondialog.setMaximumSize(QtCore.QSize(900, 16777215))
        newversiondialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        newversiondialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.letmedown = QtWidgets.QPushButton(newversiondialog)
        self.letmedown.setGeometry(QtCore.QRect(700, 462, 181, 51))
        self.letmedown.setMaximumSize(QtCore.QSize(900, 533))
        self.letmedown.setObjectName("letmedown")
        self.label = QtWidgets.QLabel(newversiondialog)
        self.label.setGeometry(QtCore.QRect(30, 465, 631, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(newversiondialog)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 241, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Y:/WorkDocs/Discharge/Pultinfo/images/MarioNovation.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.novation = QtWidgets.QTextBrowser(newversiondialog)
        self.novation.setGeometry(QtCore.QRect(240, 10, 631, 441))
        self.novation.setObjectName("novation")

        self.retranslateUi(newversiondialog)
        QtCore.QMetaObject.connectSlotsByName(newversiondialog)

    def retranslateUi(self, newversiondialog):
        _translate = QtCore.QCoreApplication.translate
        newversiondialog.setWindowTitle(_translate("newversiondialog", "Пора обновиться"))
        self.letmedown.setText(_translate("newversiondialog", "Обновить ПуЗо"))
        self.label.setText(_translate("newversiondialog", "После нажатия на кнопку справа, начнется копирование обновленной версии приложения"))
