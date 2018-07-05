# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(921, 592)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(190, 0, 721, 591))
        self.graphicsView.setObjectName("graphicsView")
        self.buttonOpenFile = QtWidgets.QPushButton(Dialog)
        self.buttonOpenFile.setGeometry(QtCore.QRect(10, 40, 171, 51))
        self.buttonOpenFile.setObjectName("buttonOpenFile")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.solve = QtWidgets.QPushButton(Dialog)
        self.solve.setGeometry(QtCore.QRect(10, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.solve.setFont(font)
        self.solve.setObjectName("solve")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 140, 171, 161))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.buttonOpenFile.setText(_translate("Dialog", "Обзор"))
        self.label.setText(_translate("Dialog", "Подгрузка данных"))
        self.solve.setText(_translate("Dialog", "Визуализация"))

