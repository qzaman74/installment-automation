# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchaseConfirmForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Services.ImgService import image
from Globals import globalVariables
from BLL.PurchaseBL import purchaseBL

class Ui_purchaseConfirmForm(object):
    _accountId = 0
    _imageCode = ''
    _itemList = []
    _policyType = ''
    _policyList = []
    def setPurchaseFields(self, date, accountId, accountName, invoice, amount, discount, netAmount, payment, balance,
                          imageCode, itemList, policyType, policyList):
        self._accountId = accountId
        self._imageCode = imageCode
        self._itemList = itemList
        self._policyType = policyType
        self._policyList = policyList

        self.le_date.setText(date)
        self.le_supplerName.setText(accountName)
        self.le_invoice.setText(invoice)
        self.le_totalBill.setText(amount)
        self.le_discountPercent.setText(discount)
        self.le_netBill.setText(netAmount)
        self.le_payment.setText(payment)
        self.le_balance.setText(balance)

        if(imageCode != ''):
            self.lbl_image.setPixmap(image.getPixmap(imageCode))
        else:
            self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon + 'invoice.png'))

        self.tbl_cart.setRowCount(0)
        for row_number, row_data in enumerate(itemList):
            self.tbl_cart.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tbl_cart.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))


    def onConfirmPurchase(self):
        date = self.le_date.text()
        accountId = self._accountId
        invoice = self.le_invoice.text()
        amount = self.le_totalBill.text()
        discount = self.le_discountPercent.text()
        netAmount = self.le_netBill.text()
        payment = self.le_payment.text()
        balance = self.le_balance.text()
        imageCode = self._imageCode
        itemList = self._itemList
        policyType = self._policyType
        policyList = self._policyList

        purchaseBL.confirmPurchase( date, accountId, invoice, amount, discount, netAmount, payment, balance, imageCode,
                                    itemList, policyType, policyList)

    def purchaseConfirmFormSetupUi(self, purchaseConfirmForm):
        purchaseConfirmForm.setObjectName("purchaseConfirmForm")
        purchaseConfirmForm.resize(1081, 594)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        purchaseConfirmForm.setWindowIcon(QtGui.QIcon(windowIcon))

        purchaseConfirmForm.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        purchaseConfirmForm.setAutoFillBackground(True)

        self.confirmPurchaseGB = QtWidgets.QGroupBox(purchaseConfirmForm)
        self.confirmPurchaseGB.setGeometry(QtCore.QRect(10, 0, 1061, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmPurchaseGB.sizePolicy().hasHeightForWidth())
        self.confirmPurchaseGB.setSizePolicy(sizePolicy)
        self.confirmPurchaseGB.setObjectName("confirmPurchaseGB")
        self.le_date = QtWidgets.QLineEdit(self.confirmPurchaseGB)
        self.le_date.setEnabled(False)
        self.le_date.setGeometry(QtCore.QRect(10, 60, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_date.sizePolicy().hasHeightForWidth())
        self.le_date.setSizePolicy(sizePolicy)
        self.le_date.setObjectName("le_date")
        self.le_supplerName = QtWidgets.QLineEdit(self.confirmPurchaseGB)
        self.le_supplerName.setEnabled(False)
        self.le_supplerName.setGeometry(QtCore.QRect(220, 60, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_supplerName.sizePolicy().hasHeightForWidth())
        self.le_supplerName.setSizePolicy(sizePolicy)
        self.le_supplerName.setObjectName("le_supplerName")
        self.le_invoice = QtWidgets.QLineEdit(self.confirmPurchaseGB)
        self.le_invoice.setEnabled(False)
        self.le_invoice.setGeometry(QtCore.QRect(430, 60, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_invoice.sizePolicy().hasHeightForWidth())
        self.le_invoice.setSizePolicy(sizePolicy)
        self.le_invoice.setObjectName("le_invoice")
        self.le_totalBill = QtWidgets.QLineEdit(self.confirmPurchaseGB)
        self.le_totalBill.setEnabled(False)
        self.le_totalBill.setGeometry(QtCore.QRect(640, 60, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_totalBill.sizePolicy().hasHeightForWidth())
        self.le_totalBill.setSizePolicy(sizePolicy)
        self.le_totalBill.setObjectName("le_totalBill")
        self.lbl_image = QtWidgets.QLabel(self.confirmPurchaseGB)
        self.lbl_image.setGeometry(QtCore.QRect(850, 20, 200, 150))
        self.lbl_image.setText("")
        self.lbl_image.setPixmap(QtGui.QPixmap("../../../Pictures/(1 of 2) a.jpg"))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")
        self.label = QtWidgets.QLabel(self.confirmPurchaseGB)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 28))
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
        self.label_2 = QtWidgets.QLabel(self.confirmPurchaseGB)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.confirmPurchaseGB)
        self.label_3.setGeometry(QtCore.QRect(430, 30, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.confirmPurchaseGB)
        self.label_4.setGeometry(QtCore.QRect(640, 30, 101, 28))
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
        self.label_5 = QtWidgets.QLabel(self.confirmPurchaseGB)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 111, 28))
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
        self.le_discountPercent = QtWidgets.QLineEdit(self.confirmPurchaseGB)
        self.le_discountPercent.setEnabled(False)
        self.le_discountPercent.setGeometry(QtCore.QRect(10, 130, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_discountPercent.sizePolicy().hasHeightForWidth())
        self.le_discountPercent.setSizePolicy(sizePolicy)
        self.le_discountPercent.setObjectName("le_discountPercent")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.confirmPurchaseGB)
        self.buttonBox.setGeometry(QtCore.QRect(890, 550, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.le_netBill = QtWidgets.QLineEdit(self.confirmPurchaseGB)
        self.le_netBill.setEnabled(False)
        self.le_netBill.setGeometry(QtCore.QRect(220, 130, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_netBill.sizePolicy().hasHeightForWidth())
        self.le_netBill.setSizePolicy(sizePolicy)
        self.le_netBill.setObjectName("le_netBill")
        self.label_6 = QtWidgets.QLabel(self.confirmPurchaseGB)
        self.label_6.setGeometry(QtCore.QRect(220, 100, 111, 28))
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

        self.tbl_cart = QtWidgets.QTableWidget(self.confirmPurchaseGB)
        self.tbl_cart.setGeometry(QtCore.QRect(5, 180, 1051, 371))
        self.tbl_cart.setRowCount(11)
        self.tbl_cart.setColumnCount(13)
        self.tbl_cart.setHorizontalHeaderLabels(['companyId', 'Company','productId','Product','Product Type',
                                                 'Engine','Chessis','Registration','Cost','Sale','Discount',
                                                 'Total','remarks'])
        self.tbl_cart.setColumnHidden(0,True)
        self.tbl_cart.setColumnHidden(2,True)
        self.tbl_cart.setColumnWidth(10,65)
        self.tbl_cart.setObjectName("tbl_cart")

        self.le_payment = QtWidgets.QLineEdit(self.confirmPurchaseGB)
        self.le_payment.setEnabled(False)
        self.le_payment.setGeometry(QtCore.QRect(430, 130, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_payment.sizePolicy().hasHeightForWidth())
        self.le_payment.setSizePolicy(sizePolicy)
        self.le_payment.setObjectName("le_payment")
        self.label_7 = QtWidgets.QLabel(self.confirmPurchaseGB)
        self.label_7.setGeometry(QtCore.QRect(640, 100, 101, 28))
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
        self.label_8 = QtWidgets.QLabel(self.confirmPurchaseGB)
        self.label_8.setGeometry(QtCore.QRect(430, 100, 101, 28))
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
        self.le_balance = QtWidgets.QLineEdit(self.confirmPurchaseGB)
        self.le_balance.setEnabled(False)
        self.le_balance.setGeometry(QtCore.QRect(640, 130, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_balance.sizePolicy().hasHeightForWidth())
        self.le_balance.setSizePolicy(sizePolicy)
        self.le_balance.setObjectName("le_balance")

        self.retranslateUi(purchaseConfirmForm)
        self.buttonBox.accepted.connect(self.onConfirmPurchase)
        self.buttonBox.accepted.connect(purchaseConfirmForm.accept)
        self.buttonBox.rejected.connect(purchaseConfirmForm.reject)
        QtCore.QMetaObject.connectSlotsByName(purchaseConfirmForm)

    def retranslateUi(self, purchaseConfirmForm):
        _translate = QtCore.QCoreApplication.translate
        purchaseConfirmForm.setWindowTitle(_translate("purchaseConfirmForm", "Confirm  Purchase"))
        self.confirmPurchaseGB.setTitle(_translate("purchaseConfirmForm", "Confirm Purchase"))
        self.label.setText(_translate("purchaseConfirmForm", "Bill Date"))
        self.label_2.setText(_translate("purchaseConfirmForm", "Account"))
        self.label_3.setText(_translate("purchaseConfirmForm", "Invoice No#"))
        self.label_4.setText(_translate("purchaseConfirmForm", "Total Bil"))
        self.label_5.setText(_translate("purchaseConfirmForm", "Discount %"))
        self.label_6.setText(_translate("purchaseConfirmForm", "Net Bill"))
        self.label_7.setText(_translate("purchaseConfirmForm", "Balance"))
        self.label_8.setText(_translate("purchaseConfirmForm", "Payment"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    purchaseConfirmForm = QtWidgets.QDialog()
    ui = Ui_purchaseConfirmForm()
    ui.purchaseConfirmFormSetupUi(purchaseConfirmForm)
    purchaseConfirmForm.show()
    sys.exit(app.exec_())

