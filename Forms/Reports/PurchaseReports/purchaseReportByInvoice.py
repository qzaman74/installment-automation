
from PyQt5 import QtCore, QtGui, QtWidgets
from BLL.ReportsBL.PurchaseReportsBL import purchaseReportByInvoiceBL

from Globals import globalVariables
from Services.MiscService import dateTime

class Ui_purchaseReportByInvoiceWindow(object):
    _filterList = None

    def init(self):
        self.le_searchByInvoice.setFocus()

    def getPurchaseByInvoice(self):
        invoice = self.le_searchByInvoice.text()
        billType = globalVariables.Variables._purchase
        if(invoice != ''):
            resultBill = purchaseReportByInvoiceBL.validateBillInvoice(invoice, billType)
            resultPurchase = purchaseReportByInvoiceBL.validatePurchaseInvoice(invoice, billType)
            self._filterList = purchaseReportByInvoiceBL.validatePurchaseInvoice(invoice, billType).fetchall().copy()

            self.showBillBYInvoice(resultBill)
            self.showPurchaseBYInvoice(resultPurchase)

    def showBillBYInvoice(self, result):
        try:
            for x in result:
                self.le_name.setText(x[0])
                self.le_fatherName.setText(x[1])
                self.le_cnic.setText(x[2])
                self.le_mobile.setText(x[3])
                self.le_totalSale.setText(str(x[4]))
                self.le_totalDiscount.setText(str(x[5]))
                self.le_netSale.setText(str(x[6]))
                self.le_balance.setText(str(x[7]))
                self.le_date.setText(str(dateTime.getDateWithoutTime(x[8])))
        except:
            pass

    def showPurchaseBYInvoice(self, result):
        try:
            discount = 0
            self.tbl_purchaseReportByInvoice.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tbl_purchaseReportByInvoice.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    if(colum_number == 6):
                        discount = discount + int(data)
                    self.tbl_purchaseReportByInvoice.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))


            self.le_itemDiscount.setText(str(discount))
        except:
            pass



    def filterFunc(self,item):
        company = self.le_filterByCompany.text()
        product = self.le_filterByProduct.text()
        engine = self.le_filterByEngine.text()
        chassis = self.le_filterByChassis.text()
        costPrice = self.le_filterByCostPrice.text()
        salePrice = self.le_filterBySalePrice.text()
        discount = self.le_filterByDiscount.text()
        totalPrice = self.le_filterByTotalPrice.text()
        remarks = self.le_filterByRemarks.text()

        if (str(item[0]).lower().startswith(company) and str(item[1]).startswith(product) and
            str(item[2]).startswith(engine) and str(item[3]).startswith(chassis)  and
            str(item[4]).startswith(costPrice) and str(item[5]).startswith(salePrice)  and
            str(item[6]).startswith(discount) and str(item[7]).startswith(totalPrice) and
            str(item[8]).lower().startswith(remarks) ):
            return True
        else:
            return False

    def filterPurchaseReport(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.showPurchaseBYInvoice(result)



    def purchaseReportByInvoiceetupUi(self, purchaseReportByInvoiceWindow):
        purchaseReportByInvoiceWindow.setObjectName("purchaseReportByInvoiceWindow")
        purchaseReportByInvoiceWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        purchaseReportByInvoiceWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        purchaseReportByInvoiceWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        purchaseReportByInvoiceWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(purchaseReportByInvoiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.purchaseGB = QtWidgets.QGroupBox(self.centralwidget)
        self.purchaseGB.setGeometry(QtCore.QRect(5, 0, 1360, 685))
        self.purchaseGB.setObjectName("purchaseGB")
        self.tbl_purchaseReportByInvoice = QtWidgets.QTableWidget(self.purchaseGB)
        self.tbl_purchaseReportByInvoice.setGeometry(QtCore.QRect(10, 140, 1340, 535))
        self.tbl_purchaseReportByInvoice.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_purchaseReportByInvoice.setShowGrid(True)
        self.tbl_purchaseReportByInvoice.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_purchaseReportByInvoice.setWordWrap(True)
        self.tbl_purchaseReportByInvoice.setRowCount(16)
        self.tbl_purchaseReportByInvoice.setColumnCount(9)
        self.tbl_purchaseReportByInvoice.setHorizontalHeaderLabels(['Company', 'Product', 'Engine', 'Chassis',
                                                                    'Cost Price', 'Sale Price', 'Discount',
                                                                    'Total Price', 'Remarks'])
        self.tbl_purchaseReportByInvoice.setColumnWidth(0,200)
        self.tbl_purchaseReportByInvoice.setColumnWidth(1,200)
        self.tbl_purchaseReportByInvoice.setColumnWidth(8,300)
        self.tbl_purchaseReportByInvoice.setObjectName("tbl_purchaseReportByInvoice")
        self.filterGB = QtWidgets.QGroupBox(self.purchaseGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 95, 1341, 41))
        self.filterGB.setObjectName("filterGB")

        self.le_filterByCompany = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompany.setGeometry(QtCore.QRect(0, 20, 230, 20))
        self.le_filterByCompany.setMaxLength(32)
        self.le_filterByCompany.setObjectName("le_filterByCompany")
        self.le_filterByCompany.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByProduct = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByProduct.setGeometry(QtCore.QRect(230, 20, 200, 20))
        self.le_filterByProduct.setMaxLength(32)
        self.le_filterByProduct.setObjectName("le_filterByProduct")
        self.le_filterByProduct.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByEngine = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByEngine.setGeometry(QtCore.QRect(430, 20, 100, 20))
        self.le_filterByEngine.setMaxLength(32)
        self.le_filterByEngine.setObjectName("le_filterByEngine")
        self.le_filterByEngine.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByChassis = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByChassis.setGeometry(QtCore.QRect(530, 20, 100, 20))
        self.le_filterByChassis.setMaxLength(32)
        self.le_filterByChassis.setObjectName("le_filterByChassis")
        self.le_filterByChassis.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByCostPrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCostPrice.setGeometry(QtCore.QRect(630, 20, 100, 20))
        self.le_filterByCostPrice.setMaxLength(32)
        self.le_filterByCostPrice.setObjectName("le_filterByCostPrice")
        self.le_filterByCostPrice.textChanged.connect(self.filterPurchaseReport)

        self.le_filterBySalePrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterBySalePrice.setGeometry(QtCore.QRect(730, 20, 100, 20))
        self.le_filterBySalePrice.setMaxLength(32)
        self.le_filterBySalePrice.setObjectName("le_filterBySalePrice")
        self.le_filterBySalePrice.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByDiscount = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDiscount.setGeometry(QtCore.QRect(830, 20, 100, 20))
        self.le_filterByDiscount.setMaxLength(32)
        self.le_filterByDiscount.setObjectName("le_filterByDiscount")
        self.le_filterByDiscount.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByTotalPrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByTotalPrice.setGeometry(QtCore.QRect(930, 20, 100, 20))
        self.le_filterByTotalPrice.setMaxLength(32)
        self.le_filterByTotalPrice.setObjectName("le_filterByTotalPrice")
        self.le_filterByTotalPrice.textChanged.connect(self.filterPurchaseReport)

        self.le_filterByRemarks = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByRemarks.setGeometry(QtCore.QRect(1030, 20, 310, 20))
        self.le_filterByRemarks.setMaxLength(32)
        self.le_filterByRemarks.setObjectName("le_filterByRemarks")
        self.le_filterByRemarks.textChanged.connect(self.filterPurchaseReport)

        self.searchGB = QtWidgets.QGroupBox(self.purchaseGB)
        self.searchGB.setGeometry(QtCore.QRect(10, 20, 1341, 75))
        self.searchGB.setObjectName("searchGB")
        self.le_searchByInvoice = QtWidgets.QLineEdit(self.searchGB)
        self.le_searchByInvoice.setGeometry(QtCore.QRect(10, 40, 100, 28))
        self.le_searchByInvoice.setObjectName("le_searchByInvoice")
        self.le_searchByInvoice.returnPressed.connect(self.getPurchaseByInvoice)

        self.label = QtWidgets.QLabel(self.searchGB)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.btn_serach = QtWidgets.QPushButton(self.searchGB)
        self.btn_serach.setGeometry(QtCore.QRect(110, 40, 100, 28))
        searchIcon = QtGui.QPixmap(globalVariables.Variables._icon+'searchIcon.png')
        self.btn_serach.setIcon(QtGui.QIcon(searchIcon))
        self.btn_serach.setObjectName("btn_serach")
        self.btn_serach.clicked.connect(self.getPurchaseByInvoice)

        self.le_totalSale = QtWidgets.QLineEdit(self.searchGB)
        self.le_totalSale.setEnabled(False)
        self.le_totalSale.setGeometry(QtCore.QRect(350, 40, 100, 28))
        self.le_totalSale.setObjectName("le_totalSale")
        self.le_itemDiscount = QtWidgets.QLineEdit(self.searchGB)
        self.le_itemDiscount.setEnabled(False)
        self.le_itemDiscount.setGeometry(QtCore.QRect(570, 40, 100, 28))
        self.le_itemDiscount.setObjectName("le_itemDiscount")

        self.btn_refresh = QtWidgets.QPushButton(self.searchGB)
        self.btn_refresh.setGeometry(QtCore.QRect(1235, 40, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getPurchaseByInvoice)

        self.btn_print = QtWidgets.QPushButton(self.searchGB)
        self.btn_print.setGeometry(QtCore.QRect(1235, 10, 100, 28))
        printIcon = QtGui.QPixmap(globalVariables.Variables._icon+'printIcon.png')
        self.btn_print.setIcon(QtGui.QIcon(printIcon))
        self.btn_print.setObjectName("btn_print")

        self.label_6 = QtWidgets.QLabel(self.searchGB)
        self.label_6.setGeometry(QtCore.QRect(470, 40, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.searchGB)
        self.label_4.setGeometry(QtCore.QRect(890, 40, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.searchGB)
        self.label_2.setGeometry(QtCore.QRect(280, 40, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.le_netSale = QtWidgets.QLineEdit(self.searchGB)
        self.le_netSale.setEnabled(False)
        self.le_netSale.setGeometry(QtCore.QRect(960, 40, 100, 28))
        self.le_netSale.setObjectName("le_netSale")
        self.le_totalDiscount = QtWidgets.QLineEdit(self.searchGB)
        self.le_totalDiscount.setEnabled(False)
        self.le_totalDiscount.setGeometry(QtCore.QRect(780, 40, 100, 28))
        self.le_totalDiscount.setObjectName("le_totalDiscount")
        self.label_3 = QtWidgets.QLabel(self.searchGB)
        self.label_3.setGeometry(QtCore.QRect(680, 40, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.searchGB)
        self.label_5.setGeometry(QtCore.QRect(470, 10, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.le_cnic = QtWidgets.QLineEdit(self.searchGB)
        self.le_cnic.setEnabled(False)
        self.le_cnic.setGeometry(QtCore.QRect(960, 10, 100, 28))
        self.le_cnic.setText("")
        self.le_cnic.setObjectName("le_cnic")
        self.label_7 = QtWidgets.QLabel(self.searchGB)
        self.label_7.setGeometry(QtCore.QRect(680, 10, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.le_name = QtWidgets.QLineEdit(self.searchGB)
        self.le_name.setEnabled(False)
        self.le_name.setGeometry(QtCore.QRect(570, 10, 100, 28))
        self.le_name.setText("")
        self.le_name.setObjectName("le_name")
        self.le_mobile = QtWidgets.QLineEdit(self.searchGB)
        self.le_mobile.setEnabled(False)
        self.le_mobile.setGeometry(QtCore.QRect(1130, 10, 100, 28))
        self.le_mobile.setText("")
        self.le_mobile.setObjectName("le_mobile")
        self.label_8 = QtWidgets.QLabel(self.searchGB)
        self.label_8.setGeometry(QtCore.QRect(910, 10, 51, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.searchGB)
        self.label_9.setGeometry(QtCore.QRect(1070, 10, 61, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.le_fatherName = QtWidgets.QLineEdit(self.searchGB)
        self.le_fatherName.setEnabled(False)
        self.le_fatherName.setGeometry(QtCore.QRect(780, 10, 100, 28))
        self.le_fatherName.setText("")
        self.le_fatherName.setObjectName("le_fatherName")
        self.label_10 = QtWidgets.QLabel(self.searchGB)
        self.label_10.setGeometry(QtCore.QRect(1070, 40, 61, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.searchGB)
        self.label_11.setGeometry(QtCore.QRect(310, 10, 41, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.le_balance = QtWidgets.QLineEdit(self.searchGB)
        self.le_balance.setEnabled(False)
        self.le_balance.setGeometry(QtCore.QRect(1130, 40, 100, 28))
        self.le_balance.setText("")
        self.le_balance.setObjectName("le_balance")
        self.le_date = QtWidgets.QLineEdit(self.searchGB)
        self.le_date.setEnabled(False)
        self.le_date.setGeometry(QtCore.QRect(350, 10, 100, 28))
        self.le_date.setText("")
        self.le_date.setObjectName("le_date")
        purchaseReportByInvoiceWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(purchaseReportByInvoiceWindow)
        self.statusbar.setObjectName("statusbar")
        purchaseReportByInvoiceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(purchaseReportByInvoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(purchaseReportByInvoiceWindow)

    def retranslateUi(self, purchaseReportByInvoiceWindow):
        _translate = QtCore.QCoreApplication.translate
        purchaseReportByInvoiceWindow.setWindowTitle(_translate("purchaseReportByInvoiceWindow", "Purchase Report By Invoice"))
        self.purchaseGB.setTitle(_translate("purchaseReportByInvoiceWindow", "Purchase Report "))
        self.filterGB.setTitle(_translate("purchaseReportByInvoiceWindow", "Filter"))
        self.le_filterByCompany.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Filter BY Company"))
        self.le_filterByEngine.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Filter BY Engine"))
        self.le_filterByChassis.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Filter BY Chassis"))
        self.le_filterByProduct.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Filter BY Product"))
        self.le_filterByRemarks.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Filter BY Remarks"))
        self.le_filterByDiscount.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Filter BY Discount"))
        self.le_filterByCostPrice.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Filter BY Cost Price"))
        self.le_filterBySalePrice.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Filter BY Sale Price"))
        self.le_filterByTotalPrice.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Filter BY Total Amount"))
        self.searchGB.setTitle(_translate("purchaseReportByInvoiceWindow", "Search Invoice"))
        self.le_searchByInvoice.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Enter Invoice"))
        self.label.setText(_translate("purchaseReportByInvoiceWindow", "Search :"))
        self.btn_serach.setText(_translate("purchaseReportByInvoiceWindow", "Search"))
        self.le_totalSale.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Total Sale"))
        self.le_itemDiscount.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Discount On Item"))
        self.btn_refresh.setText(_translate("purchaseReportByInvoiceWindow", "Refresh"))
        self.btn_print.setText(_translate("purchaseReportByInvoiceWindow", "Print"))
        self.label_6.setText(_translate("purchaseReportByInvoiceWindow", "Item Discount"))
        self.label_4.setText(_translate("purchaseReportByInvoiceWindow", "Net Sale"))
        self.label_2.setText(_translate("purchaseReportByInvoiceWindow", "Total Sale"))
        self.le_netSale.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Total Sale"))
        self.le_totalDiscount.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Discount Bill"))
        self.label_3.setText(_translate("purchaseReportByInvoiceWindow", "Total Discount"))
        self.label_5.setText(_translate("purchaseReportByInvoiceWindow", "Account Name"))
        self.le_cnic.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "CNIC"))
        self.label_7.setText(_translate("purchaseReportByInvoiceWindow", "Father Name"))
        self.le_name.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Account Name"))
        self.le_mobile.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Mobile Number"))
        self.label_8.setText(_translate("purchaseReportByInvoiceWindow", "CNIC"))
        self.label_9.setText(_translate("purchaseReportByInvoiceWindow", "Mobile :"))
        self.le_fatherName.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Father Name"))
        self.label_10.setText(_translate("purchaseReportByInvoiceWindow", "Balance:"))
        self.label_11.setText(_translate("purchaseReportByInvoiceWindow", "Date"))
        self.le_balance.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Remining Balance"))
        self.le_date.setPlaceholderText(_translate("purchaseReportByInvoiceWindow", "Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    purchaseReportByInvoiceWindow = QtWidgets.QMainWindow()
    ui = Ui_purchaseReportByInvoiceWindow()
    ui.purchaseReportByInvoiceetupUi(purchaseReportByInvoiceWindow)
    purchaseReportByInvoiceWindow.show()
    sys.exit(app.exec_())

