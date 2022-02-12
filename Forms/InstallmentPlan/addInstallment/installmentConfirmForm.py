# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installmentConfirmForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from BLL.InstallmentsBL import addInstallmentBL
from Globals import globalVariables
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_conformInstallmentDialog(object):
    _customerSchemeID = 0
    _balance = 0

    def setInstallmentConfirmFields(self, date, name, cellno, address,  customerSchemeID,  scheme, installment, balance, amount, remarks):
        self._customerSchemeID = customerSchemeID
        self._balance = balance
        self.lbl_date.setText(date)
        self.lbl_name.setText(name)
        self.lbl_cellNo.setText(cellno)
        self.lbl_address.setText(address)
        self.lbl_scheme.setText(scheme)
        self.lbl_installment.setText(installment)
        self.lbl_amount.setText(amount)
        self.lbl_remarks.setText(remarks)

    def onConfirmInstallment(self):
        customerSchemeID = self._customerSchemeID
        date = self.lbl_date.text()
        balance = self._balance
        amount = self.lbl_amount.text()
        remarks = self.lbl_remarks.text()

        addInstallmentBL.confirmInstallment(customerSchemeID, date, balance, amount, remarks)


    def conformInstallmentSetupUi(self, conformInstallmentDialog):
        conformInstallmentDialog.setObjectName("conformInstallmentDialog")
        conformInstallmentDialog.resize(241, 359)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        conformInstallmentDialog.setWindowIcon(QtGui.QIcon(windowIcon))

        conformInstallmentDialog.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        conformInstallmentDialog.setAutoFillBackground(True)

        self.confirmInstallmentGB = QtWidgets.QGroupBox(conformInstallmentDialog)
        self.confirmInstallmentGB.setGeometry(QtCore.QRect(10, 0, 221, 351))
        self.confirmInstallmentGB.setObjectName("confirmInstallmentGB")
        self.installmentGB = QtWidgets.QGroupBox(self.confirmInstallmentGB)
        self.installmentGB.setGeometry(QtCore.QRect(10, 20, 200, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.installmentGB.sizePolicy().hasHeightForWidth())
        self.installmentGB.setSizePolicy(sizePolicy)
        self.installmentGB.setTitle("")
        self.installmentGB.setObjectName("installmentGB")
        self.lbl_name = QtWidgets.QLabel(self.installmentGB)
        self.lbl_name.setGeometry(QtCore.QRect(80, 100, 120, 16))
        self.lbl_name.setText("")
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_cellNo = QtWidgets.QLabel(self.installmentGB)
        self.lbl_cellNo.setGeometry(QtCore.QRect(80, 120, 120, 16))
        self.lbl_cellNo.setText("")
        self.lbl_cellNo.setObjectName("lbl_cellNo")
        self.lbl_address = QtWidgets.QLabel(self.installmentGB)
        self.lbl_address.setGeometry(QtCore.QRect(80, 140, 120, 16))
        self.lbl_address.setText("")
        self.lbl_address.setObjectName("lbl_address")
        self.lbl_scheme = QtWidgets.QLabel(self.installmentGB)
        self.lbl_scheme.setGeometry(QtCore.QRect(80, 160, 120, 16))
        self.lbl_scheme.setText("")
        self.lbl_scheme.setObjectName("lbl_scheme")
        self.lbl_installment = QtWidgets.QLabel(self.installmentGB)
        self.lbl_installment.setGeometry(QtCore.QRect(80, 180, 120, 16))
        self.lbl_installment.setText("")
        self.lbl_installment.setObjectName("lbl_installment")
        self.lbl_amount = QtWidgets.QLabel(self.installmentGB)
        self.lbl_amount.setGeometry(QtCore.QRect(80, 200, 120, 16))
        self.lbl_amount.setText("")
        self.lbl_amount.setObjectName("lbl_amount")
        self.lbl_remarks = QtWidgets.QLabel(self.installmentGB)
        self.lbl_remarks.setGeometry(QtCore.QRect(80, 220, 120, 16))
        self.lbl_remarks.setText("")
        self.lbl_remarks.setObjectName("lbl_remarks")
        self.lbl_date = QtWidgets.QLabel(self.installmentGB)
        self.lbl_date.setGeometry(QtCore.QRect(80, 80, 120, 16))
        self.lbl_date.setText("")
        self.lbl_date.setObjectName("lbl_date")
        self.lbl_company = QtWidgets.QLabel(self.installmentGB)
        self.lbl_company.setGeometry(QtCore.QRect(0, 0, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_company.setFont(font)
        self.lbl_company.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_company.setObjectName("lbl_company")
        self.lbl_companyCellno = QtWidgets.QLabel(self.installmentGB)
        self.lbl_companyCellno.setGeometry(QtCore.QRect(0, 20, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_companyCellno.setFont(font)
        self.lbl_companyCellno.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_companyCellno.setObjectName("lbl_companyCellno")
        self.lbl_companyCellno_2 = QtWidgets.QLabel(self.installmentGB)
        self.lbl_companyCellno_2.setGeometry(QtCore.QRect(0, 40, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_companyCellno_2.setFont(font)
        self.lbl_companyCellno_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_companyCellno_2.setObjectName("lbl_companyCellno_2")
        self.lbl_remarks_2 = QtWidgets.QLabel(self.installmentGB)
        self.lbl_remarks_2.setGeometry(QtCore.QRect(10, 260, 191, 16))
        self.lbl_remarks_2.setObjectName("lbl_remarks_2")
        self.label = QtWidgets.QLabel(self.installmentGB)
        self.label.setGeometry(QtCore.QRect(10, 80, 47, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.installmentGB)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.installmentGB)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.installmentGB)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 47, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.installmentGB)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 47, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.installmentGB)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.installmentGB)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.installmentGB)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 47, 16))
        self.label_8.setObjectName("label_8")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.confirmInstallmentGB)
        self.buttonBox.setGeometry(QtCore.QRect(50, 320, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(conformInstallmentDialog)
        self.buttonBox.accepted.connect(self.onConfirmInstallment)
        self.buttonBox.accepted.connect(conformInstallmentDialog.accept)
        self.buttonBox.rejected.connect(conformInstallmentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(conformInstallmentDialog)

    def retranslateUi(self, conformInstallmentDialog):
        _translate = QtCore.QCoreApplication.translate
        conformInstallmentDialog.setWindowTitle(_translate("conformInstallmentDialog", "Confirm Installment"))
        self.confirmInstallmentGB.setTitle(_translate("conformInstallmentDialog", "Confirm Installment"))
        self.lbl_company.setText(_translate("conformInstallmentDialog", "Bike ShowRoom"))
        self.lbl_companyCellno.setText(_translate("conformInstallmentDialog", "03043228224"))
        self.lbl_companyCellno_2.setText(_translate("conformInstallmentDialog", "Installment"))
        self.lbl_remarks_2.setText(_translate("conformInstallmentDialog", "Signature : "))
        self.label.setText(_translate("conformInstallmentDialog", "Date :"))
        self.label_2.setText(_translate("conformInstallmentDialog", "Customer :"))
        self.label_3.setText(_translate("conformInstallmentDialog", "Mobile No :"))
        self.label_4.setText(_translate("conformInstallmentDialog", "Address :"))
        self.label_5.setText(_translate("conformInstallmentDialog", "Scheme :"))
        self.label_6.setText(_translate("conformInstallmentDialog", "Installment :"))
        self.label_7.setText(_translate("conformInstallmentDialog", "Paid Amount :"))
        self.label_8.setText(_translate("conformInstallmentDialog", "Remarks :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    conformInstallmentDialog = QtWidgets.QDialog()
    ui = Ui_conformInstallmentDialog()
    ui.conformInstallmentSetupUi(conformInstallmentDialog)
    conformInstallmentDialog.show()
    sys.exit(app.exec_())

