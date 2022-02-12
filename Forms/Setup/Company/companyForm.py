
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton)
from Globals import globalList,globalVariables
from Services.ImgService import camera, image, browseImage
from Services.ResetServices import formReset
from BLL.SetupBL import companyBL

class Ui_companyWindow(object):
    _imageCode = ''
    _companyList = None

    def init(self):
        self.getCompany()
        
    def onSubmit(self):
        name = self.le_name.text()
        code = self.le_code.text()
        agent = self.le_agent.text()
        contact = self.le_contact.text()
        location = self.le_location.text()
        imageCode = self._imageCode
        companyList = self._companyList

        formReset.Reset._resetCompanyForm = self.onCancel
        companyBL.validateCompany(self,name,code,agent,contact,location, imageCode,companyList)



    def onCancel(self):
        self.le_name.setText('')
        self.le_code.setText('')
        self.le_agent.setText('')
        self.le_contact.setText('')
        self.le_location.setText('')
        self.getCompany()

    def capture(self):
        try:
            base64Img = camera.capture()
            self._imageCode = base64Img
            self.lbl_image.setPixmap(image.getPixmap(base64Img))
        except:
            pass

    def browse(self):
        try:
            base64Img = browseImage.getImagePath(self.__init__())
            self._imageCode = base64Img
            self.lbl_image.setPixmap(image.getPixmap(base64Img))
        except:
            pass


    def showImage(self):
        try:
            button = self.tbl_company.sender()
            index = self.tbl_company.indexAt(button.pos())
            if index.isValid():
                companyID = self.tbl_company.model().index(index.row(), 0).data()
                companyBL.validateImage(self, companyID)
        except:
            pass

    def editCompany(self):
        button = self.tbl_company.sender()
        index = self.tbl_company.indexAt(button.pos())
        if index.isValid():
            companyID = self.tbl_company.model().index(index.row(), 0).data()
            companyBL.validateUpdate(self, companyID)

    def removeCompany(self):
        button = self.tbl_company.sender()
        index = self.tbl_company.indexAt(button.pos())
        if index.isValid():
            companyID = self.tbl_company.model().index(index.row(), 0).data()
            name = self.tbl_company.model().index(index.row(), 1).data()
            companyBL.validateRemove(self, companyID, name)

    def getCompany(self):
        result = companyBL.getCompanies()
        self._companyList = companyBL.getCompanies().fetchall().copy()
        self.showCompany(result)


    def showCompany(self,result):
        self.tbl_company.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_company.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tbl_company.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data).upper()))

                self.btn_image = QPushButton('Image')
                imageIcon = QtGui.QPixmap(globalVariables.Variables._icon+'imageIcon.png')
                self.btn_image.setIcon(QtGui.QIcon(imageIcon))
                self.tbl_company.setCellWidget(row_number,6, self.btn_image)
                self.btn_image.clicked.connect(self.showImage)

                self.btn_edit = QPushButton('Edit')
                settingIcon = QtGui.QPixmap(globalVariables.Variables._icon+'settingIcon.png')
                self.btn_edit.setIcon(QtGui.QIcon(settingIcon))
                self.tbl_company.setCellWidget(row_number,7, self.btn_edit)
                self.btn_edit.clicked.connect(self.editCompany)

                self.btn_delete = QPushButton('Delete')
                deleteIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
                self.btn_delete.setIcon(QtGui.QIcon(deleteIcon))
                self.tbl_company.setCellWidget(row_number,8, self.btn_delete)
                self.btn_delete.clicked.connect(self.removeCompany)

    def onEnterName(self):
        self.le_code.setFocus()

    def onEnterCode(self):
        self.le_agent.setFocus()

    def onEnterAgent(self):
        self.le_contact.setFocus()

    def onEnterContact(self):
        self.le_location.setFocus()

    def onEnterLocatiton(self):
        self.onSubmit()



    def filterFunc(self,item):
        name = self.le_filterByCompanyName.text()
        code = self.le_filterByCompanyCode.text()
        agent = self.le_filterByCompanyRep.text()
        contact = self.le_filterByCompanyContact.text()
        location = self.le_filterByCompanyLocation.text()

        if (str(item[1].lower()).startswith(name) and str(item[2].lower()).startswith(code) and
            str(item[3].lower()).startswith(agent) and str(item[4].lower()).startswith(contact)  and
            str(item[5].lower()).startswith(location)  ):
            return True
        else:
            return False

    def nameFilter(self):
        result = list(filter(self.filterFunc, self._companyList))
        self.showCompany(result)


        
    def companySetupUi(self, companyWindow):
        companyWindow.setObjectName("companyWindow")
        companyWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        companyWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        companyWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        companyWindow.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        charRegex=QtCore.QRegExp("[a-z-A-Z _]+")
        self.onlyChar = QtGui.QRegExpValidator(charRegex)

        self.centralwidget = QtWidgets.QWidget(companyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addCompanyGB = QtWidgets.QGroupBox(self.centralwidget)
        self.addCompanyGB.setGeometry(QtCore.QRect(10, 0, 291, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addCompanyGB.sizePolicy().hasHeightForWidth())
        self.addCompanyGB.setSizePolicy(sizePolicy)
        self.addCompanyGB.setObjectName("addCompanyGB")
        self.le_name = QtWidgets.QLineEdit(self.addCompanyGB)
        self.le_name.setEnabled(True)
        self.le_name.setGeometry(QtCore.QRect(80, 30, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_name.setFont(font)
        self.le_name.setPlaceholderText("Enter Company Name")
        self.le_name.setMaxLength(32)
        self.le_name.setValidator(self.onlyChar)
        self.le_name.setObjectName("le_name")
        self.le_name.returnPressed.connect(self.onEnterName)

        self.label_6 = QtWidgets.QLabel(self.addCompanyGB)
        self.label_6.setGeometry(QtCore.QRect(10, 65, 65, 28))
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
        self.label_5 = QtWidgets.QLabel(self.addCompanyGB)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 65, 28))
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
        self.le_code = QtWidgets.QLineEdit(self.addCompanyGB)
        self.le_code.setEnabled(True)
        self.le_code.setGeometry(QtCore.QRect(80, 65, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_code.sizePolicy().hasHeightForWidth())
        self.le_code.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_code.setFont(font)
        self.le_code.setPlaceholderText("Enter Company Code")
        self.le_code.setMaxLength(32)
        self.le_code.setValidator(self.onlyInt)
        self.le_code.setObjectName("le_code")
        self.le_code.returnPressed.connect(self.onEnterCode)

        self.le_agent = QtWidgets.QLineEdit(self.addCompanyGB)
        self.le_agent.setEnabled(True)
        self.le_agent.setGeometry(QtCore.QRect(80, 100, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_agent.sizePolicy().hasHeightForWidth())
        self.le_agent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_agent.setFont(font)
        self.le_agent.setPlaceholderText("Enter Representative")
        self.le_agent.setMaxLength(32)
        self.le_agent.setValidator(self.onlyChar)
        self.le_agent.setObjectName("le_agent")
        self.le_agent.returnPressed.connect(self.onEnterAgent)

        self.label_7 = QtWidgets.QLabel(self.addCompanyGB)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 65, 28))
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
        self.le_contact = QtWidgets.QLineEdit(self.addCompanyGB)
        self.le_contact.setEnabled(True)
        self.le_contact.setGeometry(QtCore.QRect(80, 135, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_contact.sizePolicy().hasHeightForWidth())
        self.le_contact.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_contact.setFont(font)
        self.le_contact.setPlaceholderText("Enter Compnay Contact")
        self.le_contact.setMaxLength(11)
        self.le_contact.setValidator(self.onlyInt)
        self.le_contact.setObjectName("le_contact")
        self.le_contact.returnPressed.connect(self.onEnterContact)

        self.label_8 = QtWidgets.QLabel(self.addCompanyGB)
        self.label_8.setGeometry(QtCore.QRect(10, 135, 65, 28))
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

        # self.cb_location = QtWidgets.QComboBox(self.addCompanyGB)
        # self.cb_location.setGeometry(QtCore.QRect(80, 170, 200, 28))
        # self.cb_location.addItems(globalList.List._cityList)
        # self.cb_location.setObjectName("cb_location")

        self.le_location = QtWidgets.QLineEdit(self.addCompanyGB)
        self.le_location.setGeometry(QtCore.QRect(80, 170, 200, 28))
        self.le_location.setPlaceholderText("Enter Company Location")
        self.le_location.setMaxLength(32)
        self.le_location.setValidator(self.onlyChar)
        self.le_location.setObjectName("le_location")
        self.le_location.returnPressed.connect(self.onEnterLocatiton)

        self.label_9 = QtWidgets.QLabel(self.addCompanyGB)
        self.label_9.setGeometry(QtCore.QRect(10, 170, 65, 28))
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
        self.lbl_image = QtWidgets.QLabel(self.addCompanyGB)
        self.lbl_image.setGeometry(QtCore.QRect(80, 220, 200, 200))
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'user.png'))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")
        self.label_10 = QtWidgets.QLabel(self.addCompanyGB)
        self.label_10.setGeometry(QtCore.QRect(10, 210, 65, 28))
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
        self.btn_capture = QtWidgets.QPushButton(self.addCompanyGB)
        self.btn_capture.setGeometry(QtCore.QRect(180, 440, 100, 28))
        captureIcon = QtGui.QPixmap(globalVariables.Variables._icon+'captureIcon.png')
        self.btn_capture.setIcon(QtGui.QIcon(captureIcon))
        self.btn_capture.setObjectName("btn_capture")
        # self.btn_capture.clicked.connect(self.capture)

        self.btn_submit = QtWidgets.QPushButton(self.addCompanyGB)
        self.btn_submit.setGeometry(QtCore.QRect(80, 640, 100, 28))
        submitIcon = QtGui.QPixmap(globalVariables.Variables._icon+'rightIcon.png')
        self.btn_submit.setIcon(QtGui.QIcon(submitIcon))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.onSubmit)
        
        self.btn_cancel = QtWidgets.QPushButton(self.addCompanyGB)
        self.btn_cancel.setGeometry(QtCore.QRect(180, 640, 100, 28))
        cancelIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cancelIcon.png')
        self.btn_cancel.setIcon(QtGui.QIcon(cancelIcon))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.onCancel)
        self.btn_browse = QtWidgets.QPushButton(self.addCompanyGB)
        self.btn_browse.setGeometry(QtCore.QRect(80, 440, 100, 28))
        browseIcon = QtGui.QPixmap(globalVariables.Variables._icon+'browseIcon.png')
        self.btn_browse.setIcon(QtGui.QIcon(browseIcon))
        self.btn_browse.setObjectName("btn_browse")
        # self.btn_browse.clicked.connect(self.browse)

        self.companyGB = QtWidgets.QGroupBox(self.centralwidget)
        self.companyGB.setGeometry(QtCore.QRect(310, 0, 1051, 681))
        self.companyGB.setObjectName("companyGB")

        self.tbl_company = QtWidgets.QTableWidget(self.companyGB)
        self.tbl_company.setGeometry(QtCore.QRect(10, 60, 1031, 611))
        self.tbl_company.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_company.setRowCount(19)
        self.tbl_company.setColumnCount(9)
        self.tbl_company.setHorizontalHeaderLabels(['ID', 'Company', 'Code', 'Representative', 'Contact',
                                                    'Location', 'Image', 'Setting','Remove'])
        self.tbl_company.setColumnHidden(0, True)
        self.tbl_company.setColumnWidth(1,175)
        self.tbl_company.setColumnWidth(3,160)
        self.tbl_company.setColumnWidth(5,175)
        self.tbl_company.setObjectName("tbl_company")

        self.filterGB = QtWidgets.QGroupBox(self.companyGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 15, 1031, 41))
        self.filterGB.setObjectName("filterGB")

        self.le_filterByCompanyName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompanyName.setGeometry(QtCore.QRect(0, 20, 195, 20))
        self.le_filterByCompanyName.setPlaceholderText("Filter BY Company")
        self.le_filterByCompanyName.setValidator(self.onlyChar)
        self.le_filterByCompanyName.setObjectName("le_filterByCompanyName")
        self.le_filterByCompanyName.textChanged.connect(self.nameFilter)

        self.le_filterByCompanyCode = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompanyCode.setGeometry(QtCore.QRect(195, 20, 100, 20))
        self.le_filterByCompanyCode.setPlaceholderText("Filter BY Code")
        self.le_filterByCompanyCode.setValidator(self.onlyInt)
        self.le_filterByCompanyCode.setObjectName("le_filterByCompanyCode")
        self.le_filterByCompanyCode.textChanged.connect(self.nameFilter)

        self.le_filterByCompanyRep = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompanyRep.setGeometry(QtCore.QRect(295, 20, 160, 20))
        self.le_filterByCompanyRep.setPlaceholderText("Filter BY Agent")
        self.le_filterByCompanyRep.setValidator(self.onlyChar)
        self.le_filterByCompanyRep.setObjectName("le_filterByCompanyRep")
        self.le_filterByCompanyRep.textChanged.connect(self.nameFilter)

        self.le_filterByCompanyContact = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompanyContact.setGeometry(QtCore.QRect(455, 20, 100, 20))
        self.le_filterByCompanyContact.setPlaceholderText("Filter BY Contact")
        self.le_filterByCompanyContact.setValidator(self.onlyInt)
        self.le_filterByCompanyContact.setObjectName("le_filterByCompanyContact")
        self.le_filterByCompanyContact.textChanged.connect(self.nameFilter)

        self.le_filterByCompanyLocation = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompanyLocation.setGeometry(QtCore.QRect(555, 20, 175, 20))
        self.le_filterByCompanyLocation.setPlaceholderText("Filter BY Location")
        self.le_filterByCompanyLocation.setValidator(self.onlyChar)
        self.le_filterByCompanyLocation.setObjectName("le_filterByCompanyLocation")
        self.le_filterByCompanyLocation.textChanged.connect(self.nameFilter)

        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(930, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getCompany)

        companyWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(companyWindow)
        self.statusbar.setObjectName("statusbar")
        companyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(companyWindow)
        QtCore.QMetaObject.connectSlotsByName(companyWindow)

    def retranslateUi(self, companyWindow):
        _translate = QtCore.QCoreApplication.translate
        companyWindow.setWindowTitle(_translate("companyWindow", "Company Window"))
        self.addCompanyGB.setTitle(_translate("companyWindow", "Add New Company"))
        self.label_6.setText(_translate("companyWindow", "Code"))
        self.label_5.setText(_translate("companyWindow", "Name"))
        self.label_7.setText(_translate("companyWindow", "Agent"))
        self.label_8.setText(_translate("companyWindow", "Contact"))
        self.label_9.setText(_translate("companyWindow", "Location"))
        self.label_10.setText(_translate("companyWindow", " Image"))
        self.btn_capture.setText(_translate("companyWindow", "Capture"))
        self.btn_submit.setText(_translate("companyWindow", "Submit"))
        self.btn_cancel.setText(_translate("companyWindow", "Cancel"))
        self.btn_browse.setText(_translate("companyWindow", "Browse"))
        self.companyGB.setTitle(_translate("companyWindow", "All Companies"))
        self.filterGB.setTitle(_translate("companyWindow", "Filter Company"))
        self.btn_refresh.setText(_translate("companyWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    companyWindow = QtWidgets.QMainWindow()
    ui = Ui_companyWindow()
    ui.setupUi(companyWindow)
    companyWindow.show()
    sys.exit(app.exec_())

