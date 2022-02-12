# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'companyConfirmForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Globals import globalVariables
from Services.ImgService import image
from BLL.SetupBL import companyBL

class Ui_conformDialog(object):

    _imageCode = ''
    def setCompanyFields(self, name, code, agent, contact, location, imageCode):
        self.le_name.setText(name)
        self.le_code.setText(code)
        self.le_contact.setText(contact)
        self.le_agent.setText(agent)
        self.le_location.setText(location)

        if (imageCode != ''):
            self._imageCode = imageCode
            self.lbl_image.setPixmap(image.getPixmap(imageCode))
        else:
            self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'user.png'))

    def onConfirmCompany(self):
        name = self.le_name.text()
        code = self.le_code.text()
        agent = self.le_agent.text()
        contact = self.le_contact.text()
        location = self.le_location.text()
        imageCode = self._imageCode

        companyBL.confirmCompany(self, name, code, agent, contact, location, imageCode)


    def conformSetupUi(self, conformDialog):
        conformDialog.setObjectName("conformDialog")
        conformDialog.resize(510, 246)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        conformDialog.setWindowIcon(QtGui.QIcon(windowIcon))

        conformDialog.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        conformDialog.setAutoFillBackground(True)

        self.conformCompanyGB = QtWidgets.QGroupBox(conformDialog)
        self.conformCompanyGB.setGeometry(QtCore.QRect(10, 0, 491, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conformCompanyGB.sizePolicy().hasHeightForWidth())
        self.conformCompanyGB.setSizePolicy(sizePolicy)
        self.conformCompanyGB.setObjectName("conformCompanyGB")
        self.le_name = QtWidgets.QLineEdit(self.conformCompanyGB)
        self.le_name.setEnabled(False)
        self.le_name.setGeometry(QtCore.QRect(70, 20, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        self.le_name.setObjectName("le_name")
        self.le_code = QtWidgets.QLineEdit(self.conformCompanyGB)
        self.le_code.setEnabled(False)
        self.le_code.setGeometry(QtCore.QRect(70, 50, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_code.sizePolicy().hasHeightForWidth())
        self.le_code.setSizePolicy(sizePolicy)
        self.le_code.setObjectName("le_code")
        self.le_contact = QtWidgets.QLineEdit(self.conformCompanyGB)
        self.le_contact.setEnabled(False)
        self.le_contact.setGeometry(QtCore.QRect(70, 110, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_contact.sizePolicy().hasHeightForWidth())
        self.le_contact.setSizePolicy(sizePolicy)
        self.le_contact.setObjectName("le_contact")
        self.le_agent = QtWidgets.QLineEdit(self.conformCompanyGB)
        self.le_agent.setEnabled(False)
        self.le_agent.setGeometry(QtCore.QRect(70, 80, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_agent.sizePolicy().hasHeightForWidth())
        self.le_agent.setSizePolicy(sizePolicy)
        self.le_agent.setObjectName("le_agent")
        self.lbl_image = QtWidgets.QLabel(self.conformCompanyGB)
        self.lbl_image.setGeometry(QtCore.QRect(280, 20, 200, 200))
        self.lbl_image.setText("")
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
        self.le_location.setEnabled(False)
        self.le_location.setGeometry(QtCore.QRect(70, 140, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_location.sizePolicy().hasHeightForWidth())
        self.le_location.setSizePolicy(sizePolicy)
        self.le_location.setObjectName("le_location")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.conformCompanyGB)
        self.buttonBox.setGeometry(QtCore.QRect(110, 200, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(conformDialog)
        self.buttonBox.accepted.connect(self.onConfirmCompany)
        self.buttonBox.accepted.connect(conformDialog.accept)
        self.buttonBox.rejected.connect(conformDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(conformDialog)

    def retranslateUi(self, conformDialog):
        _translate = QtCore.QCoreApplication.translate
        conformDialog.setWindowTitle(_translate("conformDialog", "Confirm Company"))
        self.conformCompanyGB.setTitle(_translate("conformDialog", "Confirm Company"))
        self.label.setText(_translate("conformDialog", "Name"))
        self.label_2.setText(_translate("conformDialog", "Code"))
        self.label_3.setText(_translate("conformDialog", "Contact"))
        self.label_4.setText(_translate("conformDialog", "Agent"))
        self.label_5.setText(_translate("conformDialog", "Loaction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    conformDialog = QtWidgets.QDialog()
    ui = Ui_conformDialog()
    ui.conformSetupUi(conformDialog)
    conformDialog.show()
    sys.exit(app.exec_())

