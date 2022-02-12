
from BLL.ReportsBL.PurchaseReportsBL import purchaseReportByDateBL
from Globals import globalVariables
from Services.MiscService import dateTime
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_purchaseReportByDateWindow(object):
    _filterList = None

    def init(self):
        self.le_startDate.setText(self.startCalendar.selectedDate().toString())
        self.le_endDate.setText(self.endCalendar.selectedDate().toString())

    def displayStartCalendar(self):
        if(self.startCalendar.isHidden()):
            self.startCalendar.show()
            self.endCalendar.hide()
        else:
            self.startCalendar.hide()

    def setStartDate(self,date):
        # print(dateTime.getStartDateWithoutTimes(str(date.toString())))
        self.le_startDate.setText(date.toString())
        self.startCalendar.hide()

    def displayEndCalendar(self):
        if(self.endCalendar.isHidden()):
            self.endCalendar.show()
            self.startCalendar.hide()
        else:
            self.endCalendar.hide()

    def setEndDate(self,date):
        self.le_endDate.setText(date.toString())
        self.endCalendar.hide()


    def getPurchaseReportByDate(self):
        try:
            startDate = self.le_startDate.text()
            endDate = self.le_endDate.text()
            billType = globalVariables.Variables._purchase

            resultReport = purchaseReportByDateBL.validatePurchaseReportDates(startDate,endDate)
            resultBill = purchaseReportByDateBL.validatePurchaseBillByDate(startDate,endDate,billType)
            self._filterList = purchaseReportByDateBL.validatePurchaseReportDates(startDate,endDate).fetchall().copy()

            self.setPurchaseBillByDate(resultBill)
            self.setPurchaseReportByDate(resultReport)
        except:
            pass

    def setPurchaseBillByDate(self, result):
        try:
            for item in result:
                self.le_totalPurchase.setText(str(item[0]))
                self.le_totalDiscount.setText(str(item[1]))
                self.le_netPurchase.setText(str(item[2]))

        except:
            pass

    def setPurchaseReportByDate(self,result):
        self.tbl_purchaseReportByDate.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_purchaseReportByDate.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if(colum_number == 1):
                    self.tbl_purchaseReportByDate.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(dateTime.getDateWithoutTime(data))))
                else:
                    self.tbl_purchaseReportByDate.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))




    def filterFunc(self,item):
        invoice = self.le_filterByInvoice.text()
        date = self.le_filterByDate.text()
        name = self.le_filterByName.text()
        mobile = self.le_filterByMobile.text()
        company = self.le_filterByCompany.text()
        product = self.le_filterByProduct.text()
        engine = self.le_filterByEngine.text()
        chassis = self.le_filterByChassis.text()
        costPrice = self.le_filterByCostPrice.text()
        salePrice = self.le_filterBySalePrice.text()
        discount = self.le_filterByDiscount.text()
        totalPrice = self.le_filterByTotalPrice.text()
        remarks = self.le_filterByRemarks.text()

        if (str(item[0]).startswith(invoice) and str(item[1]).startswith(date) and
            str(item[2]).lower().startswith(name) and str(item[3]).startswith(mobile) and
            str(item[4]).lower().startswith(company) and str(item[5]).lower().startswith(product) and
            str(item[6]).startswith(engine) and str(item[7]).startswith(chassis)  and
            str(item[8]).startswith(costPrice) and str(item[9]).startswith(salePrice)  and
            str(item[10]).startswith(discount) and str(item[11]).startswith(totalPrice) and
            str(item[12]).lower().startswith(remarks) ):
            return True
        else:
            return False

    def filterPurchaseReport(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.setPurchaseReportByDate(result)


        
    def purchaseReportByDateSetupUi(self, purchaseReportByDateWindow):
        purchaseReportByDateWindow.setObjectName("purchaseReportByDateWindow")
        purchaseReportByDateWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        purchaseReportByDateWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        purchaseReportByDateWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        purchaseReportByDateWindow.setAutoFillBackground(True)

        dateIcon = QtGui.QPixmap(globalVariables.Variables._icon+'calendarIcon.png')
        
        self.centralwidget = QtWidgets.QWidget(purchaseReportByDateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.purchaseReportGB = QtWidgets.QGroupBox(self.centralwidget)
        self.purchaseReportGB.setGeometry(QtCore.QRect(5, 0, 1355, 685))
        self.purchaseReportGB.setObjectName("purchaseReportGB")

        self.tbl_purchaseReportByDate = QtWidgets.QTableWidget(self.purchaseReportGB)
        self.tbl_purchaseReportByDate.setGeometry(QtCore.QRect(10, 135, 1340, 541))
        self.tbl_purchaseReportByDate.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_purchaseReportByDate.setShowGrid(True)
        self.tbl_purchaseReportByDate.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_purchaseReportByDate.setWordWrap(True)
        self.tbl_purchaseReportByDate.setRowCount(17)
        self.tbl_purchaseReportByDate.setColumnCount(13)
        self.tbl_purchaseReportByDate.setHorizontalHeaderLabels(['Invoice','Date','Name','Mobile','Company',
                                                                 'Product','Engine','Chassis','Cost Price','Sale Price',
                                                                 'Discount','Total Price','Remarks'])
        self.tbl_purchaseReportByDate.setObjectName("tbl_purchaseReportByDate")




        self.filterGB = QtWidgets.QGroupBox(self.purchaseReportGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 90, 1341, 41))
        self.filterGB.setObjectName("filterGB")

        self.le_filterByDate = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDate.setGeometry(QtCore.QRect(120, 15, 100, 20))
        self.le_filterByDate.setMaxLength(32)
        self.le_filterByDate.setObjectName("le_filterByDate")
        self.le_filterByDate.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByName.setGeometry(QtCore.QRect(220, 15, 100, 20))
        self.le_filterByName.setMaxLength(32)
        self.le_filterByName.setObjectName("le_filterByName")
        self.le_filterByName.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByMobile = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByMobile.setGeometry(QtCore.QRect(320, 15, 100, 20))
        self.le_filterByMobile.setMaxLength(32)
        self.le_filterByMobile.setObjectName("le_filterByMobile")
        self.le_filterByMobile.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByCompany = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompany.setGeometry(QtCore.QRect(420, 15, 100, 20))
        self.le_filterByCompany.setMaxLength(32)
        self.le_filterByCompany.setObjectName("le_filterByCompany")
        self.le_filterByCompany.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByProduct = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByProduct.setGeometry(QtCore.QRect(520, 15, 100, 20))
        self.le_filterByProduct.setMaxLength(32)
        self.le_filterByProduct.setObjectName("le_filterByProduct")
        self.le_filterByProduct.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByEngine = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByEngine.setGeometry(QtCore.QRect(620, 15, 100, 20))
        self.le_filterByEngine.setMaxLength(32)
        self.le_filterByEngine.setObjectName("le_filterByEngine")
        self.le_filterByEngine.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByChassis = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByChassis.setGeometry(QtCore.QRect(720, 15, 100, 20))
        self.le_filterByChassis.setMaxLength(32)
        self.le_filterByChassis.setObjectName("le_filterByChassis")
        self.le_filterByChassis.textChanged.connect(self.filterPurchaseReport)

        self.le_filterBySalePrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterBySalePrice.setGeometry(QtCore.QRect(920, 15, 100, 20))
        self.le_filterBySalePrice.setMaxLength(32)
        self.le_filterBySalePrice.setObjectName("le_filterBySalePrice")
        self.le_filterBySalePrice.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByDiscount = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDiscount.setGeometry(QtCore.QRect(1020, 15, 100, 20))
        self.le_filterByDiscount.setMaxLength(32)
        self.le_filterByDiscount.setObjectName("le_filterByDiscount")
        self.le_filterByDiscount.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByTotalPrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByTotalPrice.setGeometry(QtCore.QRect(1120, 15, 100, 20))
        self.le_filterByTotalPrice.setMaxLength(32)
        self.le_filterByTotalPrice.setObjectName("le_filterByTotalPrice")
        self.le_filterByTotalPrice.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByRemarks = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByRemarks.setGeometry(QtCore.QRect(1220, 15, 100, 20))
        self.le_filterByRemarks.setMaxLength(32)
        self.le_filterByRemarks.setObjectName("le_filterByRemarks")
        self.le_filterByRemarks.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByInvoice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByInvoice.setGeometry(QtCore.QRect(20, 15, 100, 20))
        self.le_filterByInvoice.setMaxLength(32)
        self.le_filterByInvoice.setObjectName("le_filterByInvoice")
        self.le_filterByInvoice.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByCostPrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCostPrice.setGeometry(QtCore.QRect(820, 15, 100, 20))
        self.le_filterByCostPrice.setMaxLength(32)
        self.le_filterByCostPrice.setObjectName("le_filterByCostPrice")
        self.le_filterByCostPrice.textChanged.connect(self.filterPurchaseReport)
        
        self.startCalendar = QtWidgets.QCalendarWidget(self.purchaseReportGB)
        self.startCalendar.setGeometry(QtCore.QRect(20, 90, 312, 183))
        self.startCalendar.setObjectName("startCalendar")
        self.startCalendar.hide()
        self.startCalendar.clicked[QtCore.QDate].connect(self.setStartDate)
        
        self.endCalendar = QtWidgets.QCalendarWidget(self.purchaseReportGB)
        self.endCalendar.setGeometry(QtCore.QRect(20, 90, 312, 183))
        self.endCalendar.setObjectName("endCalendar")
        self.endCalendar.hide()
        self.endCalendar.clicked[QtCore.QDate].connect(self.setEndDate)
        
        self.searchGB = QtWidgets.QGroupBox(self.centralwidget)
        self.searchGB.setGeometry(QtCore.QRect(16, 15, 1341, 75))
        self.searchGB.setObjectName("searchGB")
        self.le_totalDiscount = QtWidgets.QLineEdit(self.searchGB)
        self.le_totalDiscount.setEnabled(False)
        self.le_totalDiscount.setGeometry(QtCore.QRect(1070, 40, 150, 28))
        self.le_totalDiscount.setObjectName("le_totalDiscount")

        self.le_totalPurchase = QtWidgets.QLineEdit(self.searchGB)
        self.le_totalPurchase.setEnabled(False)
        self.le_totalPurchase.setGeometry(QtCore.QRect(810, 10, 150, 28))
        self.le_totalPurchase.setObjectName("le_totalPurchase")
        self.le_startDate = QtWidgets.QLineEdit(self.searchGB)
        self.le_startDate.setEnabled(False)
        self.le_startDate.setGeometry(QtCore.QRect(80, 10, 150, 28))
        self.le_startDate.setPlaceholderText("")
        self.le_startDate.setObjectName("le_startDate")
        self.le_netPurchase = QtWidgets.QLineEdit(self.searchGB)
        self.le_netPurchase.setEnabled(False)
        self.le_netPurchase.setGeometry(QtCore.QRect(810, 40, 150, 28))
        self.le_netPurchase.setObjectName("le_netPurchase")
        self.label = QtWidgets.QLabel(self.searchGB)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.btn_refresh = QtWidgets.QPushButton(self.searchGB)
        self.btn_refresh.setGeometry(QtCore.QRect(1235, 40, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getPurchaseReportByDate)
        
        self.label_2 = QtWidgets.QLabel(self.searchGB)
        self.label_2.setGeometry(QtCore.QRect(700, 10, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.searchGB)
        self.label_3.setGeometry(QtCore.QRect(970, 40, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.searchGB)
        self.label_4.setGeometry(QtCore.QRect(700, 40, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.btn_serach = QtWidgets.QPushButton(self.searchGB)
        self.btn_serach.setGeometry(QtCore.QRect(280, 40, 100, 28))
        searchIcon = QtGui.QPixmap(globalVariables.Variables._icon+'searchIcon.png')
        self.btn_serach.setIcon(QtGui.QIcon(searchIcon))
        self.btn_serach.setObjectName("btn_serach")
        self.btn_serach.clicked.connect(self.getPurchaseReportByDate)
        
        self.btn_startDate = QtWidgets.QPushButton(self.searchGB)
        self.btn_startDate.setGeometry(QtCore.QRect(230, 10, 41, 28))
        self.btn_startDate.setIcon(QtGui.QIcon(dateIcon))
        self.btn_startDate.setObjectName("btn_startDate")
        self.btn_startDate.clicked.connect(self.displayStartCalendar)
        
        self.btn_endDate = QtWidgets.QPushButton(self.searchGB)
        self.btn_endDate.setGeometry(QtCore.QRect(230, 40, 41, 28))
        self.btn_endDate.setIcon(QtGui.QIcon(dateIcon))
        self.btn_endDate.setObjectName("btn_endDate")
        self.btn_endDate.clicked.connect(self.displayEndCalendar)
        
        self.le_endDate = QtWidgets.QLineEdit(self.searchGB)
        self.le_endDate.setEnabled(False)
        self.le_endDate.setGeometry(QtCore.QRect(80, 40, 150, 28))
        self.le_endDate.setPlaceholderText("")
        self.le_endDate.setObjectName("le_endDate")
        self.label_5 = QtWidgets.QLabel(self.searchGB)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.btn_print = QtWidgets.QPushButton(self.searchGB)
        self.btn_print.setGeometry(QtCore.QRect(1235, 10, 100, 28))
        printIcon = QtGui.QPixmap(globalVariables.Variables._icon+'printIcon.png')
        self.btn_print.setIcon(QtGui.QIcon(printIcon))
        self.btn_print.setObjectName("btn_print")
        
        self.le_itemDiscount = QtWidgets.QLineEdit(self.searchGB)
        self.le_itemDiscount.setEnabled(False)
        self.le_itemDiscount.setGeometry(QtCore.QRect(1070, 10, 150, 28))
        self.le_itemDiscount.setObjectName("le_itemDiscount")
        self.label_6 = QtWidgets.QLabel(self.searchGB)
        self.label_6.setGeometry(QtCore.QRect(970, 10, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        purchaseReportByDateWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(purchaseReportByDateWindow)
        self.statusbar.setObjectName("statusbar")
        purchaseReportByDateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(purchaseReportByDateWindow)
        QtCore.QMetaObject.connectSlotsByName(purchaseReportByDateWindow)

    def retranslateUi(self, purchaseReportByDateWindow):
        _translate = QtCore.QCoreApplication.translate
        purchaseReportByDateWindow.setWindowTitle(_translate("purchaseReportByDateWindow", "Purchase Report By Date"))
        self.purchaseReportGB.setTitle(_translate("purchaseReportByDateWindow", "Purchase Report "))
        self.filterGB.setTitle(_translate("purchaseReportByDateWindow", "Filter"))
        self.le_filterByDate.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Date"))
        self.le_filterByName.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Name"))
        self.le_filterByMobile.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Mobile"))
        self.le_filterByCompany.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Company"))
        self.le_filterByProduct.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Product"))
        self.le_filterByEngine.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Engine"))
        self.le_filterByChassis.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Chassis"))
        self.le_filterBySalePrice.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Sale Price"))
        self.le_filterByDiscount.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Discount"))
        self.le_filterByTotalPrice.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Total Price"))
        self.le_filterByRemarks.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Remarks"))
        self.le_filterByInvoice.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Invoice"))
        self.le_filterByCostPrice.setPlaceholderText(_translate("purchaseReportByDateWindow", "Filter By Cost Price"))
        self.searchGB.setTitle(_translate("purchaseReportByDateWindow", "Search By Date"))
        self.label.setText(_translate("purchaseReportByDateWindow", "Date From"))
        self.btn_refresh.setText(_translate("purchaseReportByDateWindow", "Refresh"))
        self.label_2.setText(_translate("purchaseReportByDateWindow", "Total Purchases"))
        self.label_3.setText(_translate("purchaseReportByDateWindow", "Total Discount"))
        self.label_4.setText(_translate("purchaseReportByDateWindow", "Net Purchases"))
        self.btn_serach.setText(_translate("purchaseReportByDateWindow", "Search"))
        self.label_5.setText(_translate("purchaseReportByDateWindow", "Datet To"))
        self.btn_print.setText(_translate("purchaseReportByDateWindow", "Print"))
        self.label_6.setText(_translate("purchaseReportByDateWindow", "Item Discount"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    purchaseReportByDateWindow = QtWidgets.QMainWindow()
    ui = Ui_purchaseReportByDateWindow()
    ui.purchaseReportByDateSetupUi(purchaseReportByDateWindow)
    purchaseReportByDateWindow.show()
    sys.exit(app.exec_())

