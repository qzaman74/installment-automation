import sys


from BLL import mainFormBL
from BLL.AccountsBL import accountFormBL,cashTransectionBL
from BLL.PurchaseBL import purchaseBL
from BLL.SaleBL import paymentSaleBL, saleBL
from BLL.SetupBL import companyBL,productBL
from BLL.InstallmentsBL import addSchemeBL,assignSchemeBL,addInstallmentBL
from BLL.ReportsBL.AccountsReportsBL import ARReportBL,APReportBL
from BLL.ReportsBL.SaleReportsBL import saleReportByInvoiceBL, saleReportByDateBL
from BLL.ReportsBL.PurchaseReportsBL import purchaseReportByInvoiceBL,purchaseReportByDateBL
from BLL.ReportsBL.StockReportsBL import stockLevelReportBL

from Globals import globalVariables
from Services.NotificationService import notification
from Services.RecallServices import formRecall

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtChart
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPainter


class Ui_mainForm(object):

    todaySale = 0
    todayPurchase = 0
    todayCashIn = 0
    todayCashOut = 0


    def init(self):
        sale, purchase, cashIn, cashOut = mainFormBL.setDashboard()
        if(sale != None):
            self.lbl_todaySale.setText(str(sale))
            self.todaySale = int(sale)
        else:
            self.lbl_todaySale.setText("0")
            self.todaySale = 0

        if(purchase != None):
            self.lbl_todayPurchase.setText(str(purchase))
            self.todayPurchase = int(purchase)
        else:
            self.lbl_todayPurchase.setText("0")
            self.todayPurchase = 0

        if(cashIn != None):
            self.lbl_todayCashIn.setText(str(cashIn))
            self.todayCashIn = int(cashIn)
        else:
            self.lbl_todayCashIn.setText("0")
            self.todayCashIn = 0

        if(cashOut != None):
            self.lbl_todayCashOut.setText(str(cashOut))
            self.todayCashOut = int(cashOut)
        else:
            self.lbl_todayCashOut.setText("0")
            self.todayCashOut = 0


    def actionExitClicked(self):
        confirm = notification.confirmPopup("Do You Want to Exit ..!" ,"Exit")
        if (confirm == 'OK'):
            exit(-1)
            return
        else:
            return

    # def drawChart(self, saleValue, purchaseValue, cashInValue, cashOutValue):

    def drawChart(self):
        pieChart = QtChart.QChart()

        saleValue = 35
        purchaseValue = 15
        cashInValue = 25
        cashOutValue = 250

        # pieChart.setTitle("Title")

        list = [("Sale", self.todaySale), ("Purchase", self.todayPurchase), ("Cash In", self.todayCashIn), ("Cash Out", self.todayCashOut)]

        # list = [("Sale", 23), ("Purchase", 33), ("Cash In", 43), ("Cash Out", 53)]

        series = QtChart.QPieSeries(pieChart)

        for item, value in list:
            slice = series.append(item,value)

        series.setLabelsVisible(True)
        series.setLabelsPosition(QtChart.QPieSlice.LabelOutside)
        pieChart.legend().hide()
        pieChart.addSeries(series)
        pieChart.createDefaultAxes()



        todayVistaGraph = QtChart.QChartView(pieChart)
        todayVistaGraph.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        todayVistaGraph.setRenderHint(QPainter.Antialiasing, True)

        todayChartConfiguracion = QtWidgets.QVBoxLayout()
        todayChartConfiguracion.addStretch()

        todayBaseDisign = QtWidgets.QGridLayout()
        todayBaseDisign.addLayout(todayChartConfiguracion, 0, 0, 0, 0)
        todayBaseDisign.addWidget(todayVistaGraph)


        return todayBaseDisign


    def actionNew_AccountClicked(self):
        accountFormBL.openAccountForm(self)

    def actionNew_SaleClicked(self):
        saleBL.openSaleForm(self)

    def actionPayment_SaleClicked(self):
        paymentSaleBL.openPaymentSaleForm(self)

    def actionNew_PurchaseClicked(self):
        purchaseBL.openPurchaseForm(self)

    def actionAdd_InstallmentClicked(self):
        addInstallmentBL.openAddInstallmentForm(self)

    def actionAssign_SchemeClicked(self):
        assignSchemeBL.openAssignSchemeForm(self)

    def actionAdd_SchemeClicked(self):
        addSchemeBL.openAddSchemeFormForm(self)

    def actionCash_TransectionClicked(self):
        cashTransectionBL.openCashTransectionForm(self)

    def actionNew_CompanyClicked(self):
        companyBL.openCompanyForm(self)

    def actionNew_ProductClicked(self):
        productBL.openProductForm(self)

    def actionSale_Report_By_DateClicked(self):
        saleReportByDateBL.openSaleReportByDateForm(self)

    def actionSale_Report_By_InvoiceClicked(self):
        saleReportByInvoiceBL.openSaleReportByInvoiceForm(self)

    def actionPurchase_Report_By_DateClicked(self):
        purchaseReportByDateBL.openPurchaseReportByDateForm(self)

    def actionPurchase_Report_By_InvoiceClicked(self):
        purchaseReportByInvoiceBL.openPurchaseReportByInvoiceForm(self)

    def actionAccounts_Report_By_ReceivableClicked(self):
        ARReportBL.openARReportForm(self)

    def actionAccounts_Report_By_PayableClicked(self):
        APReportBL.openAPReportForm(self)

    def actionStock_Report_By_LevelClicked(self):
        stockLevelReportBL.openStockLevelReportForm(self)

    def onLogOut(self):
        confirm = notification.confirmPopup("Do You Want to Logout ..!","Exit")
        if (confirm == 'OK'):
            sys.exit(-1)
        else:
            return

    def closeEvt(self, event):
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()








    def mainFormSetupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(1365, 700)

        formRecall.Recall._recallDashboard = self.init

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        mainForm.setWindowIcon(QtGui.QIcon(windowIcon))

        mainForm.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        mainForm.setAutoFillBackground(True)

        mainForm.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(mainForm)
        self.centralwidget.setObjectName("centralwidget")

        #----------------- images--------------------#

        saleImage = QtGui.QPixmap(globalVariables.Variables._icon + 'saleIcon.png')
        purchaseImage = QtGui.QPixmap(globalVariables.Variables._icon + 'purchaseIcon.png')
        cashInImage = QtGui.QPixmap(globalVariables.Variables._icon + 'cashInIcon.png')
        cashOutImage = QtGui.QPixmap(globalVariables.Variables._icon + 'cashOutIcon.png')
        logoutImage = QtGui.QPixmap(globalVariables.Variables._icon + 'logoutIcon.png')
        refreshImage = QtGui.QPixmap(globalVariables.Variables._icon + 'refreshIcon.png')
        exitImage = QtGui.QPixmap(globalVariables.Variables._icon + 'exitIcon.png')
        newImage = QtGui.QPixmap(globalVariables.Variables._icon + 'newIcon.png')
        addImage = QtGui.QPixmap(globalVariables.Variables._icon + 'addIcon.png')
        accountImage = QtGui.QPixmap(globalVariables.Variables._icon + 'addAccountIcon.png')
        assignmentImage = QtGui.QPixmap(globalVariables.Variables._icon + 'assignmentIcon.png')
        reportImage = QtGui.QPixmap(globalVariables.Variables._icon + 'reportIcon.png')
        calendarImage = QtGui.QPixmap(globalVariables.Variables._icon + 'calendarIcon.png')
        invoiceImage = QtGui.QPixmap(globalVariables.Variables._icon + 'invoice.png')

        backgroundImage = QtGui.QPixmap(globalVariables.Variables._icon + 'main.jpg')

        # ----------------- end  images--------------------#


        # self.lbl_dashboardImage = QtWidgets.QLabel(self.centralwidget)
        # self.lbl_dashboardImage.setGeometry(QtCore.QRect(0, 0, 1365, 200))
        # self.lbl_dashboardImage.setPixmap(QtGui.QPixmap(backgroundImage))
        # self.lbl_dashboardImage.setObjectName("lbl_dashboardImage")



        self.btn_refresh = QtWidgets.QToolButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(10, 20, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_refresh.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(refreshImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_refresh.setIcon(icon)
        self.btn_refresh.setIconSize(QtCore.QSize(100, 80))
        self.btn_refresh.setCheckable(False)
        self.btn_refresh.setAutoRepeat(False)
        self.btn_refresh.setAutoExclusive(False)
        self.btn_refresh.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_refresh.setAutoRaise(False)
        self.btn_refresh.setArrowType(QtCore.Qt.NoArrow)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.init)
        
        self.btn_quickPurchase = QtWidgets.QToolButton(self.centralwidget)
        self.btn_quickPurchase.setGeometry(QtCore.QRect(10, 280, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_quickPurchase.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(purchaseImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_quickPurchase.setIcon(icon1)
        self.btn_quickPurchase.setIconSize(QtCore.QSize(100, 80))
        self.btn_quickPurchase.setCheckable(False)
        self.btn_quickPurchase.setAutoRepeat(False)
        self.btn_quickPurchase.setAutoExclusive(False)
        self.btn_quickPurchase.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_quickPurchase.setAutoRaise(False)
        self.btn_quickPurchase.setArrowType(QtCore.Qt.NoArrow)
        self.btn_quickPurchase.setObjectName("btn_quickPurchase")
        self.btn_quickPurchase.clicked.connect(self.actionNew_PurchaseClicked)

        self.btn_quickSale = QtWidgets.QToolButton(self.centralwidget)
        self.btn_quickSale.setGeometry(QtCore.QRect(10, 150, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_quickSale.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(saleImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_quickSale.setIcon(icon2)
        self.btn_quickSale.setIconSize(QtCore.QSize(100, 80))
        self.btn_quickSale.setCheckable(False)
        self.btn_quickSale.setAutoRepeat(False)
        self.btn_quickSale.setAutoExclusive(False)
        self.btn_quickSale.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_quickSale.setAutoRaise(False)
        self.btn_quickSale.setArrowType(QtCore.Qt.NoArrow)
        self.btn_quickSale.setObjectName("btn_quickSale")
        self.btn_quickSale.clicked.connect(self.actionNew_SaleClicked)

        self.btn_logout = QtWidgets.QToolButton(self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(10, 540, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(logoutImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_logout.setIcon(icon3)
        self.btn_logout.setIconSize(QtCore.QSize(100, 80))
        self.btn_logout.setCheckable(False)
        self.btn_logout.setAutoRepeat(False)
        self.btn_logout.setAutoExclusive(False)
        self.btn_logout.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_logout.setAutoRaise(False)
        self.btn_logout.setArrowType(QtCore.Qt.NoArrow)
        self.btn_logout.setObjectName("btn_logout")
        self.btn_logout.clicked.connect(self.onLogOut)

        self.btn_quickCash = QtWidgets.QToolButton(self.centralwidget)
        self.btn_quickCash.setGeometry(QtCore.QRect(10, 410, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_quickCash.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(cashInImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_quickCash.setIcon(icon4)
        self.btn_quickCash.setIconSize(QtCore.QSize(100, 80))
        self.btn_quickCash.setCheckable(False)
        self.btn_quickCash.setAutoRepeat(False)
        self.btn_quickCash.setAutoExclusive(False)
        self.btn_quickCash.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_quickCash.setAutoRaise(False)
        self.btn_quickCash.setArrowType(QtCore.Qt.NoArrow)
        self.btn_quickCash.setObjectName("btn_quickCash")
        self.btn_quickCash.clicked.connect(self.actionCash_TransectionClicked)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 15, 1210, 210))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.btn_todaySale = QtWidgets.QToolButton(self.groupBox)
        self.btn_todaySale.setGeometry(QtCore.QRect(20, 19, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_todaySale.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(saleImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_todaySale.setIcon(icon5)
        self.btn_todaySale.setIconSize(QtCore.QSize(130, 120))
        self.btn_todaySale.setCheckable(False)
        self.btn_todaySale.setAutoRepeat(False)
        self.btn_todaySale.setAutoExclusive(False)
        self.btn_todaySale.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_todaySale.setAutoRaise(True)
        self.btn_todaySale.setArrowType(QtCore.Qt.NoArrow)
        self.btn_todaySale.setObjectName("btn_todaySale")

        self.lbl_todaySale = QtWidgets.QLabel(self.groupBox)
        self.lbl_todaySale.setGeometry(QtCore.QRect(20, 170, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_todaySale.setFont(font)
        self.lbl_todaySale.setText("")
        self.lbl_todaySale.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_todaySale.setObjectName("lbl_todaySale")

        self.lbl_todayPurchase = QtWidgets.QLabel(self.groupBox)
        self.lbl_todayPurchase.setGeometry(QtCore.QRect(240, 171, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_todayPurchase.setFont(font)
        self.lbl_todayPurchase.setText("")
        self.lbl_todayPurchase.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_todayPurchase.setObjectName("lbl_todayPurchase")

        self.btn_todayPurchase = QtWidgets.QToolButton(self.groupBox)
        self.btn_todayPurchase.setGeometry(QtCore.QRect(240, 20, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_todayPurchase.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(purchaseImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_todayPurchase.setIcon(icon6)
        self.btn_todayPurchase.setIconSize(QtCore.QSize(130, 120))
        self.btn_todayPurchase.setCheckable(False)
        self.btn_todayPurchase.setAutoRepeat(False)
        self.btn_todayPurchase.setAutoExclusive(False)
        self.btn_todayPurchase.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_todayPurchase.setAutoRaise(True)
        self.btn_todayPurchase.setArrowType(QtCore.Qt.NoArrow)
        self.btn_todayPurchase.setObjectName("btn_todayPurchase")

        self.btn_todayCashOut = QtWidgets.QToolButton(self.groupBox)
        self.btn_todayCashOut.setGeometry(QtCore.QRect(680, 21, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_todayCashOut.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(cashOutImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_todayCashOut.setIcon(icon7)
        self.btn_todayCashOut.setIconSize(QtCore.QSize(130, 120))
        self.btn_todayCashOut.setCheckable(False)
        self.btn_todayCashOut.setAutoRepeat(False)
        self.btn_todayCashOut.setAutoExclusive(False)
        self.btn_todayCashOut.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_todayCashOut.setAutoRaise(True)
        self.btn_todayCashOut.setArrowType(QtCore.Qt.NoArrow)
        self.btn_todayCashOut.setObjectName("btn_todayCashOut")

        self.lbl_todayCashIn = QtWidgets.QLabel(self.groupBox)
        self.lbl_todayCashIn.setGeometry(QtCore.QRect(460, 171, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_todayCashIn.setFont(font)
        self.lbl_todayCashIn.setText("")
        self.lbl_todayCashIn.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_todayCashIn.setObjectName("lbl_todayCashIn")

        self.lbl_todayCashOut = QtWidgets.QLabel(self.groupBox)
        self.lbl_todayCashOut.setGeometry(QtCore.QRect(680, 172, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_todayCashOut.setFont(font)
        self.lbl_todayCashOut.setText("")
        self.lbl_todayCashOut.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_todayCashOut.setObjectName("lbl_todayCashOut")

        self.btn_todayCashIn = QtWidgets.QToolButton(self.groupBox)
        self.btn_todayCashIn.setGeometry(QtCore.QRect(460, 20, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_todayCashIn.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(cashInImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_todayCashIn.setIcon(icon8)
        self.btn_todayCashIn.setIconSize(QtCore.QSize(130, 120))
        self.btn_todayCashIn.setCheckable(False)
        self.btn_todayCashIn.setAutoRepeat(False)
        self.btn_todayCashIn.setAutoExclusive(False)
        self.btn_todayCashIn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_todayCashIn.setAutoRaise(True)
        self.btn_todayCashIn.setArrowType(QtCore.Qt.NoArrow)
        self.btn_todayCashIn.setObjectName("btn_todayCashIn")
        # todayVistaGraph = QtChart.QChartView(self.drawChart(self.todaySale, self.todayPurchase, self.todayCashIn, self.todayCashOut))
        #
        # todayVistaGraph = QtChart.QChartView(self.drawChart())
        # todayVistaGraph.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        # todayVistaGraph.setRenderHint(QPainter.Antialiasing, True)
        #
        # todayChartConfiguracion = QtWidgets.QVBoxLayout()
        # todayChartConfiguracion.addStretch()
        #
        # todayBaseDisign = QtWidgets.QGridLayout()
        # todayBaseDisign.addLayout(todayChartConfiguracion, 0, 0, 0, 0)
        # todayBaseDisign.addWidget(todayVistaGraph)

        self.gv_todayChart = QtWidgets.QGraphicsView(self.groupBox)
        self.gv_todayChart.setGeometry(QtCore.QRect(900, 5, 300, 205))
        self.gv_todayChart.setObjectName("gv_todayChart")

        todayBaseDisign = self.drawChart()

        self.gv_todayChart.setLayout(todayBaseDisign)


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(140, 230, 1210, 210))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")


        self.lbl_monthlyCashIn = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_monthlyCashIn.setGeometry(QtCore.QRect(460, 172, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_monthlyCashIn.setFont(font)
        self.lbl_monthlyCashIn.setText("")
        self.lbl_monthlyCashIn.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_monthlyCashIn.setObjectName("lbl_monthlyCashIn")

        self.btn_monthlyPurchase = QtWidgets.QToolButton(self.groupBox_2)
        self.btn_monthlyPurchase.setGeometry(QtCore.QRect(240, 21, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_monthlyPurchase.setFont(font)
        self.btn_monthlyPurchase.setIcon(icon6)
        self.btn_monthlyPurchase.setIconSize(QtCore.QSize(130, 120))
        self.btn_monthlyPurchase.setCheckable(False)
        self.btn_monthlyPurchase.setAutoRepeat(False)
        self.btn_monthlyPurchase.setAutoExclusive(False)
        self.btn_monthlyPurchase.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_monthlyPurchase.setAutoRaise(True)
        self.btn_monthlyPurchase.setArrowType(QtCore.Qt.NoArrow)
        self.btn_monthlyPurchase.setObjectName("btn_monthlyPurchase")

        self.gv_monthlyChart = QtWidgets.QGraphicsView(self.groupBox_2)
        self.gv_monthlyChart.setGeometry(QtCore.QRect(900, 6, 300, 205))
        self.gv_monthlyChart.setObjectName("gv_monthlyChart")
        self.btn_monthlyCashOut = QtWidgets.QToolButton(self.groupBox_2)
        self.btn_monthlyCashOut.setGeometry(QtCore.QRect(680, 22, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_monthlyCashOut.setFont(font)
        self.btn_monthlyCashOut.setIcon(icon7)
        self.btn_monthlyCashOut.setIconSize(QtCore.QSize(130, 120))
        self.btn_monthlyCashOut.setCheckable(False)
        self.btn_monthlyCashOut.setAutoRepeat(False)
        self.btn_monthlyCashOut.setAutoExclusive(False)
        self.btn_monthlyCashOut.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_monthlyCashOut.setAutoRaise(True)
        self.btn_monthlyCashOut.setArrowType(QtCore.Qt.NoArrow)
        self.btn_monthlyCashOut.setObjectName("btn_monthlyCashOut")
        self.btn_monthlyCashIn = QtWidgets.QToolButton(self.groupBox_2)
        self.btn_monthlyCashIn.setGeometry(QtCore.QRect(460, 21, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_monthlyCashIn.setFont(font)
        self.btn_monthlyCashIn.setIcon(icon8)
        self.btn_monthlyCashIn.setIconSize(QtCore.QSize(130, 120))
        self.btn_monthlyCashIn.setCheckable(False)
        self.btn_monthlyCashIn.setAutoRepeat(False)
        self.btn_monthlyCashIn.setAutoExclusive(False)
        self.btn_monthlyCashIn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_monthlyCashIn.setAutoRaise(True)
        self.btn_monthlyCashIn.setArrowType(QtCore.Qt.NoArrow)
        self.btn_monthlyCashIn.setObjectName("btn_monthlyCashIn")
        
        self.lbl_monthlySale = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_monthlySale.setGeometry(QtCore.QRect(20, 171, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_monthlySale.setFont(font)
        self.lbl_monthlySale.setText("")
        self.lbl_monthlySale.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_monthlySale.setObjectName("lbl_monthlySale")
        
        self.lbl_monthlyCashOut = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_monthlyCashOut.setGeometry(QtCore.QRect(680, 173, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_monthlyCashOut.setFont(font)
        self.lbl_monthlyCashOut.setText("")
        self.lbl_monthlyCashOut.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_monthlyCashOut.setObjectName("lbl_monthlyCashOut")
        
        self.lbl_monthlyPurchase = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_monthlyPurchase.setGeometry(QtCore.QRect(240, 172, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_monthlyPurchase.setFont(font)
        self.lbl_monthlyPurchase.setText("")
        self.lbl_monthlyPurchase.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_monthlyPurchase.setObjectName("lbl_monthlyPurchase")
        
        self.btn_monthlySale = QtWidgets.QToolButton(self.groupBox_2)
        self.btn_monthlySale.setGeometry(QtCore.QRect(20, 20, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_monthlySale.setFont(font)
        self.btn_monthlySale.setIcon(icon5)
        self.btn_monthlySale.setIconSize(QtCore.QSize(130, 120))
        self.btn_monthlySale.setCheckable(False)
        self.btn_monthlySale.setAutoRepeat(False)
        self.btn_monthlySale.setAutoExclusive(False)
        self.btn_monthlySale.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_monthlySale.setAutoRaise(True)
        self.btn_monthlySale.setArrowType(QtCore.Qt.NoArrow)
        self.btn_monthlySale.setObjectName("btn_monthlySale")
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(140, 450, 1210, 210))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")

        self.lbl_yearlyCashIn = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_yearlyCashIn.setGeometry(QtCore.QRect(460, 172, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_yearlyCashIn.setFont(font)
        self.lbl_yearlyCashIn.setText("")
        self.lbl_yearlyCashIn.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_yearlyCashIn.setObjectName("lbl_yearlyCashIn")

        self.btn_yearlyPurchase = QtWidgets.QToolButton(self.groupBox_3)
        self.btn_yearlyPurchase.setGeometry(QtCore.QRect(240, 21, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_yearlyPurchase.setFont(font)
        self.btn_yearlyPurchase.setIcon(icon6)
        self.btn_yearlyPurchase.setIconSize(QtCore.QSize(130, 120))
        self.btn_yearlyPurchase.setCheckable(False)
        self.btn_yearlyPurchase.setAutoRepeat(False)
        self.btn_yearlyPurchase.setAutoExclusive(False)
        self.btn_yearlyPurchase.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_yearlyPurchase.setAutoRaise(True)
        self.btn_yearlyPurchase.setArrowType(QtCore.Qt.NoArrow)
        self.btn_yearlyPurchase.setObjectName("btn_yearlyPurchase")
        
        self.gv_yearlyChart = QtWidgets.QGraphicsView(self.groupBox_3)
        self.gv_yearlyChart.setGeometry(QtCore.QRect(900, 6, 300, 205))
        self.gv_yearlyChart.setObjectName("gv_yearlyChart")
        
        self.btn_yearlyCashOut = QtWidgets.QToolButton(self.groupBox_3)
        self.btn_yearlyCashOut.setGeometry(QtCore.QRect(680, 22, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_yearlyCashOut.setFont(font)
        self.btn_yearlyCashOut.setIcon(icon7)
        self.btn_yearlyCashOut.setIconSize(QtCore.QSize(130, 120))
        self.btn_yearlyCashOut.setCheckable(False)
        self.btn_yearlyCashOut.setAutoRepeat(False)
        self.btn_yearlyCashOut.setAutoExclusive(False)
        self.btn_yearlyCashOut.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_yearlyCashOut.setAutoRaise(True)
        self.btn_yearlyCashOut.setArrowType(QtCore.Qt.NoArrow)
        self.btn_yearlyCashOut.setObjectName("btn_yearlyCashOut")
        
        self.btn_yearlyCashIn = QtWidgets.QToolButton(self.groupBox_3)
        self.btn_yearlyCashIn.setGeometry(QtCore.QRect(460, 21, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_yearlyCashIn.setFont(font)
        self.btn_yearlyCashIn.setIcon(icon8)
        self.btn_yearlyCashIn.setIconSize(QtCore.QSize(130, 120))
        self.btn_yearlyCashIn.setCheckable(False)
        self.btn_yearlyCashIn.setAutoRepeat(False)
        self.btn_yearlyCashIn.setAutoExclusive(False)
        self.btn_yearlyCashIn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_yearlyCashIn.setAutoRaise(True)
        self.btn_yearlyCashIn.setArrowType(QtCore.Qt.NoArrow)
        self.btn_yearlyCashIn.setObjectName("btn_yearlyCashIn")
        
        self.lbl_yearlySale = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_yearlySale.setGeometry(QtCore.QRect(20, 171, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_yearlySale.setFont(font)
        self.lbl_yearlySale.setText("")
        self.lbl_yearlySale.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_yearlySale.setObjectName("lbl_yearlySale")
        
        self.lbl_yearlyCashOut = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_yearlyCashOut.setGeometry(QtCore.QRect(680, 173, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_yearlyCashOut.setFont(font)
        self.lbl_yearlyCashOut.setText("")
        self.lbl_yearlyCashOut.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_yearlyCashOut.setObjectName("lbl_yearlyCashOut")
        
        self.lbl_yearlyPurchase = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_yearlyPurchase.setGeometry(QtCore.QRect(240, 172, 160, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_yearlyPurchase.setFont(font)
        self.lbl_yearlyPurchase.setText("")
        self.lbl_yearlyPurchase.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_yearlyPurchase.setObjectName("lbl_yearlyPurchase")
        
        self.btn_yearlySale = QtWidgets.QToolButton(self.groupBox_3)
        self.btn_yearlySale.setGeometry(QtCore.QRect(20, 20, 160, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_yearlySale.setFont(font)
        self.btn_yearlySale.setIcon(icon5)
        self.btn_yearlySale.setIconSize(QtCore.QSize(130, 120))
        self.btn_yearlySale.setCheckable(False)
        self.btn_yearlySale.setAutoRepeat(False)
        self.btn_yearlySale.setAutoExclusive(False)
        self.btn_yearlySale.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btn_yearlySale.setAutoRaise(True)
        self.btn_yearlySale.setArrowType(QtCore.Qt.NoArrow)
        self.btn_yearlySale.setObjectName("btn_yearlySale")





      #---------------- Menubar starts-------------------#




        
        mainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1365, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setSeparatorsCollapsible(False)
        self.menuFile.setToolTipsVisible(False)
        self.menuFile.setObjectName("menuFile")

        self.menuPurchase = QtWidgets.QMenu(self.menubar)
        self.menuPurchase.setObjectName("menuPurchase")

        self.menuInstallment_Plan = QtWidgets.QMenu(self.menubar)
        self.menuInstallment_Plan.setObjectName("menuInstallment_Plan")

        self.menuAccounts = QtWidgets.QMenu(self.menubar)
        self.menuAccounts.setObjectName("menuAccounts")

        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")

        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")

        self.menuSale_Reports = QtWidgets.QMenu(self.menuReports)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(reportImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSale_Reports.setIcon(icon9)
        self.menuSale_Reports.setObjectName("menuSale_Reports")

        self.menuPurchase_Reports = QtWidgets.QMenu(self.menuReports)
        self.menuPurchase_Reports.setIcon(icon9)
        self.menuPurchase_Reports.setObjectName("menuPurchase_Reports")

        self.menuAccounts_Reports = QtWidgets.QMenu(self.menuReports)
        self.menuAccounts_Reports.setIcon(icon9)
        self.menuAccounts_Reports.setObjectName("menuAccounts_Reports")

        self.menuStock_Reports = QtWidgets.QMenu(self.menuReports)
        self.menuStock_Reports.setIcon(icon9)
        self.menuStock_Reports.setObjectName("menuStock_Reports")

        self.menuSale = QtWidgets.QMenu(self.menubar)
        self.menuSale.setObjectName("menuSale")

        mainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainForm)
        self.statusbar.setObjectName("statusbar")

        mainForm.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(mainForm)
        self.actionClose.setObjectName("actionClose")

        self.actionAdd_Sale = QtWidgets.QAction(mainForm)
        self.actionAdd_Sale.setObjectName("actionAdd_Sale")

        self.actionAdd_Purchase = QtWidgets.QAction(mainForm)
        self.actionAdd_Purchase.setObjectName("actionAdd_Purchase")

        self.actionAdd_Installment = QtWidgets.QAction(mainForm)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(addImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Installment.setIcon(icon10)
        self.actionAdd_Installment.setShortcut("Alt+I")
        self.actionAdd_Installment.setObjectName("actionAdd_Installment")
        self.actionAdd_Installment.triggered.connect(self.actionAdd_InstallmentClicked)


        self.actionAssign_Scheme = QtWidgets.QAction(mainForm)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(assignmentImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAssign_Scheme.setIcon(icon11)
        self.actionAssign_Scheme.setObjectName("actionAssign_Scheme")
        self.actionAssign_Scheme.triggered.connect(self.actionAssign_SchemeClicked)

        self.actionNew_Scheme = QtWidgets.QAction(mainForm)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(newImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Scheme.setIcon(icon12)
        self.actionNew_Scheme.setObjectName("actionNew_Scheme")
        self.actionNew_Scheme.triggered.connect(self.actionAdd_SchemeClicked)

        self.actionNew_Account = QtWidgets.QAction(mainForm)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(accountImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Account.setIcon(icon13)
        self.actionNew_Account.setObjectName("actionNew_Account")
        self.actionNew_Account.triggered.connect(self.actionNew_AccountClicked)

        self.actionCash_Transection = QtWidgets.QAction(mainForm)
        self.actionCash_Transection.setIcon(icon4)
        self.actionCash_Transection.setObjectName("actionCash_Transection")
        self.actionCash_Transection.triggered.connect(self.actionCash_TransectionClicked)

        self.actionAccount_To_Account = QtWidgets.QAction(mainForm)
        self.actionAccount_To_Account.setObjectName("actionAccount_To_Account")

        self.actionNew_Company = QtWidgets.QAction(mainForm)
        self.actionNew_Company.setIcon(icon10)
        self.actionNew_Company.setObjectName("actionNew_Company")
        self.actionNew_Company.triggered.connect(self.actionNew_CompanyClicked)

        self.actionNew_Product = QtWidgets.QAction(mainForm)
        self.actionNew_Product.setIcon(icon10)
        self.actionNew_Product.setObjectName("actionNew_Product")
        self.actionNew_Product.triggered.connect(self.actionNew_ProductClicked)

        self.actionBy_Date = QtWidgets.QAction(mainForm)
        self.actionBy_Date.setObjectName("actionBy_Date")

        self.actionBy_Invoice = QtWidgets.QAction(mainForm)
        self.actionBy_Invoice.setObjectName("actionBy_Invoice")

        self.actionBy_Date_2 = QtWidgets.QAction(mainForm)
        self.actionBy_Date_2.setObjectName("actionBy_Date_2")

        self.actionBy_Invoice_2 = QtWidgets.QAction(mainForm)
        self.actionBy_Invoice_2.setObjectName("actionBy_Invoice_2")

        self.actionReceivable = QtWidgets.QAction(mainForm)
        self.actionReceivable.setObjectName("actionReceivable")

        self.actionPayable = QtWidgets.QAction(mainForm)
        self.actionPayable.setObjectName("actionPayable")

        self.actionStock_Level = QtWidgets.QAction(mainForm)
        self.actionStock_Level.setObjectName("actionStock_Level")

        self.actionSale_Report_By_Date = QtWidgets.QAction(mainForm)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(calendarImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSale_Report_By_Date.setIcon(icon14)
        self.actionSale_Report_By_Date.setObjectName("actionSale_Report_By_Date")
        self.actionSale_Report_By_Date.triggered.connect(self.actionSale_Report_By_DateClicked)

        self.actionSale_Report_By_Invoice = QtWidgets.QAction(mainForm)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(invoiceImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSale_Report_By_Invoice.setIcon(icon15)
        self.actionSale_Report_By_Invoice.setObjectName("actionSale_Report_By_Invoice")
        self.actionSale_Report_By_Invoice.triggered.connect(self.actionSale_Report_By_InvoiceClicked)

        self.actionPurchase_Report_By_Date = QtWidgets.QAction(mainForm)
        self.actionPurchase_Report_By_Date.setIcon(icon14)
        self.actionPurchase_Report_By_Date.setObjectName("actionPurchase_Report_By_Date")
        self.actionPurchase_Report_By_Date.triggered.connect(self.actionPurchase_Report_By_DateClicked)

        self.actionPurchase_Report_By_Invoice = QtWidgets.QAction(mainForm)
        self.actionPurchase_Report_By_Invoice.setIcon(icon15)
        self.actionPurchase_Report_By_Invoice.setObjectName("actionPurchase_Report_By_Invoice")
        self.actionPurchase_Report_By_Invoice.triggered.connect(self.actionPurchase_Report_By_InvoiceClicked)

        self.actionAccounts_Report_By_Receivable = QtWidgets.QAction(mainForm)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(cashInImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAccounts_Report_By_Receivable.setIcon(icon16)
        self.actionAccounts_Report_By_Receivable.setObjectName("actionAccounts_Report_By_Receivable")
        self.actionAccounts_Report_By_Receivable.triggered.connect(self.actionAccounts_Report_By_ReceivableClicked)

        self.actionAccounts_Report_By_Payable = QtWidgets.QAction(mainForm)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(cashOutImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAccounts_Report_By_Payable.setIcon(icon17)
        self.actionAccounts_Report_By_Payable.setObjectName("actionAccounts_Report_By_Payable")
        self.actionAccounts_Report_By_Payable.triggered.connect(self.actionAccounts_Report_By_PayableClicked)

        self.actionStock_Report_By_Level = QtWidgets.QAction(mainForm)
        self.actionStock_Report_By_Level.setIcon(icon9)
        self.actionStock_Report_By_Level.setObjectName("actionStock_Report_By_Level")
        self.actionStock_Report_By_Level.triggered.connect(self.actionStock_Report_By_LevelClicked)

        self.actionEixt = QtWidgets.QAction(mainForm)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(exitImage), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEixt.setIcon(icon18)
        self.actionEixt.setShortcut("Alt+E")
        self.actionEixt.setObjectName("actionEixt")
        self.actionEixt.triggered.connect(self.actionExitClicked)

        self.actionNew_Sale = QtWidgets.QAction(mainForm)
        self.actionNew_Sale.setIcon(icon12)
        self.actionNew_Sale.setShortcut("Alt+S")
        self.actionNew_Sale.setObjectName("actionNew_Sale")
        self.actionNew_Sale.triggered.connect(self.actionNew_SaleClicked)

        self.actionNew_Purchase = QtWidgets.QAction(mainForm)
        self.actionNew_Purchase.setIcon(icon12)
        self.actionNew_Purchase.setShortcut("Alt+P")
        self.actionNew_Purchase.setObjectName("actionNew_Purchase")
        self.actionNew_Purchase.triggered.connect(self.actionNew_PurchaseClicked)


        self.menuFile.addAction(self.actionEixt)
        self.menuPurchase.addAction(self.actionNew_Purchase)
        self.menuInstallment_Plan.addAction(self.actionAdd_Installment)
        self.menuInstallment_Plan.addAction(self.actionAssign_Scheme)
        self.menuInstallment_Plan.addAction(self.actionNew_Scheme)
        self.menuAccounts.addAction(self.actionNew_Account)
        self.menuAccounts.addAction(self.actionCash_Transection)
        self.menuSetup.addAction(self.actionNew_Company)
        self.menuSetup.addAction(self.actionNew_Product)
        self.menuSale_Reports.addAction(self.actionSale_Report_By_Date)
        self.menuSale_Reports.addAction(self.actionSale_Report_By_Invoice)
        self.menuPurchase_Reports.addAction(self.actionPurchase_Report_By_Date)
        self.menuPurchase_Reports.addAction(self.actionPurchase_Report_By_Invoice)
        self.menuAccounts_Reports.addAction(self.actionAccounts_Report_By_Receivable)
        self.menuAccounts_Reports.addAction(self.actionAccounts_Report_By_Payable)
        self.menuStock_Reports.addAction(self.actionStock_Report_By_Level)
        self.menuReports.addAction(self.menuSale_Reports.menuAction())
        self.menuReports.addAction(self.menuPurchase_Reports.menuAction())
        self.menuReports.addAction(self.menuAccounts_Reports.menuAction())
        self.menuReports.addAction(self.menuStock_Reports.menuAction())
        self.menuSale.addAction(self.actionNew_Sale)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSale.menuAction())
        self.menubar.addAction(self.menuPurchase.menuAction())
        self.menubar.addAction(self.menuInstallment_Plan.menuAction())
        self.menubar.addAction(self.menuAccounts.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "OPTIM SOFTWARE SOLUTIONS -- AUTOiT"))
        self.btn_refresh.setText(_translate("mainForm", "Refresh"))
        self.btn_quickPurchase.setText(_translate("mainForm", "Purchase"))
        self.btn_quickSale.setText(_translate("mainForm", "Sale"))
        self.btn_logout.setText(_translate("mainForm", "Logout"))
        self.btn_quickCash.setText(_translate("mainForm", "Cash"))
        self.groupBox.setTitle(_translate("mainForm", "Today"))
        self.btn_todaySale.setText(_translate("mainForm", "Sale"))
        self.btn_todayPurchase.setText(_translate("mainForm", "Purchase"))
        self.btn_todayCashOut.setText(_translate("mainForm", "Cash Out"))
        self.btn_todayCashIn.setText(_translate("mainForm", "Cash In"))
        self.groupBox_2.setTitle(_translate("mainForm", "Last Month"))
        self.btn_monthlyPurchase.setText(_translate("mainForm", "Purchase"))
        self.btn_monthlyCashOut.setText(_translate("mainForm", "Cash Out"))
        self.btn_monthlyCashIn.setText(_translate("mainForm", "Cash In"))
        self.btn_monthlySale.setText(_translate("mainForm", "Sale"))
        self.groupBox_3.setTitle(_translate("mainForm", "Last Year"))
        self.btn_yearlyPurchase.setText(_translate("mainForm", "Purchase"))
        self.btn_yearlyCashOut.setText(_translate("mainForm", "Cash Out"))
        self.btn_yearlyCashIn.setText(_translate("mainForm", "Cash In"))
        self.btn_yearlySale.setText(_translate("mainForm", "Sale"))
        self.menuFile.setTitle(_translate("mainForm", "File"))
        self.menuPurchase.setTitle(_translate("mainForm", "Purchase"))
        self.menuInstallment_Plan.setTitle(_translate("mainForm", "Installment Plan"))
        self.menuAccounts.setTitle(_translate("mainForm", "Accounts"))
        self.menuSetup.setTitle(_translate("mainForm", "Setup"))
        self.menuReports.setTitle(_translate("mainForm", "Reports"))
        self.menuSale_Reports.setTitle(_translate("mainForm", "Sale Reports"))
        self.menuPurchase_Reports.setTitle(_translate("mainForm", "Purchase Reports"))
        self.menuAccounts_Reports.setTitle(_translate("mainForm", "Accounts Reports"))
        self.menuStock_Reports.setTitle(_translate("mainForm", "Stock Reports"))
        self.menuSale.setTitle(_translate("mainForm", "Sale"))
        self.actionClose.setText(_translate("mainForm", "Close"))
        self.actionAdd_Sale.setText(_translate("mainForm", "Add Sale"))
        self.actionAdd_Purchase.setText(_translate("mainForm", "Add Purchase"))
        self.actionAdd_Installment.setText(_translate("mainForm", "Add Installment"))
        self.actionAssign_Scheme.setText(_translate("mainForm", "Assign Scheme"))
        self.actionNew_Scheme.setText(_translate("mainForm", "New Scheme"))
        self.actionNew_Account.setText(_translate("mainForm", "New Account"))
        self.actionCash_Transection.setText(_translate("mainForm", "Cash Transection"))
        self.actionAccount_To_Account.setText(_translate("mainForm", "Account To Account"))
        self.actionNew_Company.setText(_translate("mainForm", "New Company"))
        self.actionNew_Product.setText(_translate("mainForm", "New Product"))
        self.actionBy_Date.setText(_translate("mainForm", "By Date"))
        self.actionBy_Invoice.setText(_translate("mainForm", "By Invoice"))
        self.actionBy_Date_2.setText(_translate("mainForm", "By Date"))
        self.actionBy_Invoice_2.setText(_translate("mainForm", "By Invoice"))
        self.actionReceivable.setText(_translate("mainForm", "Receivable"))
        self.actionPayable.setText(_translate("mainForm", "Payable"))
        self.actionStock_Level.setText(_translate("mainForm", "Stock Level"))
        self.actionSale_Report_By_Date.setText(_translate("mainForm", "By Date"))
        self.actionSale_Report_By_Invoice.setText(_translate("mainForm", "By Invoice"))
        self.actionPurchase_Report_By_Date.setText(_translate("mainForm", "By Date"))
        self.actionPurchase_Report_By_Invoice.setText(_translate("mainForm", "By Invoice"))
        self.actionAccounts_Report_By_Receivable.setText(_translate("mainForm", "Receivable"))
        self.actionAccounts_Report_By_Payable.setText(_translate("mainForm", "Payable"))
        self.actionStock_Report_By_Level.setText(_translate("mainForm", "Stock Level"))
        self.actionEixt.setText(_translate("mainForm", "Eixt"))
        self.actionNew_Sale.setText(_translate("mainForm", "New Sale"))
        self.actionNew_Purchase.setText(_translate("mainForm", "New Purchase"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainForm = QtWidgets.QMainWindow()
    ui = Ui_mainForm()
    ui.mainFormSetupUi(mainForm)
    mainForm.show()
    sys.exit(app.exec_())

