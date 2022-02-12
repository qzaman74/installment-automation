# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountUpdateForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BLL.AccountsBL import accountFormBL
from Globals import globalVariables,globalList

class Ui_accountUpdateForm(object):
    _accountId = 0

    ###
    def setAccountUpdateFields(self,result):
        for x in result:
            self._accountId = x[0]
            self.le_cellNo.setText(str(x[6]))
            self.le_address.setText(str(x[8]))

    def onUpdateAccount(self):
        acId = self._accountId
        cellNo = self.le_cellNo.text()
        address = self.le_address.text()
        acStatus = self.cb_status.currentText()
        acType = self.cb_type.currentText()
        accountFormBL.updateAccountForm(acId, cellNo, address, acType, acStatus)



    def accountUpdateSetupUi(self, accountUpdateForm):
        accountUpdateForm.setObjectName("accountUpdateForm")
        accountUpdateForm.resize(320, 190)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        accountUpdateForm.setWindowIcon(QtGui.QIcon(windowIcon))

        accountUpdateForm.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        accountUpdateForm.setAutoFillBackground(True)

        self.updateAccountGB = QtWidgets.QGroupBox(accountUpdateForm)
        self.updateAccountGB.setGeometry(QtCore.QRect(10, 0, 301, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateAccountGB.sizePolicy().hasHeightForWidth())
        self.updateAccountGB.setSizePolicy(sizePolicy)
        self.updateAccountGB.setObjectName("updateAccountGB")
        self.le_cellNo = QtWidgets.QLineEdit(self.updateAccountGB)
        self.le_cellNo.setEnabled(True)
        self.le_cellNo.setGeometry(QtCore.QRect(90, 20, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cellNo.sizePolicy().hasHeightForWidth())
        self.le_cellNo.setSizePolicy(sizePolicy)
        self.le_cellNo.setMaxLength(11)
        self.le_cellNo.setObjectName("le_cellNo")
        self.le_address = QtWidgets.QLineEdit(self.updateAccountGB)
        self.le_address.setEnabled(True)
        self.le_address.setGeometry(QtCore.QRect(90, 50, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_address.sizePolicy().hasHeightForWidth())
        self.le_address.setSizePolicy(sizePolicy)
        self.le_address.setMaxLength(100)
        self.le_address.setObjectName("le_address")
        self.label_4 = QtWidgets.QLabel(self.updateAccountGB)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 81, 28))
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
        self.label_5 = QtWidgets.QLabel(self.updateAccountGB)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 81, 28))
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
        self.cb_type = QtWidgets.QComboBox(self.updateAccountGB)
        self.cb_type.setGeometry(QtCore.QRect(90, 80, 200, 28))
        self.cb_type.addItems(globalList.List._accountTypeList)
        self.cb_type.setObjectName("cb_type")

        self.cb_status = QtWidgets.QComboBox(self.updateAccountGB)
        self.cb_status.setGeometry(QtCore.QRect(90, 110, 200, 28))
        self.cb_status.addItems(globalList.List._accountStatusList)
        self.cb_status.setObjectName("cb_status")

        self.label_8 = QtWidgets.QLabel(self.updateAccountGB)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.updateAccountGB)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 81, 28))
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
        self.buttonBox = QtWidgets.QDialogButtonBox(self.updateAccountGB)
        self.buttonBox.setGeometry(QtCore.QRect(130, 140, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(accountUpdateForm)
        self.buttonBox.accepted.connect(self.onUpdateAccount)
        self.buttonBox.accepted.connect(accountUpdateForm.accept)
        self.buttonBox.rejected.connect(accountUpdateForm.reject)
        QtCore.QMetaObject.connectSlotsByName(accountUpdateForm)

    def retranslateUi(self, accountUpdateForm):
        _translate = QtCore.QCoreApplication.translate
        accountUpdateForm.setWindowTitle(_translate("accountUpdateForm", "Update Account"))
        self.updateAccountGB.setTitle(_translate("accountUpdateForm", "Update Account"))
        self.label_4.setText(_translate("accountUpdateForm", "Mobile No. :"))
        self.label_5.setText(_translate("accountUpdateForm", "Address :"))
        self.label_8.setText(_translate("accountUpdateForm", "Type :"))
        self.label_9.setText(_translate("accountUpdateForm", "Status :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    accountUpdateForm = QtWidgets.QDialog()
    ui = Ui_accountUpdateForm()
    ui.accountUpdateSetupUi(accountUpdateForm)
    accountUpdateForm.show()
    sys.exit(app.exec_())

