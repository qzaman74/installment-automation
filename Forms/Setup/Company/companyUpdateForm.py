# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateCompanyForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Globals import globalVariables
from BLL.SetupBL import companyBL
from Services.ResetServices import formReset

class Ui_updateCompany(object):
    _imageCode = ''
    _compnayId = None
    def setUpdateFields(self,result):
        for x in result:
            self._compnayId = x[0]
            self.le_name.setText(x[1])
            self.le_code.setText(x[2])
            self.le_agent.setText(x[3])
            self.le_contact.setText(x[4])
            self.le_location.setText(x[5])

    def confirmUpdate(self):
        id = self._compnayId
        name = self.le_name.text()
        code = self.le_code.text()
        agent = self.le_agent.text()
        contact = self.le_contact.text()
        location = self.le_location.text()

        companyBL.confirmUpdate(id,name,code,agent,contact,location,self._imageCode)


    def updateSetupUi(self, updateCompany):
        updateCompany.setObjectName("updateCompany")
        updateCompany.resize(510, 245)
        updateCompany.setMaximumSize(510, 245)
        updateCompany.setMinimumSize(510, 245)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        updateCompany.setWindowIcon(QtGui.QIcon(windowIcon))

        updateCompany.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        updateCompany.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        charRegex=QtCore.QRegExp("[a-z-A-Z _]+")
        self.onlyChar = QtGui.QRegExpValidator(charRegex)

        self.conformCompanyGB = QtWidgets.QGroupBox(updateCompany)
        self.conformCompanyGB.setGeometry(QtCore.QRect(10, 0, 491, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conformCompanyGB.sizePolicy().hasHeightForWidth())
        self.conformCompanyGB.setSizePolicy(sizePolicy)
        self.conformCompanyGB.setObjectName("conformCompanyGB")
        self.le_name = QtWidgets.QLineEdit(self.conformCompanyGB)
        self.le_name.setEnabled(True)
        self.le_name.setGeometry(QtCore.QRect(70, 20, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        self.le_name.setMaxLength(32)
        self.le_name.setValidator(self.onlyChar)
        self.le_name.setObjectName("le_name")

        self.le_code = QtWidgets.QLineEdit(self.conformCompanyGB)
        self.le_code.setEnabled(True)
        self.le_code.setGeometry(QtCore.QRect(70, 50, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_code.sizePolicy().hasHeightForWidth())
        self.le_code.setSizePolicy(sizePolicy)
        self.le_code.setMaxLength(32)
        self.le_code.setValidator(self.onlyInt)
        self.le_code.setObjectName("le_code")

        self.le_contact = QtWidgets.QLineEdit(self.conformCompanyGB)
        self.le_contact.setEnabled(True)
        self.le_contact.setGeometry(QtCore.QRect(70, 110, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_contact.sizePolicy().hasHeightForWidth())
        self.le_contact.setSizePolicy(sizePolicy)
        self.le_contact.setMaxLength(11)
        self.le_contact.setValidator(self.onlyInt)
        self.le_contact.setObjectName("le_contact")

        self.le_agent = QtWidgets.QLineEdit(self.conformCompanyGB)
        self.le_agent.setEnabled(True)
        self.le_agent.setGeometry(QtCore.QRect(70, 80, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_agent.sizePolicy().hasHeightForWidth())
        self.le_agent.setSizePolicy(sizePolicy)
        self.le_agent.setMaxLength(32)
        self.le_agent.setValidator(self.onlyChar)
        self.le_agent.setObjectName("le_agent")

        self.lbl_image = QtWidgets.QLabel(self.conformCompanyGB)
        self.lbl_image.setGeometry(QtCore.QRect(280, 20, 200, 200))
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'user.png'))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")
        self.label = QtWidgets.QLabel(self.conformCompanyGB)
        self.label.setGeometry(QtCore.QRect(10, 20, 60, 28))
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
        self.label_2 = QtWidgets.QLabel(self.conformCompanyGB)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 60, 28))
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
        self.label_3 = QtWidgets.QLabel(self.conformCompanyGB)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 60, 28))
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
        self.label_4 = QtWidgets.QLabel(self.conformCompanyGB)
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
        self.label_5 = QtWidgets.QLabel(self.conformCompanyGB)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 60, 28))
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

        self.le_location = QtWidgets.QLineEdit(self.conformCompanyGB)
        self.le_location.setEnabled(True)
        self.le_location.setGeometry(QtCore.QRect(70, 140, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_location.sizePolicy().hasHeightForWidth())
        self.le_location.setSizePolicy(sizePolicy)
        self.le_location.setMaxLength(32)
        self.le_location.setValidator(self.onlyChar)
        self.le_location.setObjectName("le_location")


        self.buttonBox = QtWidgets.QDialogButtonBox(self.conformCompanyGB)
        self.buttonBox.setGeometry(QtCore.QRect(110, 200, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.btn_capture = QtWidgets.QPushButton(self.conformCompanyGB)
        self.btn_capture.setGeometry(QtCore.QRect(195, 170, 75, 23))
        self.btn_capture.setObjectName("btn_capture")
        self.btn_browse = QtWidgets.QPushButton(self.conformCompanyGB)
        self.btn_browse.setGeometry(QtCore.QRect(115, 170, 75, 23))
        self.btn_browse.setObjectName("btn_browse")

        self.retranslateUi(updateCompany)
        self.buttonBox.accepted.connect(self.confirmUpdate)
        self.buttonBox.accepted.connect(updateCompany.accept)
        self.buttonBox.rejected.connect(updateCompany.reject)
        QtCore.QMetaObject.connectSlotsByName(updateCompany)

    def retranslateUi(self, updateCompany):
        _translate = QtCore.QCoreApplication.translate
        updateCompany.setWindowTitle(_translate("updateCompany", "Update Company"))
        self.conformCompanyGB.setTitle(_translate("updateCompany", "Update Company"))
        self.label.setText(_translate("updateCompany", "Name"))
        self.label_2.setText(_translate("updateCompany", "Code"))
        self.label_3.setText(_translate("updateCompany", "Contact"))
        self.label_4.setText(_translate("updateCompany", "Agent"))
        self.label_5.setText(_translate("updateCompany", "Loaction"))
        self.btn_capture.setText(_translate("updateCompany", "Capture"))
        self.btn_browse.setText(_translate("updateCompany", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    updateCompany = QtWidgets.QDialog()
    ui = Ui_updateCompany()
    ui.updateSetupUi(updateCompany)
    updateCompany.show()
    sys.exit(app.exec_())

