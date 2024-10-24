# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_date_for_107(object):
    def setupUi(self, date_for_107):
        date_for_107.setObjectName("date_for_107")
        date_for_107.setWindowModality(QtCore.Qt.ApplicationModal)
        date_for_107.resize(400, 91)
        date_for_107.setMinimumSize(QtCore.QSize(400, 91))
        date_for_107.setMaximumSize(QtCore.QSize(400, 91))
        date_for_107.setFocusPolicy(QtCore.Qt.StrongFocus)
        date_for_107.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(date_for_107)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.dateTimeEdit_107 = QtWidgets.QDateTimeEdit(date_for_107)
        self.dateTimeEdit_107.setGeometry(QtCore.QRect(70, 30, 194, 22))
        self.dateTimeEdit_107.setProperty("showGroupSeparator", False)
        self.dateTimeEdit_107.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 5), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_107.setCalendarPopup(True)
        self.dateTimeEdit_107.setObjectName("dateTimeEdit_107")

        self.retranslateUi(date_for_107)
        self.buttonBox.accepted.connect(date_for_107.accept)
        self.buttonBox.rejected.connect(date_for_107.reject)
        QtCore.QMetaObject.connectSlotsByName(date_for_107)

    def retranslateUi(self, date_for_107):
        _translate = QtCore.QCoreApplication.translate
        date_for_107.setWindowTitle(_translate("date_for_107", "Задайте время файлу"))
        self.dateTimeEdit_107.setDisplayFormat(_translate("date_for_107", "dd.MM.yyyy H:mm"))
