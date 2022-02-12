# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paymentConfirmForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from BLL.SaleBL import paymentSaleBL
from Globals import globalVariables
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_confirmSaleDialog(object):
    _accountId = 0
    _billType = ''
    _remarks = ''
    def setConfirmSalePaymentFields(self,date,billId,billType,accountId,name, mobile,address,soldItem,amount,balance,remarks):
        self.lbl_date.setText(date)
        self.lbl_billId.setText(str(billId))
        self.lbl_name.setText(name)
        self.lbl_cellNo.setText(mobile)
        self.lbl_address.setText(address)
        self.lbl_item.setText(soldItem)
        self.lbl_amount.setText(amount)
        self.lbl_balance.setText(balance)
        self._accountId = accountId
        self._billType =billType
        self._remarks = remarks

    def onConfirmPaymentSale(self):
        accountId = self._accountId
        billId = self.lbl_billId.text()
        billType = self._billType
        date = self.lbl_date.text()
        amount = self.lbl_amount.text()
        balance = self.lbl_balance.text()
        remarks = self._remarks

        paymentSaleBL.confirmPaymentSale(accountId,billId,billType,date,amount,balance,remarks)


    def confirmSaleSetupUi(self, confirmSaleDialog):
        confirmSaleDialog.setObjectName("confirmSaleDialog")
        confirmSaleDialog.resize(240, 355)
        confirmSaleDialog.setMaximumSize(240, 355)
        confirmSaleDialog.setMinimumSize(240, 355)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        confirmSaleDialog.setWindowIcon(QtGui.QIcon(windowIcon))

        confirmSaleDialog.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        confirmSaleDialog.setAutoFillBackground(True)

        self.confirmSaleGB = QtWidgets.QGroupBox(confirmSaleDialog)
        self.confirmSaleGB.setGeometry(QtCore.QRect(10, 0, 221, 351))
        self.confirmSaleGB.setObjectName("confirmSaleGB")
        self.paymentGB = QtWidgets.QGroupBox(self.confirmSaleGB)
        self.paymentGB.setGeometry(QtCore.QRect(10, 20, 200, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paymentGB.sizePolicy().hasHeightForWidth())
        self.paymentGB.setSizePolicy(sizePolicy)
        self.paymentGB.setTitle("")
        self.paymentGB.setObjectName("paymentGB")
        self.lbl_name = QtWidgets.QLabel(self.paymentGB)
        self.lbl_name.setGeometry(QtCore.QRect(80, 120, 120, 16))
        self.lbl_name.setText("")
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_cellNo = QtWidgets.QLabel(self.paymentGB)
        self.lbl_cellNo.setGeometry(QtCore.QRect(80, 140, 120, 16))
        self.lbl_cellNo.setText("")
        self.lbl_cellNo.setObjectName("lbl_cellNo")
        self.lbl_address = QtWidgets.QLabel(self.paymentGB)
        self.lbl_address.setGeometry(QtCore.QRect(80, 160, 120, 16))
        self.lbl_address.setText("")
        self.lbl_address.setObjectName("lbl_address")
        self.lbl_item = QtWidgets.QLabel(self.paymentGB)
        self.lbl_item.setGeometry(QtCore.QRect(80, 180, 120, 16))
        self.lbl_item.setText("")
        self.lbl_item.setObjectName("lbl_item")
        self.lbl_billId = QtWidgets.QLabel(self.paymentGB)
        self.lbl_billId.setGeometry(QtCore.QRect(80, 100, 120, 16))
        self.lbl_billId.setText("")
        self.lbl_billId.setObjectName("lbl_billId")
        self.lbl_amount = QtWidgets.QLabel(self.paymentGB)
        self.lbl_amount.setGeometry(QtCore.QRect(80, 200, 120, 16))
        self.lbl_amount.setText("")
        self.lbl_amount.setObjectName("lbl_amount")
        self.lbl_balance = QtWidgets.QLabel(self.paymentGB)
        self.lbl_balance.setGeometry(QtCore.QRect(80, 220, 120, 16))
        self.lbl_balance.setText("")
        self.lbl_balance.setObjectName("lbl_balance")
        self.lbl_date = QtWidgets.QLabel(self.paymentGB)
        self.lbl_date.setGeometry(QtCore.QRect(80, 80, 120, 16))
        self.lbl_date.setText("")
        self.lbl_date.setObjectName("lbl_date")
        self.lbl_header = QtWidgets.QLabel(self.paymentGB)
        self.lbl_header.setGeometry(QtCore.QRect(0, 0, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_header.setFont(font)
        self.lbl_header.setText("")
        self.lbl_header.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header.setObjectName("lbl_header")
        self.lbl_headerAddress = QtWidgets.QLabel(self.paymentGB)
        self.lbl_headerAddress.setGeometry(QtCore.QRect(0, 20, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_headerAddress.setFont(font)
        self.lbl_headerAddress.setText("")
        self.lbl_headerAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_headerAddress.setObjectName("lbl_headerAddress")
        self.lbl_headerCellno = QtWidgets.QLabel(self.paymentGB)
        self.lbl_headerCellno.setGeometry(QtCore.QRect(0, 40, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_headerCellno.setFont(font)
        self.lbl_headerCellno.setText("")
        self.lbl_headerCellno.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_headerCellno.setObjectName("lbl_headerCellno")
        self.lbl_signature = QtWidgets.QLabel(self.paymentGB)
        self.lbl_signature.setGeometry(QtCore.QRect(10, 260, 191, 16))
        self.lbl_signature.setObjectName("lbl_signature")
        self.label = QtWidgets.QLabel(self.paymentGB)
        self.label.setGeometry(QtCore.QRect(10, 80, 47, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.paymentGB)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.paymentGB)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.paymentGB)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 47, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.paymentGB)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.paymentGB)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.paymentGB)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.paymentGB)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.label_8.setObjectName("label_8")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.confirmSaleGB)
        self.buttonBox.setGeometry(QtCore.QRect(50, 320, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(confirmSaleDialog)
        self.buttonBox.accepted.connect(self.onConfirmPaymentSale)
        self.buttonBox.accepted.connect(confirmSaleDialog.accept)
        self.buttonBox.rejected.connect(confirmSaleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(confirmSaleDialog)

    def retranslateUi(self, confirmSaleDialog):
        _translate = QtCore.QCoreApplication.translate
        confirmSaleDialog.setWindowTitle(_translate("confirmSaleDialog", "Confirm Payment"))
        self.lbl_header.setText(_translate("confirmSaleDialog", globalVariables.Variables._companyName))
        self.lbl_headerAddress.setText(_translate("confirmSaleDialog", globalVariables.Variables._compnayAddress))
        self.lbl_headerCellno.setText(_translate("confirmSaleDialog", globalVariables.Variables._compnayMobile))

        self.confirmSaleGB.setTitle(_translate("confirmSaleDialog", "Confirm Sale Payment"))
        self.lbl_signature.setText(_translate("confirmSaleDialog", "Signature : "))
        self.label.setText(_translate("confirmSaleDialog", "Date :"))
        self.label_2.setText(_translate("confirmSaleDialog", "Customer :"))
        self.label_3.setText(_translate("confirmSaleDialog", "Mobile No :"))
        self.label_4.setText(_translate("confirmSaleDialog", "Address :"))
        self.label_5.setText(_translate("confirmSaleDialog", "Sold Item :"))
        self.label_6.setText(_translate("confirmSaleDialog", "Invoice No."))
        self.label_7.setText(_translate("confirmSaleDialog", "Paid Amount :"))
        self.label_8.setText(_translate("confirmSaleDialog", "Remaining :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmSaleDialog = QtWidgets.QDialog()
    ui = Ui_confirmSaleDialog()
    ui.confirmSaleSetupUi(confirmSaleDialog)
    confirmSaleDialog.show()
    sys.exit(app.exec_())

