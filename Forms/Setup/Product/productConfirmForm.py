# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productConfirmForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Globals import globalVariables
from Services.ImgService import image
from BLL.SetupBL import productBL

class Ui_confirmProduct(object):
    _imageCode = ''

    def setConfirmFiels(self, companyId, companyName, productType, name, code, remarks, imageCode):
        self._companyId = companyId
        self.le_company.setText(companyName)
        self.le_type.setText(productType)
        self.le_name.setText(name)
        self.le_code.setText(code)
        self.le_remarks.setText(remarks)

        if (imageCode != ''):
            self._imageCode = imageCode
            self.lbl_image.setPixmap(image.getPixmap(imageCode))
        else:
            self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon + 'product.png'))

    def onConfirmProduct(self):
        companyId = self._companyId
        productType = self.le_type.text()
        name = self.le_name.text()
        code = self.le_code.text()
        remarks = self.le_remarks.text()
        imageCode = self._imageCode

        productBL.confirmProduct(companyId,productType,name,code,remarks,imageCode)

    def confirmProductSetupUi(self, confirmProduct):
        confirmProduct.setObjectName("confirmProduct")
        confirmProduct.resize(528, 247)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        confirmProduct.setWindowIcon(QtGui.QIcon(windowIcon))

        confirmProduct.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        confirmProduct.setAutoFillBackground(True)

        self.conformProductGB = QtWidgets.QGroupBox(confirmProduct)
        self.conformProductGB.setGeometry(QtCore.QRect(10, 0, 511, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conformProductGB.sizePolicy().hasHeightForWidth())
        self.conformProductGB.setSizePolicy(sizePolicy)
        self.conformProductGB.setObjectName("conformProductGB")
        self.le_company = QtWidgets.QLineEdit(self.conformProductGB)
        self.le_company.setEnabled(False)
        self.le_company.setGeometry(QtCore.QRect(80, 20, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_company.sizePolicy().hasHeightForWidth())
        self.le_company.setSizePolicy(sizePolicy)
        self.le_company.setObjectName("le_company")
        self.le_type = QtWidgets.QLineEdit(self.conformProductGB)
        self.le_type.setEnabled(False)
        self.le_type.setGeometry(QtCore.QRect(80, 50, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_type.sizePolicy().hasHeightForWidth())
        self.le_type.setSizePolicy(sizePolicy)
        self.le_type.setObjectName("le_type")
        self.le_code = QtWidgets.QLineEdit(self.conformProductGB)
        self.le_code.setEnabled(False)
        self.le_code.setGeometry(QtCore.QRect(80, 110, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_code.sizePolicy().hasHeightForWidth())
        self.le_code.setSizePolicy(sizePolicy)
        self.le_code.setObjectName("le_code")
        self.le_name = QtWidgets.QLineEdit(self.conformProductGB)
        self.le_name.setEnabled(False)
        self.le_name.setGeometry(QtCore.QRect(80, 80, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        self.le_name.setObjectName("le_name")
        self.lbl_image = QtWidgets.QLabel(self.conformProductGB)
        self.lbl_image.setGeometry(QtCore.QRect(290, 20, 200, 200))
        self.lbl_image.setText("")
        self.lbl_image.setPixmap(QtGui.QPixmap("../../../Pictures/(1 of 2) a.jpg"))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")
        self.label = QtWidgets.QLabel(self.conformProductGB)
        self.label.setGeometry(QtCore.QRect(10, 20, 65, 28))
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
        self.label_2 = QtWidgets.QLabel(self.conformProductGB)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 65, 28))
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
        self.label_3 = QtWidgets.QLabel(self.conformProductGB)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 65, 28))
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
        self.label_4 = QtWidgets.QLabel(self.conformProductGB)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 65, 28))
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
        self.label_5 = QtWidgets.QLabel(self.conformProductGB)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 65, 28))
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
        self.le_remarks = QtWidgets.QLineEdit(self.conformProductGB)
        self.le_remarks.setEnabled(False)
        self.le_remarks.setGeometry(QtCore.QRect(80, 140, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_remarks.sizePolicy().hasHeightForWidth())
        self.le_remarks.setSizePolicy(sizePolicy)
        self.le_remarks.setObjectName("le_remarks")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.conformProductGB)
        self.buttonBox.setGeometry(QtCore.QRect(120, 200, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(confirmProduct)
        self.buttonBox.accepted.connect(self.onConfirmProduct)
        self.buttonBox.accepted.connect(confirmProduct.accept)
        self.buttonBox.rejected.connect(confirmProduct.reject)
        QtCore.QMetaObject.connectSlotsByName(confirmProduct)

    def retranslateUi(self, confirmProduct):
        _translate = QtCore.QCoreApplication.translate
        confirmProduct.setWindowTitle(_translate("confirmProduct", "Confirm Product"))
        self.conformProductGB.setTitle(_translate("confirmProduct", "Confirm Product"))
        self.label.setText(_translate("confirmProduct", "Company"))
        self.label_2.setText(_translate("confirmProduct", "Type"))
        self.label_3.setText(_translate("confirmProduct", "Code"))
        self.label_4.setText(_translate("confirmProduct", "Name"))
        self.label_5.setText(_translate("confirmProduct", "Remakrs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmProduct = QtWidgets.QDialog()
    ui = Ui_confirmProduct()
    ui.confirmProductSetupUi(confirmProduct)
    confirmProduct.show()
    sys.exit(app.exec_())

