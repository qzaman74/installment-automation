# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productUpdateForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Globals import globalVariables,globalList
from BLL.SetupBL import productBL

class Ui_updateProduct(object):
    _productId = 0
    _imageCode = ''

    def setProductFields(self,result, companyList):
        for x in result:
            self._productId = x[0]
            self.le_company.setText(x[1])
            self.le_type.setText(x[2])
            self.le_name.setText(x[3])
            self.le_code.setText(x[4])
            self.le_remarks.setText(x[5])

        for id, name, code, representative, contact, location in companyList:
            self.cb_company.addItem(name,id)

    def confirmUpdateProduct(self):
        productId = self._productId
        companyId = self.cb_company.currentData()
        productType = self.cb_type.currentText()
        product = self.le_name.text()
        code = self.le_code.text()
        remarks = self.le_remarks.text()
        imageCode = self._imageCode
        productBL.confirmUpdate(productId,companyId,productType,product,code,remarks,imageCode)



    def onChangeCompany(self):
        self.le_company.setText(self.cb_company.currentText())

    def onChangeType(self):
        self.le_type.setText(self.cb_type.currentText())

    def updateSetupUi(self, updateProduct):
        updateProduct.setObjectName("updateProduct")
        updateProduct.resize(510, 265)
        updateProduct.setMinimumSize(510, 265)
        updateProduct.setMaximumSize(510, 265)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        updateProduct.setWindowIcon(QtGui.QIcon(windowIcon))

        updateProduct.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        updateProduct.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        charRegex=QtCore.QRegExp("[a-z-A-Z _]+")
        self.onlyChar = QtGui.QRegExpValidator(charRegex)
        self.confirmProductGB = QtWidgets.QGroupBox(updateProduct)
        self.confirmProductGB.setGeometry(QtCore.QRect(10, 0, 491, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmProductGB.sizePolicy().hasHeightForWidth())
        self.confirmProductGB.setSizePolicy(sizePolicy)
        self.confirmProductGB.setObjectName("confirmProductGB")
        self.le_name = QtWidgets.QLineEdit(self.confirmProductGB)
        self.le_name.setEnabled(True)
        self.le_name.setGeometry(QtCore.QRect(70, 140, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        self.le_name.setObjectName("le_name")
        self.le_code = QtWidgets.QLineEdit(self.confirmProductGB)
        self.le_code.setEnabled(True)
        self.le_code.setGeometry(QtCore.QRect(70, 170, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_code.sizePolicy().hasHeightForWidth())
        self.le_code.setSizePolicy(sizePolicy)
        self.le_code.setObjectName("le_code")
        self.lbl_image = QtWidgets.QLabel(self.confirmProductGB)
        self.lbl_image.setGeometry(QtCore.QRect(280, 20, 200, 200))
        self.lbl_image.setText("")
        self.lbl_image.setPixmap(QtGui.QPixmap("E:/Project/Pictures/(1 of 2) a.jpg"))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")
        self.label = QtWidgets.QLabel(self.confirmProductGB)
        self.label.setGeometry(QtCore.QRect(10, 140, 60, 28))
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
        self.label_2 = QtWidgets.QLabel(self.confirmProductGB)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 60, 28))
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
        self.label_5 = QtWidgets.QLabel(self.confirmProductGB)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 60, 28))
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
        self.le_remarks = QtWidgets.QLineEdit(self.confirmProductGB)
        self.le_remarks.setEnabled(True)
        self.le_remarks.setGeometry(QtCore.QRect(70, 200, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_remarks.sizePolicy().hasHeightForWidth())
        self.le_remarks.setSizePolicy(sizePolicy)
        self.le_remarks.setObjectName("le_remarks")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.confirmProductGB)
        self.buttonBox.setGeometry(QtCore.QRect(110, 230, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.btn_capture = QtWidgets.QPushButton(self.confirmProductGB)
        self.btn_capture.setGeometry(QtCore.QRect(410, 230, 75, 23))
        self.btn_capture.setObjectName("btn_capture")
        self.btn_browse = QtWidgets.QPushButton(self.confirmProductGB)
        self.btn_browse.setGeometry(QtCore.QRect(330, 230, 75, 23))
        self.btn_browse.setObjectName("btn_browse")
        self.cb_company = QtWidgets.QComboBox(self.confirmProductGB)
        self.cb_company.setGeometry(QtCore.QRect(70, 20, 200, 28))
        self.cb_company.setObjectName("cb_company")
        self.cb_company.activated.connect(self.onChangeCompany)

        self.label_3 = QtWidgets.QLabel(self.confirmProductGB)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 60, 28))
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
        self.label_4 = QtWidgets.QLabel(self.confirmProductGB)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 60, 28))
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
        self.cb_type = QtWidgets.QComboBox(self.confirmProductGB)
        self.cb_type.setGeometry(QtCore.QRect(70, 80, 200, 28))
        self.cb_type.addItems(globalList.List._productTypeList)
        self.cb_type.setObjectName("cb_type")
        self.cb_type.activated.connect(self.onChangeType)

        self.le_company = QtWidgets.QLineEdit(self.confirmProductGB)
        self.le_company.setEnabled(False)
        self.le_company.setGeometry(QtCore.QRect(70, 50, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_company.sizePolicy().hasHeightForWidth())
        self.le_company.setSizePolicy(sizePolicy)
        self.le_company.setObjectName("le_company")
        self.le_type = QtWidgets.QLineEdit(self.confirmProductGB)
        self.le_type.setEnabled(False)
        self.le_type.setGeometry(QtCore.QRect(70, 110, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_type.sizePolicy().hasHeightForWidth())
        self.le_type.setSizePolicy(sizePolicy)
        self.le_type.setObjectName("le_type")

        self.retranslateUi(updateProduct)
        self.buttonBox.accepted.connect(self.confirmUpdateProduct)
        self.buttonBox.accepted.connect(updateProduct.accept)
        self.buttonBox.rejected.connect(updateProduct.reject)
        QtCore.QMetaObject.connectSlotsByName(updateProduct)

    def retranslateUi(self, updateProduct):
        _translate = QtCore.QCoreApplication.translate
        updateProduct.setWindowTitle(_translate("updateProduct", "Update Product"))
        self.confirmProductGB.setTitle(_translate("updateProduct", "Update Product"))
        self.label.setText(_translate("updateProduct", "Product"))
        self.label_2.setText(_translate("updateProduct", "Code"))
        self.label_5.setText(_translate("updateProduct", "Remarks"))
        self.btn_capture.setText(_translate("updateProduct", "Capture"))
        self.btn_browse.setText(_translate("updateProduct", "Browse"))
        self.label_3.setText(_translate("updateProduct", "Company"))
        self.label_4.setText(_translate("updateProduct", "Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    updateProduct = QtWidgets.QDialog()
    ui = Ui_updateProduct()
    ui.updateSetupUi(updateProduct)
    updateProduct.show()
    sys.exit(app.exec_())

