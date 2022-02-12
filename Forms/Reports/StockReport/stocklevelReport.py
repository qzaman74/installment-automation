# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stocklevelReport.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BLL.ReportsBL.StockReportsBL import stockLevelReportBL
from Globals import globalVariables

class Ui_stockLevelWindow(object):

    def init(self):
        self.getStockLevel()

    def getStockLevel(self):
        result = stockLevelReportBL.getStockLevel()

        self.tbl_stockLevel.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_stockLevel.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tbl_stockLevel.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))




    def stockLevelSetupUi(self, stockLevelWindow):
        stockLevelWindow.setObjectName("stockLevelWindow")
        stockLevelWindow.resize(360, 519)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        stockLevelWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        stockLevelWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        stockLevelWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(stockLevelWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stockLevelGB = QtWidgets.QGroupBox(self.centralwidget)
        self.stockLevelGB.setGeometry(QtCore.QRect(5, 0, 350, 500))
        self.stockLevelGB.setObjectName("stockLevelGB")
        self.tbl_stockLevel = QtWidgets.QTableWidget(self.stockLevelGB)
        self.tbl_stockLevel.setGeometry(QtCore.QRect(5, 15, 340, 475))
        self.tbl_stockLevel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_stockLevel.setShowGrid(True)
        self.tbl_stockLevel.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_stockLevel.setWordWrap(True)
        self.tbl_stockLevel.setRowCount(15)
        self.tbl_stockLevel.setColumnCount(3)
        self.tbl_stockLevel.setHorizontalHeaderLabels(['Company', 'Product','Quantity'])
        self.tbl_stockLevel.setColumnWidth(0,125)
        self.tbl_stockLevel.setColumnWidth(1,130)
        self.tbl_stockLevel.setColumnWidth(2,60)

        self.tbl_stockLevel.setObjectName("tbl_stockLevel")

        stockLevelWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(stockLevelWindow)
        self.statusbar.setObjectName("statusbar")
        stockLevelWindow.setStatusBar(self.statusbar)

        self.retranslateUi(stockLevelWindow)
        QtCore.QMetaObject.connectSlotsByName(stockLevelWindow)

    def retranslateUi(self, stockLevelWindow):
        _translate = QtCore.QCoreApplication.translate
        stockLevelWindow.setWindowTitle(_translate("stockLevelWindow", "Stock Level"))
        self.stockLevelGB.setTitle(_translate("stockLevelWindow", "Current Stock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stockLevelWindow = QtWidgets.QMainWindow()
    ui = Ui_stockLevelWindow()
    ui.stockLevelSetupUi(stockLevelWindow)
    stockLevelWindow.show()
    sys.exit(app.exec_())

