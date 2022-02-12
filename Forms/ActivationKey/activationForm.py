# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activationForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BLL.ActivationKeyBL import activationBL
from Globals import globalVariables
from Services.CloseServices import formClose

class Ui_activationDialog(object):
    def init(self):
        self.le_key.setFocus()

    def onChangeKey(self,text):
        if(len(text) == 4 ):
            self.le_key_1.setFocus()

    def onChangeKey1(self,text):
        if(len(text) == 5 ):
            self.le_key_2.setFocus()

    def onSubmit(self):
        key = self.le_key.text()
        key1 = self.le_key_1.text()
        key2 = self.le_key_2.text()

        activationBL.validateActivationKey(key, key1, key2)



    def activationSetupUi(self, activationDialog):
        activationDialog.setObjectName("activationDialog")
        activationDialog.resize(356, 110)
        formClose.Close._closeActivationForm = activationDialog.close

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        activationDialog.setWindowIcon(QtGui.QIcon(windowIcon))

        activationDialog.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        activationDialog.setAutoFillBackground(True)

        self.groupBox = QtWidgets.QGroupBox(activationDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 91))
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.le_key = QtWidgets.QLineEdit(self.groupBox)
        self.le_key.setEnabled(True)
        self.le_key.setGeometry(QtCore.QRect(120, 20, 45, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_key.sizePolicy().hasHeightForWidth())
        self.le_key.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_key.setFont(font)
        self.le_key.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_key.setMaxLength(4)
        self.le_key.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.le_key.setAlignment(QtCore.Qt.AlignCenter)
        self.le_key.setObjectName("le_key")
        self.le_key.textChanged.connect(self.onChangeKey)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(160, 50, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.le_key_1 = QtWidgets.QLineEdit(self.groupBox)
        self.le_key_1.setEnabled(True)
        self.le_key_1.setGeometry(QtCore.QRect(190, 20, 50, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_key_1.sizePolicy().hasHeightForWidth())
        self.le_key_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_key_1.setFont(font)
        self.le_key_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_key_1.setMaxLength(5)
        self.le_key_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.le_key_1.setAlignment(QtCore.Qt.AlignCenter)
        self.le_key_1.setObjectName("le_key_1")
        self.le_key_1.textChanged.connect(self.onChangeKey1)

        self.le_key_2 = QtWidgets.QLineEdit(self.groupBox)
        self.le_key_2.setEnabled(True)
        self.le_key_2.setGeometry(QtCore.QRect(260, 20, 45, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_key_2.sizePolicy().hasHeightForWidth())
        self.le_key_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_key_2.setFont(font)
        self.le_key_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_key_2.setMaxLength(4)
        self.le_key_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.le_key_2.setAlignment(QtCore.Qt.AlignCenter)
        self.le_key_2.setObjectName("le_key_2")
        self.le_key_2.returnPressed.connect(self.onSubmit)


        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(170, 20, 16, 28))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(240, 20, 16, 28))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(activationDialog)
        self.buttonBox.accepted.connect(self.onSubmit)
        self.buttonBox.rejected.connect(activationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(activationDialog)

    def retranslateUi(self, activationDialog):
        _translate = QtCore.QCoreApplication.translate
        activationDialog.setWindowTitle(_translate("activationDialog", "Activation Window"))
        self.groupBox.setTitle(_translate("activationDialog", "Enter Activation Key"))
        self.label_6.setText(_translate("activationDialog", "Activation Key"))
        self.label_7.setText(_translate("activationDialog", "-"))
        self.label_8.setText(_translate("activationDialog", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    activationDialog = QtWidgets.QDialog()
    ui = Ui_activationDialog()
    ui.activationSetupUi(activationDialog)
    activationDialog.show()
    sys.exit(app.exec_())

