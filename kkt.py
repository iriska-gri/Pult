# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kkt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kkt4period(object):
    def setupUi(self, kkt4period):
        kkt4period.setObjectName("kkt4period")
        kkt4period.resize(609, 126)
        self.kkt_date_start = QtWidgets.QDateEdit(kkt4period)
        self.kkt_date_start.setGeometry(QtCore.QRect(80, 30, 110, 22))
        self.kkt_date_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(1, 0, 0)))
        self.kkt_date_start.setTime(QtCore.QTime(1, 0, 0))
        self.kkt_date_start.setCalendarPopup(True)
        self.kkt_date_start.setObjectName("kkt_date_start")
        self.date_end = QtWidgets.QDateEdit(kkt4period)
        self.date_end.setGeometry(QtCore.QRect(240, 30, 110, 22))
        self.date_end.setCalendarPopup(True)
        self.date_end.setObjectName("date_end")
        self.label = QtWidgets.QLabel(kkt4period)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(kkt4period)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 71, 21))
        self.label_2.setObjectName("label_2")
        self.kktto38 = QtWidgets.QPushButton(kkt4period)
        self.kktto38.setGeometry(QtCore.QRect(110, 80, 81, 23))
        self.kktto38.setObjectName("kktto38")
        self.kkttozip = QtWidgets.QPushButton(kkt4period)
        self.kkttozip.setGeometry(QtCore.QRect(240, 80, 111, 23))
        self.kkttozip.setObjectName("kkttozip")

        self.retranslateUi(kkt4period)
        QtCore.QMetaObject.connectSlotsByName(kkt4period)

    def retranslateUi(self, kkt4period):
        _translate = QtCore.QCoreApplication.translate
        kkt4period.setWindowTitle(_translate("kkt4period", "ККТ"))
        self.label.setText(_translate("kkt4period", "Начало"))
        self.label_2.setText(_translate("kkt4period", "Конец"))
        self.kktto38.setText(_translate("kkt4period", "На 38"))
        self.kkttozip.setText(_translate("kkt4period", "Качай Оригиналы"))
