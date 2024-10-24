# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'handprop.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 214)
        Dialog.setMinimumSize(QtCore.QSize(546, 214))
        Dialog.setMaximumSize(QtCore.QSize(546, 214))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 170, 511, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.excel2010 = QtWidgets.QPushButton(Dialog)
        self.excel2010.setGeometry(QtCore.QRect(40, 60, 81, 23))
        self.excel2010.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excel2010.setAccessibleDescription("")
        self.excel2010.setAutoFillBackground(False)
        self.excel2010.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0   rgba(0, 170, 0,255), stop:0.05 rgba(0, 170,03, 255), stop:0.935 rgba(239, 236, 55, 255));")
        icon = QtGui.QIcon.fromTheme("Excel")
        self.excel2010.setIcon(icon)
        self.excel2010.setObjectName("excel2010")
        self.excel2013 = QtWidgets.QPushButton(Dialog)
        self.excel2013.setGeometry(QtCore.QRect(40, 100, 81, 23))
        self.excel2013.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excel2013.setAccessibleDescription("")
        self.excel2013.setAutoFillBackground(False)
        self.excel2013.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0   rgba(0, 170, 0,255), stop:0.05 rgba(0, 170,03, 255), stop:0.935 rgba(239, 236, 55, 255));")
        icon = QtGui.QIcon.fromTheme("Excel")
        self.excel2013.setIcon(icon)
        self.excel2013.setObjectName("excel2013")
        self.excel2010edit = QtWidgets.QLineEdit(Dialog)
        self.excel2010edit.setGeometry(QtCore.QRect(140, 60, 371, 20))
        self.excel2010edit.setObjectName("excel2010edit")
        self.excel2013edit = QtWidgets.QLineEdit(Dialog)
        self.excel2013edit.setGeometry(QtCore.QRect(140, 100, 371, 20))
        self.excel2013edit.setObjectName("excel2013edit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lotusNotes = QtWidgets.QLineEdit(Dialog)
        self.lotusNotes.setGeometry(QtCore.QRect(190, 140, 221, 20))
        self.lotusNotes.setObjectName("lotusNotes")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 140, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(420, 140, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ручная настройка путей"))
        self.label.setText(_translate("Dialog", "Ручная настройка путей программ:"))
        self.excel2010.setText(_translate("Dialog", "Эксель 2010"))
        self.excel2013.setText(_translate("Dialog", "Эксель 2013"))
        self.label_2.setText(_translate("Dialog", "LotusNotes"))
        self.lotusNotes.setToolTip(_translate("Dialog", "<html><head/><body><p>Заходим в Lotus -&gt;ПКМ на папке с почтой -&gt;Приложения -&gt; Свойства. В открывшемся окошке из поля &quot;имя файла&quot; переписать имя файла без .nsf</p><p>то есть по типу: <span style=\" font-weight:600;\">9966ФАМИЛИЯИО</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "mail\\"))
        self.label_4.setText(_translate("Dialog", ".nsf"))
