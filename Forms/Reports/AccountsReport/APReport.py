# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APReport.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Globals import globalVariables
from BLL.ReportsBL.AccountsReportsBL import APReportBL

class Ui_APReportWindow(object):
    _filterList = None
    
    def init(self):
        self.getAccountsPayable()

    def getAccountsPayable(self):
        result = APReportBL.getAccountsPayable()
        self.showAccountsPayable(result)

        self._filterList = APReportBL.getAccountsPayable().fetchall().copy()

    def showAccountsPayable(self,result):

        total = 0
        self.tbl_APReport.setRowCount(0)
        for row_number, row_data in enumerate(result):
            total = int(row_data[8]) + total
            self.tbl_APReport.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tbl_APReport.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

        self.le_totalAP.setText(str(total))


    def filterFunc(self,item):
        name = self.le_filterByName.text()
        fatherName = self.le_filterByFatherName.text()
        cnic = self.le_filterByCnic.text()
        mobile = self.le_filterByMobile.text()
        gender = self.le_filterByGender.text()
        address = self.le_filterByAddress.text()
        _type = self.le_filterByType.text()
        status = self.le_filterByStatus.text()
        balance = self.le_filterByBalance.text()

        if (str(item[0].lower()).startswith(name) and str(item[1].lower()).startswith(fatherName) and
            str(item[2]).startswith(cnic) and str(item[3]).startswith(mobile)  and
            str(item[4].lower()).startswith(gender) and str(item[5].lower()).startswith(address) and
            str(item[6].lower()).startswith(_type) and str(item[7].lower()).startswith(status) and
            str(item[8]).startswith(balance) ):
            return True
        else:
            return False

    def filterAP(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.showAccountsPayable(result)


    def APReportSetupUi(self, APReportWindow):
        APReportWindow.setObjectName("APReportWindow")
        APReportWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        APReportWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        APReportWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        APReportWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(APReportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.arGB = QtWidgets.QGroupBox(self.centralwidget)
        self.arGB.setGeometry(QtCore.QRect(5, 0, 1350, 685))
        self.arGB.setTitle("")
        self.arGB.setObjectName("arGB")
        self.tbl_APReport = QtWidgets.QTableWidget(self.arGB)
        self.tbl_APReport.setGeometry(QtCore.QRect(10, 75, 1330, 605))
        self.tbl_APReport.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_APReport.setShowGrid(True)
        self.tbl_APReport.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_APReport.setWordWrap(True)
        self.tbl_APReport.setRowCount(19)
        self.tbl_APReport.setColumnCount(9)
        self.tbl_APReport.setHorizontalHeaderLabels(['Name', 'Father Name', 'CNIC', 'Mobile No.', 'Gender', 'Address',
                                                     'Type', 'Status', 'Amount'])
        self.tbl_APReport.setColumnWidth(0,170)
        self.tbl_APReport.setColumnWidth(1,170)
        self.tbl_APReport.setColumnWidth(5,360)
        self.tbl_APReport.setObjectName("tbl_APReport")
        self.filterGB = QtWidgets.QGroupBox(self.arGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 10, 1330, 60))
        self.filterGB.setTitle("")
        self.filterGB.setObjectName("filterGB")
        
        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(1225, 5, 100, 28))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getAccountsPayable)
        


        self.le_filterByName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByName.setGeometry(QtCore.QRect(0, 35, 190, 20))
        self.le_filterByName.setMaxLength(32)
        self.le_filterByName.setObjectName("le_filterByName")
        self.le_filterByName.textChanged.connect(self.filterAP)

        self.le_filterByFatherName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByFatherName.setGeometry(QtCore.QRect(190, 35, 170, 20))
        self.le_filterByFatherName.setMaxLength(32)
        self.le_filterByFatherName.setObjectName("le_filterByFatherName")
        self.le_filterByFatherName.textChanged.connect(self.filterAP)

        self.le_filterByCnic = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCnic.setGeometry(QtCore.QRect(360, 35, 100, 20))
        self.le_filterByCnic.setMaxLength(32)
        self.le_filterByCnic.setObjectName("le_filterByCnic")
        self.le_filterByCnic.textChanged.connect(self.filterAP)

        self.le_filterByMobile = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByMobile.setGeometry(QtCore.QRect(460, 35, 100, 20))
        self.le_filterByMobile.setMaxLength(32)
        self.le_filterByMobile.setObjectName("le_filterByMobile")
        self.le_filterByMobile.textChanged.connect(self.filterAP)

        self.le_filterByGender = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByGender.setGeometry(QtCore.QRect(560, 35, 100, 20))
        self.le_filterByGender.setMaxLength(32)
        self.le_filterByGender.setObjectName("le_filterByGender")
        self.le_filterByGender.textChanged.connect(self.filterAP)

        self.le_filterByAddress = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByAddress.setGeometry(QtCore.QRect(660, 35, 360, 20))
        self.le_filterByAddress.setMaxLength(32)
        self.le_filterByAddress.setObjectName("le_filterByAddress")
        self.le_filterByAddress.textChanged.connect(self.filterAP)

        self.le_filterByType = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByType.setGeometry(QtCore.QRect(1020, 35, 100, 20))
        self.le_filterByType.setMaxLength(32)
        self.le_filterByType.setObjectName("le_filterByType")
        self.le_filterByType.textChanged.connect(self.filterAP)

        self.le_filterByStatus = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByStatus.setGeometry(QtCore.QRect(1120, 35, 100, 20))
        self.le_filterByStatus.setMaxLength(32)
        self.le_filterByStatus.setObjectName("le_filterByStatus")
        self.le_filterByStatus.textChanged.connect(self.filterAP)

        self.le_filterByBalance = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByBalance.setGeometry(QtCore.QRect(1220, 35, 100, 20))
        self.le_filterByBalance.setMaxLength(32)
        self.le_filterByBalance.setObjectName("le_filterByBalance")
        self.le_filterByBalance.textChanged.connect(self.filterAP)

        
        self.le_totalAP = QtWidgets.QLineEdit(self.filterGB)
        self.le_totalAP.setEnabled(False)
        self.le_totalAP.setGeometry(QtCore.QRect(970, 5, 150, 28))
        self.le_totalAP.setObjectName("le_totalAP")
        self.btn_print = QtWidgets.QPushButton(self.filterGB)
        self.btn_print.setGeometry(QtCore.QRect(1125, 5, 100, 28))
        self.btn_print.setObjectName("btn_print")
        self.label_4 = QtWidgets.QLabel(self.filterGB)
        self.label_4.setGeometry(QtCore.QRect(900, 5, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        APReportWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(APReportWindow)
        self.statusbar.setObjectName("statusbar")
        APReportWindow.setStatusBar(self.statusbar)

        self.retranslateUi(APReportWindow)
        QtCore.QMetaObject.connectSlotsByName(APReportWindow)

    def retranslateUi(self, APReportWindow):
        _translate = QtCore.QCoreApplication.translate
        APReportWindow.setWindowTitle(_translate("APReportWindow", "Account Payable Report"))
        self.btn_refresh.setText(_translate("APReportWindow", "Refresh"))
        self.btn_print.setText(_translate("APReportWindow", "Print"))
        self.label_4.setText(_translate("APReportWindow", "Total A.P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    APReportWindow = QtWidgets.QMainWindow()
    ui = Ui_APReportWindow()
    ui.APReportSetupUi(APReportWindow)
    APReportWindow.show()
    sys.exit(app.exec_())

