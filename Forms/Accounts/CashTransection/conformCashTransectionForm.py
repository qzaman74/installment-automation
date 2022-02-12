# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conformCashTransectionForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from BLL.AccountsBL import cashTransectionBL
from Globals import globalVariables
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_conformCashTransectionWindow(object):
    _accountId = 0
    _balance = 0
    def setConfirmField(self, acID, amountType, remarks, amount, name, mob, balance):
        self._accountId = acID
        self.le_name.setText(name)
        self.le_cellNo.setText(mob)
        self.le_type.setText(amountType)
        self.le_remarks.setText(remarks)
        self.le_amount.setText(amount)
        self._balance = balance

    def confirmTransection(self):
        acID = self._accountId
        _type = self.le_type.text()
        amount = self.le_amount.text()
        balance = self._balance
        remarks = self.le_remarks.text()

        cashTransectionBL.confirmCashTransection(acID, _type, remarks, amount, balance)


    def conformCashTransectionSetupUi(self, conformCashTransectionWindow):
        conformCashTransectionWindow.setObjectName("conformCashTransectionWindow")
        conformCashTransectionWindow.resize(310, 239)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        conformCashTransectionWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        conformCashTransectionWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        conformCashTransectionWindow.setAutoFillBackground(True)

        self.conformTransectionGB = QtWidgets.QGroupBox(conformCashTransectionWindow)
        self.conformTransectionGB.setGeometry(QtCore.QRect(5, 5, 301, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conformTransectionGB.sizePolicy().hasHeightForWidth())
        self.conformTransectionGB.setSizePolicy(sizePolicy)
        self.conformTransectionGB.setObjectName("conformTransectionGB")
        self.le_name = QtWidgets.QLineEdit(self.conformTransectionGB)
        self.le_name.setEnabled(False)
        self.le_name.setGeometry(QtCore.QRect(90, 20, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        self.le_name.setObjectName("le_name")
        self.le_cellNo = QtWidgets.QLineEdit(self.conformTransectionGB)
        self.le_cellNo.setEnabled(False)
        self.le_cellNo.setGeometry(QtCore.QRect(90, 50, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cellNo.sizePolicy().hasHeightForWidth())
        self.le_cellNo.setSizePolicy(sizePolicy)
        self.le_cellNo.setObjectName("le_cellNo")
        self.le_amount = QtWidgets.QLineEdit(self.conformTransectionGB)
        self.le_amount.setEnabled(False)
        self.le_amount.setGeometry(QtCore.QRect(90, 80, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_amount.sizePolicy().hasHeightForWidth())
        self.le_amount.setSizePolicy(sizePolicy)
        self.le_amount.setObjectName("le_amount")
        self.label = QtWidgets.QLabel(self.conformTransectionGB)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.conformTransectionGB)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 61, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.conformTransectionGB)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 61, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.conformTransectionGB)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.le_type = QtWidgets.QLineEdit(self.conformTransectionGB)
        self.le_type.setEnabled(False)
        self.le_type.setGeometry(QtCore.QRect(90, 140, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_type.sizePolicy().hasHeightForWidth())
        self.le_type.setSizePolicy(sizePolicy)
        self.le_type.setObjectName("le_type")
        self.le_remarks = QtWidgets.QLineEdit(self.conformTransectionGB)
        self.le_remarks.setEnabled(False)
        self.le_remarks.setGeometry(QtCore.QRect(90, 110, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_remarks.sizePolicy().hasHeightForWidth())
        self.le_remarks.setSizePolicy(sizePolicy)
        self.le_remarks.setObjectName("le_remarks")
        self.label_9 = QtWidgets.QLabel(self.conformTransectionGB)
        self.label_9.setGeometry(QtCore.QRect(10, 140, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.conformTransectionGB)
        self.buttonBox.setGeometry(QtCore.QRect(130, 190, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(conformCashTransectionWindow)
        self.buttonBox.accepted.connect(self.confirmTransection)
        self.buttonBox.accepted.connect(conformCashTransectionWindow.accept)

        self.buttonBox.rejected.connect(conformCashTransectionWindow.reject)

        QtCore.QMetaObject.connectSlotsByName(conformCashTransectionWindow)

    def retranslateUi(self, conformCashTransectionWindow):
        _translate = QtCore.QCoreApplication.translate
        conformCashTransectionWindow.setWindowTitle(_translate("conformCashTransectionWindow", "Conform Cash Transection Window"))
        self.conformTransectionGB.setTitle(_translate("conformCashTransectionWindow", "Conform Transection"))
        self.label.setText(_translate("conformCashTransectionWindow", "Name"))
        self.label_4.setText(_translate("conformCashTransectionWindow", "Cell No"))
        self.label_5.setText(_translate("conformCashTransectionWindow", "Amount"))
        self.label_7.setText(_translate("conformCashTransectionWindow", "Remarks"))
        self.label_9.setText(_translate("conformCashTransectionWindow", "Transection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    conformCashTransectionWindow = QtWidgets.QDialog()
    ui = Ui_conformCashTransectionWindow()
    ui.conformCashTransectionSetupUi(conformCashTransectionWindow)
    conformCashTransectionWindow.show()
    sys.exit(app.exec_())

