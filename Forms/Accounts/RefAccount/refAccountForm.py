# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refAccountForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!


from BLL.AccountsBL import refAccountBL
from Services.ImgService import camera,image,browseImage
from Services.ResetServices import formReset
from Services.RecallServices import formRecall
from Globals import globalVariables,globalList
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

class Ui_refAccountWindow(object):
    _imageCode = ''
    _filterList = None

    def init(self):
        self.getRefAccounts()

    def onEnterName(self):
        self.le_fatherName.setFocus()

    def onEnterFatherName(self):
        self.le_cnic.setFocus()

    def onEnterCnic(self):
        self.le_cellNo.setFocus()

    def onEnterCellNo(self):
        self.te_address.setFocus()



    def captureImage(self):
        try:
            base64Img = camera.capture()
            self._imageCode = base64Img
            self.lbl_image.setPixmap(image.getPixmap(base64Img))
        except:
            pass

    def browseImage(self):
        try:
            base64Img = browseImage.getImagePath(self.__init__())
            self._imageCode = base64Img
            self.lbl_image.setPixmap(image.getPixmap(base64Img))
        except:
            pass

    def onSubmit(self):
        name = self.le_name.text()
        fatherName = self.le_fatherName.text()
        cnic = self.le_cnic.text()
        mobile = self.le_cellNo.text()
        gender = globalVariables.Variables._male
        if(self.rb_female.isChecked()):
            gender = globalVariables.Variables._female
        address = self.te_address.toPlainText()
        imageCode = self._imageCode
        
        formReset.Reset._resetRefAccountForm = self.onCancel

        refAccountBL.validateRefAccount(self,name,fatherName,cnic,mobile,gender,address,imageCode,self._filterList)


    def onCancel(self):
        self.le_name.setText('')
        self.le_fatherName.setText('')
        self.le_cnic.setText('')
        self.le_cellNo.setText('')
        self.te_address.setPlainText('')
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'user.png'))
        self.getRefAccounts()


    def showImage(self):
        try:
            button = self.tbl_refAccount.sender()
            index = self.tbl_refAccount.indexAt(button.pos())
            if index.isValid():
                accountID = self.tbl_refAccount.model().index(index.row(), 0).data()
                refAccountBL.validateImage(self, accountID)
        except:
            pass

    def editAccount(self):
        button = self.tbl_refAccount.sender()
        index = self.tbl_refAccount.indexAt(button.pos())
        if index.isValid():
            accountID = self.tbl_refAccount.model().index(index.row(), 0).data()
            refAccountBL.validateUpdate(self, accountID)

    def removeAccount(self):
        button = self.tbl_refAccount.sender()
        index = self.tbl_refAccount.indexAt(button.pos())
        if index.isValid():
            formRecall.Recall._recallRefAccount = self.getRefAccounts
            accountID = self.tbl_refAccount.model().index(index.row(), 0).data()
            name = self.tbl_refAccount.model().index(index.row(), 1).data()
            refAccountBL.deleteAccount(self, accountID, name)

    def getRefAccounts(self):
        result = refAccountBL.getAllRefAccounts()
        self.showRefAccouts(result)
        self._filterList = refAccountBL.getAllRefAccounts().fetchall().copy()



    def showRefAccouts(self,result):
        self.tbl_refAccount.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_refAccount.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tbl_refAccount.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data).upper()))

                self.btn_image = QPushButton('Image')
                imageIcon = QtGui.QPixmap(globalVariables.Variables._icon+'imageIcon.png')
                self.btn_image.setIcon(QtGui.QIcon(imageIcon))
                self.tbl_refAccount.setCellWidget(row_number, 7, self.btn_image)

                self.btn_edit = QPushButton('Setting')
                settingIcon = QtGui.QPixmap(globalVariables.Variables._icon+'settingIcon.png')
                self.btn_edit.setIcon(QtGui.QIcon(settingIcon))
                self.tbl_refAccount.setCellWidget(row_number, 8, self.btn_edit)

                self.btn_remove = QPushButton('Delete')
                removeIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
                self.btn_remove.setIcon(QtGui.QIcon(removeIcon))
                self.tbl_refAccount.setCellWidget(row_number, 9, self.btn_remove)
                self.btn_remove.clicked.connect(self.removeAccount)

        if(self.tbl_refAccount.rowCount() < 19):
            self.tbl_refAccount.setRowCount(19)




    def filterFunc(self,item):
        name = self.le_filterByName.text()
        fatherName = self.le_filterByFatherName.text()
        cnic = self.le_filterByCnic.text()
        mobile = self.le_filterByMobile.text()
        gender = self.le_filterByGender.text()
        address = self.le_filterByAddress.text()

        if (str(item[1].lower()).startswith(name) and str(item[2].lower()).startswith(fatherName) and
            str(item[3]).startswith(cnic) and str(item[4]).startswith(mobile)  and
            str(item[5].lower()).startswith(gender) and str(item[6].lower()).startswith(address) ):
            return True
        else:
            return False

    def refAccountFilter(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.showRefAccouts(result)




    def refAccountSetupUi(self, refAccountWindow):
        refAccountWindow.setObjectName("refAccountWindow")
        refAccountWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        refAccountWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        refAccountWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        refAccountWindow.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        charRegex=QtCore.QRegExp("[a-z-A-Z _]+")
        self.onlyChar = QtGui.QRegExpValidator(charRegex)


        self.centralwidget = QtWidgets.QWidget(refAccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addRefAccountGB = QtWidgets.QGroupBox(self.centralwidget)
        self.addRefAccountGB.setGeometry(QtCore.QRect(10, 0, 311, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRefAccountGB.sizePolicy().hasHeightForWidth())
        self.addRefAccountGB.setSizePolicy(sizePolicy)
        self.addRefAccountGB.setObjectName("addRefAccountGB")
        self.le_name = QtWidgets.QLineEdit(self.addRefAccountGB)
        self.le_name.setEnabled(True)
        self.le_name.setGeometry(QtCore.QRect(100, 20, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_name.setFont(font)
        self.le_name.setMaxLength(32)
        self.le_name.setValidator(self.onlyChar)
        self.le_name.setObjectName("le_name")
        self.le_name.returnPressed.connect(self.onEnterName)

        self.le_cnic = QtWidgets.QLineEdit(self.addRefAccountGB)
        self.le_cnic.setEnabled(True)
        self.le_cnic.setGeometry(QtCore.QRect(100, 80, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cnic.sizePolicy().hasHeightForWidth())
        self.le_cnic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cnic.setFont(font)
        self.le_cnic.setMaxLength(13)
        self.le_cnic.setValidator(self.onlyInt)
        self.le_cnic.setObjectName("le_cnic")
        self.le_cnic.returnPressed.connect(self.onEnterCnic)

        self.le_cellNo = QtWidgets.QLineEdit(self.addRefAccountGB)
        self.le_cellNo.setEnabled(True)
        self.le_cellNo.setGeometry(QtCore.QRect(100, 110, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cellNo.sizePolicy().hasHeightForWidth())
        self.le_cellNo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cellNo.setFont(font)
        self.le_cellNo.setMaxLength(11)
        self.le_cellNo.setValidator(self.onlyInt)
        self.le_cellNo.setObjectName("le_cellNo")
        self.le_cellNo.returnPressed.connect(self.onEnterCellNo)

        self.rb_male = QtWidgets.QRadioButton(self.addRefAccountGB)
        self.rb_male.setGeometry(QtCore.QRect(100, 140, 51, 28))
        self.rb_male.setChecked(True)
        self.rb_male.setObjectName("rb_male")
        self.rb_female = QtWidgets.QRadioButton(self.addRefAccountGB)
        self.rb_female.setGeometry(QtCore.QRect(160, 140, 61, 28))
        self.rb_female.setObjectName("rb_female")

        self.lbl_image = QtWidgets.QLabel(self.addRefAccountGB)
        self.lbl_image.setGeometry(QtCore.QRect(100, 260, 200, 201))
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'user.png'))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")

        self.btn_capture = QtWidgets.QPushButton(self.addRefAccountGB)
        self.btn_capture.setGeometry(QtCore.QRect(200, 480, 100, 28))
        captureIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cameraIcon.png')
        self.btn_capture.setIcon(QtGui.QIcon(captureIcon))
        self.btn_capture.setObjectName("btn_capture")
        self.btn_capture.clicked.connect(self.captureImage)

        self.label = QtWidgets.QLabel(self.addRefAccountGB)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 28))
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
        self.label_3 = QtWidgets.QLabel(self.addRefAccountGB)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 28))
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
        self.label_4 = QtWidgets.QLabel(self.addRefAccountGB)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 71, 28))
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
        self.label_5 = QtWidgets.QLabel(self.addRefAccountGB)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 71, 28))
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
        self.label_8 = QtWidgets.QLabel(self.addRefAccountGB)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 71, 28))
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
        self.label_9 = QtWidgets.QLabel(self.addRefAccountGB)
        self.label_9.setGeometry(QtCore.QRect(10, 255, 71, 28))
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

        self.btn_submit = QtWidgets.QPushButton(self.addRefAccountGB)
        self.btn_submit.setGeometry(QtCore.QRect(100, 640, 100, 28))
        submitIcon = QtGui.QPixmap(globalVariables.Variables._icon+'rightIcon.png')
        self.btn_submit.setIcon(QtGui.QIcon(submitIcon))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.onSubmit)

        self.btn_cancel = QtWidgets.QPushButton(self.addRefAccountGB)
        self.btn_cancel.setGeometry(QtCore.QRect(200, 640, 100, 28))
        cancelIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cancelIcon.png')
        self.btn_cancel.setIcon(QtGui.QIcon(cancelIcon))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.onCancel)

        self.btn_browse = QtWidgets.QPushButton(self.addRefAccountGB)
        self.btn_browse.setGeometry(QtCore.QRect(100, 480, 100, 28))
        browseIcon = QtGui.QPixmap(globalVariables.Variables._icon+'browseIcon.png')
        self.btn_browse.setIcon(QtGui.QIcon(browseIcon))
        self.btn_browse.setObjectName("btn_browse")
        self.btn_browse.clicked.connect(self.browseImage)

        self.label_2 = QtWidgets.QLabel(self.addRefAccountGB)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 28))
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
        self.le_fatherName = QtWidgets.QLineEdit(self.addRefAccountGB)
        self.le_fatherName.setEnabled(True)
        self.le_fatherName.setGeometry(QtCore.QRect(100, 50, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_fatherName.sizePolicy().hasHeightForWidth())
        self.le_fatherName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_fatherName.setFont(font)
        self.le_fatherName.setMaxLength(32)
        self.le_fatherName.setValidator(self.onlyChar)
        self.le_fatherName.setObjectName("le_fatherName")
        self.le_fatherName.returnPressed.connect(self.onEnterFatherName)

        self.te_address = QtWidgets.QTextEdit(self.addRefAccountGB)
        self.te_address.setGeometry(QtCore.QRect(100, 170, 200, 75))
        self.te_address.setObjectName("te_address")
        self.showRefAccountGB = QtWidgets.QGroupBox(self.centralwidget)
        self.showRefAccountGB.setGeometry(QtCore.QRect(330, 0, 1031, 681))
        self.showRefAccountGB.setObjectName("showRefAccountGB")

        self.tbl_refAccount = QtWidgets.QTableWidget(self.showRefAccountGB)
        self.tbl_refAccount.setGeometry(QtCore.QRect(10, 60, 1010, 615))
        self.tbl_refAccount.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_refAccount.setRowCount(19)
        self.tbl_refAccount.setColumnCount(10)
        self.tbl_refAccount.setHorizontalHeaderLabels(['ID','Name', 'S/O', 'CNIC', 'Mobile','Gender','Address', 'Image', 'Setting', 'Remove'])
        self.tbl_refAccount.setColumnHidden(0, True)
        self.tbl_refAccount.setColumnWidth(1,150)
        self.tbl_refAccount.setColumnWidth(2,150)
        self.tbl_refAccount.setColumnWidth(6,130)
        self.tbl_refAccount.setColumnWidth(7,80)
        self.tbl_refAccount.setColumnWidth(8,80)
        self.tbl_refAccount.setColumnWidth(9,80)
        self.tbl_refAccount.setObjectName("tbl_refAccount")

        self.filterGB = QtWidgets.QGroupBox(self.showRefAccountGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 15, 1011, 41))
        self.filterGB.setObjectName("filterGB")
        self.le_filterByName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByName.setGeometry(QtCore.QRect(0, 15, 200, 20))
        self.le_filterByName.setObjectName("le_filterByName")
        self.le_filterByName.textChanged.connect(self.refAccountFilter)

        self.le_filterByFatherName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByFatherName.setGeometry(QtCore.QRect(200, 15, 200, 20))
        self.le_filterByFatherName.setObjectName("le_filterByFatherName")
        self.le_filterByFatherName.textChanged.connect(self.refAccountFilter)

        self.le_filterByCnic = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCnic.setGeometry(QtCore.QRect(400, 15, 100, 20))
        self.le_filterByCnic.setObjectName("le_filterByCnic")
        self.le_filterByCnic.textChanged.connect(self.refAccountFilter)

        self.le_filterByMobile = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByMobile.setGeometry(QtCore.QRect(500, 15, 100, 20))
        self.le_filterByMobile.setObjectName("le_filterByMobile")
        self.le_filterByMobile.textChanged.connect(self.refAccountFilter)

        self.le_filterByAddress = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByAddress.setGeometry(QtCore.QRect(700, 15, 100, 20))
        self.le_filterByAddress.setObjectName("le_filterByAddress")
        self.le_filterByAddress.textChanged.connect(self.refAccountFilter)

        self.le_filterByGender = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByGender.setGeometry(QtCore.QRect(600, 15, 100, 20))
        self.le_filterByGender.setObjectName("le_filterByGender")
        self.le_filterByGender.textChanged.connect(self.refAccountFilter)

        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(910, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getRefAccounts)

        refAccountWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(refAccountWindow)
        self.statusbar.setObjectName("statusbar")
        refAccountWindow.setStatusBar(self.statusbar)

        self.retranslateUi(refAccountWindow)
        QtCore.QMetaObject.connectSlotsByName(refAccountWindow)

    def retranslateUi(self, refAccountWindow):
        _translate = QtCore.QCoreApplication.translate
        refAccountWindow.setWindowTitle(_translate("refAccountWindow", "Reference Account Window"))
        self.addRefAccountGB.setTitle(_translate("refAccountWindow", "Add Reference Account"))
        self.le_name.setPlaceholderText(_translate("refAccountWindow", "Enter Name"))
        self.le_cnic.setPlaceholderText(_translate("refAccountWindow", "Enter CNIC"))
        self.le_cellNo.setPlaceholderText(_translate("refAccountWindow", "Enter Mobile No."))
        self.rb_male.setText(_translate("refAccountWindow", "Male"))
        self.rb_female.setText(_translate("refAccountWindow", "Female"))
        self.btn_capture.setText(_translate("refAccountWindow", "Capture"))
        self.label.setText(_translate("refAccountWindow", "Ref Name"))
        self.label_3.setText(_translate("refAccountWindow", "CNIC"))
        self.label_4.setText(_translate("refAccountWindow", "Mobile No"))
        self.label_5.setText(_translate("refAccountWindow", "Address"))
        self.label_8.setText(_translate("refAccountWindow", "Gender"))
        self.label_9.setText(_translate("refAccountWindow", "Picture"))
        self.btn_submit.setText(_translate("refAccountWindow", "Submit"))
        self.btn_cancel.setText(_translate("refAccountWindow", "Cancel"))
        self.btn_browse.setText(_translate("refAccountWindow", "Browse"))
        self.label_2.setText(_translate("refAccountWindow", "Father Name"))
        self.le_fatherName.setPlaceholderText(_translate("refAccountWindow", "Enter Father\'s Name"))
        self.te_address.setPlaceholderText(_translate("refAccountWindow", "Enter  Address"))
        self.showRefAccountGB.setTitle(_translate("refAccountWindow", "All Reference Account"))
        self.filterGB.setTitle(_translate("refAccountWindow", "Filter"))
        self.le_filterByName.setPlaceholderText(_translate("refAccountWindow", "Filter"))
        self.le_filterByFatherName.setPlaceholderText(_translate("refAccountWindow", "Filter"))
        self.le_filterByCnic.setPlaceholderText(_translate("refAccountWindow", "Filter"))
        self.le_filterByMobile.setPlaceholderText(_translate("refAccountWindow", "Filter"))
        self.le_filterByAddress.setPlaceholderText(_translate("refAccountWindow", "Filter"))
        self.le_filterByGender.setPlaceholderText(_translate("refAccountWindow", "Filter"))
        self.btn_refresh.setText(_translate("refAccountWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    refAccountWindow = QtWidgets.QMainWindow()
    ui = Ui_refAccountWindow()
    ui.refAccountSetupUi(refAccountWindow)
    refAccountWindow.show()
    sys.exit(app.exec_())

