# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSchemeForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from BLL.InstallmentsBL import addSchemeBL
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from Globals import globalVariables
from Services.MiscService import dateTime

class Ui_schemeWindow(object):
    def init(self):
        self.le_startDate.setText(self.cw_startCalendar.selectedDate().toString())
        self.le_endDate.setText(self.cw_endCalendar.selectedDate().toString())
        self.showAllScheme()

    def onStartDate(self):
        if(self.cw_startCalendar.isHidden()):
            self.cw_startCalendar.show()
        else:
            self.cw_startCalendar.hide()

    def setStartDate(self,date):
        self.le_startDate.setText(date.toString())
        self.cw_startCalendar.hide()
        self.btn_endDate.setFocus()

    def onEndDate(self):
        if(self.cw_endCalendar.isHidden()):
            self.cw_endCalendar.show()
        else:
            self.cw_endCalendar.hide()

    def setEndDate(self,date):
        self.le_endDate.setText(date.toString())
        self.cw_endCalendar.hide()
        self.sb_dueDate.setFocus()

    def onEnterScheme(self):
        self.btn_startDate.setFocus()

    def onChangeDueDate(self):
        self.le_installments.setFocus()
    def onEnterInstallments(self):
        self.le_installmentAmount.setFocus()

    def onEnterInstallmentAmount(self):
        self.te_remarks.setFocus()

    def onSubmit(self):

        scheme = self.le_scheme.text()
        startDate = self.le_startDate.text()
        endDate = self.le_endDate.text()
        dueDate = self.sb_dueDate.value()
        installments = self.le_installments.text()
        amount = self.le_installmentAmount.text()
        remarks = self.te_remarks.toPlainText()

        addSchemeBL.validateScheme(self, scheme, startDate, endDate, dueDate, installments, amount, remarks)

    def deleteScheme(self):
        button = self.tbl_scheme.sender()
        index = self.tbl_scheme.indexAt(button.pos())
        if index.isValid():
            schemeID = self.tbl_scheme.model().index(index.row(), 0).data()
            title = self.tbl_scheme.model().index(index.row(), 1).data()
            addSchemeBL.deleteScheme(self, schemeID, title)

    def showAllScheme(self):
        result = addSchemeBL.getAllSchemes()

        self.tbl_scheme.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_scheme.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if(colum_number == 2 or colum_number == 3):
                    self.tbl_scheme.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(dateTime.getDateWithoutTime(data)))
                else:
                    self.tbl_scheme.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

                self.btn_delete = QPushButton('Remove')
                delIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
                self.btn_delete.setIcon(QtGui.QIcon(delIcon))
                self.tbl_scheme.setCellWidget(row_number,8, self.btn_delete)
                self.btn_delete.clicked.connect(self.deleteScheme)

        if(self.tbl_scheme.rowCount()<18):
            self.tbl_scheme.setRowCount(18)


    def onCancel(self):
        self.le_scheme.setText('')
        self.le_startDate.setText(self.cw_startCalendar.selectedDate().toString())
        self.le_endDate.setText(self.cw_endCalendar.selectedDate().toString())
        self.sb_dueDate.setValue(1)
        self.le_installments.setText('')
        self.le_installmentAmount.setText('')
        self.te_remarks.setText('')



    def schemeSetupUi(self, schemeWindow):
        schemeWindow.setObjectName("schemeWindow")
        schemeWindow.resize(1373, 723)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        schemeWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        schemeWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        schemeWindow.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        charRegex=QtCore.QRegExp("[a-z-A-Z- -_]+")
        self.onlyChar = QtGui.QRegExpValidator(charRegex)


        self.centralwidget = QtWidgets.QWidget(schemeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addSchemeGB = QtWidgets.QGroupBox(self.centralwidget)
        self.addSchemeGB.setEnabled(True)
        self.addSchemeGB.setGeometry(QtCore.QRect(10, 0, 311, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSchemeGB.sizePolicy().hasHeightForWidth())
        self.addSchemeGB.setSizePolicy(sizePolicy)
        self.addSchemeGB.setObjectName("addSchemeGB")
        self.btn_submit = QtWidgets.QPushButton(self.addSchemeGB)
        self.btn_submit.setGeometry(QtCore.QRect(100, 640, 100, 28))
        submitIcon = QtGui.QPixmap(globalVariables.Variables._icon+'rightIcon.png')
        self.btn_submit.setIcon(QtGui.QIcon(submitIcon))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.onSubmit)

        self.btn_cancel = QtWidgets.QPushButton(self.addSchemeGB)
        self.btn_cancel.setGeometry(QtCore.QRect(200, 640, 100, 28))
        cancelIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cancelIcon.png')
        self.btn_cancel.setIcon(QtGui.QIcon(cancelIcon))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.onCancel)

        self.label_11 = QtWidgets.QLabel(self.addSchemeGB)
        self.label_11.setGeometry(QtCore.QRect(10, 25, 81, 28))
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
        self.le_scheme = QtWidgets.QLineEdit(self.addSchemeGB)
        self.le_scheme.setEnabled(True)
        self.le_scheme.setGeometry(QtCore.QRect(100, 25, 200, 28))
        self.le_scheme.setObjectName("le_scheme")
        self.le_scheme.returnPressed.connect(self.onEnterScheme)

        self.le_installments = QtWidgets.QLineEdit(self.addSchemeGB)
        self.le_installments.setEnabled(True)
        self.le_installments.setGeometry(QtCore.QRect(100, 165, 200, 28))
        self.le_installments.setObjectName("le_installments")
        self.le_installments.returnPressed.connect(self.onEnterInstallments)
        self.label_13 = QtWidgets.QLabel(self.addSchemeGB)
        self.label_13.setGeometry(QtCore.QRect(10, 200, 81, 28))
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
        self.le_installmentAmount = QtWidgets.QLineEdit(self.addSchemeGB)
        self.le_installmentAmount.setGeometry(QtCore.QRect(100, 200, 200, 28))
        self.le_installmentAmount.setObjectName("le_installmentAmount")
        self.le_installmentAmount.returnPressed.connect(self.onEnterInstallmentAmount)
        self.label_6 = QtWidgets.QLabel(self.addSchemeGB)
        self.label_6.setGeometry(QtCore.QRect(10, 235, 71, 28))
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
        self.te_remarks = QtWidgets.QTextEdit(self.addSchemeGB)
        self.te_remarks.setEnabled(True)
        self.te_remarks.setGeometry(QtCore.QRect(100, 235, 200, 71))
        self.te_remarks.setObjectName("te_remarks")
        self.label_12 = QtWidgets.QLabel(self.addSchemeGB)
        self.label_12.setGeometry(QtCore.QRect(10, 165, 91, 28))
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
        self.label_14 = QtWidgets.QLabel(self.addSchemeGB)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 81, 28))
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
        self.le_startDate = QtWidgets.QLineEdit(self.addSchemeGB)
        self.le_startDate.setEnabled(False)
        self.le_startDate.setGeometry(QtCore.QRect(100, 60, 170, 28))
        self.le_startDate.setObjectName("le_startDate")
        self.le_endDate = QtWidgets.QLineEdit(self.addSchemeGB)
        self.le_endDate.setEnabled(False)
        self.le_endDate.setGeometry(QtCore.QRect(100, 95, 170, 28))
        self.le_endDate.setObjectName("le_endDate")
        self.label_15 = QtWidgets.QLabel(self.addSchemeGB)
        self.label_15.setGeometry(QtCore.QRect(10, 95, 81, 28))
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

        self.btn_startDate = QtWidgets.QPushButton(self.addSchemeGB)
        self.btn_startDate.setGeometry(QtCore.QRect(270, 60, 30, 28))
        calendarIcon = QtGui.QPixmap(globalVariables.Variables._icon+'calendarIcon.png')
        self.btn_startDate.setIcon(QtGui.QIcon(calendarIcon))
        self.btn_startDate.setText("")
        self.btn_startDate.setObjectName("btn_startDate")
        self.btn_startDate.clicked.connect(self.onStartDate)

        self.btn_endDate = QtWidgets.QPushButton(self.addSchemeGB)
        self.btn_endDate.setGeometry(QtCore.QRect(270, 95, 30, 28))
        calendarIcon = QtGui.QPixmap(globalVariables.Variables._icon+'calendarIcon.png')
        self.btn_endDate.setIcon(QtGui.QIcon(calendarIcon))
        self.btn_endDate.setText("")
        self.btn_endDate.setObjectName("btn_endDate")
        self.btn_endDate.clicked.connect(self.onEndDate)

        self.sb_dueDate = QtWidgets.QSpinBox(self.addSchemeGB)
        self.sb_dueDate.setGeometry(QtCore.QRect(100, 130, 200, 28))
        self.sb_dueDate.setMinimum(1)
        self.sb_dueDate.setMaximum(31)
        self.sb_dueDate.setObjectName("sb_dueDate")
        self.sb_dueDate.valueChanged.connect(self.onChangeDueDate)

        self.label_16 = QtWidgets.QLabel(self.addSchemeGB)
        self.label_16.setGeometry(QtCore.QRect(10, 130, 81, 28))
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


        self.cw_startCalendar = QtWidgets.QCalendarWidget(self.addSchemeGB)
        self.cw_startCalendar.setGeometry(QtCore.QRect(0, 90, 312, 183))
        self.cw_startCalendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.cw_startCalendar.setVisible(False)
        self.cw_startCalendar.setObjectName("cw_startCalendar")
        self.cw_startCalendar.hide()
        self.cw_startCalendar.clicked[QtCore.QDate].connect(self.setStartDate)

        self.cw_endCalendar = QtWidgets.QCalendarWidget(self.addSchemeGB)
        self.cw_endCalendar.setGeometry(QtCore.QRect(0, 120, 312, 183))
        self.cw_endCalendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.cw_endCalendar.setObjectName("cw_endCalendar")
        self.cw_endCalendar.hide()
        self.cw_endCalendar.clicked[QtCore.QDate].connect(self.setEndDate)


        self.showSchemeGB = QtWidgets.QGroupBox(self.centralwidget)
        self.showSchemeGB.setGeometry(QtCore.QRect(330, 0, 1031, 681))
        self.showSchemeGB.setObjectName("showSchemeGB")
        self.tbl_scheme = QtWidgets.QTableWidget(self.showSchemeGB)
        self.tbl_scheme.setGeometry(QtCore.QRect(10, 70, 1011, 601))
        self.tbl_scheme.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_scheme.setRowCount(19)
        self.tbl_scheme.setColumnCount(9)
        self.tbl_scheme.setHorizontalHeaderLabels(['ID', 'Title', 'Start Date', 'End Date', 'Due Date',
                                                   'Installments','Amount', 'Remarks','Remove'])
        self.tbl_scheme.hideColumn(0)
        self.tbl_scheme.setColumnWidth(1,150)
        self.tbl_scheme.setColumnWidth(4,55)
        self.tbl_scheme.setColumnWidth(5,65)
        self.tbl_scheme.setColumnWidth(6,50)
        self.tbl_scheme.setColumnWidth(7,360)
        self.tbl_scheme.setObjectName("tbl_scheme")

        self.filterAccountGB = QtWidgets.QGroupBox(self.showSchemeGB)
        self.filterAccountGB.setGeometry(QtCore.QRect(10, 20, 1011, 41))
        self.filterAccountGB.setObjectName("filterAccountGB")
        self.le_filterByName = QtWidgets.QLineEdit(self.filterAccountGB)
        self.le_filterByName.setGeometry(QtCore.QRect(0, 20, 100, 20))
        self.le_filterByName.setObjectName("le_filterByName")
        self.le_filterByUserName = QtWidgets.QLineEdit(self.filterAccountGB)
        self.le_filterByUserName.setGeometry(QtCore.QRect(110, 20, 100, 20))
        self.le_filterByUserName.setObjectName("le_filterByUserName")
        self.le_filterByCnic = QtWidgets.QLineEdit(self.filterAccountGB)
        self.le_filterByCnic.setGeometry(QtCore.QRect(220, 20, 100, 20))
        self.le_filterByCnic.setObjectName("le_filterByCnic")
        self.le_filterByMobile = QtWidgets.QLineEdit(self.filterAccountGB)
        self.le_filterByMobile.setGeometry(QtCore.QRect(330, 20, 100, 20))
        self.le_filterByMobile.setObjectName("le_filterByMobile")
        self.le_filterByAddress = QtWidgets.QLineEdit(self.filterAccountGB)
        self.le_filterByAddress.setGeometry(QtCore.QRect(440, 20, 100, 20))
        self.le_filterByAddress.setObjectName("le_filterByAddress")

        self.btn_refresh = QtWidgets.QPushButton(self.filterAccountGB)
        self.btn_refresh.setGeometry(QtCore.QRect(910, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.showAllScheme)

        schemeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(schemeWindow)
        self.statusbar.setObjectName("statusbar")
        schemeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(schemeWindow)
        QtCore.QMetaObject.connectSlotsByName(schemeWindow)

    def retranslateUi(self, schemeWindow):
        _translate = QtCore.QCoreApplication.translate
        schemeWindow.setWindowTitle(_translate("schemeWindow", "Add Scheme Window"))
        self.addSchemeGB.setTitle(_translate("schemeWindow", "Add New Scheme"))
        self.btn_submit.setText(_translate("schemeWindow", "Submit"))
        self.btn_cancel.setText(_translate("schemeWindow", "Cancel"))
        self.label_11.setText(_translate("schemeWindow", "Scheme"))
        self.label_13.setText(_translate("schemeWindow", "Amount"))
        self.label_6.setText(_translate("schemeWindow", "Remarks"))
        self.label_12.setText(_translate("schemeWindow", "Installments"))
        self.label_14.setText(_translate("schemeWindow", "Start Date"))
        self.label_15.setText(_translate("schemeWindow", "End Date"))
        self.label_16.setText(_translate("schemeWindow", "Due Date"))
        self.showSchemeGB.setTitle(_translate("schemeWindow", "All scheme"))
        self.filterAccountGB.setTitle(_translate("schemeWindow", "Filter"))
        self.btn_refresh.setText(_translate("schemeWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    schemeWindow = QtWidgets.QMainWindow()
    ui = Ui_schemeWindow()
    ui.schemeSetupUi(schemeWindow)
    schemeWindow.show()
    sys.exit(app.exec_())

