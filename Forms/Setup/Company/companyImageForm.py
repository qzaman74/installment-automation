# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userImage.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from Globals import globalVariables
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_imageDialog(object):
    def getImage(self,imageCode):
        self.lbl_displayImage.setPixmap(imageCode)
    def imageSetupUi(self, imageDialog):
        imageDialog.setObjectName("imageDialog")
        imageDialog.resize(360, 290)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        imageDialog.setWindowIcon(QtGui.QIcon(windowIcon))

        imageDialog.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        imageDialog.setAutoFillBackground(True)

        self.groupBox = QtWidgets.QGroupBox(imageDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 340, 270))
        self.groupBox.setObjectName("groupBox")
        self.lbl_displayImage = QtWidgets.QLabel(self.groupBox)
        self.lbl_displayImage.setGeometry(QtCore.QRect(10, -20, 320, 320))
        self.lbl_displayImage.setText("")
        self.lbl_displayImage.setObjectName("lbl_displayImage")

        self.retranslateUi(imageDialog)
        QtCore.QMetaObject.connectSlotsByName(imageDialog)

    def retranslateUi(self, imageDialog):
        _translate = QtCore.QCoreApplication.translate
        imageDialog.setWindowTitle(_translate("imageDialog", "Display Picture"))
        self.groupBox.setTitle(_translate("imageDialog", "Profile Picture"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    imageDialog = QtWidgets.QDialog()
    ui = Ui_imageDialog()
    ui.imageSetupUi(imageDialog)
    imageDialog.show()
    sys.exit(app.exec_())

