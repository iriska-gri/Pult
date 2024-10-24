# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RestoreCSV(object):
    def setupUi(self, RestoreCSV):
        RestoreCSV.setObjectName("RestoreCSV")
        RestoreCSV.resize(503, 121)
        RestoreCSV.setMinimumSize(QtCore.QSize(503, 121))
        RestoreCSV.setMaximumSize(QtCore.QSize(503, 121))
        self.lookup = QtWidgets.QPushButton(RestoreCSV)
        self.lookup.setGeometry(QtCore.QRect(410, 50, 75, 23))
        self.lookup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lookup.setObjectName("lookup")
        self.label = QtWidgets.QLabel(RestoreCSV)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setObjectName("label")
        self.basename = QtWidgets.QLineEdit(RestoreCSV)
        self.basename.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.basename.setObjectName("basename")
        self.label_2 = QtWidgets.QLabel(RestoreCSV)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 101, 21))
        self.label_2.setObjectName("label_2")
        self.tablename = QtWidgets.QLineEdit(RestoreCSV)
        self.tablename.setGeometry(QtCore.QRect(260, 10, 151, 20))
        self.tablename.setObjectName("tablename")
        self.filelabel = QtWidgets.QLabel(RestoreCSV)
        self.filelabel.setGeometry(QtCore.QRect(20, 50, 47, 16))
        self.filelabel.setWordWrap(False)
        self.filelabel.setObjectName("filelabel")
        self.filename = QtWidgets.QLabel(RestoreCSV)
        self.filename.setGeometry(QtCore.QRect(90, 50, 291, 16))
        self.filename.setObjectName("filename")
        self.Upload = QtWidgets.QPushButton(RestoreCSV)
        self.Upload.setGeometry(QtCore.QRect(140, 80, 231, 31))
        self.Upload.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.Upload.setObjectName("Upload")

        self.retranslateUi(RestoreCSV)
        QtCore.QMetaObject.connectSlotsByName(RestoreCSV)

    def retranslateUi(self, RestoreCSV):
        _translate = QtCore.QCoreApplication.translate
        RestoreCSV.setWindowTitle(_translate("RestoreCSV", "Залить в базу на 38 сервер"))
        self.lookup.setText(_translate("RestoreCSV", "Обзор..."))
        self.label.setText(_translate("RestoreCSV", "База Данных"))
        self.label_2.setText(_translate("RestoreCSV", "Таблица"))
        self.filelabel.setText(_translate("RestoreCSV", "Файл"))
        self.filename.setText(_translate("RestoreCSV", "Файл не выбран"))
        self.Upload.setText(_translate("RestoreCSV", "Залить файл"))
