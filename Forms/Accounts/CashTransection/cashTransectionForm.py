# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cashTransectionForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from BLL.AccountsBL import cashTransectionBL
from Services.ResetServices import formReset
from Globals import globalVariables,globalList
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cashTransectionWindow(object):
    _filterList = None
    def init(self):
        self.cb_accountType.setFocus()


    def onAccountTypeChange(self,text):
        if(self.cb_accountType.currentIndex()>0):
            self.setAccounts(text)
            self.cb_account.setFocus()

    def setAccounts(self,accountType):
        self.cb_account.clear()
        self.cb_account.addItem("",0)
        accountList = cashTransectionBL.getAccountByType(accountType)
        for id, name, mob in accountList:
            self.cb_account.addItem(mob+"-"+name,id)

    def onChangeAccount(self):
        accountId = self.cb_account.currentData()
        result = cashTransectionBL.getAccountDataById(accountId)
        for account_id, name, father_name, user_name, cnic, mobile_no, gender, address, password, Type, status, balance  in result:
            self.le_name.setText(name)
            self.le_cnic.setText(cnic)
            self.le_address.setText(address)
            self.le_type.setText(Type)
            self.le_status.setText(status)
            self.le_balance.setText(str(balance))
        self.getCashTransection()

        self.le_amount.setFocus()

    def onClickDeposit(self):
        self.cb_withdrwa.setChecked(False)
        self.cb_deposit.setChecked(True)

    def onClickWithDrawal(self):
        self.cb_deposit.setChecked(False)
        self.cb_withdrwa.setChecked(True)


    def onClear(self):
        self.le_amount.setText('')
        self.te_remarks.setPlainText('')
        self.getCashTransection()

    def onCancel(self):

        self.cb_account.setCurrentIndex(0)
        self.le_name.setText("")
        self.le_cnic.setText("")
        self.le_balance.setText("")
        self.le_status.setText("")
        self.le_type.setText("")
        self.le_address.setText("")
        self.onClear()

    def onEnterAmount(self):
        self.te_remarks.setFocus()

    def onSubmit(self):
        acID = self.cb_account.currentData()
        name = self.le_name.text()
        mob = self.cb_account.currentText()
        balance = self.le_balance.text()

        amountType = ''
        if(self.cb_withdrwa.isChecked()):
            amountType =  globalVariables.Variables._withDrawal

        if(self.cb_deposit.isChecked()):
            amountType =  globalVariables.Variables._deposit

        amount = self.le_amount.text()
        remarks = self.te_remarks.toPlainText()

        cashTransectionBL.validateCashTransection(self, acID, amountType, remarks, amount, name, mob, balance)

        formReset.Reset._resetCashTranectionForm = self.onClear

    def getCashTransection(self):
        try:
            accountId = self.cb_account.currentData()
            result = cashTransectionBL.getCashTransectionByAccountId(accountId)
            self.setCashTransection(result)

            self._filterList = cashTransectionBL.getCashTransectionByAccountId(accountId).fetchall().copy()
        except:
            pass

    def setCashTransection(self,result):
        bal = 0
        dr = 0
        cr = 0
        balance = 0
        self.tbl_transection.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_transection.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if(colum_number == 3 and data != None):
                    dr = dr + data
                    bal = bal + data
                if(colum_number == 4 and data != None):
                    cr = cr + data
                    bal = bal - data

                self.tbl_transection.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                self.tbl_transection.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(bal)))
        self.le_dr.setText(str(dr))
        self.le_cr.setText(str(cr))
        self.le_totalBalance.setText(str(dr - cr))


    def filterFunc(self,item):
        name = self.le_filterByName.text()
        mobile = self.le_filterByMobile.text()
        _type = self.le_filterByType.text()
        dr = self.le_filterByDr.text()
        cr = self.le_filterByCr.text()
        balance = self.le_filterByBalance.text()
        remarks = self.le_filterByRemarks.text()

        if (str(item[0].lower()).startswith(name) and str(item[1]).startswith(mobile) and
            str(item[2].lower()).startswith(_type) and str(item[3]).startswith(dr)  and
            str(item[4]).startswith(cr) and str(item[5]).startswith(balance) and
            str(item[6].lower()).startswith(remarks) ):
            return True
        else:
            return False

    def transectionsFilter(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.setCashTransection(result)



    def cashTransectionSetupUi(self, cashTransectionWindow):
        cashTransectionWindow.setObjectName("cashTransectionWindow")
        cashTransectionWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        cashTransectionWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        cashTransectionWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        cashTransectionWindow.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        charRegex=QtCore.QRegExp("[a-z-A-Z _]+")
        self.onlyChar = QtGui.QRegExpValidator(charRegex)

        self.centralwidget = QtWidgets.QWidget(cashTransectionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addTransectionGB = QtWidgets.QGroupBox(self.centralwidget)
        self.addTransectionGB.setGeometry(QtCore.QRect(10, 0, 280, 680))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTransectionGB.sizePolicy().hasHeightForWidth())
        self.addTransectionGB.setSizePolicy(sizePolicy)
        self.addTransectionGB.setObjectName("addTransectionGB")
        self.le_name = QtWidgets.QLineEdit(self.addTransectionGB)
        self.le_name.setEnabled(False)
        self.le_name.setGeometry(QtCore.QRect(75, 80, 200, 28))
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
        self.le_cnic = QtWidgets.QLineEdit(self.addTransectionGB)
        self.le_cnic.setEnabled(False)
        self.le_cnic.setGeometry(QtCore.QRect(75, 110, 200, 28))
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
        self.le_type = QtWidgets.QLineEdit(self.addTransectionGB)
        self.le_type.setEnabled(False)
        self.le_type.setGeometry(QtCore.QRect(75, 170, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_type.sizePolicy().hasHeightForWidth())
        self.le_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_type.setFont(font)
        self.le_type.setMaxLength(11)
        self.le_type.setObjectName("le_type")
        self.le_address = QtWidgets.QLineEdit(self.addTransectionGB)
        self.le_address.setEnabled(False)
        self.le_address.setGeometry(QtCore.QRect(75, 140, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_address.sizePolicy().hasHeightForWidth())
        self.le_address.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_address.setFont(font)
        self.le_address.setMaxLength(100)
        self.le_address.setObjectName("le_address")
        self.label = QtWidgets.QLabel(self.addTransectionGB)
        self.label.setGeometry(QtCore.QRect(10, 80, 65, 28))
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
        self.label_3 = QtWidgets.QLabel(self.addTransectionGB)
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
        self.label_4 = QtWidgets.QLabel(self.addTransectionGB)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 65, 28))
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
        self.label_5 = QtWidgets.QLabel(self.addTransectionGB)
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
        self.btn_submit = QtWidgets.QPushButton(self.addTransectionGB)
        self.btn_submit.setGeometry(QtCore.QRect(75, 640, 100, 28))
        submitIcon = QtGui.QPixmap(globalVariables.Variables._icon+'rightIcon.png')
        self.btn_submit.setIcon(QtGui.QIcon(submitIcon))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.onSubmit)
        
        self.btn_cancel = QtWidgets.QPushButton(self.addTransectionGB)
        self.btn_cancel.setGeometry(QtCore.QRect(175, 640, 100, 28))
        cancelIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cancelIcon.png')
        self.btn_cancel.setIcon(QtGui.QIcon(cancelIcon))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.onCancel)
        
        self.label_11 = QtWidgets.QLabel(self.addTransectionGB)
        self.label_11.setGeometry(QtCore.QRect(10, 200, 65, 28))
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
        
        self.cb_accountType = QtWidgets.QComboBox(self.addTransectionGB)
        self.cb_accountType.setGeometry(QtCore.QRect(75, 20, 200, 28))
        self.cb_accountType.addItem('SELECT')
        self.cb_accountType.addItems(globalList.List._accountTypeList)
        self.cb_accountType.setObjectName("cb_accountType")
        self.cb_accountType.activated[str].connect(self.onAccountTypeChange)
        
        self.label_10 = QtWidgets.QLabel(self.addTransectionGB)
        self.label_10.setGeometry(QtCore.QRect(10, 170, 65, 28))
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
        self.cb_account = QtWidgets.QComboBox(self.addTransectionGB)
        self.cb_account.setGeometry(QtCore.QRect(75, 50, 200, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_account.setFont(font)
        self.cb_account.setObjectName("cb_account")
        self.cb_account.activated.connect(self.onChangeAccount)
        
        self.label_6 = QtWidgets.QLabel(self.addTransectionGB)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 65, 28))
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
        self.le_status = QtWidgets.QLineEdit(self.addTransectionGB)
        self.le_status.setEnabled(False)
        self.le_status.setGeometry(QtCore.QRect(75, 200, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_status.sizePolicy().hasHeightForWidth())
        self.le_status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_status.setFont(font)
        self.le_status.setMaxLength(11)
        self.le_status.setObjectName("le_status")
        self.le_amount = QtWidgets.QLineEdit(self.addTransectionGB)
        self.le_amount.setEnabled(True)
        self.le_amount.setGeometry(QtCore.QRect(75, 290, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_amount.sizePolicy().hasHeightForWidth())
        self.le_amount.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_amount.setFont(font)
        self.le_amount.setMaxLength(15)
        self.le_amount.setValidator(self.onlyInt)
        self.le_amount.setObjectName("le_amount")
        self.le_amount.returnPressed.connect(self.onEnterAmount)

        self.label_12 = QtWidgets.QLabel(self.addTransectionGB)
        self.label_12.setGeometry(QtCore.QRect(10, 320, 65, 28))
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
        self.label_13 = QtWidgets.QLabel(self.addTransectionGB)
        self.label_13.setGeometry(QtCore.QRect(10, 290, 65, 28))
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
        self.cb_deposit = QtWidgets.QCheckBox(self.addTransectionGB)
        self.cb_deposit.setGeometry(QtCore.QRect(75, 260, 100, 28))
        self.cb_deposit.setChecked(True)
        self.cb_deposit.setObjectName("cb_deposit")
        self.cb_deposit.clicked.connect(self.onClickDeposit)
        
        self.cb_withdrwa = QtWidgets.QCheckBox(self.addTransectionGB)
        self.cb_withdrwa.setGeometry(QtCore.QRect(175, 260, 100, 28))
        self.cb_withdrwa.setObjectName("cb_withdrwa")
        self.cb_withdrwa.clicked.connect(self.onClickWithDrawal)
        
        self.le_balance = QtWidgets.QLineEdit(self.addTransectionGB)
        self.le_balance.setEnabled(False)
        self.le_balance.setGeometry(QtCore.QRect(75, 230, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_balance.sizePolicy().hasHeightForWidth())
        self.le_balance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_balance.setFont(font)
        self.le_balance.setMaxLength(150)
        self.le_balance.setObjectName("le_balance")
        
        self.label_14 = QtWidgets.QLabel(self.addTransectionGB)
        self.label_14.setGeometry(QtCore.QRect(10, 230, 65, 28))
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
        
        self.te_remarks = QtWidgets.QTextEdit(self.addTransectionGB)
        self.te_remarks.setGeometry(QtCore.QRect(75, 320, 200, 75))
        self.te_remarks.setObjectName("te_remarks")
        
        self.showTransectionGB = QtWidgets.QGroupBox(self.centralwidget)
        self.showTransectionGB.setGeometry(QtCore.QRect(300, 0, 1061, 681))
        self.showTransectionGB.setObjectName("showTransectionGB")
        
        self.tbl_transection = QtWidgets.QTableWidget(self.showTransectionGB)
        self.tbl_transection.setGeometry(QtCore.QRect(10, 60, 1041, 580))
        self.tbl_transection.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_transection.setRowCount(18)
        self.tbl_transection.setColumnCount(7)
        self.tbl_transection.setHorizontalHeaderLabels(['Name', 'Mobile', 'Type', 'Debit', 'Credit','Balance','Remarks'])
        self.tbl_transection.setColumnWidth(0,200)
        self.tbl_transection.setColumnWidth(6,300)
        self.tbl_transection.setObjectName("tbl_transection")
        
        self.filterGB = QtWidgets.QGroupBox(self.showTransectionGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 15, 1041, 41))
        self.filterGB.setObjectName("filterGB")

        self.le_filterByName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByName.setGeometry(QtCore.QRect(0, 15, 220, 20))
        self.le_filterByName.setObjectName("le_filterByName")
        self.le_filterByName.textChanged.connect(self.transectionsFilter)

        self.le_filterByMobile = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByMobile.setGeometry(QtCore.QRect(220, 15, 100, 20))
        self.le_filterByMobile.setObjectName("le_filterByMobile")
        self.le_filterByMobile.textChanged.connect(self.transectionsFilter)

        self.le_filterByDr = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDr.setGeometry(QtCore.QRect(420, 15, 100, 20))
        self.le_filterByDr.setObjectName("le_filterByDr")
        self.le_filterByDr.textChanged.connect(self.transectionsFilter)

        self.le_filterByCr = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCr.setGeometry(QtCore.QRect(520, 15, 100, 20))
        self.le_filterByCr.setObjectName("le_filterByCr")
        self.le_filterByCr.textChanged.connect(self.transectionsFilter)

        self.le_filterByBalance = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByBalance.setGeometry(QtCore.QRect(620, 15, 100, 20))
        self.le_filterByBalance.setObjectName("le_filterByBalance")
        self.le_filterByBalance.textChanged.connect(self.transectionsFilter)

        self.le_filterByRemarks = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByRemarks.setGeometry(QtCore.QRect(720, 15, 190, 20))
        self.le_filterByRemarks.setObjectName("le_filterByRemarks")
        self.le_filterByRemarks.textChanged.connect(self.transectionsFilter)

        self.le_filterByType = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByType.setGeometry(QtCore.QRect(320, 15, 100, 20))
        self.le_filterByType.setObjectName("le_filterByType")
        self.le_filterByType.textChanged.connect(self.transectionsFilter)


        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(930, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getCashTransection)

        self.le_dr = QtWidgets.QLineEdit(self.showTransectionGB)
        self.le_dr.setEnabled(False)
        self.le_dr.setGeometry(QtCore.QRect(60, 645, 100, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_dr.sizePolicy().hasHeightForWidth())
        self.le_dr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_dr.setFont(font)
        self.le_dr.setText("")
        self.le_dr.setMaxLength(15)
        self.le_dr.setObjectName("le_dr")
        self.label_15 = QtWidgets.QLabel(self.showTransectionGB)
        self.label_15.setGeometry(QtCore.QRect(10, 645, 41, 28))
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
        self.label_16 = QtWidgets.QLabel(self.showTransectionGB)
        self.label_16.setGeometry(QtCore.QRect(180, 640, 51, 28))
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
        self.le_cr = QtWidgets.QLineEdit(self.showTransectionGB)
        self.le_cr.setEnabled(False)
        self.le_cr.setGeometry(QtCore.QRect(240, 645, 100, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cr.sizePolicy().hasHeightForWidth())
        self.le_cr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cr.setFont(font)
        self.le_cr.setText("")
        self.le_cr.setMaxLength(15)
        self.le_cr.setObjectName("le_cr")
        self.le_totalBalance = QtWidgets.QLineEdit(self.showTransectionGB)
        self.le_totalBalance.setEnabled(False)
        self.le_totalBalance.setGeometry(QtCore.QRect(950, 645, 100, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_totalBalance.sizePolicy().hasHeightForWidth())
        self.le_totalBalance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_totalBalance.setFont(font)
        self.le_totalBalance.setText("")
        self.le_totalBalance.setMaxLength(15)
        self.le_totalBalance.setObjectName("le_totalBalance")
        self.label_17 = QtWidgets.QLabel(self.showTransectionGB)
        self.label_17.setGeometry(QtCore.QRect(880, 645, 61, 28))
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
        cashTransectionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(cashTransectionWindow)
        self.statusbar.setObjectName("statusbar")
        cashTransectionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(cashTransectionWindow)
        QtCore.QMetaObject.connectSlotsByName(cashTransectionWindow)

    def retranslateUi(self, cashTransectionWindow):
        _translate = QtCore.QCoreApplication.translate
        cashTransectionWindow.setWindowTitle(_translate("cashTransectionWindow", "Cash Transection Window"))
        self.addTransectionGB.setTitle(_translate("cashTransectionWindow", "Add Transection"))
        self.le_name.setPlaceholderText(_translate("cashTransectionWindow", "Account Name"))
        self.le_cnic.setPlaceholderText(_translate("cashTransectionWindow", "Account CNIC"))
        self.le_type.setPlaceholderText(_translate("cashTransectionWindow", "Account Type"))
        self.le_address.setPlaceholderText(_translate("cashTransectionWindow", "Account Address"))
        self.label.setText(_translate("cashTransectionWindow", "Name"))
        self.label_3.setText(_translate("cashTransectionWindow", "CNIC"))
        self.label_4.setText(_translate("cashTransectionWindow", "Account"))
        self.label_5.setText(_translate("cashTransectionWindow", "Address"))
        self.btn_submit.setText(_translate("cashTransectionWindow", "Submit"))
        self.btn_cancel.setText(_translate("cashTransectionWindow", "Cancel"))
        self.label_11.setText(_translate("cashTransectionWindow", "Status"))
        self.label_10.setText(_translate("cashTransectionWindow", "Type"))
        self.label_6.setText(_translate("cashTransectionWindow", "A/C Type"))
        self.le_status.setPlaceholderText(_translate("cashTransectionWindow", "Account Status"))
        self.le_amount.setPlaceholderText(_translate("cashTransectionWindow", "Paying Amount"))
        self.label_12.setText(_translate("cashTransectionWindow", "Remarks"))
        self.label_13.setText(_translate("cashTransectionWindow", "Amount"))
        self.cb_deposit.setText(_translate("cashTransectionWindow", "Deposet"))
        self.cb_withdrwa.setText(_translate("cashTransectionWindow", "Withdraw"))
        self.le_balance.setPlaceholderText(_translate("cashTransectionWindow", "Account Balance"))
        self.label_14.setText(_translate("cashTransectionWindow", "Balance"))
        self.te_remarks.setPlaceholderText(_translate("cashTransectionWindow", "Remarks"))
        self.showTransectionGB.setTitle(_translate("cashTransectionWindow", "All Transection History"))
        self.filterGB.setTitle(_translate("cashTransectionWindow", "Filter Transection"))
        self.le_filterByName.setPlaceholderText(_translate("cashTransectionWindow", "Filter By Name"))
        self.le_filterByMobile.setPlaceholderText(_translate("cashTransectionWindow", "Filter By Mobile"))
        self.le_filterByDr.setPlaceholderText(_translate("cashTransectionWindow", "Filter By Debit"))
        self.le_filterByCr.setPlaceholderText(_translate("cashTransectionWindow", "Filter By Credit"))
        self.le_filterByBalance.setPlaceholderText(_translate("cashTransectionWindow", "Filter By Balance"))
        self.btn_refresh.setText(_translate("cashTransectionWindow", "Refresh"))
        self.le_filterByRemarks.setPlaceholderText(_translate("cashTransectionWindow", "Filter By Remarks"))
        self.le_filterByType.setPlaceholderText(_translate("cashTransectionWindow", "Filter By Type"))
        self.label_15.setText(_translate("cashTransectionWindow", "Debit :"))
        self.label_16.setText(_translate("cashTransectionWindow", "Credit :"))
        self.label_17.setText(_translate("cashTransectionWindow", "Balance :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cashTransectionWindow = QtWidgets.QMainWindow()
    ui = Ui_cashTransectionWindow()
    ui.setupUi(cashTransectionWindow)
    cashTransectionWindow.show()
    sys.exit(app.exec_())

