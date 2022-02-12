# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saleReportByInvoice.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BLL.ReportsBL.SaleReportsBL import saleReportByInvoiceBL
from Services.MiscService import dateTime
from Globals import globalVariables

class Ui_saleReportByInvoiceWindow(object):
    _filterList = None

    def init(self):
        self.le_searchByInvoice.setFocus()

    def getSaleByInvoice(self):
        invoice = self.le_searchByInvoice.text()
        if(invoice != ''):
            billType = globalVariables.Variables._sale

            resultBill = saleReportByInvoiceBL.validateBillInvoice(invoice,billType)
            resultSale = saleReportByInvoiceBL.validateSaleInvoice(invoice,billType)
            self._filterList = saleReportByInvoiceBL.validateSaleInvoice(invoice,billType).fetchall().copy()

            self.showBillBYInvoice(resultBill)
            self.showSaleBYInvoice(resultSale)

    def showBillBYInvoice(self,result):
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


    def showSaleBYInvoice(self,result):
        discount = 0
        self.tbl_saleReportByInvoice.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_saleReportByInvoice.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if(colum_number == 5):
                    discount = discount + int(data)
                self.tbl_saleReportByInvoice.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

        self.le_itemDiscount.setText(str(discount))


    def filterFunc(self,item):
        company = self.le_filterByCompany.text()
        product = self.le_filterByProduct.text()
        engine = self.le_filterByEngine.text()
        chassis = self.le_filterByChassis.text()
        salePrice = self.le_filterBySalePrice.text()
        discount = self.le_filterByDiscount.text()
        totalPrice = self.le_filterByTotalPrice.text()
        remarks = self.le_filterByRemarks.text()

        if (str(item[0]).lower().startswith(company) and str(item[1]).startswith(product) and
            str(item[2]).startswith(engine) and str(item[3]).startswith(chassis)  and
            str(item[4]).startswith(salePrice)  and str(item[5]).startswith(discount) and
            str(item[6]).startswith(totalPrice) and str(item[7]).lower().startswith(remarks) ):
            return True
        else:
            return False

    def filterSaleReport(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.showSaleBYInvoice(result)


    def saleReportByInvoiceSetupUi(self, saleReportByInvoiceWindow):
        saleReportByInvoiceWindow.setObjectName("saleReportByInvoiceWindow")
        saleReportByInvoiceWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        saleReportByInvoiceWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        saleReportByInvoiceWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        saleReportByInvoiceWindow.setAutoFillBackground(True)
        
        self.centralwidget = QtWidgets.QWidget(saleReportByInvoiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saleGB = QtWidgets.QGroupBox(self.centralwidget)
        self.saleGB.setGeometry(QtCore.QRect(5, 0, 1360, 685))
        self.saleGB.setObjectName("saleGB")
        self.tbl_saleReportByInvoice = QtWidgets.QTableWidget(self.saleGB)
        self.tbl_saleReportByInvoice.setGeometry(QtCore.QRect(10, 140, 1340, 535))
        self.tbl_saleReportByInvoice.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_saleReportByInvoice.setShowGrid(True)
        self.tbl_saleReportByInvoice.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_saleReportByInvoice.setWordWrap(True)
        self.tbl_saleReportByInvoice.setRowCount(16)
        self.tbl_saleReportByInvoice.setColumnCount(8)
        self.tbl_saleReportByInvoice.setHorizontalHeaderLabels(['Company', 'Product', 'Engine','Chassis', 'Sale Price',
                                                                'Discount', 'Total Price', 'Remarks'])

        self.tbl_saleReportByInvoice.setColumnWidth(0,200)
        self.tbl_saleReportByInvoice.setColumnWidth(1,200)
        self.tbl_saleReportByInvoice.setColumnWidth(7,400)

        self.tbl_saleReportByInvoice.setObjectName("tbl_saleReportByInvoice")

        self.filterGB = QtWidgets.QGroupBox(self.saleGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 95, 1341, 41))
        self.filterGB.setObjectName("filterGB")


        self.le_filterByCompany = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompany.setGeometry(QtCore.QRect(0, 20, 230, 20))
        self.le_filterByCompany.setMaxLength(32)
        self.le_filterByCompany.setObjectName("le_filterByCompany")
        self.le_filterByCompany.textChanged.connect(self.filterSaleReport)

        self.le_filterByProduct = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByProduct.setGeometry(QtCore.QRect(230, 20, 200, 20))
        self.le_filterByProduct.setMaxLength(32)
        self.le_filterByProduct.setObjectName("le_filterByProduct")
        self.le_filterByProduct.textChanged.connect(self.filterSaleReport)

        self.le_filterByEngine = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByEngine.setGeometry(QtCore.QRect(430, 20, 100, 20))
        self.le_filterByEngine.setMaxLength(32)
        self.le_filterByEngine.setObjectName("le_filterByEngine")
        self.le_filterByEngine.textChanged.connect(self.filterSaleReport)

        self.le_filterByChassis = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByChassis.setGeometry(QtCore.QRect(530, 20, 100, 20))
        self.le_filterByChassis.setMaxLength(32)
        self.le_filterByChassis.setObjectName("le_filterByChassis")
        self.le_filterByChassis.textChanged.connect(self.filterSaleReport)

        self.le_filterBySalePrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterBySalePrice.setGeometry(QtCore.QRect(630, 20, 100, 20))
        self.le_filterBySalePrice.setMaxLength(32)
        self.le_filterBySalePrice.setObjectName("le_filterBySalePrice")
        self.le_filterBySalePrice.textChanged.connect(self.filterSaleReport)

        self.le_filterByDiscount = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDiscount.setGeometry(QtCore.QRect(730, 20, 100, 20))
        self.le_filterByDiscount.setMaxLength(32)
        self.le_filterByDiscount.setObjectName("le_filterByDiscount")
        self.le_filterByDiscount.textChanged.connect(self.filterSaleReport)

        self.le_filterByTotalPrice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByTotalPrice.setGeometry(QtCore.QRect(830, 20, 100, 20))
        self.le_filterByTotalPrice.setMaxLength(32)
        self.le_filterByTotalPrice.setObjectName("le_filterByTotalPrice")
        self.le_filterByTotalPrice.textChanged.connect(self.filterSaleReport)

        self.le_filterByRemarks = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByRemarks.setGeometry(QtCore.QRect(930, 20, 410, 20))
        self.le_filterByRemarks.setMaxLength(32)
        self.le_filterByRemarks.setObjectName("le_filterByRemarks")
        self.le_filterByRemarks.textChanged.connect(self.filterSaleReport)
        
        self.searchGB = QtWidgets.QGroupBox(self.saleGB)
        self.searchGB.setGeometry(QtCore.QRect(10, 20, 1341, 75))
        self.searchGB.setObjectName("searchGB")
        
        self.le_searchByInvoice = QtWidgets.QLineEdit(self.searchGB)
        self.le_searchByInvoice.setGeometry(QtCore.QRect(10, 40, 100, 28))
        self.le_searchByInvoice.setObjectName("le_searchByInvoice")
        self.le_searchByInvoice.returnPressed.connect(self.getSaleByInvoice)
        
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
        self.btn_serach.clicked.connect(self.getSaleByInvoice)
        
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
        self.btn_refresh.clicked.connect(self.getSaleByInvoice)

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
        saleReportByInvoiceWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(saleReportByInvoiceWindow)
        self.statusbar.setObjectName("statusbar")
        saleReportByInvoiceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(saleReportByInvoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(saleReportByInvoiceWindow)

    def retranslateUi(self, saleReportByInvoiceWindow):
        _translate = QtCore.QCoreApplication.translate
        saleReportByInvoiceWindow.setWindowTitle(_translate("saleReportByInvoiceWindow", "Sale Report By Invoice"))
        self.saleGB.setTitle(_translate("saleReportByInvoiceWindow", "Sale Report "))
        self.filterGB.setTitle(_translate("saleReportByInvoiceWindow", "Filter"))
        self.le_filterByCompany.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Filter BY Company"))
        self.le_filterByProduct.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Filter BY Product"))
        self.le_filterByEngine.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Filter BY Engine"))
        self.le_filterByChassis.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Filter BY Chassis"))
        self.le_filterByRemarks.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Filter BY Remarks"))
        self.le_filterByDiscount.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Filter BY Discount"))
        self.le_filterBySalePrice.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Filter BY Sale Price"))
        self.le_filterByTotalPrice.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Filter BY Total Amount"))
        self.searchGB.setTitle(_translate("saleReportByInvoiceWindow", "Search Invoice"))
        self.le_searchByInvoice.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Enter Invoice"))
        self.label.setText(_translate("saleReportByInvoiceWindow", "Search :"))
        self.btn_serach.setText(_translate("saleReportByInvoiceWindow", "Search"))
        self.le_totalSale.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Total Sale"))
        self.le_itemDiscount.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Discount On Item"))
        self.btn_refresh.setText(_translate("saleReportByInvoiceWindow", "Refresh"))
        self.btn_print.setText(_translate("saleReportByInvoiceWindow", "Print"))
        self.label_6.setText(_translate("saleReportByInvoiceWindow", "Item Discount"))
        self.label_4.setText(_translate("saleReportByInvoiceWindow", "Net Sale"))
        self.label_2.setText(_translate("saleReportByInvoiceWindow", "Total Sale"))
        self.le_netSale.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Total Sale"))
        self.le_totalDiscount.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Discount Bill"))
        self.label_3.setText(_translate("saleReportByInvoiceWindow", "Total Discount"))
        self.label_5.setText(_translate("saleReportByInvoiceWindow", "Account Name"))
        self.le_cnic.setPlaceholderText(_translate("saleReportByInvoiceWindow", "CNIC"))
        self.label_7.setText(_translate("saleReportByInvoiceWindow", "Father Name"))
        self.le_name.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Account Name"))
        self.le_mobile.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Mobile Number"))
        self.label_8.setText(_translate("saleReportByInvoiceWindow", "CNIC"))
        self.label_9.setText(_translate("saleReportByInvoiceWindow", "Mobile :"))
        self.le_fatherName.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Father Name"))
        self.label_10.setText(_translate("saleReportByInvoiceWindow", "Balance:"))
        self.label_11.setText(_translate("saleReportByInvoiceWindow", "Date"))
        self.le_balance.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Remining Balance"))
        self.le_date.setPlaceholderText(_translate("saleReportByInvoiceWindow", "Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saleReportByInvoiceWindow = QtWidgets.QMainWindow()
    ui = Ui_saleReportByInvoiceWindow()
    ui.saleReportByInvoiceSetupUi(saleReportByInvoiceWindow)
    saleReportByInvoiceWindow.show()
    sys.exit(app.exec_())

