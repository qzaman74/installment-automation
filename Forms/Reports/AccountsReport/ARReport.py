# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ARReport.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Globals import globalVariables
from BLL.ReportsBL.AccountsReportsBL import ARReportBL

class Ui_ARReportWindow(object):
    _filterList = None

    def init(self):
        self.getAccountsReceivable()

    def getAccountsReceivable(self):
        result = ARReportBL.getAccountsReceivable()
        self.showAccountsReceivable(result)

        self._filterList = ARReportBL.getAccountsReceivable().fetchall().copy()


    def showAccountsReceivable(self,result):
        total = 0
        self.tbl_ARReport.setRowCount(0)
        for row_number, row_data in enumerate(result):
            total = int(row_data[8]) + total
            self.tbl_ARReport.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if(colum_number == 8):
                    self.tbl_ARReport.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(int(data) * -1)))
                else:
                    self.tbl_ARReport.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

        self.le_totalAR.setText(str(total * -1))

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

    def filterAR(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.showAccountsReceivable(result)

    def ARReportSetupUi(self, ARReportWindow):
        ARReportWindow.setObjectName("ARReportWindow")
        ARReportWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        ARReportWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        ARReportWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        ARReportWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(ARReportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.arGB = QtWidgets.QGroupBox(self.centralwidget)
        self.arGB.setGeometry(QtCore.QRect(5, 0, 1350, 685))
        self.arGB.setTitle("")
        self.arGB.setObjectName("arGB")
        self.tbl_ARReport = QtWidgets.QTableWidget(self.arGB)
        self.tbl_ARReport.setGeometry(QtCore.QRect(10, 75, 1330, 605))
        self.tbl_ARReport.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_ARReport.setShowGrid(True)
        self.tbl_ARReport.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_ARReport.setWordWrap(True)
        self.tbl_ARReport.setRowCount(19)
        self.tbl_ARReport.setColumnCount(9)
        self.tbl_ARReport.setHorizontalHeaderLabels(['Name', 'Father Name', 'CNIC', 'Mobile No.', 'Gender', 'Address',
                                                     'Type', 'Status', 'Amount'])
        self.tbl_ARReport.setColumnWidth(0,170)
        self.tbl_ARReport.setColumnWidth(1,170)
        self.tbl_ARReport.setColumnWidth(5,360)
        self.tbl_ARReport.setObjectName("tbl_ARReport")

        self.filterGB = QtWidgets.QGroupBox(self.arGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 10, 1330, 60))
        self.filterGB.setTitle("")
        self.filterGB.setObjectName("filterGB")

        self.le_filterByName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByName.setGeometry(QtCore.QRect(0, 35, 190, 20))
        self.le_filterByName.setMaxLength(32)
        self.le_filterByName.setObjectName("le_filterByName")
        self.le_filterByName.textChanged.connect(self.filterAR)

        self.le_filterByFatherName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByFatherName.setGeometry(QtCore.QRect(190, 35, 170, 20))
        self.le_filterByFatherName.setMaxLength(32)
        self.le_filterByFatherName.setObjectName("le_filterByFatherName")
        self.le_filterByFatherName.textChanged.connect(self.filterAR)

        self.le_filterByCnic = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCnic.setGeometry(QtCore.QRect(360, 35, 100, 20))
        self.le_filterByCnic.setMaxLength(32)
        self.le_filterByCnic.setObjectName("le_filterByCnic")
        self.le_filterByCnic.textChanged.connect(self.filterAR)

        self.le_filterByMobile = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByMobile.setGeometry(QtCore.QRect(460, 35, 100, 20))
        self.le_filterByMobile.setMaxLength(32)
        self.le_filterByMobile.setObjectName("le_filterByMobile")
        self.le_filterByMobile.textChanged.connect(self.filterAR)

        self.le_filterByGender = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByGender.setGeometry(QtCore.QRect(560, 35, 100, 20))
        self.le_filterByGender.setMaxLength(32)
        self.le_filterByGender.setObjectName("le_filterByGender")
        self.le_filterByGender.textChanged.connect(self.filterAR)

        self.le_filterByAddress = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByAddress.setGeometry(QtCore.QRect(660, 35, 360, 20))
        self.le_filterByAddress.setMaxLength(32)
        self.le_filterByAddress.setObjectName("le_filterByAddress")
        self.le_filterByAddress.textChanged.connect(self.filterAR)

        self.le_filterByType = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByType.setGeometry(QtCore.QRect(1020, 35, 100, 20))
        self.le_filterByType.setMaxLength(32)
        self.le_filterByType.setObjectName("le_filterByType")
        self.le_filterByType.textChanged.connect(self.filterAR)

        self.le_filterByStatus = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByStatus.setGeometry(QtCore.QRect(1120, 35, 100, 20))
        self.le_filterByStatus.setMaxLength(32)
        self.le_filterByStatus.setObjectName("le_filterByStatus")
        self.le_filterByStatus.textChanged.connect(self.filterAR)

        self.le_filterByBalance = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByBalance.setGeometry(QtCore.QRect(1220, 35, 100, 20))
        self.le_filterByBalance.setMaxLength(32)
        self.le_filterByBalance.setObjectName("le_filterByBalance")
        self.le_filterByBalance.textChanged.connect(self.filterAR)

        self.label_4 = QtWidgets.QLabel(self.filterGB)
        self.label_4.setGeometry(QtCore.QRect(900, 5, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(1225, 5, 100, 28))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getAccountsReceivable)

        self.btn_print = QtWidgets.QPushButton(self.filterGB)
        self.btn_print.setGeometry(QtCore.QRect(1125, 5, 100, 28))
        self.btn_print.setObjectName("btn_print")

        self.le_totalAR = QtWidgets.QLineEdit(self.filterGB)
        self.le_totalAR.setEnabled(False)
        self.le_totalAR.setGeometry(QtCore.QRect(970, 5, 150, 28))
        self.le_totalAR.setObjectName("le_totalAR")

        ARReportWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ARReportWindow)
        self.statusbar.setObjectName("statusbar")
        ARReportWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ARReportWindow)
        QtCore.QMetaObject.connectSlotsByName(ARReportWindow)

    def retranslateUi(self, ARReportWindow):
        _translate = QtCore.QCoreApplication.translate
        ARReportWindow.setWindowTitle(_translate("ARReportWindow", "Account Receiveable Report"))
        self.label_4.setText(_translate("ARReportWindow", "Total A.R"))
        self.btn_refresh.setText(_translate("ARReportWindow", "Refresh"))
        self.btn_print.setText(_translate("ARReportWindow", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ARReportWindow = QtWidgets.QMainWindow()
    ui = Ui_ARReportWindow()
    ui.ARReportSetupUi(ARReportWindow)
    ARReportWindow.show()
    sys.exit(app.exec_())

