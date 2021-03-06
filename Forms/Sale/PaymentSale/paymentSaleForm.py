# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paymentSaleForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from BLL.SaleBL import paymentSaleBL

from Globals import globalVariables,globalList
from Services.MiscService import dateTime
from Services.ResetServices import formReset

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_paymentSaleWindow(object):
    _filterList = None

    def init(self):
        self.le_date.setText(self.calendar.selectedDate().toString())
        self.cb_accountType.setFocus()


    def showCalendar(self):
        if (self.calendar.isHidden()):
            self.calendar.show()
        else:
            self.calendar.hide()

    def setDate(self, date):
        self.le_date.setText(date.toString())
        self.calendar.hide()


    def onAccountTypeChange(self,text):
        if(self.cb_accountType.currentIndex() == 0):
            self.onCancel()
        if(self.cb_accountType.currentIndex()>0):
            self.setAccounts(text)
            self.cb_account.setFocus()

    def setAccounts(self,accountType):
        self.cb_account.clear()
        self.cb_account.addItem("",0)
        accountList = paymentSaleBL.getAccountByType(accountType)
        for id, name, mob in accountList:
            self.cb_account.addItem(mob+"-"+name,id)

    def onChangeAccount(self):
        accountId = self.cb_account.currentData()
        self.setAccountData(accountId)
        self.setSaleItem(accountId)
        self.cb_sale.setFocus()

    def setAccountData(self,accountId):
        result = paymentSaleBL.getAccountData(accountId)
        for item in result:
            self.le_name.setText(item[1])
            self.le_fatherName.setText(item[2])
            self.le_cnic.setText(item[4])
            self.le_cellNo.setText(item[5])
            self.te_address.setText(item[7])
            self.le_status.setText(item[10])

    def setSaleItem(self,accountId):
        self.cb_sale.clear()
        self.cb_sale.addItem("")
        itemList = paymentSaleBL.getSaleItem(accountId)
        for id, company, product in itemList:
            self.cb_sale.addItem(company+"-"+product,id)

    def onChangeSaleItem(self):
        try:
            billId = self.cb_sale.currentData()
            if(billId != None):
                self.setSaleItemDetail(billId)
                self.getPayment()
                self.le_payment.setFocus()
            else:
                self.clearItem()
        except:
            pass

    def setSaleItemDetail(self,billId):
        detailList = paymentSaleBL.getSaleItemDetail(billId)
        for item in detailList:
            self.le_dueDate.setText(item[3])
            self.le_endDate.setText(dateTime.getDateWithoutTime(item[4]))
            self.le_remainingAmount.setText(str(item[12]))

    def onChangePayment(self):
        payment = self.le_payment.text()
        remaining = self.le_remainingAmount.text()
        if (remaining != '' and payment != ''):
            balance = int(remaining) - int(payment)
            self.le_balance.setText(str(balance))
        else:
            self.le_balance.setText(remaining)

    def onEnterPayment(self):
        self.te_address.setFocus()

    def onSubmit(self):
        accountId = self.cb_account.currentData()
        name = self.le_name.text()
        mobile = self.le_cellNo.text()
        address = self.te_address.toPlainText()
        soldItem = self.cb_sale.currentText()
        billId = self.cb_sale.currentData()
        billType = globalVariables.Variables._sale
        date = self.le_date.text()
        amount = self.le_payment.text()
        balance = self.le_balance.text()
        remarks = self.te_remarks.toPlainText()
        formReset.Reset._resetPaymentSaleForm = self.clearItem

        paymentSaleBL.validatePayment(self,date,billId,billType,accountId,name, mobile,address,soldItem,amount,balance,remarks)

    def clearItem(self):
        self.le_dueDate.setText('')
        self.le_endDate.setText('')
        self.le_remainingAmount.setText('')

        self.le_balance.setText('')
        self.le_payment.setText('')
        self.te_remarks.setPlainText('')
        self.le_quickCount.setText('')
        self.tbl_payment.setRowCount(0)
        self.tbl_payment.setRowCount(19)
        self.getPayment()

    def onCancel(self):
        self.cb_account.setCurrentIndex(0)
        self.le_fatherName.setText('')
        self.le_cnic.setText('')
        self.le_cellNo.setText('')
        self.te_address.setPlainText('')
        self.le_status.setText('')

        self.cb_sale.clear()
        self.le_dueDate.setText('')
        self.le_endDate.setText('')
        self.le_remainingAmount.setText('')

        self.le_balance.setText('')
        self.le_payment.setText('')
        self.te_remarks.setPlainText('')
        self.le_quickCount.setText('')
        self.tbl_payment.setRowCount(0)
        self.tbl_payment.setRowCount(19)

    def getPayment(self):
        try:
            billId = self.cb_sale.currentData()
            if(billId != None):
                result = paymentSaleBL.getPaymentLog(billId)
                self._filterList = paymentSaleBL.getPaymentLog(billId).fetchall().copy()
                self.setPaymentLog(result)
        except:
            pass

    def setPaymentLog(self,result):
        total = 0
        self.tbl_payment.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_payment.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if (colum_number == 1):
                    total = total + data
                if (colum_number == 0):
                    self.tbl_payment.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(dateTime.getDateWithoutTime(data))))
                else:
                    self.tbl_payment.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

        self.le_quickCount.setText(str(total))


    def filterFunc(self,item):
        date = self.le_filterByDate.text()
        amount = self.le_filterByAmount.text()
        balance = self.le_filterByBalance.text()
        remarks = self.le_filterByRemarks.text()

        if (str(item[0]).startswith(date) and str(item[1]).startswith(amount) and
            str(item[2]).startswith(balance) and str(item[3].lower()).startswith(remarks) ):
            return True
        else:
            return False

    def filterPayment(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.setPaymentLog(result)



    def paymentSaleSetupUi(self, paymentWindow):
        paymentWindow.setObjectName("paymentWindow")
        paymentWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        paymentWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        paymentWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        paymentWindow.setAutoFillBackground(True)
        
        self.centralwidget = QtWidgets.QWidget(paymentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.paymentGB = QtWidgets.QGroupBox(self.centralwidget)
        self.paymentGB.setGeometry(QtCore.QRect(10, 0, 281, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paymentGB.sizePolicy().hasHeightForWidth())
        self.paymentGB.setSizePolicy(sizePolicy)
        self.paymentGB.setObjectName("paymentGB")
        self.btn_submit = QtWidgets.QPushButton(self.paymentGB)
        self.btn_submit.setGeometry(QtCore.QRect(70, 640, 100, 28))
        submitIcon = QtGui.QPixmap(globalVariables.Variables._icon+'rightIcon.png')
        self.btn_submit.setIcon(QtGui.QIcon(submitIcon))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.onSubmit)
        
        self.btn_cancel = QtWidgets.QPushButton(self.paymentGB)
        self.btn_cancel.setGeometry(QtCore.QRect(170, 640, 100, 28))
        cancelIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cancelIcon.png')
        self.btn_cancel.setIcon(QtGui.QIcon(cancelIcon))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.onCancel)
        
        self.label_11 = QtWidgets.QLabel(self.paymentGB)
        self.label_11.setGeometry(QtCore.QRect(5, 340, 60, 28))
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
        self.te_remarks = QtWidgets.QTextEdit(self.paymentGB)
        self.te_remarks.setEnabled(True)
        self.te_remarks.setGeometry(QtCore.QRect(70, 520, 200, 71))
        self.te_remarks.setObjectName("te_remarks")
        self.le_cellNo = QtWidgets.QLineEdit(self.paymentGB)
        self.le_cellNo.setEnabled(False)
        self.le_cellNo.setGeometry(QtCore.QRect(70, 200, 200, 28))
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
        self.le_name = QtWidgets.QLineEdit(self.paymentGB)
        self.le_name.setEnabled(False)
        self.le_name.setGeometry(QtCore.QRect(70, 110, 200, 28))
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
        self.le_cnic = QtWidgets.QLineEdit(self.paymentGB)
        self.le_cnic.setEnabled(False)
        self.le_cnic.setGeometry(QtCore.QRect(70, 170, 200, 28))
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
        
        self.cb_account = QtWidgets.QComboBox(self.paymentGB)
        self.cb_account.setGeometry(QtCore.QRect(70, 80, 200, 28))
        self.cb_account.setEditable(True)
        self.cb_account.setObjectName("cb_account")
        self.cb_account.activated.connect(self.onChangeAccount)
        
        self.label_3 = QtWidgets.QLabel(self.paymentGB)
        self.label_3.setGeometry(QtCore.QRect(5, 170, 60, 28))
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
        self.cb_sale = QtWidgets.QComboBox(self.paymentGB)
        self.cb_sale.setGeometry(QtCore.QRect(70, 340, 200, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_sale.setFont(font)
        self.cb_sale.setEditable(False)
        self.cb_sale.setObjectName("cb_sale")
        self.cb_sale.activated.connect(self.onChangeSaleItem)

        self.label_5 = QtWidgets.QLabel(self.paymentGB)
        self.label_5.setGeometry(QtCore.QRect(5, 230, 60, 28))
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
        self.label_10 = QtWidgets.QLabel(self.paymentGB)
        self.label_10.setGeometry(QtCore.QRect(5, 80, 60, 28))
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
        self.label_13 = QtWidgets.QLabel(self.paymentGB)
        self.label_13.setGeometry(QtCore.QRect(5, 460, 60, 28))
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

        self.le_payment = QtWidgets.QLineEdit(self.paymentGB)
        self.le_payment.setGeometry(QtCore.QRect(70, 460, 200, 28))
        self.le_payment.setObjectName("le_payment")
        self.le_payment.textChanged.connect(self.onChangePayment)
        self.le_payment.returnPressed.connect(self.onEnterPayment)

        self.label_4 = QtWidgets.QLabel(self.paymentGB)
        self.label_4.setGeometry(QtCore.QRect(5, 200, 60, 28))
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
        self.te_address = QtWidgets.QTextEdit(self.paymentGB)
        self.te_address.setEnabled(False)
        self.te_address.setGeometry(QtCore.QRect(70, 230, 200, 71))
        self.te_address.setObjectName("te_address")
        self.label_6 = QtWidgets.QLabel(self.paymentGB)
        self.label_6.setGeometry(QtCore.QRect(5, 520, 60, 28))
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
        self.label = QtWidgets.QLabel(self.paymentGB)
        self.label.setGeometry(QtCore.QRect(5, 110, 60, 28))
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
        self.label_14 = QtWidgets.QLabel(self.paymentGB)
        self.label_14.setGeometry(QtCore.QRect(5, 20, 60, 28))
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
        self.label_15 = QtWidgets.QLabel(self.paymentGB)
        self.label_15.setGeometry(QtCore.QRect(5, 305, 60, 28))
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
        self.le_status = QtWidgets.QLineEdit(self.paymentGB)
        self.le_status.setEnabled(False)
        self.le_status.setGeometry(QtCore.QRect(70, 305, 200, 28))
        self.le_status.setObjectName("le_status")
        self.le_date = QtWidgets.QLineEdit(self.paymentGB)
        self.le_date.setEnabled(False)
        self.le_date.setGeometry(QtCore.QRect(70, 20, 170, 28))
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
        self.btn_date = QtWidgets.QPushButton(self.paymentGB)
        self.btn_date.setGeometry(QtCore.QRect(240, 20, 30, 28))
        dateIcon = QtGui.QPixmap(globalVariables.Variables._icon+'calendarIcon.png')
        self.btn_date.setIcon(QtGui.QIcon(dateIcon))
        self.btn_date.setObjectName("btn_date")
        self.btn_date.clicked.connect(self.showCalendar)
        
        self.label_18 = QtWidgets.QLabel(self.paymentGB)
        self.label_18.setGeometry(QtCore.QRect(5, 50, 60, 28))
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
        
        self.cb_accountType = QtWidgets.QComboBox(self.paymentGB)
        self.cb_accountType.setGeometry(QtCore.QRect(70, 50, 200, 28))
        self.cb_accountType.addItem('SELECT')
        self.cb_accountType.addItems(globalList.List._accountTypeList)
        self.cb_accountType.setObjectName("cb_accountType")
        self.cb_accountType.activated[str].connect(self.onAccountTypeChange)
        
        self.le_fatherName = QtWidgets.QLineEdit(self.paymentGB)
        self.le_fatherName.setEnabled(False)
        self.le_fatherName.setGeometry(QtCore.QRect(70, 140, 200, 28))
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
        self.label_2 = QtWidgets.QLabel(self.paymentGB)
        self.label_2.setGeometry(QtCore.QRect(5, 140, 60, 28))
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
        self.label_16 = QtWidgets.QLabel(self.paymentGB)
        self.label_16.setGeometry(QtCore.QRect(4, 430, 60, 28))
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
        self.le_remainingAmount = QtWidgets.QLineEdit(self.paymentGB)
        self.le_remainingAmount.setEnabled(False)
        self.le_remainingAmount.setGeometry(QtCore.QRect(70, 430, 200, 28))
        self.le_remainingAmount.setObjectName("le_remainingAmount")
        self.calendar = QtWidgets.QCalendarWidget(self.paymentGB)
        self.calendar.setGeometry(QtCore.QRect(0, 50, 281, 183))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.calendar.setFont(font)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setObjectName("calendar")
        self.calendar.hide()
        self.calendar.clicked[QtCore.QDate].connect(self.setDate)
        
        self.label_19 = QtWidgets.QLabel(self.paymentGB)
        self.label_19.setGeometry(QtCore.QRect(4, 370, 60, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.le_dueDate = QtWidgets.QLineEdit(self.paymentGB)
        self.le_dueDate.setEnabled(False)
        self.le_dueDate.setGeometry(QtCore.QRect(70, 370, 200, 28))
        self.le_dueDate.setObjectName("le_dueDate")
        self.label_20 = QtWidgets.QLabel(self.paymentGB)
        self.label_20.setGeometry(QtCore.QRect(4, 400, 60, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.le_endDate = QtWidgets.QLineEdit(self.paymentGB)
        self.le_endDate.setEnabled(False)
        self.le_endDate.setGeometry(QtCore.QRect(70, 400, 200, 28))
        self.le_endDate.setObjectName("le_endDate")
        self.le_balance = QtWidgets.QLineEdit(self.paymentGB)
        self.le_balance.setEnabled(False)
        self.le_balance.setGeometry(QtCore.QRect(70, 490, 200, 28))
        self.le_balance.setObjectName("le_balance")
        self.label_21 = QtWidgets.QLabel(self.paymentGB)
        self.label_21.setGeometry(QtCore.QRect(5, 490, 60, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.showPaymentGB = QtWidgets.QGroupBox(self.centralwidget)
        self.showPaymentGB.setGeometry(QtCore.QRect(300, 0, 1061, 681))
        self.showPaymentGB.setObjectName("showPaymentGB")
        self.tbl_payment = QtWidgets.QTableWidget(self.showPaymentGB)
        self.tbl_payment.setGeometry(QtCore.QRect(10, 60, 1041, 610))
        self.tbl_payment.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_payment.setRowCount(19)
        self.tbl_payment.setColumnCount(4)
        self.tbl_payment.setHorizontalHeaderLabels(['Date', 'Amount', 'Balance', 'Remarks',])
        self.tbl_payment.setColumnWidth(3,700)
        self.tbl_payment.setObjectName("tbl_payment")
        
        self.filterGB = QtWidgets.QGroupBox(self.showPaymentGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 15, 1041, 41))
        self.filterGB.setObjectName("filterGB")

        self.le_filterByDate = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDate.setGeometry(QtCore.QRect(0, 20, 120, 20))
        self.le_filterByDate.setObjectName("le_filterByDate")
        self.le_filterByDate.textChanged.connect(self.filterPayment)

        self.le_filterByAmount = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByAmount.setGeometry(QtCore.QRect(120, 20, 100, 20))
        self.le_filterByAmount.setObjectName("le_filterByAmount")
        self.le_filterByAmount.textChanged.connect(self.filterPayment)

        self.le_filterByBalance = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByBalance.setGeometry(QtCore.QRect(220, 20, 100, 20))
        self.le_filterByBalance.setObjectName("le_filterByBalance")
        self.le_filterByBalance.textChanged.connect(self.filterPayment)

        self.le_filterByRemarks = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByRemarks.setGeometry(QtCore.QRect(320, 20, 375, 20))
        self.le_filterByRemarks.setObjectName("le_filterByRemarks")
        self.le_filterByRemarks.textChanged.connect(self.filterPayment)
        
        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(940, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getPayment)
        
        self.label_17 = QtWidgets.QLabel(self.filterGB)
        self.label_17.setGeometry(QtCore.QRect(740, 10, 91, 28))
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
        self.le_quickCount.setGeometry(QtCore.QRect(830, 10, 100, 28))
        self.le_quickCount.setObjectName("le_quickCount")
        paymentWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(paymentWindow)
        self.statusbar.setObjectName("statusbar")
        paymentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(paymentWindow)
        QtCore.QMetaObject.connectSlotsByName(paymentWindow)

    def retranslateUi(self, paymentWindow):
        _translate = QtCore.QCoreApplication.translate
        paymentWindow.setWindowTitle(_translate("paymentWindow", "Payment Window"))
        self.paymentGB.setTitle(_translate("paymentWindow", "Add Payment"))
        self.btn_submit.setText(_translate("paymentWindow", "Submit"))
        self.btn_cancel.setText(_translate("paymentWindow", "Cancel"))
        self.label_11.setText(_translate("paymentWindow", "Sold"))
        self.te_remarks.setPlaceholderText(_translate("paymentWindow", "Remarks"))
        self.le_cellNo.setPlaceholderText(_translate("paymentWindow", "Mobile Number"))
        self.le_name.setPlaceholderText(_translate("paymentWindow", "Account Name"))
        self.le_cnic.setPlaceholderText(_translate("paymentWindow", "CNIC Number"))
        self.label_3.setText(_translate("paymentWindow", "CNIC"))
        self.label_5.setText(_translate("paymentWindow", "Address"))
        self.label_10.setText(_translate("paymentWindow", "Account"))
        self.label_13.setText(_translate("paymentWindow", "Amount"))
        self.le_payment.setPlaceholderText(_translate("paymentWindow", "Paying Amount"))
        self.label_4.setText(_translate("paymentWindow", "Cell No#"))
        self.te_address.setPlaceholderText(_translate("paymentWindow", "Address"))
        self.label_6.setText(_translate("paymentWindow", "Remarks"))
        self.label.setText(_translate("paymentWindow", "Name"))
        self.label_14.setText(_translate("paymentWindow", "Date"))
        self.label_15.setText(_translate("paymentWindow", "Status"))
        self.le_status.setPlaceholderText(_translate("paymentWindow", "Current Status"))
        self.label_18.setText(_translate("paymentWindow", "AC Type"))
        self.le_fatherName.setPlaceholderText(_translate("paymentWindow", "Father Name"))
        self.label_2.setText(_translate("paymentWindow", "S/O"))
        self.label_16.setText(_translate("paymentWindow", "Remaing"))
        self.le_remainingAmount.setPlaceholderText(_translate("paymentWindow", "Remaining  Amount"))
        self.label_19.setText(_translate("paymentWindow", "Due Date"))
        self.le_dueDate.setPlaceholderText(_translate("paymentWindow", "Due Date"))
        self.label_20.setText(_translate("paymentWindow", "End Date"))
        self.le_endDate.setPlaceholderText(_translate("paymentWindow", "Completion Date"))
        self.le_balance.setPlaceholderText(_translate("paymentWindow", "Balance"))
        self.label_21.setText(_translate("paymentWindow", "Balance"))
        self.showPaymentGB.setTitle(_translate("paymentWindow", "All Payment"))
        self.filterGB.setTitle(_translate("paymentWindow", "Filter"))
        self.le_filterByDate.setPlaceholderText(_translate("paymentWindow", "Search"))
        self.le_filterByAmount.setPlaceholderText(_translate("paymentWindow", "Search"))
        self.le_filterByBalance.setPlaceholderText(_translate("paymentWindow", "Search"))
        self.btn_refresh.setText(_translate("paymentWindow", "Refresh"))
        self.label_17.setText(_translate("paymentWindow", "Quick Count :"))
        self.le_filterByRemarks.setPlaceholderText(_translate("paymentWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    paymentWindow = QtWidgets.QMainWindow()
    ui = Ui_paymentWindow()
    ui.setupUi(paymentWindow)
    paymentWindow.show()
    sys.exit(app.exec_())

