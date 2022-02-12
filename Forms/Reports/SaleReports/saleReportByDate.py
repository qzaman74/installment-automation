
from BLL.ReportsBL.SaleReportsBL import saleReportByDateBL
from Globals import globalVariables
from Services.MiscService import dateTime
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_saleReportByDateWindow(object):

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


    def getSaleReportByDate(self):
        try:
            startDate = self.le_startDate.text()
            endDate = self.le_endDate.text()
            billType = globalVariables.Variables._sale

            resultReport = saleReportByDateBL.validateSaleReportDates(startDate,endDate)
            resultBill = saleReportByDateBL.validateSaleBillByDate(startDate,endDate,billType)
            self._filterList = saleReportByDateBL.validateSaleReportDates(startDate,endDate).fetchall().copy()

            self.setSaleBillByDate(resultBill)
            self.setSaleReportByDate(resultReport)
        except:
            pass

    def setSaleBillByDate(self, result):
        try:
            for item in result:
                self.le_totalSale.setText(str(item[0]))
                self.le_totalDiscount.setText(str(item[1]))
                self.le_netSale.setText(str(item[2]))

        except:
            pass

    def setSaleReportByDate(self,result):
        self.tbl_saleReportByDate.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_saleReportByDate.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if(colum_number == 1):
                    self.tbl_saleReportByDate.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(dateTime.getDateWithoutTime(data))))
                else:
                    self.tbl_saleReportByDate.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))




    def filterFunc(self,item):
        invoice = self.le_filterByInvoice.text()
        date = self.le_filterByDate.text()
        name = self.le_filterByName.text()
        mobile = self.le_filterByMobile.text()
        company = self.le_filterByCompany.text()
        product = self.le_filterByProduct.text()
        engine = self.le_filterByEngine.text()
        chassis = self.le_filterByChassis.text()
        salePrice = self.le_filterBySalePrice.text()
        saleAmount = self.le_filterBySaleAmount.text()
        discount = self.le_filterByDiscount.text()
        totalPrice = self.le_filterByTotalPrice.text()
        remarks = self.le_filterByRemarks.text()

        if (str(item[0]).startswith(invoice) and str(item[1]).startswith(date) and
            str(item[2]).lower().startswith(name) and str(item[3]).startswith(mobile) and
            str(item[4]).lower().startswith(company) and str(item[5]).lower().startswith(product) and
            str(item[6]).startswith(engine) and str(item[7]).startswith(chassis)  and
            str(item[8]).startswith(salePrice) and str(item[9]).startswith(saleAmount)  and
            str(item[10]).startswith(discount) and str(item[11]).startswith(totalPrice) and
            str(item[12]).lower().startswith(remarks) ):
            return True
        else:
            return False

    def filterSaleReport(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.setSaleReportByDate(result)



    def saleReportByDateSetupUi(self, saleReportByDateWindow):
        saleReportByDateWindow.setObjectName("saleReportByDateWindow")
        saleReportByDateWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        saleReportByDateWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        saleReportByDateWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        saleReportByDateWindow.setAutoFillBackground(True)

        dateIcon = QtGui.QPixmap(globalVariables.Variables._icon+'calendarIcon.png')
        
        self.centralwidget = QtWidgets.QWidget(saleReportByDateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saleReportGB = QtWidgets.QGroupBox(self.centralwidget)
        self.saleReportGB.setGeometry(QtCore.QRect(5, 0, 1355, 685))
        self.saleReportGB.setObjectName("saleReportGB")
        self.tbl_saleReportByDate = QtWidgets.QTableWidget(self.saleReportGB)
        self.tbl_saleReportByDate.setGeometry(QtCore.QRect(10, 135, 1340, 541))
        self.tbl_saleReportByDate.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_saleReportByDate.setShowGrid(True)
        self.tbl_saleReportByDate.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_saleReportByDate.setWordWrap(True)
        self.tbl_saleReportByDate.setRowCount(17)
        self.tbl_saleReportByDate.setColumnCount(13)
        self.tbl_saleReportByDate.setHorizontalHeaderLabels(['Invoice','Date','Name','Mobile','Company',
                                                                 'Product','Engine','Chassis','Sale Price','Sale Amount',
                                                                 'Discount','Total Price','Remarks'])
        self.tbl_saleReportByDate.setObjectName("tbl_saleReportByDate")


        self.filterGB = QtWidgets.QGroupBox(self.saleReportGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 90, 1341, 41))
        self.filterGB.setObjectName("filterGB")


        self.le_filterByDate = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDate.setGeometry(QtCore.QRect(120, 15, 100, 20))
        self.le_filterByDate.setMaxLength(32)
        self.le_filterByDate.setObjectName("le_filterByDate")
        self.le_filterByDate.textChanged.connect(self.filterSaleReport)

        self.le_filterByName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByName.setGeometry(QtCore.QRect(220, 15, 100, 20))
        self.le_filterByName.setMaxLength(32)
        self.le_filterByName.setObjectName("le_filterByName")
        self.le_filterByName.textChanged.connect(self.filterSaleReport)

        self.le_filterByMobile = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByMobile.setGeometry(QtCore.QRect(320, 15, 100, 20))
        self.le_filterByMobile.setMaxLength(32)
        self.le_filterByMobile.setObjectName("le_filterByMobile")
        self.le_filterByMobile.textChanged.connect(self.filterSaleReport)

        self.le_filterByCompany = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompany.setGeometry(QtCore.QRect(420, 15, 100, 20))
        self.le_filterByCompany.setMaxLength(32)
        self.le_filterByCompany.setObjectName("le_filterByCompany")
        self.le_filterByCompany.textChanged.connect(self.filterSaleReport)

        self.le_filterByProduct = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByProduct.setGeometry(QtCore.QRect(520, 15, 100, 20))
        self.le_filterByProduct.setMaxLength(32)
        self.le_filterByProduct.setObjectName("le_filterByProduct")
        self.le_filterByProduct.textChanged.connect(self.filterSaleReport)

        self.le_filterByEngine = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByEngine.setGeometry(QtCore.QRect(620, 15, 100, 20))
        self.le_filterByEngine.setMaxLength(32)
        self.le_filterByEngine.setObjectName("le_filterByEngine")
        self.le_filterByEngine.textChanged.connect(self.filterSaleReport)

        self.le_filterByChassis = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByChassis.setGeometry(QtCore.QRect(720, 15, 100, 20))
        self.le_filterByChassis.setMaxLength(32)
        self.le_filterByChassis.setObjectName("le_filterByChassis")
        self.le_filterByChassis.textChanged.connect(self.filterSaleReport)

        self.le_filterBySalePrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterBySalePrice.setGeometry(QtCore.QRect(820, 15, 100, 20))
        self.le_filterBySalePrice.setMaxLength(32)
        self.le_filterBySalePrice.setObjectName("le_filterBySalePrice")
        self.le_filterBySalePrice.textChanged.connect(self.filterSaleReport)

        self.le_filterBySaleAmount = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterBySaleAmount.setGeometry(QtCore.QRect(920, 15, 100, 20))
        self.le_filterBySaleAmount.setMaxLength(32)
        self.le_filterBySaleAmount.setObjectName("le_filterBySaleAmount")
        self.le_filterBySaleAmount.textChanged.connect(self.filterSaleReport)

        self.le_filterByDiscount = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDiscount.setGeometry(QtCore.QRect(1020, 15, 100, 20))
        self.le_filterByDiscount.setMaxLength(32)
        self.le_filterByDiscount.setObjectName("le_filterByDiscount")
        self.le_filterByDiscount.textChanged.connect(self.filterSaleReport)

        self.le_filterByTotalPrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByTotalPrice.setGeometry(QtCore.QRect(1120, 15, 100, 20))
        self.le_filterByTotalPrice.setMaxLength(32)
        self.le_filterByTotalPrice.setObjectName("le_filterByTotalPrice")
        self.le_filterByTotalPrice.textChanged.connect(self.filterSaleReport)

        self.le_filterByRemarks = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByRemarks.setGeometry(QtCore.QRect(1220, 15, 100, 20))
        self.le_filterByRemarks.setMaxLength(32)
        self.le_filterByRemarks.setObjectName("le_filterByRemarks")
        self.le_filterByRemarks.textChanged.connect(self.filterSaleReport)

        self.le_filterByInvoice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByInvoice.setGeometry(QtCore.QRect(20, 15, 100, 20))
        self.le_filterByInvoice.setMaxLength(32)
        self.le_filterByInvoice.setObjectName("le_filterByInvoice")
        self.le_filterByInvoice.textChanged.connect(self.filterSaleReport)


        self.startCalendar = QtWidgets.QCalendarWidget(self.saleReportGB)
        self.startCalendar.setGeometry(QtCore.QRect(20, 90, 312, 183))
        self.startCalendar.setObjectName("startCalendar")
        self.startCalendar.hide()
        self.startCalendar.clicked[QtCore.QDate].connect(self.setStartDate)

        self.endCalendar = QtWidgets.QCalendarWidget(self.saleReportGB)
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
        self.le_totalSale = QtWidgets.QLineEdit(self.searchGB)
        self.le_totalSale.setEnabled(False)
        self.le_totalSale.setGeometry(QtCore.QRect(810, 10, 150, 28))
        self.le_totalSale.setObjectName("le_totalSale")
        self.le_startDate = QtWidgets.QLineEdit(self.searchGB)
        self.le_startDate.setEnabled(False)
        self.le_startDate.setGeometry(QtCore.QRect(80, 10, 150, 28))
        self.le_startDate.setPlaceholderText("")
        self.le_startDate.setObjectName("le_startDate")
        self.le_netSale = QtWidgets.QLineEdit(self.searchGB)
        self.le_netSale.setEnabled(False)
        self.le_netSale.setGeometry(QtCore.QRect(810, 40, 150, 28))
        self.le_netSale.setObjectName("le_netSale")
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
        self.btn_refresh.clicked.connect(self.getSaleReportByDate)

        self.label_2 = QtWidgets.QLabel(self.searchGB)
        self.label_2.setGeometry(QtCore.QRect(740, 10, 71, 28))
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
        self.label_4.setGeometry(QtCore.QRect(740, 40, 71, 28))
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
        self.btn_serach.clicked.connect(self.getSaleReportByDate)

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
        saleReportByDateWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(saleReportByDateWindow)
        self.statusbar.setObjectName("statusbar")
        saleReportByDateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(saleReportByDateWindow)
        QtCore.QMetaObject.connectSlotsByName(saleReportByDateWindow)

    def retranslateUi(self, saleReportByDateWindow):
        _translate = QtCore.QCoreApplication.translate
        saleReportByDateWindow.setWindowTitle(_translate("saleReportByDateWindow", "Sale Report By Date"))
        self.saleReportGB.setTitle(_translate("saleReportByDateWindow", "Sale Report "))
        self.filterGB.setTitle(_translate("saleReportByDateWindow", "Filter"))
        self.le_filterByDate.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Date"))
        self.le_filterByName.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Name"))
        self.le_filterByMobile.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Mobile"))
        self.le_filterByCompany.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Company"))
        self.le_filterByProduct.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Product"))
        self.le_filterByEngine.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Engine"))
        self.le_filterByChassis.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Chassis"))
        self.le_filterBySalePrice.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Sale Price"))
        self.le_filterByDiscount.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Discount"))
        self.le_filterByTotalPrice.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Total Price"))
        self.le_filterByRemarks.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Remarks"))
        self.le_filterByInvoice.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Invoice"))
        self.le_filterBySaleAmount.setPlaceholderText(_translate("saleReportByDateWindow", "Filter By Sale Amount"))
        self.searchGB.setTitle(_translate("saleReportByDateWindow", "Search By Date"))
        self.label.setText(_translate("saleReportByDateWindow", "Date From"))
        self.btn_refresh.setText(_translate("saleReportByDateWindow", "Refresh"))
        self.label_2.setText(_translate("saleReportByDateWindow", "Total Sale"))
        self.label_3.setText(_translate("saleReportByDateWindow", "Total Discount"))
        self.label_4.setText(_translate("saleReportByDateWindow", "Net Sale"))
        self.btn_serach.setText(_translate("saleReportByDateWindow", "Search"))
        self.label_5.setText(_translate("saleReportByDateWindow", "Datet To"))
        self.btn_print.setText(_translate("saleReportByDateWindow", "Print"))
        self.label_6.setText(_translate("saleReportByDateWindow", "Item Discount"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saleReportByDateWindow = QtWidgets.QMainWindow()
    ui = Ui_saleReportByDateWindow()
    ui.saleReportByDateSetupUi(saleReportByDateWindow)
    saleReportByDateWindow.show()
    sys.exit(app.exec_())

