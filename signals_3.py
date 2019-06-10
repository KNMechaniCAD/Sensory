# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TimeButton = QtWidgets.QPushButton(self.centralwidget)
        self.TimeButton.setGeometry(QtCore.QRect(610, 30, 131, 31))
        self.TimeButton.setObjectName("TimeButton")
        self.FreqButton = QtWidgets.QPushButton(self.centralwidget)
        self.FreqButton.setGeometry(QtCore.QRect(610, 90, 131, 31))
        self.FreqButton.setObjectName("FreqButton")
        self.Display = MplWidget(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(10, 10, 591, 521))
        self.Display.setObjectName("Display")
        self.CutAt0 = QtWidgets.QCheckBox(self.centralwidget)
        self.CutAt0.setGeometry(QtCore.QRect(760, 100, 16, 16))
        self.CutAt0.setText("")
        self.CutAt0.setChecked(False)
        self.CutAt0.setTristate(False)
        self.CutAt0.setObjectName("CutAt0")
        self.STFTButton = QtWidgets.QPushButton(self.centralwidget)
        self.STFTButton.setGeometry(QtCore.QRect(610, 150, 131, 31))
        self.STFTButton.setObjectName("STFTButton")
        self.CWTButton = QtWidgets.QPushButton(self.centralwidget)
        self.CWTButton.setGeometry(QtCore.QRect(610, 210, 131, 31))
        self.CWTButton.setObjectName("CWTButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.newFunc = QtWidgets.QAction(MainWindow)
        self.newFunc.setObjectName("newFunc")
        self.actionFreq = QtWidgets.QAction(MainWindow)
        self.actionFreq.setObjectName("actionFreq")
        self.menuMenu.addAction(self.newFunc)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TimeButton.setText(_translate("MainWindow", "Time domain"))
        self.FreqButton.setText(_translate("MainWindow", "Frequency domain"))
        self.STFTButton.setText(_translate("MainWindow", "STFT"))
        self.CWTButton.setText(_translate("MainWindow", "CWT"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.newFunc.setText(_translate("MainWindow", "New"))
        self.actionFreq.setText(_translate("MainWindow", "Freq"))

from mplwidget import MplWidget

if _name_ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())