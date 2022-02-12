# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refAccountConfirmForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from BLL.AccountsBL import refAccountBL
from Services.ImgService import image
from Globals import globalVariables
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_refAccountConfirmDialog(object):
    _imageCode = ''

    def setAccountFields(self, name,fatherName,cnic,mobile,gender,address,imageCode):
        self.le_name.setText(name)
        self.le_fatherName.setText(fatherName)
        self.le_cellNo.setText(mobile)
        self.le_cnic.setText(cnic)
        self.rb_gender.setText(gender)
        self.le_address.setText(address)

        if (imageCode != ''):
            self._imageCode = imageCode
            self.lbl_image.setPixmap(image.getPixmap(imageCode))
        else:
            self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'user.png'))

    def confirmValidation(self):
        name = self.le_name.text()
        fatherName = self.le_fatherName.text()
        cnic = self.le_cnic.text()
        mobile = self.le_cellNo.text()
        gender = self.rb_gender.text()
        address = self.le_address.text()
        imageCode = self._imageCode
        refAccountBL.confirmRefAccountValidation(name,fatherName,cnic,mobile,gender,address,imageCode)


    def refAccountConfirmSetupUi(self, refAccountConfirmDialog):
        refAccountConfirmDialog.setObjectName("refAccountConfirmDialog")
        refAccountConfirmDialog.resize(510, 280)
        refAccountConfirmDialog.setMaximumSize(510, 280)
        refAccountConfirmDialog.setMinimumSize(510, 280)

        self.refAccountConfirmGB = QtWidgets.QGroupBox(refAccountConfirmDialog)
        self.refAccountConfirmGB.setGeometry(QtCore.QRect(5, 0, 501, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refAccountConfirmGB.sizePolicy().hasHeightForWidth())
        self.refAccountConfirmGB.setSizePolicy(sizePolicy)
        self.refAccountConfirmGB.setObjectName("refAccountConfirmGB")
        self.le_name = QtWidgets.QLineEdit(self.refAccountConfirmGB)
        self.le_name.setEnabled(False)
        self.le_name.setGeometry(QtCore.QRect(70, 20, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        self.le_name.setObjectName("le_name")
        self.le_cnic = QtWidgets.QLineEdit(self.refAccountConfirmGB)
        self.le_cnic.setEnabled(False)
        self.le_cnic.setGeometry(QtCore.QRect(70, 80, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cnic.sizePolicy().hasHeightForWidth())
        self.le_cnic.setSizePolicy(sizePolicy)
        self.le_cnic.setObjectName("le_cnic")
        self.le_cellNo = QtWidgets.QLineEdit(self.refAccountConfirmGB)
        self.le_cellNo.setEnabled(False)
        self.le_cellNo.setGeometry(QtCore.QRect(70, 110, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cellNo.sizePolicy().hasHeightForWidth())
        self.le_cellNo.setSizePolicy(sizePolicy)
        self.le_cellNo.setObjectName("le_cellNo")
        self.le_address = QtWidgets.QLineEdit(self.refAccountConfirmGB)
        self.le_address.setEnabled(False)
        self.le_address.setGeometry(QtCore.QRect(70, 170, 200, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_address.sizePolicy().hasHeightForWidth())
        self.le_address.setSizePolicy(sizePolicy)
        self.le_address.setObjectName("le_address")
        self.rb_gender = QtWidgets.QRadioButton(self.refAccountConfirmGB)
        self.rb_gender.setEnabled(False)
        self.rb_gender.setGeometry(QtCore.QRect(70, 140, 61, 28))
        self.rb_gender.setObjectName("rb_gender")
        self.lbl_image = QtWidgets.QLabel(self.refAccountConfirmGB)
        self.lbl_image.setGeometry(QtCore.QRect(290, 20, 200, 200))
        self.lbl_image.setText("")
        self.lbl_image.setPixmap(QtGui.QPixmap("../../../Pictures/(1 of 2) a.jpg"))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")
        self.label = QtWidgets.QLabel(self.refAccountConfirmGB)
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
        self.label_3 = QtWidgets.QLabel(self.refAccountConfirmGB)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 59, 28))
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
        self.label_4 = QtWidgets.QLabel(self.refAccountConfirmGB)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 61, 28))
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
        self.label_5 = QtWidgets.QLabel(self.refAccountConfirmGB)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 59, 28))
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
        self.label_8 = QtWidgets.QLabel(self.refAccountConfirmGB)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 61, 28))
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
        self.buttonBox = QtWidgets.QDialogButtonBox(self.refAccountConfirmGB)
        self.buttonBox.setGeometry(QtCore.QRect(320, 230, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_6 = QtWidgets.QLabel(self.refAccountConfirmGB)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 59, 28))
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
        self.le_fatherName = QtWidgets.QLineEdit(self.refAccountConfirmGB)
        self.le_fatherName.setEnabled(False)
        self.le_fatherName.setGeometry(QtCore.QRect(70, 50, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_fatherName.sizePolicy().hasHeightForWidth())
        self.le_fatherName.setSizePolicy(sizePolicy)
        self.le_fatherName.setText("")
        self.le_fatherName.setObjectName("le_fatherName")

        self.retranslateUi(refAccountConfirmDialog)
        self.buttonBox.accepted.connect(self.confirmValidation)
        self.buttonBox.accepted.connect(refAccountConfirmDialog.accept)
        self.buttonBox.rejected.connect(refAccountConfirmDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(refAccountConfirmDialog)

    def retranslateUi(self, refAccountConfirmDialog):
        _translate = QtCore.QCoreApplication.translate
        refAccountConfirmDialog.setWindowTitle(_translate("refAccountConfirmDialog", "Reference Account Confirm"))
        self.refAccountConfirmGB.setTitle(_translate("refAccountConfirmDialog", "Confirm Reference Account"))
        self.rb_gender.setText(_translate("refAccountConfirmDialog", "Gender"))
        self.label.setText(_translate("refAccountConfirmDialog", "Name"))
        self.label_3.setText(_translate("refAccountConfirmDialog", "CNIC "))
        self.label_4.setText(_translate("refAccountConfirmDialog", "Cell No"))
        self.label_5.setText(_translate("refAccountConfirmDialog", "Address"))
        self.label_8.setText(_translate("refAccountConfirmDialog", "Gender"))
        self.label_6.setText(_translate("refAccountConfirmDialog", "S / O"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    refAccountConfirmDialog = QtWidgets.QDialog()
    ui = Ui_refAccountConfirmDialog()
    ui.refAccountConfirmSetupUi(refAccountConfirmDialog)
    refAccountConfirmDialog.show()
    sys.exit(app.exec_())

