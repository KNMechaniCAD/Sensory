# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cwtBox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 231, 191))
        self.groupBox.setObjectName("groupBox")
        self.radioCMOR = QtWidgets.QRadioButton(self.groupBox)
        self.radioCMOR.setGeometry(QtCore.QRect(10, 30, 61, 20))
        self.radioCMOR.setChecked(True)
        self.radioCMOR.setObjectName("radioCMOR")
        self.radioMEXH = QtWidgets.QRadioButton(self.groupBox)
        self.radioMEXH.setGeometry(QtCore.QRect(10, 70, 61, 20))
        self.radioMEXH.setObjectName("radioMEXH")
        self.radioMORL = QtWidgets.QRadioButton(self.groupBox)
        self.radioMORL.setGeometry(QtCore.QRect(10, 110, 61, 20))
        self.radioMORL.setObjectName("radioMORL")
        self.radioSHAN = QtWidgets.QRadioButton(self.groupBox)
        self.radioSHAN.setGeometry(QtCore.QRect(10, 150, 61, 20))
        self.radioSHAN.setObjectName("radioSHAN")
        self.radioCGAU1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioCGAU1.setGeometry(QtCore.QRect(90, 30, 95, 20))
        self.radioCGAU1.setObjectName("radioCGAU1")
        self.radioCGAU3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioCGAU3.setGeometry(QtCore.QRect(90, 70, 95, 20))
        self.radioCGAU3.setObjectName("radioCGAU3")
        self.radioGAUS1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioGAUS1.setGeometry(QtCore.QRect(90, 110, 95, 20))
        self.radioGAUS1.setObjectName("radioGAUS1")
        self.radioGAUS3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioGAUS3.setGeometry(QtCore.QRect(90, 150, 95, 20))
        self.radioGAUS3.setObjectName("radioGAUS3")
        self.ScalesMin = QtWidgets.QLineEdit(Dialog)
        self.ScalesMin.setGeometry(QtCore.QRect(270, 70, 113, 22))
        self.ScalesMin.setObjectName("ScalesMin")
        self.ScalesMax = QtWidgets.QLineEdit(Dialog)
        self.ScalesMax.setGeometry(QtCore.QRect(260, 160, 113, 22))
        self.ScalesMax.setObjectName("ScalesMax")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 40, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 140, 71, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.radioCMOR.setText(_translate("Dialog", "cmor"))
        self.radioMEXH.setText(_translate("Dialog", "mexh"))
        self.radioMORL.setText(_translate("Dialog", "morl"))
        self.radioSHAN.setText(_translate("Dialog", "shan"))
        self.radioCGAU1.setText(_translate("Dialog", "cgau1"))
        self.radioCGAU3.setText(_translate("Dialog", "cgau3"))
        self.radioGAUS1.setText(_translate("Dialog", "gaus1"))
        self.radioGAUS3.setText(_translate("Dialog", "gaus3"))
        self.ScalesMin.setText(_translate("Dialog", "1"))
        self.ScalesMax.setText(_translate("Dialog", "10"))
        self.label.setText(_translate("Dialog", "Scales Min"))
        self.label_2.setText(_translate("Dialog", "Scales Max"))


if _name_ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())