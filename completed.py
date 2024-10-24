# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'completed.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_finished(object):
    def setupUi(self, finished):
        finished.setObjectName("finished")
        finished.resize(685, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(finished.sizePolicy().hasHeightForWidth())
        finished.setSizePolicy(sizePolicy)
        finished.setMinimumSize(QtCore.QSize(685, 300))
        finished.setMaximumSize(QtCore.QSize(685, 300))
        self.pushButton = QtWidgets.QPushButton(finished)
        self.pushButton.setGeometry(QtCore.QRect(280, 260, 141, 23))
        self.pushButton.setObjectName("pushButton")
        self.messagefinish = QtWidgets.QLabel(finished)
        self.messagefinish.setGeometry(QtCore.QRect(70, 50, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.messagefinish.setFont(font)
        self.messagefinish.setText("")
        self.messagefinish.setObjectName("messagefinish")
        self.mario = QtWidgets.QLabel(finished)
        self.mario.setGeometry(QtCore.QRect(60, 90, 51, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(17)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mario.sizePolicy().hasHeightForWidth())
        self.mario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mario.setFont(font)
        self.mario.setText("")
        self.mario.setTextFormat(QtCore.Qt.RichText)
        self.mario.setPixmap(QtGui.QPixmap("images/mariooknobg.png"))
        self.mario.setScaledContents(True)
        self.mario.setIndent(-3)
        self.mario.setObjectName("mario")
        self.line = QtWidgets.QFrame(finished)
        self.line.setGeometry(QtCore.QRect(0, 150, 691, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.block = QtWidgets.QLabel(finished)
        self.block.setGeometry(QtCore.QRect(0, 50, 171, 31))
        self.block.setText("")
        self.block.setPixmap(QtGui.QPixmap("images/block.png"))
        self.block.setScaledContents(True)
        self.block.setObjectName("block")
        self.filenamessag = QtWidgets.QLabel(finished)
        self.filenamessag.setGeometry(QtCore.QRect(50, 159, 541, 31))
        self.filenamessag.setObjectName("filenamessag")
        self.label = QtWidgets.QLabel(finished)
        self.label.setGeometry(QtCore.QRect(50, 190, 121, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(finished)
        self.label_2.setGeometry(QtCore.QRect(50, 220, 121, 20))
        self.label_2.setObjectName("label_2")
        self.old_time = QtWidgets.QLabel(finished)
        self.old_time.setGeometry(QtCore.QRect(190, 190, 101, 21))
        self.old_time.setObjectName("old_time")
        self.new_time = QtWidgets.QLabel(finished)
        self.new_time.setGeometry(QtCore.QRect(190, 220, 101, 21))
        self.new_time.setObjectName("new_time")

        self.retranslateUi(finished)
        QtCore.QMetaObject.connectSlotsByName(finished)

    def retranslateUi(self, finished):
        _translate = QtCore.QCoreApplication.translate
        finished.setWindowTitle(_translate("finished", "Операция завершена"))
        self.pushButton.setText(_translate("finished", "OK"))
        self.filenamessag.setText(_translate("finished", "Файл не использовался"))
        self.label.setText(_translate("finished", "Прошлое выполнение:"))
        self.label_2.setText(_translate("finished", "В этот раз:"))
        self.old_time.setText(_translate("finished", "Нет данных"))
        self.new_time.setText(_translate("finished", "Нет данных"))
