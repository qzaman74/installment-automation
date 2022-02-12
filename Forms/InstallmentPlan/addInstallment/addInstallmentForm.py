# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addInstallmentForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from BLL.InstallmentsBL import addInstallmentBL
from PyQt5 import QtCore, QtGui, QtWidgets
from Globals import globalVariables,globalList
from Services.MiscService import dateTime

class Ui_addInstallmentWindow(object):
    _customerSchemeID = 0
    _accountID = 0

    def init(self):
        self.le_date.setText(self.calendar.selectedDate().toString())

    def showCalendar(self):
        if (self.calendar.isHidden()):
            self.calendar.show()
        else:
            self.calendar.hide()

    def setDate(self, date):
        self.le_date.setText(date.toString())
        self.calendar.hide()


    def onAccountTypeChange(self,text):
        if(self.cb_accountType.currentIndex()>0):
            self.setAccounts(text)
            self.cb_account.setFocus()

    def setAccounts(self,accountType):
        self.cb_account.clear()
        self.cb_account.addItem("",0)
        accountList = addInstallmentBL.getAccountByType(accountType)
        for id, name, mob in accountList:
            self.cb_account.addItem(mob+"-"+name,id)

    def onAccountChange(self):
        id = self.cb_account.currentData()
        if(self.cb_account.currentIndex() > 0):
            self.getSetAccountsinfo(id)
            self.setSchemeList(id)
            self._accountID = id
            self.cb_scheme.setFocus()
        else:
            self._accountID = 0
            self.le_name.setText('')
            self.le_fatherName.setText('')
            self.le_cnic.setText('')
            self.le_cellNo.setText('')
            self.te_address.setPlainText('')
            self.le_status.setText('')
            self.cb_scheme.setCurrentIndex(0)
            self.le_installment.setText('')
            self.te_remarks.setPlainText('')


    def getSetAccountsinfo(self,accountID):
        accountInfoList = addInstallmentBL.getAccountInfo(accountID)
        for x in accountInfoList:
            self._accountID = x[0]
            self.le_name.setText(x[2])
            self.le_fatherName.setText(x[3])
            self.le_cnic.setText(x[5])
            self.le_cellNo.setText(x[6])
            self.te_address.setText(x[8])
            self.le_status.setText(x[11])

    def setSchemeList(self,accountId):
        self.cb_scheme.clear()
        self.cb_scheme.addItem('SELECT')
        schemeList = addInstallmentBL.getSchemeList(accountId)
        for id, name in schemeList:
            self.cb_scheme.addItem(name,id)


    def onSchemeChange(self):
        id = self.cb_scheme.currentData()
        if(self.cb_scheme.currentIndex() > 0):
            self.setSchemeinfo(id)
            self._customerSchemeID = id
            self.showInstallmentHistory()
            self.le_installment.setFocus()
        else:
            self._customerSchemeID = 0
            self.le_installmentAmount.setText('')
            self.le_installments.setText('')

    def setSchemeinfo(self,customerSchemeID):
        schemeInfoList = addInstallmentBL.getSchemeInfo(customerSchemeID)
        for x in schemeInfoList:
            self.le_installments.setText(str(x[0]))
            self.le_installmentAmount.setText(str(x[1]))


    def showInstallmentHistory(self):
        try:
            _balance = 0
            result = addInstallmentBL.getInstallmentHistory(self._accountID, self._customerSchemeID)
            self.tbl_installment.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tbl_installment.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    if(colum_number == 0):
                        self.tbl_installment.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(dateTime.getDateWithoutTime(data)))
                    else:
                        self.tbl_installment.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                        if (colum_number == 1):
                            _balance = _balance + int(str(data))
            self.le_quickCount.setText(str(_balance))
        except:
            pass


    def onSubmit(self):
        date = self.le_date.text()
        name = self.le_name.text()
        cellno = self.le_cellNo.text()
        address = self.te_address.toPlainText()
        customerSchemeID = self._customerSchemeID
        scheme = self.cb_scheme.currentText()
        installment = self.le_installmentAmount.text()
        balance = self.le_quickCount.text()
        amount = self.le_installment.text()
        remarks = self.te_remarks.toPlainText()

        addInstallmentBL.validateAddInstallment(self, date, name, cellno, address,  customerSchemeID,  scheme,
                                           installment, balance, amount, remarks)





    def addInstallmentSetupUi(self, addInstallmentWindow):
        addInstallmentWindow.setObjectName("addInstallmentWindow")
        addInstallmentWindow.resize(1373, 723)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        addInstallmentWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        addInstallmentWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        addInstallmentWindow.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        charRegex=QtCore.QRegExp("[a-z-A-Z- -_]+")
        self.onlyChar = QtGui.QRegExpValidator(charRegex)
        
        self.centralwidget = QtWidgets.QWidget(addInstallmentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addInstallmentGB = QtWidgets.QGroupBox(self.centralwidget)
        self.addInstallmentGB.setGeometry(QtCore.QRect(10, 0, 311, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addInstallmentGB.sizePolicy().hasHeightForWidth())
        self.addInstallmentGB.setSizePolicy(sizePolicy)
        self.addInstallmentGB.setObjectName("addInstallmentGB")
        self.btn_submit = QtWidgets.QPushButton(self.addInstallmentGB)
        self.btn_submit.setGeometry(QtCore.QRect(100, 640, 100, 28))
        submitIcon = QtGui.QPixmap(globalVariables.Variables._icon+'rightIcon.png')
        self.btn_submit.setIcon(QtGui.QIcon(submitIcon))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.onSubmit)

        self.btn_cancel = QtWidgets.QPushButton(self.addInstallmentGB)
        self.btn_cancel.setGeometry(QtCore.QRect(200, 640, 100, 28))
        cancelIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cancelIcon.png')
        self.btn_cancel.setIcon(QtGui.QIcon(cancelIcon))
        self.btn_cancel.setObjectName("btn_cancel")

        self.label_11 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_11.setGeometry(QtCore.QRect(5, 340, 85, 28))
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
        self.le_installmentAmount = QtWidgets.QLineEdit(self.addInstallmentGB)
        self.le_installmentAmount.setEnabled(False)
        self.le_installmentAmount.setGeometry(QtCore.QRect(100, 370, 200, 28))
        self.le_installmentAmount.setObjectName("le_installmentAmount")
        self.te_remarks = QtWidgets.QTextEdit(self.addInstallmentGB)
        self.te_remarks.setEnabled(True)
        self.te_remarks.setGeometry(QtCore.QRect(100, 460, 200, 71))
        self.te_remarks.setObjectName("te_remarks")
        self.le_cellNo = QtWidgets.QLineEdit(self.addInstallmentGB)
        self.le_cellNo.setEnabled(False)
        self.le_cellNo.setGeometry(QtCore.QRect(100, 200, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cellNo.sizePolicy().hasHeightForWidth())
        self.le_cellNo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cellNo.setFont(font)
        self.le_cellNo.setMaxLength(11)
        self.le_cellNo.setObjectName("le_cellNo")
        self.le_installments = QtWidgets.QLineEdit(self.addInstallmentGB)
        self.le_installments.setEnabled(False)
        self.le_installments.setGeometry(QtCore.QRect(100, 400, 200, 28))
        self.le_installments.setObjectName("le_installments")
        self.le_name = QtWidgets.QLineEdit(self.addInstallmentGB)
        self.le_name.setEnabled(False)
        self.le_name.setGeometry(QtCore.QRect(100, 110, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_name.setFont(font)
        self.le_name.setMaxLength(32)
        self.le_name.setObjectName("le_name")
        self.le_cnic = QtWidgets.QLineEdit(self.addInstallmentGB)
        self.le_cnic.setEnabled(False)
        self.le_cnic.setGeometry(QtCore.QRect(100, 170, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cnic.sizePolicy().hasHeightForWidth())
        self.le_cnic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cnic.setFont(font)
        self.le_cnic.setMaxLength(13)
        self.le_cnic.setObjectName("le_cnic")
        self.cb_account = QtWidgets.QComboBox(self.addInstallmentGB)
        self.cb_account.setGeometry(QtCore.QRect(100, 80, 200, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_account.setFont(font)
        self.cb_account.setEditable(True)
        self.cb_account.setObjectName("cb_account")
        self.cb_account.activated[str].connect(self.onAccountChange)

        self.label_3 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_3.setGeometry(QtCore.QRect(5, 170, 85, 28))
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
        self.cb_scheme = QtWidgets.QComboBox(self.addInstallmentGB)
        self.cb_scheme.setGeometry(QtCore.QRect(100, 340, 200, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_scheme.setFont(font)
        self.cb_scheme.setEditable(False)
        self.cb_scheme.setObjectName("cb_scheme")
        self.cb_scheme.activated[str].connect(self.onSchemeChange)

        self.label_5 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_5.setGeometry(QtCore.QRect(5, 230, 85, 28))
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
        self.label_10 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_10.setGeometry(QtCore.QRect(5, 80, 85, 28))
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
        self.label_13 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_13.setGeometry(QtCore.QRect(5, 430, 85, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.le_installment = QtWidgets.QLineEdit(self.addInstallmentGB)
        self.le_installment.setGeometry(QtCore.QRect(100, 430, 200, 28))
        self.le_installment.setObjectName("le_installment")
        self.label_4 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_4.setGeometry(QtCore.QRect(5, 200, 85, 28))
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
        self.te_address = QtWidgets.QTextEdit(self.addInstallmentGB)
        self.te_address.setEnabled(False)
        self.te_address.setGeometry(QtCore.QRect(100, 230, 200, 71))
        self.te_address.setObjectName("te_address")
        self.label_6 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_6.setGeometry(QtCore.QRect(5, 460, 85, 28))
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
        self.label = QtWidgets.QLabel(self.addInstallmentGB)
        self.label.setGeometry(QtCore.QRect(5, 110, 85, 28))
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
        self.label_14 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_14.setGeometry(QtCore.QRect(5, 20, 85, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_15.setGeometry(QtCore.QRect(5, 305, 85, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.le_status = QtWidgets.QLineEdit(self.addInstallmentGB)
        self.le_status.setEnabled(False)
        self.le_status.setGeometry(QtCore.QRect(100, 305, 200, 28))
        self.le_status.setObjectName("le_status")
        self.le_date = QtWidgets.QLineEdit(self.addInstallmentGB)
        self.le_date.setEnabled(False)
        self.le_date.setGeometry(QtCore.QRect(100, 20, 170, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_date.sizePolicy().hasHeightForWidth())
        self.le_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_date.setFont(font)
        self.le_date.setMaxLength(32)
        self.le_date.setObjectName("le_date")
        self.btn_date = QtWidgets.QPushButton(self.addInstallmentGB)
        self.btn_date.setGeometry(QtCore.QRect(270, 20, 30, 28))
        dateIcon = QtGui.QPixmap(globalVariables.Variables._icon+'calendarIcon.png')
        self.btn_date.setIcon(QtGui.QIcon(dateIcon))
        self.btn_date.setObjectName("btn_date")
        self.btn_date.clicked.connect(self.showCalendar)

        self.label_12 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_12.setGeometry(QtCore.QRect(5, 370, 85, 28))
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
        self.label_16 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_16.setGeometry(QtCore.QRect(5, 400, 85, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_18.setGeometry(QtCore.QRect(5, 50, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.cb_accountType = QtWidgets.QComboBox(self.addInstallmentGB)
        self.cb_accountType.setGeometry(QtCore.QRect(100, 50, 200, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_accountType.setFont(font)
        self.cb_accountType.setEditable(False)
        self.cb_accountType.addItem('SELECT')
        self.cb_accountType.addItems(globalList.List._accountTypeList)
        self.cb_accountType.setObjectName("cb_accountType")
        self.cb_accountType.activated[str].connect(self.onAccountTypeChange)

        self.le_fatherName = QtWidgets.QLineEdit(self.addInstallmentGB)
        self.le_fatherName.setEnabled(False)
        self.le_fatherName.setGeometry(QtCore.QRect(100, 140, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_fatherName.sizePolicy().hasHeightForWidth())
        self.le_fatherName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_fatherName.setFont(font)
        self.le_fatherName.setMaxLength(32)
        self.le_fatherName.setObjectName("le_fatherName")
        self.label_2 = QtWidgets.QLabel(self.addInstallmentGB)
        self.label_2.setGeometry(QtCore.QRect(5, 140, 85, 28))
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
        self.calendar = QtWidgets.QCalendarWidget(self.addInstallmentGB)
        self.calendar.setGeometry(QtCore.QRect(0, 50, 312, 183))
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setMaximumDate(globalVariables.Variables._calendarMaxDate)
        self.calendar.setObjectName("calendar")
        self.calendar.hide()
        self.calendar.clicked[QtCore.QDate].connect(self.setDate)

        self.showInstallmentGB = QtWidgets.QGroupBox(self.centralwidget)
        self.showInstallmentGB.setGeometry(QtCore.QRect(330, 0, 1031, 681))
        self.showInstallmentGB.setObjectName("showInstallmentGB")
        
        self.tbl_installment = QtWidgets.QTableWidget(self.showInstallmentGB)
        self.tbl_installment.setGeometry(QtCore.QRect(10, 70, 1011, 601))
        self.tbl_installment.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_installment.setRowCount(19)
        self.tbl_installment.setColumnCount(4)
        self.tbl_installment.setHorizontalHeaderLabels(['Date','Amount','Balance', 'Remarks'])
        self.tbl_installment.setColumnWidth(0,80)
        self.tbl_installment.setColumnWidth(1,60)
        self.tbl_installment.setColumnWidth(2,60)
        self.tbl_installment.setColumnWidth(3,780)
        self.tbl_installment.setObjectName("tbl_installment")
        
        self.filterGB = QtWidgets.QGroupBox(self.showInstallmentGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 20, 1011, 41))
        self.filterGB.setObjectName("filterGB")
        self.le_filterByName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByName.setGeometry(QtCore.QRect(0, 20, 100, 20))
        self.le_filterByName.setObjectName("le_filterByName")
        self.le_filterByUserName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByUserName.setGeometry(QtCore.QRect(110, 20, 100, 20))
        self.le_filterByUserName.setObjectName("le_filterByUserName")
        self.le_filterByCnic = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCnic.setGeometry(QtCore.QRect(220, 20, 100, 20))
        self.le_filterByCnic.setObjectName("le_filterByCnic")
        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(910, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.showInstallmentHistory)

        self.label_17 = QtWidgets.QLabel(self.filterGB)
        self.label_17.setGeometry(QtCore.QRect(710, 10, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.le_quickCount = QtWidgets.QLineEdit(self.filterGB)
        self.le_quickCount.setEnabled(False)
        self.le_quickCount.setGeometry(QtCore.QRect(800, 10, 100, 28))
        self.le_quickCount.setObjectName("le_quickCount")
        addInstallmentWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addInstallmentWindow)
        self.statusbar.setObjectName("statusbar")
        addInstallmentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(addInstallmentWindow)
        QtCore.QMetaObject.connectSlotsByName(addInstallmentWindow)

    def retranslateUi(self, addInstallmentWindow):
        _translate = QtCore.QCoreApplication.translate
        addInstallmentWindow.setWindowTitle(_translate("addInstallmentWindow", "Add Installment Window"))
        self.addInstallmentGB.setTitle(_translate("addInstallmentWindow", "Add New Installment"))
        self.btn_submit.setText(_translate("addInstallmentWindow", "Submit"))
        self.btn_cancel.setText(_translate("addInstallmentWindow", "Cancel"))
        self.label_11.setText(_translate("addInstallmentWindow", "Scheme"))
        self.le_installmentAmount.setPlaceholderText(_translate("addInstallmentWindow", "Installment Amount"))
        self.te_remarks.setPlaceholderText(_translate("addInstallmentWindow", "Remarks"))
        self.le_cellNo.setPlaceholderText(_translate("addInstallmentWindow", "Mobile Number"))
        self.le_installments.setPlaceholderText(_translate("addInstallmentWindow", "Total Installments"))
        self.le_name.setPlaceholderText(_translate("addInstallmentWindow", "Account Name"))
        self.le_cnic.setPlaceholderText(_translate("addInstallmentWindow", "CNIC Number"))
        self.label_3.setText(_translate("addInstallmentWindow", "CNIC"))
        self.label_5.setText(_translate("addInstallmentWindow", "Address"))
        self.label_10.setText(_translate("addInstallmentWindow", "Account"))
        self.label_13.setText(_translate("addInstallmentWindow", "Amount"))
        self.le_installment.setPlaceholderText(_translate("addInstallmentWindow", "Paying Amount"))
        self.label_4.setText(_translate("addInstallmentWindow", "Cell No#"))
        self.te_address.setPlaceholderText(_translate("addInstallmentWindow", "Address"))
        self.label_6.setText(_translate("addInstallmentWindow", "Remarks"))
        self.label.setText(_translate("addInstallmentWindow", "Name"))
        self.label_14.setText(_translate("addInstallmentWindow", "Date"))
        self.label_15.setText(_translate("addInstallmentWindow", "Status"))
        self.le_status.setPlaceholderText(_translate("addInstallmentWindow", "Current Status"))
        self.label_12.setText(_translate("addInstallmentWindow", "Installment"))
        self.label_16.setText(_translate("addInstallmentWindow", "Installments"))
        self.label_18.setText(_translate("addInstallmentWindow", "Account Type"))
        self.le_fatherName.setPlaceholderText(_translate("addInstallmentWindow", "Father Name"))
        self.label_2.setText(_translate("addInstallmentWindow", "S/O"))
        self.showInstallmentGB.setTitle(_translate("addInstallmentWindow", "All Installments"))
        self.filterGB.setTitle(_translate("addInstallmentWindow", "Filter"))
        self.le_filterByName.setPlaceholderText(_translate("addInstallmentWindow", "Search"))
        self.le_filterByUserName.setPlaceholderText(_translate("addInstallmentWindow", "Search"))
        self.le_filterByCnic.setPlaceholderText(_translate("addInstallmentWindow", "Search"))
        self.btn_refresh.setText(_translate("addInstallmentWindow", "Refresh"))
        self.label_17.setText(_translate("addInstallmentWindow", "Quick Count :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addInstallmentWindow = QtWidgets.QMainWindow()
    ui = Ui_addInstallmentWindow()
    ui.addInstallmentSetupUi(addInstallmentWindow)
    addInstallmentWindow.show()
    sys.exit(app.exec_())
