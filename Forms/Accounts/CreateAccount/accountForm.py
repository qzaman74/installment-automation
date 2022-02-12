
from BLL.AccountsBL import accountFormBL
from Services.ImgService import camera,image,browseImage
from Services.ResetServices import formReset

from Globals import globalVariables,globalList
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton


class Ui_accountWindow(object):
    _imageCode = ''
    _filterList = []

    def init(self):
        self.getAccounts()


    def captureImage(self):
        base64Img = camera.capture()
        self._imageCode = base64Img
        self.lbl_image.setPixmap(image.getPixmap(base64Img))

    def browseImage(self):
        base64Img = browseImage.getImagePath(self.__init__())
        self._imageCode = base64Img
        self.lbl_image.setPixmap(image.getPixmap(base64Img))


    def onSubmitAccount(self):
        name = self.le_name.text()
        fatherName = self.le_fatherName.text()
        cnic = self.le_cnic.text()
        mobileNo = self.le_cellNo.text()

        gender = globalVariables.Variables._male

        if(self.rb_female.isChecked()):
            gender = globalVariables.Variables._female

        address = self.te_address.toPlainText()
        accountType = self.cb_type.currentText()
        accountStatus = self.cb_status.currentText()
        balance = self.le_balance.text()

        imageCode = self._imageCode

        formReset.Reset._resetAccountForm = self.onCancel

        accountFormBL.validateAccount(self, name, fatherName, cnic, mobileNo, gender, address, accountType,
                                      accountStatus, balance, imageCode,self._filterList)



    def onCancel(self):
        self.le_name.setText('')
        self.le_fatherName.setText('')
        self.le_cnic.setText('')
        self.le_cellNo.setText('')
        self.le_balance.setText('0')
        self.te_address.setPlainText('')
        self.rb_male.setChecked(True)
        self.cb_status.setCurrentIndex(0)
        self.cb_type.setCurrentIndex(0)
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'user.png'))
        self.getAccounts()



    def showImage(self):
        try:
            button = self.tbl_account.sender()
            index = self.tbl_account.indexAt(button.pos())
            if index.isValid():
                accountID = self.tbl_account.model().index(index.row(), 0).data()
                accountFormBL.validateImage(self, accountID)
        except:
            pass

    def editAccount(self):
        button = self.tbl_account.sender()
        index = self.tbl_account.indexAt(button.pos())
        if index.isValid():
            accountID = self.tbl_account.model().index(index.row(), 0).data()
            accountFormBL.validateUpdate(self, accountID)

    def removeAccount(self):
        button = self.tbl_account.sender()
        index = self.tbl_account.indexAt(button.pos())
        if index.isValid():
            accountID = self.tbl_account.model().index(index.row(), 0).data()
            name = self.tbl_account.model().index(index.row(), 1).data()
            accountFormBL.deleteAccount(self, accountID, name)

    def getAccounts(self):
        result = accountFormBL.getAllAccounts()
        self.showAccouts(result)
        self._filterList = accountFormBL.getAllAccounts().fetchall().copy()



    def showAccouts(self,result):
        self.tbl_account.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_account.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tbl_account.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data).upper()))

                self.btn_image = QPushButton('Image')
                imageIcon = QtGui.QPixmap(globalVariables.Variables._icon+'imageIcon.png')
                self.btn_image.setIcon(QtGui.QIcon(imageIcon))
                self.tbl_account.setCellWidget(row_number, 9, self.btn_image)
                self.btn_image.clicked.connect(self.showImage)

                self.btn_edit = QPushButton('Setting')
                settingIcon = QtGui.QPixmap(globalVariables.Variables._icon+'settingIcon.png')
                self.btn_edit.setIcon(QtGui.QIcon(settingIcon))
                self.tbl_account.setCellWidget(row_number, 10, self.btn_edit)
                self.btn_edit.clicked.connect(self.editAccount)

                self.btn_remove = QPushButton('Delete')
                removeIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
                self.btn_remove.setIcon(QtGui.QIcon(removeIcon))
                self.tbl_account.setCellWidget(row_number, 11, self.btn_remove)
                self.btn_remove.clicked.connect(self.removeAccount)

        if(self.tbl_account.rowCount() < 19):
            self.tbl_account.setRowCount(19)


    def filterFunc(self,item):
        name = self.le_filterByName.text()
        fatherName = self.le_filterByFatherName.text()
        cnic = self.le_filterByCnic.text()
        mobile = self.le_filterByMobile.text()
        address = self.le_filterByAddress.text()
        _type = self.le_filterByType.text()
        status = self.le_filterByStatus.text()
        balance = self.le_filterByBalance.text()

        if (str(item[1].lower()).startswith(name) and str(item[2].lower()).startswith(fatherName) and
            str(item[3]).startswith(cnic) and str(item[4]).startswith(mobile)  and
            str(item[5].lower()).startswith(address) and str(item[6].lower()).startswith(_type) and
            str(item[7].lower()).startswith(status) and str(item[8]).startswith(balance) ):
            return True
        else:
            return False

    def accountFilter(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.showAccouts(result)


    def onEnterName(self):
        self.le_fatherName.setFocus()

    def onEnterFatherName(self):
        self.le_cnic.setFocus()

    def onEnterCNIC(self):
        self.le_cellNo.setFocus()

    def onEnterCellNo(self):
        self.te_address.setFocus()

    def onEnterBalance(self):
        self.cb_type.setFocus()

    def onChangeType(self):
        self.cb_status.setFocus()

    def onChangeStutus(self):
        self.btn_submit.setFocus()


    def accountSetupUi(self, accountWindow):
        accountWindow.setObjectName("accountWindow")
        accountWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        accountWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        accountWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        accountWindow.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        charRegex=QtCore.QRegExp("[a-z-A-Z _]+")
        self.onlyChar = QtGui.QRegExpValidator(charRegex)

        self.centralwidget = QtWidgets.QWidget(accountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addAccountGB = QtWidgets.QGroupBox(self.centralwidget)
        self.addAccountGB.setGeometry(QtCore.QRect(10, 0, 311, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addAccountGB.sizePolicy().hasHeightForWidth())
        self.addAccountGB.setSizePolicy(sizePolicy)
        self.addAccountGB.setObjectName("addAccountGB")

        self.le_name = QtWidgets.QLineEdit(self.addAccountGB)
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

        self.le_fatherName = QtWidgets.QLineEdit(self.addAccountGB)
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

        self.le_cnic = QtWidgets.QLineEdit(self.addAccountGB)
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
        self.le_cnic.returnPressed.connect(self.onEnterCNIC)

        self.le_cellNo = QtWidgets.QLineEdit(self.addAccountGB)
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

        self.rb_male = QtWidgets.QRadioButton(self.addAccountGB)
        self.rb_male.setGeometry(QtCore.QRect(100, 140, 51, 28))
        self.rb_male.setChecked(True)
        self.rb_male.setObjectName("rb_male")
        self.rb_female = QtWidgets.QRadioButton(self.addAccountGB)
        self.rb_female.setGeometry(QtCore.QRect(160, 140, 61, 28))
        self.rb_female.setObjectName("rb_female")

        self.lbl_image = QtWidgets.QLabel(self.addAccountGB)
        self.lbl_image.setGeometry(QtCore.QRect(100, 350, 200, 201))
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'user.png'))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")

        self.btn_capture = QtWidgets.QPushButton(self.addAccountGB)
        self.btn_capture.setGeometry(QtCore.QRect(200, 570, 100, 28))
        captureIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cameraIcon.png')
        self.btn_capture.setIcon(QtGui.QIcon(captureIcon))
        self.btn_capture.setObjectName("btn_capture")
        # self.btn_capture.clicked.connect(self.captureImage)

        self.btn_browse = QtWidgets.QPushButton(self.addAccountGB)
        self.btn_browse.setGeometry(QtCore.QRect(100, 570, 100, 28))
        browseIcon = QtGui.QPixmap(globalVariables.Variables._icon+'browseIcon.png')
        self.btn_browse.setIcon(QtGui.QIcon(browseIcon))
        self.btn_browse.setObjectName("btn_browse")
        # self.btn_browse.clicked.connect(self.browseImage)

        self.btn_submit = QtWidgets.QPushButton(self.addAccountGB)
        self.btn_submit.setGeometry(QtCore.QRect(100, 640, 100, 28))
        submitIcon = QtGui.QPixmap(globalVariables.Variables._icon+'rightIcon.png')
        self.btn_submit.setIcon(QtGui.QIcon(submitIcon))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.onSubmitAccount)

        self.btn_cancel = QtWidgets.QPushButton(self.addAccountGB)
        self.btn_cancel.setGeometry(QtCore.QRect(200, 640, 100, 28))
        cancelIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cancelIcon.png')
        self.btn_cancel.setIcon(QtGui.QIcon(cancelIcon))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.onCancel)

        self.label = QtWidgets.QLabel(self.addAccountGB)
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
        self.label_3 = QtWidgets.QLabel(self.addAccountGB)
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
        self.label_4 = QtWidgets.QLabel(self.addAccountGB)
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
        self.label_5 = QtWidgets.QLabel(self.addAccountGB)
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
        self.label_8 = QtWidgets.QLabel(self.addAccountGB)
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
        self.label_9 = QtWidgets.QLabel(self.addAccountGB)
        self.label_9.setGeometry(QtCore.QRect(10, 345, 71, 28))
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
        self.label_11 = QtWidgets.QLabel(self.addAccountGB)
        self.label_11.setGeometry(QtCore.QRect(10, 310, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.cb_status = QtWidgets.QComboBox(self.addAccountGB)
        self.cb_status.setGeometry(QtCore.QRect(100, 310, 200, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_status.setFont(font)
        self.cb_status.setObjectName("cb_status")
        self.cb_status.addItems(globalList.List._accountStatusList)
        self.cb_status.activated.connect(self.onChangeStutus)

        self.label_10 = QtWidgets.QLabel(self.addAccountGB)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.cb_type = QtWidgets.QComboBox(self.addAccountGB)
        self.cb_type.setGeometry(QtCore.QRect(100, 280, 200, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_type.setFont(font)
        self.cb_type.setObjectName("cb_type")
        self.cb_type.addItems(globalList.List._accountTypeList)
        self.cb_type.activated.connect(self.onChangeType)

        self.le_balance = QtWidgets.QLineEdit(self.addAccountGB)
        self.le_balance.setGeometry(QtCore.QRect(100, 250, 200, 28))
        self.le_balance.setText("0")
        self.le_balance.setValidator(self.onlyInt)
        self.le_balance.setObjectName("le_balance")
        self.le_balance.returnPressed.connect(self.onEnterBalance)

        self.label_12 = QtWidgets.QLabel(self.addAccountGB)
        self.label_12.setGeometry(QtCore.QRect(10, 250, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_2 = QtWidgets.QLabel(self.addAccountGB)
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

        self.te_address = QtWidgets.QTextEdit(self.addAccountGB)
        self.te_address.setGeometry(QtCore.QRect(100, 170, 200, 75))
        self.te_address.setObjectName("te_address")

        self.showAccountGB = QtWidgets.QGroupBox(self.centralwidget)
        self.showAccountGB.setGeometry(QtCore.QRect(330, 0, 1031, 681))
        self.showAccountGB.setObjectName("showAccountGB")

        self.tbl_account = QtWidgets.QTableWidget(self.showAccountGB)
        self.tbl_account.setGeometry(QtCore.QRect(10, 60, 1010, 615))
        self.tbl_account.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_account.setRowCount(19)
        self.tbl_account.setColumnCount(12)
        self.tbl_account.setHorizontalHeaderLabels(['ID','Name', 'S/O', 'CNIC', 'Mobile','Address', 'Type', 'Status',
                                                    'Balance', 'Image', 'Setting', 'Remove'])
        self.tbl_account.setColumnHidden(0, True)
        self.tbl_account.setColumnWidth(5,140)
        self.tbl_account.setColumnWidth(6,70)
        self.tbl_account.setColumnWidth(7,60)
        self.tbl_account.setColumnWidth(8,70)
        self.tbl_account.setColumnWidth(9,80)
        self.tbl_account.setColumnWidth(10,80)
        self.tbl_account.setColumnWidth(11,80)
        self.tbl_account.setObjectName("tbl_account")

        self.filterGB = QtWidgets.QGroupBox(self.showAccountGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 15, 1011, 41))
        self.filterGB.setObjectName("filterGB")
        self.le_filterByName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByName.setGeometry(QtCore.QRect(25, 20, 100, 20))
        self.le_filterByName.setValidator(self.onlyChar)
        self.le_filterByName.setObjectName("le_filterByName")
        self.le_filterByName.textChanged.connect(self.accountFilter)

        self.le_filterByFatherName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByFatherName.setGeometry(QtCore.QRect(125, 20, 100, 20))
        self.le_filterByFatherName.setValidator(self.onlyChar)
        self.le_filterByFatherName.setObjectName("le_filterByFatherName")
        self.le_filterByFatherName.textChanged.connect(self.accountFilter)

        self.le_filterByCnic = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCnic.setGeometry(QtCore.QRect(225, 20, 100, 20))
        self.le_filterByCnic.setValidator(self.onlyInt)
        self.le_filterByCnic.setObjectName("le_filterByCnic")
        self.le_filterByCnic.textChanged.connect(self.accountFilter)

        self.le_filterByMobile = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByMobile.setGeometry(QtCore.QRect(325, 20, 100, 20))
        self.le_filterByMobile.setObjectName("le_filterByMobile")
        self.le_filterByMobile.setValidator(self.onlyInt)
        self.le_filterByMobile.textChanged.connect(self.accountFilter)

        self.le_filterByAddress = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByAddress.setGeometry(QtCore.QRect(425, 20, 145, 20))
        self.le_filterByAddress.setObjectName("le_filterByAddress")
        self.le_filterByAddress.textChanged.connect(self.accountFilter)

        self.le_filterByType = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByType.setGeometry(QtCore.QRect(570, 20, 70, 20))
        self.le_filterByType.setValidator(self.onlyChar)
        self.le_filterByType.setObjectName("le_filterByType")
        self.le_filterByType.textChanged.connect(self.accountFilter)

        self.le_filterByStatus = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByStatus.setGeometry(QtCore.QRect(640, 20, 55, 20))
        self.le_filterByStatus.setValidator(self.onlyChar)
        self.le_filterByStatus.setObjectName("le_filterByStatus")
        self.le_filterByStatus.textChanged.connect(self.accountFilter)

        self.le_filterByBalance = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByBalance.setGeometry(QtCore.QRect(695, 20, 80, 20))
        self.le_filterByBalance.setValidator(self.onlyInt)
        self.le_filterByBalance.setObjectName("le_filterByBalance")
        self.le_filterByBalance.textChanged.connect(self.accountFilter)

        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(910, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getAccounts)

        accountWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(accountWindow)
        self.statusbar.setObjectName("statusbar")
        accountWindow.setStatusBar(self.statusbar)

        self.retranslateUi(accountWindow)
        QtCore.QMetaObject.connectSlotsByName(accountWindow)

    def retranslateUi(self, accountWindow):
        _translate = QtCore.QCoreApplication.translate
        accountWindow.setWindowTitle(_translate("accountWindow", "Account Window"))
        self.addAccountGB.setTitle(_translate("accountWindow", "Add New Account"))
        self.le_name.setPlaceholderText(_translate("accountWindow", "Enter Name"))
        self.le_cnic.setPlaceholderText(_translate("accountWindow", "Enter CNIC"))
        self.le_cellNo.setPlaceholderText(_translate("accountWindow", "Enter Mobile No."))
        self.rb_male.setText(_translate("accountWindow", "Male"))
        self.rb_female.setText(_translate("accountWindow", "Female"))
        self.btn_capture.setText(_translate("accountWindow", "Capture"))
        self.label.setText(_translate("accountWindow", "Name"))
        self.label_3.setText(_translate("accountWindow", "CNIC"))
        self.label_4.setText(_translate("accountWindow", "Mobile No"))
        self.label_5.setText(_translate("accountWindow", "Address"))
        self.label_8.setText(_translate("accountWindow", "Gender"))
        self.label_9.setText(_translate("accountWindow", "Picture"))
        self.btn_submit.setText(_translate("accountWindow", "Submit"))
        self.btn_cancel.setText(_translate("accountWindow", "Cancel"))
        self.label_11.setText(_translate("accountWindow", "Status"))
        self.label_10.setText(_translate("accountWindow", "Type"))
        self.le_balance.setPlaceholderText(_translate("accountWindow", "Enter Balance"))
        self.label_12.setText(_translate("accountWindow", "Balance"))
        self.btn_browse.setText(_translate("accountWindow", "Browse"))
        self.label_2.setText(_translate("accountWindow", "Father Name"))
        self.le_fatherName.setPlaceholderText(_translate("accountWindow", "Enter Father\'s Name"))
        self.te_address.setPlaceholderText(_translate("accountWindow", "Enter  Address"))
        self.showAccountGB.setTitle(_translate("accountWindow", "All Account"))
        self.filterGB.setTitle(_translate("accountWindow", "Filter Account"))
        self.le_filterByName.setPlaceholderText(_translate("accountWindow", "Filter"))
        self.le_filterByFatherName.setPlaceholderText(_translate("accountWindow", "Filter"))
        self.le_filterByCnic.setPlaceholderText(_translate("accountWindow", "Filter"))
        self.le_filterByMobile.setPlaceholderText(_translate("accountWindow", "Filter"))
        self.le_filterByAddress.setPlaceholderText(_translate("accountWindow", "Filter"))
        self.le_filterByType.setPlaceholderText(_translate("accountWindow", "Filter"))
        self.le_filterByStatus.setPlaceholderText(_translate("accountWindow", "Filter"))
        self.le_filterByBalance.setPlaceholderText(_translate("accountWindow", "Filter"))
        self.btn_refresh.setText(_translate("accountWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    accountWindow = QtWidgets.QMainWindow()
    ui = Ui_accountWindow()
    ui.accountSetupUi(accountWindow)
    accountWindow.show()
    sys.exit(app.exec_())

