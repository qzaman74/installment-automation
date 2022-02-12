
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

from Globals import globalVariables,globalList
from BLL.PurchaseBL import purchaseBL

from Services.ImgService import camera,image,browseImage
from Services.MiscService import dateTime
from Services.ResetServices import formReset
from Services.RecallServices import formRecall

class Ui_purchaseWindow(object):
    _cartItemList = []
    _policyList = []
    _filterList = []

    _imageCode = ''

    def init(self):
        self.le_date.setText(self.calendar.selectedDate().toString())
        self.setCompany()
        self.cb_accountType.setCurrentIndex(2)
        self.onAccountTypeChange(self.cb_accountType.currentText())

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
            self.cb_account.clear()
        if(self.cb_accountType.currentIndex()>0):
            self.setAccounts(text)
            self.cb_account.setFocus()

    def setAccounts(self,accountType):
        self.cb_account.clear()
        self.cb_account.addItem("")
        accountList = purchaseBL.getAccountByType(accountType)
        for id, name, mob in accountList:
            self.cb_account.addItem(mob+"-"+name.upper(),id)

    def onChangeAccount(self):
        self.getPurchase()
        self.le_invoice.setFocus()

    def onEnterInvoice(self):
        self.cb_company.setFocus()

    def setCompany(self):
        self.cb_company.clear()
        self.cb_company.addItem("SELECT")
        companyList = purchaseBL.getCompany()
        for id, name, code, representative, contact, location in companyList:
            self.cb_company.addItem(name.upper(),id)

    def onCompanyChange(self):
        companyID = self.cb_company.currentData()
        if(self.cb_company.currentIndex()>0):
            self.setProduct(companyID)
            self.cb_product.setFocus()
        else:
            pass

    def setProduct(self,companyID):
        self.cb_product.clear()
        self.cb_product.addItem("SELECT")
        productList = purchaseBL.getProduct(companyID)
        for productId, companyId, productType, name, code, remarks in productList:
            self.cb_product.addItem(name.upper(),productId)

    def onChangeProduct(self):
        self.le_engine.setFocus()

    def onEnterEngine(self):
        self.le_chassis.setFocus()

    def onEnterChassis(self):
        self.le_registration.setFocus()
        
    def onEnterRegistration(self):
        self.le_costPrice.setFocus()

    def onEnterCostPrice(self):
        self.le_salePrice.setFocus()

    def onChangeCostPrice(self):
        self.le_totalPrice.setText(self.le_costPrice.text())

    def onEnterSalePrice(self):
        self.le_itemDiscountPercent.setFocus()

    def onEnterItemDiscountPercent(self):
        self.le_itemDiscountAmount.setFocus()

    def onEnterItemDiscountAmount(self):
        self.le_remarks.setFocus()

    def onEnterRemarks(self):
        self.onAddItem()


    def quickAccount(self):
        purchaseBL.validateOpenQuickAccount(self)
        formRecall.Recall._recallQuickAccount = self.setAccounts(self.cb_accountType.currentText())

    def quickCompnay(self):
        formRecall.Recall._recallCompanyListForPurchase = self.setCompany
        purchaseBL.validateOpenQuickCompany(self)

    def quickProduct(self):
        purchaseBL.validateOpenQuickProduct(self)

    def onCheckNet(self):
        self.cb_net.setChecked(True)
        self.cb_shortTerm.setChecked(False)
        self.cb_lease.setChecked(False)
        self.tbl_lease.setEnabled(False)

    def onCheckShortTerm(self):
        self.cb_shortTerm.setChecked(True)
        self.cb_net.setChecked(False)
        self.cb_lease.setChecked(False)
        self.tbl_lease.setEnabled(True)

    def onCheckLease(self):
        self.cb_lease.setChecked(True)
        self.cb_shortTerm.setChecked(False)
        self.cb_net.setChecked(False)
        self.tbl_lease.setEnabled(True)

    def capture(self):
        try:
            base64Img = camera.capture()
            self._imageCode = base64Img
            self.lbl_image.setPixmap(image.getPixmap(base64Img))
        except:
            pass

    def browse(self):
        try:
            base64Img = browseImage.getImagePath(self.__init__())
            self._imageCode = base64Img
            self.lbl_image.setPixmap(image.getPixmap(base64Img))
        except:
            pass


    def calculateItemDiscountAmount(self):
        cp = self.le_costPrice.text()
        dp = self.le_itemDiscountPercent.text()
        da = 0
        try:
            if(dp != '' and cp != ''):
                da = ((int(cp) * int(dp)) / 100)
                amount = (int(cp) - da)
                self.le_itemDiscountAmount.setText(str(da))
                self.le_totalPrice.setText(str(amount))

            else:
                self.le_itemDiscountAmount.setText('')
                self.le_totalPrice.setText(cp)
        except:
            pass

    def calculateItemDiscountPercentage(self):
        cp = self.le_costPrice.text()
        da = self.le_itemDiscountAmount.text()
        dp = 0
        try:
            if(da != '' and cp != ''):
                dp = (int(da) * 100) / int(cp)
                amount = (int(cp) - int(da))
                self.le_itemDiscountPercent.setText(str(dp))
                self.le_totalPrice.setText(str(amount))
            else:
                self.le_itemDiscountPercent.setText('')
                self.le_totalPrice.setText(cp)
        except:
            pass


    def calculateBillDiscountAmount(self):
        tb = self.le_totalBill.text()
        dp = self.le_billDiscountPercent.text()
        payment = self.le_payment.text()
        da = 0
        try:
            if(dp != '' and tb != ''):
                da = ((int(tb) * int(dp)) / 100)
                amount = (int(tb) - da)
                self.le_billDiscountAmount.setText(str(da))
                self.le_netBill.setText(str(amount))
                self.le_balance.setText(str(amount))
                if(payment != ''):
                    balance = amount - int(payment)
                    self.le_balance.setText(str(balance))

            else:
                self.le_billDiscountAmount.setText('')
                self.le_netBill.setText(tb)
                self.le_balance.setText(tb)
                if(payment != ''):
                    balance = int(tb) - int(payment)
                    self.le_balance.setText(str(balance))
        except:
            pass

    def calculateBillDiscountPercentage(self):
        tb = self.le_totalBill.text()
        da = self.le_billDiscountAmount.text()
        payment = self.le_payment.text()
        dp = 0
        try:
            if(da != '' and tb != ''):
                dp = (int(da) * 100) / int(tb)
                amount = (int(tb) - int(da))
                self.le_billDiscountPercent.setText(str(dp))
                self.le_netBill.setText(str(amount))
                self.le_balance.setText(str(amount))
                if(payment != ''):
                    balance = amount - int(payment)
                    self.le_balance.setText(str(balance))
            else:
                self.le_billDiscountPercent.setText('')
                self.le_netBill.setText(tb)
                self.le_balance.setText(tb)
                if (payment != ''):
                    balance = int(tb) - int(payment)
                    self.le_balance.setText(str(balance))
        except:
            pass




    def onSubmit(self):
        policyType = ''


        if(self.cb_net.isChecked() == True):
            policyType = globalVariables.Variables._net

        if(self.cb_shortTerm.isChecked() == True):
            policyType = globalVariables.Variables._shortTerm

            tblRows = self.tbl_lease.rowCount()
            for row in range(1, tblRows):
                twi0 = self.tbl_lease.item(row, 0).text()
                twi1 = self.tbl_lease.item(row, 1).text()
                twi2 = self.tbl_lease.item(row, 2).text()
                self._policyList.append(twi0 + ',' + twi1 + ',' + twi2)

        if(self.cb_lease.isChecked() == True):
            policyType = globalVariables.Variables._lease

            tblRows = self.tbl_lease.rowCount()
            for row in range(1, tblRows):
                twi0 = self.tbl_lease.item(row, 0).text()
                twi1 = self.tbl_lease.item(row, 1).text()
                twi2 = self.tbl_lease.item(row, 2).text()
                self._policyList.append(twi0 + ',' + twi1 + ',' + twi2)



        date = self.le_date.text()
        accountId = self.cb_account.currentData()
        accountName = self.cb_account.currentText()
        invoice = self.le_invoice.text()
        # billType = globalVariables.Variables._purchase
        amount = self.le_totalBill.text()
        discount = self.le_billDiscountAmount.text()
        netAmount = self.le_netBill.text()
        payment = self.le_payment.text()
        balance = self.le_balance.text()
        imageCode = self._imageCode
        itemList = self._cartItemList
        policyList = self._policyList

        formReset.Reset._resetPurchaseForm = self.onCancel

        purchaseBL.validatePurchase(self, date, accountId, accountName, invoice, amount, discount,
                                    netAmount, payment, balance, imageCode, itemList, policyType, policyList)


    def onAddItem(self):

        companyId = self.cb_company.currentData()
        companyName = self.cb_company.currentText()
        productId = self.cb_product.currentData()
        productName = self.cb_product.currentText()

        productType = ''
        if(self.rb_new.isChecked() == True):
            productType = globalVariables.Variables._newProduct
        if(self.rb_used.isChecked() == True):
            productType = globalVariables.Variables._usedProduct

        engine = self.le_engine.text()
        chessis = self.le_chassis.text()
        registration = self.le_registration.text()

        costPrice = self.le_costPrice.text()
        salePrice = self.le_salePrice.text()

        discountAmount = self.le_itemDiscountAmount.text()
        totalPrice = self.le_totalPrice.text()

        remarks = self.le_remarks.text()
        if(remarks == ''):
            remarks = 'NO remarks'

        formReset.Reset._resetPurchaseItem = self.clearItem

        purchaseBL.validateAddItem( companyId, companyName, productId, productName, productType, engine, chessis,
                                    registration, costPrice, salePrice, discountAmount, totalPrice, remarks)
        self.showCartItem()
        self.le_engine.setFocus()

    def removeItem(self):
        button = self.tbl_cart.sender()
        index = self.tbl_cart.indexAt(button.pos())
        itemIndex = int(str(index.row()))
        purchaseBL.removeItemFromCart(itemIndex)
        self.showCartItem()

    def showCartItem(self):
        totalBill = 0

        self.tbl_cart.setRowCount(0)
        for row_number, row_data in enumerate(self._cartItemList):
            self.tbl_cart.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tbl_cart.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                if(colum_number == 11):
                    totalBill = totalBill + int(float(data))

                self.btn_deleteItem = QPushButton('')
                removeIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
                self.btn_deleteItem.setIcon(QtGui.QIcon(removeIcon))
                self.tbl_cart.setCellWidget(row_number,13, self.btn_deleteItem)
                self.btn_deleteItem.clicked.connect(self.removeItem)

        if(self.tbl_cart.rowCount()<14):
            self.tbl_cart.setRowCount(14)

        self.le_totalBill.setText(str(totalBill))
        self.le_netBill.setText(str(totalBill))
        self.le_balance.setText(str(totalBill))
        self.tbl_lease.setItem(0, 2, QtWidgets.QTableWidgetItem(str(totalBill)))

    def onChangePayment(self):
        try:
            payment = self.le_payment.text()
            netBill = self.le_netBill.text()
            if(netBill != '' and payment != ''):
                balance = int(netBill) - int(payment)
                self.le_balance.setText(str(balance))
                self.tbl_lease.setItem(0, 2, QtWidgets.QTableWidgetItem(str(balance)))
            else:
                self.le_balance.setText(netBill)
                self.tbl_lease.setItem(0, 2, QtWidgets.QTableWidgetItem(str(netBill)))
        except:
            pass

    def clearItem(self):
        self.le_engine.setText('')
        self.le_chassis.setText('')
        self.le_registration.setText('')
        self.le_costPrice.setText('')
        self.le_salePrice.setText('')
        self.le_itemDiscountAmount.setText('0')
        self.le_itemDiscountPercent.setText('0')
        self.le_totalPrice.setText('')
        self.le_remarks.setText('')

    def onCancel(self):
        self.cb_accountType.setCurrentIndex(0)
        self.le_invoice.clear()
        self.cb_company.setCurrentIndex(0)
        self.cb_product.setCurrentIndex(0)
        self.le_totalBill.setText('0')
        self.le_netBill.setText('0')
        self.le_billDiscountAmount.setText('0')
        self.le_billDiscountPercent.setText('0')
        self.le_payment.setText('0')
        self.le_balance.setText('0')
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'invoice.png'))
        del self._cartItemList[:]
        del self._policyList[:]
        self.tbl_lease.setRowCount(1)

        self.clearItem()
        self.showCartItem()


    def getPurchase(self):
        try:
            accountId = None
            accountId = self.cb_account.currentData()
            if(accountId != None):
                billType = globalVariables.Variables._purchase
                result = purchaseBL.getBill(accountId, billType)
                self.showPurchase(result)
                self._filterList = purchaseBL.getBill(accountId, billType).fetchall().copy()
        except:
            pass

    def showPurchase(self,result):
        self.tbl_purchase.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_purchase.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if(colum_number == 2):
                    self.tbl_purchase.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(dateTime.getDateWithoutTime(data))))
                else:
                    self.tbl_purchase.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

                self.btn_billImage = QPushButton('')
                imageIcon = QtGui.QPixmap(globalVariables.Variables._icon + 'imageIcon.png')
                self.btn_billImage.setIcon(QtGui.QIcon(imageIcon))
                self.tbl_purchase.setCellWidget(row_number, 11, self.btn_billImage)

                self.btn_billDetail = QPushButton('')
                detailIcon = QtGui.QPixmap(globalVariables.Variables._icon + 'viewDetailIcon.png')
                self.btn_billDetail.setIcon(QtGui.QIcon(detailIcon))
                self.tbl_purchase.setCellWidget(row_number, 12, self.btn_billDetail)

        if(self.tbl_purchase.rowCount()<12):
            self.tbl_purchase.setRowCount(12)


    def filterFunc(self,item):
        invoice= self.le_filterByInvoice.text()
        date = self.le_filterByDate.text()
        discount = self.le_filterByDiscount.text()
        netBill = self.le_filterByNetBill.text()
        payment = self.le_filterByPayment.text()
        balance = self.le_filterByBalance.text()

        if (str(item[2]).startswith(date) and str(item[3]).startswith(invoice) and
            str(item[6]).startswith(discount) and str(item[7]).startswith(netBill)  and
            str(item[8]).startswith(payment) and str(item[9]).startswith(balance) ):
            return True
        else:
            return False

    def filter(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.showPurchase(result)

    def onAddLeaseRow(self):
        try:
            button = self.tbl_lease.sender()
            index = self.tbl_lease.indexAt(button.pos())
            row = index.row()
            # if(self.tbl_lease.item(row,0) != None and self.tbl_lease.item(row,1) != None and self.tbl_lease.item(row,2) != None and self.tbl_lease.item(row,2) != '0' ):
            if(int(self.tbl_lease.item(row,2).text()) > 0):
                self.tbl_lease.insertRow(row + 1)

                self.btn_addLease = QPushButton('')
                addIcon = QtGui.QPixmap(globalVariables.Variables._icon+'addIcon.png')
                self.btn_addLease.setIcon(QtGui.QIcon(addIcon))
                self.tbl_lease.setCellWidget(row + 1 , 3, self.btn_addLease)
                self.btn_addLease.clicked.connect(self.onAddLeaseRow)

            self.btn_removeLease = QPushButton('')
            removeIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
            self.btn_removeLease.setIcon(QtGui.QIcon(removeIcon))
            self.tbl_lease.setCellWidget(row + 1, 4, self.btn_removeLease)
            self.btn_removeLease.clicked.connect(self.onRemoveLeaseRow)
        except:
            pass

    def onRemoveLeaseRow(self):
        button = self.tbl_lease.sender()
        index = self.tbl_lease.indexAt(button.pos())
        itemIndex = int(str(index.row()))
        if(itemIndex != 0 ):
            self.tbl_lease.removeRow(itemIndex)

    def changeTbl(self, item):
        try:
            balance  = 0
            row = item.row()
            col = item.column()

            if(row > 0 and col == 1 ):
                amount = self.tbl_lease.item(row,1).text()
                bal = self.tbl_lease.item(row - 1, 2).text()
                if( int(bal) > 0 ):
                    balance = str(int(bal)-int(amount))
                    # print(str(balance))
                    # balance = int(bal) - int(amount)
                    self.tbl_lease.setItem(row, 2, QtWidgets.QTableWidgetItem(balance))
                if(amount == 0 ):
                    balance = self.le_payment
                    self.tbl_lease.setItem(row, 2, QtWidgets.QTableWidgetItem(balance))
        except:
            pass



    def showPlanCalendar(self, row, column):
        if(row != 0 ):
            self.planCalendarRow = row
            if(column == 0):
                if (self.planCalendar.isHidden()):
                    self.planCalendar.show()
                else:
                    self.planCalendar.hide()

    def setPlanDate(self, date):
        if(self.planCalendarRow != 0 ):
            self.tbl_lease.setItem(self.planCalendarRow, 0, QtWidgets.QTableWidgetItem(date.toString()))
            self.planCalendar.hide()

    def purchaseSetupUi(self, purchaseWindow):
        purchaseWindow.setObjectName("purchaseWindow")
        purchaseWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        purchaseWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        purchaseWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        purchaseWindow.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)
        
        self.centralwidget = QtWidgets.QWidget(purchaseWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.addPurchaseGB = QtWidgets.QGroupBox(self.centralwidget)
        self.addPurchaseGB.setGeometry(QtCore.QRect(10, 0, 281, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPurchaseGB.sizePolicy().hasHeightForWidth())
        self.addPurchaseGB.setSizePolicy(sizePolicy)
        self.addPurchaseGB.setObjectName("addPurchaseGB")
        
        self.btn_date = QtWidgets.QPushButton(self.addPurchaseGB)
        self.btn_date.setGeometry(QtCore.QRect(240, 15, 30, 25))
        dateIcon = QtGui.QPixmap(globalVariables.Variables._icon+'calendarIcon.png')
        self.btn_date.setIcon(QtGui.QIcon(dateIcon))
        self.btn_date.setObjectName("btn_date")
        self.btn_date.clicked.connect(self.showCalendar)
        
        self.le_date = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_date.setEnabled(False)
        self.le_date.setGeometry(QtCore.QRect(90, 15, 150, 25))
        self.le_date.setObjectName("le_date")
        
        self.cb_account = QtWidgets.QComboBox(self.addPurchaseGB)
        self.cb_account.setGeometry(QtCore.QRect(90, 70, 180, 25))
        self.cb_account.setEditable(True)
        self.cb_account.setObjectName("cb_account")
        self.cb_account.activated.connect(self.onChangeAccount)
        
        self.le_invoice = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_invoice.setGeometry(QtCore.QRect(90, 98, 180, 25))
        self.le_invoice.setMaxLength(32)
        self.le_invoice.setObjectName("le_invoice")
        self.le_invoice.returnPressed.connect(self.onEnterInvoice)
        
        self.cb_company = QtWidgets.QComboBox(self.addPurchaseGB)
        self.cb_company.setGeometry(QtCore.QRect(90, 147, 150, 25))
        self.cb_company.setObjectName("cb_company")
        self.cb_company.activated[str].connect(self.onCompanyChange)
        
        self.btn_quickCompany = QtWidgets.QPushButton(self.addPurchaseGB)
        self.btn_quickCompany.setGeometry(QtCore.QRect(240, 147, 30, 25))
        addIcon = QtGui.QPixmap(globalVariables.Variables._icon+'addIcon.png')
        self.btn_quickCompany.setIcon(QtGui.QIcon(addIcon))
        self.btn_quickCompany.setToolTip("Add Company Quickly")
        self.btn_quickCompany.setObjectName("btn_quickCompany")
        self.btn_quickCompany.clicked.connect(self.quickCompnay)
        
        self.cb_product = QtWidgets.QComboBox(self.addPurchaseGB)
        self.cb_product.setGeometry(QtCore.QRect(90, 176, 150, 25))
        self.cb_product.setObjectName("cb_product")
        self.cb_product.activated.connect(self.onChangeProduct)
        
        self.btn_quickProduct = QtWidgets.QPushButton(self.addPurchaseGB)
        self.btn_quickProduct.setGeometry(QtCore.QRect(240, 176, 30, 25))
        addIcon = QtGui.QPixmap(globalVariables.Variables._icon+'addIcon.png')
        self.btn_quickProduct.setIcon(QtGui.QIcon(addIcon))
        self.btn_quickProduct.setToolTip("Add Product Quickly")
        self.btn_quickProduct.setObjectName("btn_quickProduct")
        self.btn_quickProduct.clicked.connect(self.quickProduct)
        
        self.le_engine = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_engine.setGeometry(QtCore.QRect(90, 205, 180, 25))
        self.le_engine.setMaxLength(32)
        self.le_engine.setObjectName("le_engine")
        self.le_engine.returnPressed.connect(self.onEnterEngine)
        
        self.le_chassis = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_chassis.setGeometry(QtCore.QRect(90, 232, 180, 25))
        self.le_chassis.setMaxLength(32)
        self.le_chassis.setObjectName("le_chassis")
        self.le_chassis.returnPressed.connect(self.onEnterChassis)
        
        self.le_registration = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_registration.setGeometry(QtCore.QRect(90, 260, 180, 25))
        self.le_registration.setMaxLength(32)
        self.le_registration.setObjectName("le_registration")
        self.le_registration.returnPressed.connect(self.onEnterRegistration)
        
        self.le_costPrice = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_costPrice.setGeometry(QtCore.QRect(90, 288, 180, 25))
        self.le_costPrice.setMaxLength(32)
        self.le_costPrice.setValidator(self.onlyInt)
        self.le_costPrice.setObjectName("le_costPrice")
        self.le_costPrice.textChanged.connect(self.onChangeCostPrice)
        self.le_costPrice.returnPressed.connect(self.onEnterCostPrice)
        
        self.le_salePrice = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_salePrice.setGeometry(QtCore.QRect(90, 315, 180, 25))
        self.le_salePrice.setMaxLength(32)
        self.le_salePrice.setValidator(self.onlyInt)
        self.le_salePrice.setObjectName("le_salePrice")
        self.le_salePrice.returnPressed.connect(self.onEnterSalePrice)
        
        self.lbl_date_5 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_5.setGeometry(QtCore.QRect(10, 147, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_5.setFont(font)
        self.lbl_date_5.setObjectName("lbl_date_5")
        
        self.lbl_date_9 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_9.setGeometry(QtCore.QRect(10, 288, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_9.setFont(font)
        self.lbl_date_9.setObjectName("lbl_date_9")
        self.lbl_date_3 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_3.setGeometry(QtCore.QRect(10, 70, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_3.setFont(font)
        self.lbl_date_3.setObjectName("lbl_date_3")
        self.lbl_date_8 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_8.setGeometry(QtCore.QRect(10, 232, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_8.setFont(font)
        self.lbl_date_8.setObjectName("lbl_date_8")
        self.lbl_date_2 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_2.setGeometry(QtCore.QRect(10, 15, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_2.setFont(font)
        self.lbl_date_2.setObjectName("lbl_date_2")
        self.lbl_date_4 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_4.setGeometry(QtCore.QRect(10, 98, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_4.setFont(font)
        self.lbl_date_4.setObjectName("lbl_date_4")
        self.lbl_date_7 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_7.setGeometry(QtCore.QRect(10, 205, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_7.setFont(font)
        self.lbl_date_7.setObjectName("lbl_date_7")
        self.lbl_date_10 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_10.setGeometry(QtCore.QRect(10, 315, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_10.setFont(font)
        self.lbl_date_10.setObjectName("lbl_date_10")
        self.lbl_date_6 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_6.setGeometry(QtCore.QRect(10, 176, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_6.setFont(font)
        self.lbl_date_6.setObjectName("lbl_date_6")
        
        self.le_itemDiscountPercent = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_itemDiscountPercent.setGeometry(QtCore.QRect(90, 342, 180, 25))
        self.le_itemDiscountPercent.setText('0')
        self.le_itemDiscountPercent.setValidator(self.onlyInt)
        self.le_itemDiscountPercent.setObjectName("le_itemDiscountPercent")
        self.le_itemDiscountPercent.textChanged.connect(self.calculateItemDiscountAmount)
        self.le_itemDiscountPercent.returnPressed.connect(self.onEnterItemDiscountPercent)

        self.le_itemDiscountAmount = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_itemDiscountAmount.setGeometry(QtCore.QRect(90, 370, 180, 25))
        self.le_itemDiscountAmount.setText('0')
        self.le_itemDiscountAmount.setValidator(self.onlyInt)
        self.le_itemDiscountAmount.setObjectName("le_itemDiscountAmount")
        self.le_itemDiscountAmount.textChanged.connect(self.calculateItemDiscountPercentage)
        self.le_itemDiscountAmount.returnPressed.connect(self.onEnterItemDiscountAmount)

        self.btn_addItem = QtWidgets.QPushButton(self.addPurchaseGB)
        self.btn_addItem.setGeometry(QtCore.QRect(170, 450, 100, 28))
        addIcon = QtGui.QPixmap(globalVariables.Variables._icon+'addIcon.png')
        self.btn_addItem.setIcon(QtGui.QIcon(addIcon))
        self.btn_addItem.setObjectName("btn_addItem")
        self.btn_addItem.clicked.connect(self.onAddItem)
        
        self.le_totalPrice = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_totalPrice.setGeometry(QtCore.QRect(90, 398, 180, 25))
        self.le_totalPrice.setMaxLength(32)
        self.le_totalPrice.setEnabled(False)
        self.le_totalPrice.setObjectName("le_totalPrice")
        
        self.lbl_date_11 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_11.setGeometry(QtCore.QRect(10, 398, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_11.setFont(font)
        self.lbl_date_11.setObjectName("lbl_date_11")
        
        self.lbl_date_18 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_18.setGeometry(QtCore.QRect(10, 342, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_18.setFont(font)
        self.lbl_date_18.setObjectName("lbl_date_18")
        
        self.lbl_date_19 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_19.setGeometry(QtCore.QRect(10, 370, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_19.setFont(font)
        self.lbl_date_19.setObjectName("lbl_date_19")
        
        self.lbl_date_21 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_21.setGeometry(QtCore.QRect(10, 425, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_21.setFont(font)
        self.lbl_date_21.setObjectName("lbl_date_21")
        self.lbl_date_22 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_22.setGeometry(QtCore.QRect(10, 42, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_22.setFont(font)
        self.lbl_date_22.setObjectName("lbl_date_22")
        
        self.cb_accountType = QtWidgets.QComboBox(self.addPurchaseGB)
        self.cb_accountType.setGeometry(QtCore.QRect(90, 42, 150, 25))
        self.cb_accountType.addItem('SELECT')
        self.cb_accountType.addItems(globalList.List._accountTypeList)
        self.cb_accountType.setObjectName("cb_accountType")
        self.cb_accountType.activated[str].connect(self.onAccountTypeChange)
        
        self.btn_quickAccount = QtWidgets.QPushButton(self.addPurchaseGB)
        self.btn_quickAccount.setGeometry(QtCore.QRect(240, 42, 30, 25))
        acIcon = QtGui.QPixmap(globalVariables.Variables._icon+'user.png')
        self.btn_quickAccount.setIcon(QtGui.QIcon(acIcon))
        self.btn_quickAccount.setObjectName("btn_quickAccount")
        self.btn_quickAccount.clicked.connect(self.quickAccount)
        
        self.lbl_date_23 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_23.setGeometry(QtCore.QRect(10, 122, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_23.setFont(font)
        self.lbl_date_23.setObjectName("lbl_date_23")

        self.rb_new = QtWidgets.QRadioButton(self.addPurchaseGB)
        self.rb_new.setGeometry(QtCore.QRect(90, 122, 51, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_new.setFont(font)
        self.rb_new.setObjectName("rb_new")
        self.rb_new.setChecked(True)

        self.rb_used = QtWidgets.QRadioButton(self.addPurchaseGB)
        self.rb_used.setGeometry(QtCore.QRect(150, 122, 51, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_used.setFont(font)
        self.rb_used.setObjectName("rb_used")

        self.lbl_date_24 = QtWidgets.QLabel(self.addPurchaseGB)
        self.lbl_date_24.setGeometry(QtCore.QRect(10, 260, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_24.setFont(font)
        self.lbl_date_24.setObjectName("lbl_date_24")

        self.le_remarks = QtWidgets.QLineEdit(self.addPurchaseGB)
        self.le_remarks.setGeometry(QtCore.QRect(90, 425, 180, 25))
        self.le_remarks.setMaxLength(32)
        self.le_remarks.setObjectName("le_remarks")
        self.le_remarks.returnPressed.connect(self.onEnterRemarks)
        
        self.calendar = QtWidgets.QCalendarWidget(self.addPurchaseGB)
        self.calendar.setGeometry(QtCore.QRect(0, 40, 280, 183))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.calendar.setFont(font)
        self.calendar.setAcceptDrops(False)
        self.calendar.setAutoFillBackground(True)
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setObjectName("calendar")
        self.calendar.hide()
        self.calendar.clicked[QtCore.QDate].connect(self.setDate)
        
        self.purchaseGB = QtWidgets.QGroupBox(self.centralwidget)
        self.purchaseGB.setGeometry(QtCore.QRect(820, 0, 541, 481))
        self.purchaseGB.setObjectName("purchaseGB")
        
        self.tbl_purchase = QtWidgets.QTableWidget(self.purchaseGB)
        self.tbl_purchase.setGeometry(QtCore.QRect(10, 55, 520, 420))
        self.tbl_purchase.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_purchase.setRowCount(11)
        self.tbl_purchase.setColumnCount(13)
        self.tbl_purchase.setHorizontalHeaderLabels(['billId', 'accountId', 'Date', 'Invoice', 'type',
                                                 'Amount', 'Discount', 'Net Bill', 'Payment', 'Balance',
                                                     'remarks', 'Image','Detail'])
        self.tbl_purchase.setColumnHidden(0,True)
        self.tbl_purchase.setColumnHidden(1,True)
        self.tbl_purchase.setColumnHidden(4,True)
        self.tbl_purchase.setColumnHidden(5,True)
        self.tbl_purchase.setColumnHidden(10,True)

        self.tbl_purchase.setColumnWidth(2,70)
        self.tbl_purchase.setColumnWidth(3,70)
        self.tbl_purchase.setColumnWidth(6,65)
        self.tbl_purchase.setColumnWidth(7,70)
        self.tbl_purchase.setColumnWidth(8,70)
        self.tbl_purchase.setColumnWidth(9,50)

        self.tbl_purchase.setColumnWidth(11,37)
        self.tbl_purchase.setColumnWidth(12,37)

        self.tbl_purchase.setObjectName("tbl_purchase")
        
        self.filterGB = QtWidgets.QGroupBox(self.purchaseGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 15, 521, 41))
        self.filterGB.setObjectName("filterGB")
        
        self.le_filterByDate = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDate.setGeometry(QtCore.QRect(0, 15, 100, 20))
        self.le_filterByDate.setMaxLength(32)
        self.le_filterByDate.setObjectName("le_filterByDate")
        self.le_filterByDate.textChanged.connect(self.filter)
        
        self.le_filterByInvoice = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByInvoice.setGeometry(QtCore.QRect(100, 15, 70, 20))
        self.le_filterByInvoice.setValidator(self.onlyInt)
        self.le_filterByInvoice.setMaxLength(10)
        self.le_filterByInvoice.setObjectName("le_filterByInvoice")
        self.le_filterByInvoice.textChanged.connect(self.filter)
        
        self.le_filterByDiscount = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDiscount.setGeometry(QtCore.QRect(170, 15, 65, 20))
        self.le_filterByDiscount.setValidator(self.onlyInt)
        self.le_filterByDiscount.setMaxLength(10)
        self.le_filterByDiscount.setObjectName("le_filterByDiscount")
        self.le_filterByDiscount.textChanged.connect(self.filter)
        
        self.le_filterByNetBill = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByNetBill.setGeometry(QtCore.QRect(235, 15, 70, 20))
        self.le_filterByNetBill.setValidator(self.onlyInt)
        self.le_filterByNetBill.setMaxLength(10)
        self.le_filterByNetBill.setObjectName("le_filterByNetBill")
        self.le_filterByNetBill.textChanged.connect(self.filter)
        
        self.le_filterByPayment = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByPayment.setGeometry(QtCore.QRect(305, 15, 70, 20))
        self.le_filterByPayment.setValidator(self.onlyInt)
        self.le_filterByPayment.setMaxLength(10)
        self.le_filterByPayment.setObjectName("le_filterByPayment")
        self.le_filterByPayment.textChanged.connect(self.filter)
        
        self.le_filterByBalance = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByBalance.setGeometry(QtCore.QRect(375, 15, 45, 20))
        self.le_filterByBalance.setValidator(self.onlyInt)
        self.le_filterByBalance.setMaxLength(10)
        self.le_filterByBalance.setObjectName("le_filterByBalance")
        self.le_filterByBalance.textChanged.connect(self.filter)
        
        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(420, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getPurchase)
        
        self.cartGB = QtWidgets.QGroupBox(self.centralwidget)
        self.cartGB.setGeometry(QtCore.QRect(300, 0, 511, 480))
        self.cartGB.setObjectName("cartGB")
        self.tbl_cart = QtWidgets.QTableWidget(self.cartGB)
        self.tbl_cart.setGeometry(QtCore.QRect(5, 15, 500, 465))
        self.tbl_cart.setTabKeyNavigation(True)
        self.tbl_cart.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_cart.setRowCount(14)
        self.tbl_cart.setColumnCount(14)
        self.tbl_cart.setHorizontalHeaderLabels(['companyId', 'Company','productId','Product','Product Type',
                                                 'Engine','Chessis','Registration','Cost','Sale','Discount',
                                                 'Total','remarks','Remove'])
        self.tbl_cart.setColumnHidden(0,True)
        self.tbl_cart.setColumnHidden(1,True)
        self.tbl_cart.setColumnHidden(2,True)
        self.tbl_cart.setColumnHidden(4,True)
        self.tbl_cart.setColumnHidden(12,True)

        self.tbl_cart.setColumnWidth(3,60)
        self.tbl_cart.setColumnWidth(5,55)
        self.tbl_cart.setColumnWidth(6,55)
        self.tbl_cart.setColumnWidth(7,60)
        self.tbl_cart.setColumnWidth(8,55)
        self.tbl_cart.setColumnWidth(9,50)
        self.tbl_cart.setColumnWidth(10,40)
        self.tbl_cart.setColumnWidth(11,55)
        self.tbl_cart.setColumnWidth(13,40)

        self.tbl_cart.setObjectName("tbl_cart")
        
        self.cartBillGB = QtWidgets.QGroupBox(self.centralwidget)
        self.cartBillGB.setGeometry(QtCore.QRect(10, 480, 1351, 200))
        self.cartBillGB.setObjectName("cartBillGB")
        self.finalBillGB = QtWidgets.QGroupBox(self.cartBillGB)
        self.finalBillGB.setGeometry(QtCore.QRect(300, 10, 491, 190))
        self.finalBillGB.setObjectName("finalBillGB")
        self.le_totalBill = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_totalBill.setEnabled(False)
        self.le_totalBill.setGeometry(QtCore.QRect(10, 35, 150, 25))
        self.le_totalBill.setMaxLength(32)
        self.le_totalBill.setObjectName("le_totalBill")
        self.le_billDiscountPercent = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_billDiscountPercent.setGeometry(QtCore.QRect(10, 80, 150, 25))
        self.le_billDiscountPercent.setText('0')
        self.le_billDiscountPercent.setValidator(self.onlyInt)
        self.le_billDiscountPercent.setMaxLength(32)
        self.le_billDiscountPercent.setObjectName("le_billDiscountPercent")
        self.le_billDiscountPercent.textChanged.connect(self.calculateBillDiscountAmount)

        self.le_billDiscountAmount = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_billDiscountAmount.setGeometry(QtCore.QRect(10, 130, 150, 25))
        self.le_billDiscountAmount.setText('0')
        self.le_billDiscountAmount.setValidator(self.onlyInt)
        self.le_billDiscountAmount.setMaxLength(32)
        self.le_billDiscountAmount.setObjectName("le_billDiscountAmount")
        self.le_billDiscountAmount.textChanged.connect(self.calculateBillDiscountPercentage)

        self.lbl_date_12 = QtWidgets.QLabel(self.finalBillGB)
        self.lbl_date_12.setGeometry(QtCore.QRect(10, 15, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_12.setFont(font)
        self.lbl_date_12.setObjectName("lbl_date_12")
        self.lbl_date_13 = QtWidgets.QLabel(self.finalBillGB)
        self.lbl_date_13.setGeometry(QtCore.QRect(10, 60, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_13.setFont(font)
        self.lbl_date_13.setObjectName("lbl_date_13")
        self.lbl_date_14 = QtWidgets.QLabel(self.finalBillGB)
        self.lbl_date_14.setGeometry(QtCore.QRect(10, 110, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_14.setFont(font)
        self.lbl_date_14.setObjectName("lbl_date_14")
        
        self.le_payment = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_payment.setGeometry(QtCore.QRect(170, 80, 150, 25))
        self.le_payment.setText('0')
        self.le_payment.setValidator(self.onlyInt)
        self.le_payment.setObjectName("le_payment")
        self.le_payment.textChanged.connect(self.onChangePayment)
        self.le_payment.returnPressed.connect(self.onSubmit)
        
        self.le_balance = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_balance.setGeometry(QtCore.QRect(170, 130, 150, 25))
        self.le_balance.setEnabled(False)
        self.le_balance.setObjectName("le_remarks")
        
        self.le_netBill = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_netBill.setEnabled(False)
        self.le_netBill.setGeometry(QtCore.QRect(170, 35, 150, 25))
        self.le_netBill.setMaxLength(32)
        self.le_netBill.setValidator(self.onlyInt)
        self.le_netBill.setObjectName("le_netBill")
        
        self.lbl_date_15 = QtWidgets.QLabel(self.finalBillGB)
        self.lbl_date_15.setGeometry(QtCore.QRect(170, 15, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_15.setFont(font)
        self.lbl_date_15.setObjectName("lbl_date_15")
        self.lbl_date_16 = QtWidgets.QLabel(self.finalBillGB)
        self.lbl_date_16.setGeometry(QtCore.QRect(170, 60, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_16.setFont(font)
        self.lbl_date_16.setObjectName("lbl_date_16")
        self.lbl_date_17 = QtWidgets.QLabel(self.finalBillGB)
        self.lbl_date_17.setGeometry(QtCore.QRect(170, 110, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_17.setFont(font)
        self.lbl_date_17.setObjectName("lbl_date_17")

        self.btn_submit = QtWidgets.QPushButton(self.finalBillGB)
        self.btn_submit.setGeometry(QtCore.QRect(290, 160, 100, 28))
        submitIcon = QtGui.QPixmap(globalVariables.Variables._icon+'rightIcon.png')
        self.btn_submit.setIcon(QtGui.QIcon(submitIcon))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.onSubmit)
        
        self.btn_cancel = QtWidgets.QPushButton(self.finalBillGB)
        self.btn_cancel.setGeometry(QtCore.QRect(390, 160, 100, 28))
        cancelIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cancelIcon.png')
        self.btn_cancel.setIcon(QtGui.QIcon(cancelIcon))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.onCancel)

        self.cb_net = QtWidgets.QCheckBox(self.finalBillGB)
        self.cb_net.setGeometry(QtCore.QRect(385, 40, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cb_net.setFont(font)
        self.cb_net.setObjectName("cb_net")
        self.cb_net.setChecked(True)
        self.cb_net.clicked.connect(self.onCheckNet)

        self.cb_shortTerm = QtWidgets.QCheckBox(self.finalBillGB)
        self.cb_shortTerm.setGeometry(QtCore.QRect(385, 100, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cb_shortTerm.setFont(font)
        self.cb_shortTerm.setObjectName("cb_shortTerm")
        self.cb_shortTerm.clicked.connect(self.onCheckShortTerm)

        self.cb_lease = QtWidgets.QCheckBox(self.finalBillGB)
        self.cb_lease.setGeometry(QtCore.QRect(385, 70, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cb_lease.setFont(font)
        self.cb_lease.setObjectName("cb_lease")
        self.cb_lease.clicked.connect(self.onCheckLease)

        self.lbl_date_20 = QtWidgets.QLabel(self.cartBillGB)
        self.lbl_date_20.setGeometry(QtCore.QRect(10, 20, 51, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_date_20.setFont(font)
        self.lbl_date_20.setObjectName("lbl_date_20")
        self.planGB = QtWidgets.QGroupBox(self.cartBillGB)
        self.planGB.setGeometry(QtCore.QRect(810, 10, 535, 190))
        self.planGB.setObjectName("planGB")


        self.tab_plan = QtWidgets.QTabWidget(self.planGB)
        self.tab_plan.setGeometry(QtCore.QRect(0, 15, 531, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tab_plan.setFont(font)
        self.tab_plan.setObjectName("tab_plan")
        self.lease = QtWidgets.QWidget()
        self.lease.setObjectName("lease")

        self.tbl_lease = QtWidgets.QTableWidget(self.lease)
        self.tbl_lease.setGeometry(QtCore.QRect(5, 0, 515, 140))
        self.tbl_lease.setRowCount(1)
        self.tbl_lease.setColumnCount(5)
        self.tbl_lease.setHorizontalHeaderLabels(['Date', 'Amount','Balance','Add','Remove'])

        self.btn_addLease = QPushButton('')
        self.btn_addLease.setIcon(QtGui.QIcon(addIcon))
        self.tbl_lease.setCellWidget(0, 3, self.btn_addLease)
        self.btn_addLease.clicked.connect(self.onAddLeaseRow)

        self.btn_removeLease = QPushButton('')
        removeIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
        self.btn_removeLease.setIcon(QtGui.QIcon(removeIcon))
        self.tbl_lease.setCellWidget(0, 4, self.btn_removeLease)
        self.btn_removeLease.clicked.connect(self.onRemoveLeaseRow)

        self.tbl_lease.setObjectName("tbl_lease")
        self.tbl_lease.setEnabled(False)
        self.tbl_lease.itemChanged.connect(self.changeTbl)
        self.tbl_lease.cellClicked.connect(self.showPlanCalendar)





        self.tab_plan.addTab(self.lease, "")

        # self.short_term = QtWidgets.QWidget()
        # self.short_term.setObjectName("short_term")
        # self.tbl_shortTerm = QtWidgets.QTableWidget(self.short_term)
        # self.tbl_shortTerm.setGeometry(QtCore.QRect(5, 0, 515, 140))
        # self.tbl_shortTerm.setRowCount(1)
        # self.tbl_shortTerm.setColumnCount(4)
        # self.tbl_shortTerm.setHorizontalHeaderLabels(['Date', 'Amount','Balance','Add'])
        # self.tbl_shortTerm.setObjectName("tbl_shortTerm")
        # self.tab_plan.addTab(self.short_term, "")

        self.planCalendar = QtWidgets.QCalendarWidget(self.planGB)
        self.planCalendar.setGeometry(QtCore.QRect(120, 0, 312, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.planCalendar.setFont(font)
        self.planCalendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.planCalendar.setObjectName("planCalendar")
        self.planCalendar.hide()
        self.planCalendar.clicked[QtCore.QDate].connect(self.setPlanDate)


        self.btn_captureImage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_captureImage.setGeometry(QtCore.QRect(200, 650, 100, 28))
        captureIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cameraIcon.png')
        self.btn_captureImage.setIcon(QtGui.QIcon(captureIcon))
        self.btn_captureImage.setObjectName("btn_captureImage")
        
        self.lbl_image = QtWidgets.QLabel(self.centralwidget)
        self.lbl_image.setGeometry(QtCore.QRect(90, 500, 200, 140))
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'invoice.png'))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")
        
        self.btn_browseImage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browseImage.setGeometry(QtCore.QRect(100, 650, 100, 28))
        browseIcon = QtGui.QPixmap(globalVariables.Variables._icon+'browseIcon.png')
        self.btn_browseImage.setIcon(QtGui.QIcon(browseIcon))
        self.btn_browseImage.setObjectName("btn_browseImage")
        
        purchaseWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(purchaseWindow)
        self.statusbar.setObjectName("statusbar")
        purchaseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(purchaseWindow)
        self.tab_plan.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(purchaseWindow)

    def retranslateUi(self, purchaseWindow):
        _translate = QtCore.QCoreApplication.translate
        purchaseWindow.setWindowTitle(_translate("purchaseWindow", "Purchase Window"))
        self.addPurchaseGB.setTitle(_translate("purchaseWindow", "Add Purchase"))
        self.le_invoice.setPlaceholderText(_translate("purchaseWindow", "Bill Number"))
        self.le_engine.setPlaceholderText(_translate("purchaseWindow", "Engine Number"))
        self.le_chassis.setPlaceholderText(_translate("purchaseWindow", "Chassis Number"))
        self.le_costPrice.setPlaceholderText(_translate("purchaseWindow", "Cost Price"))
        self.le_salePrice.setPlaceholderText(_translate("purchaseWindow", "Sale Price"))
        self.lbl_date_5.setText(_translate("purchaseWindow", "Company"))
        self.lbl_date_9.setText(_translate("purchaseWindow", "Cost Price"))
        self.lbl_date_3.setText(_translate("purchaseWindow", "Account"))
        self.lbl_date_8.setText(_translate("purchaseWindow", "Chassis"))
        self.lbl_date_2.setText(_translate("purchaseWindow", "Date"))
        self.lbl_date_4.setText(_translate("purchaseWindow", "Invoice"))
        self.lbl_date_7.setText(_translate("purchaseWindow", "Engine"))
        self.lbl_date_10.setText(_translate("purchaseWindow", "Sale Price"))
        self.lbl_date_6.setText(_translate("purchaseWindow", "Product"))
        self.le_itemDiscountPercent.setPlaceholderText(_translate("purchaseWindow", "Item Discount Percentage"))
        self.le_itemDiscountAmount.setPlaceholderText(_translate("purchaseWindow", "Item Discount Amount"))
        self.btn_addItem.setText(_translate("purchaseWindow", "Add Item"))
        self.le_totalPrice.setPlaceholderText(_translate("purchaseWindow", "Item Total Price"))
        self.lbl_date_11.setText(_translate("purchaseWindow", "Total Price"))
        self.lbl_date_18.setText(_translate("purchaseWindow", "Discount %"))
        self.lbl_date_19.setText(_translate("purchaseWindow", "Discount Rs."))
        self.lbl_date_21.setText(_translate("purchaseWindow", "Remarks"))
        self.lbl_date_22.setText(_translate("purchaseWindow", "AC Type"))
        self.lbl_date_23.setText(_translate("purchaseWindow", "Type"))
        self.rb_new.setText(_translate("purchaseWindow", "New"))
        self.rb_used.setText(_translate("purchaseWindow", "Used"))
        self.lbl_date_24.setText(_translate("purchaseWindow", "Reg"))
        self.le_registration.setPlaceholderText(_translate("purchaseWindow", "Registration Number"))
        self.le_remarks.setPlaceholderText(_translate("purchaseWindow", "Remarks"))
        self.purchaseGB.setTitle(_translate("purchaseWindow", "All Purchase"))
        self.filterGB.setTitle(_translate("purchaseWindow", "Filter"))
        self.le_filterByDate.setPlaceholderText(_translate("purchaseWindow", "Filter "))
        self.le_filterByInvoice.setPlaceholderText(_translate("purchaseWindow", "Filter "))
        self.le_filterByDiscount.setPlaceholderText(_translate("purchaseWindow", "Filter "))
        self.btn_refresh.setText(_translate("purchaseWindow", "Refresh"))
        self.le_filterByNetBill.setPlaceholderText(_translate("purchaseWindow", "Filter "))
        self.le_filterByPayment.setPlaceholderText(_translate("purchaseWindow", "Filter "))
        self.le_filterByBalance.setPlaceholderText(_translate("purchaseWindow", "Filter "))
        self.cartGB.setTitle(_translate("purchaseWindow", "Purchase Cart"))
        self.tbl_cart.setSortingEnabled(True)
        self.cartBillGB.setTitle(_translate("purchaseWindow", "CART BILL"))
        self.finalBillGB.setTitle(_translate("purchaseWindow", "Calculation"))
        self.le_totalBill.setPlaceholderText(_translate("purchaseWindow", "Bill Before Discount"))
        self.le_billDiscountPercent.setPlaceholderText(_translate("purchaseWindow", "Bill Discount Percentage"))
        self.le_billDiscountAmount.setPlaceholderText(_translate("purchaseWindow", "Bill Discount Amount"))
        self.lbl_date_12.setText(_translate("purchaseWindow", "Total Bill"))
        self.lbl_date_13.setText(_translate("purchaseWindow", "Discount %"))
        self.lbl_date_14.setText(_translate("purchaseWindow", "Discount Rs."))
        self.le_payment.setPlaceholderText(_translate("purchaseWindow", "Paid Amount"))
        self.le_balance.setPlaceholderText(_translate("purchaseWindow", "Remaing Balance"))
        self.le_netBill.setPlaceholderText(_translate("purchaseWindow", "Bill After Discount"))
        self.lbl_date_15.setText(_translate("purchaseWindow", "Net Bill"))
        self.lbl_date_16.setText(_translate("purchaseWindow", "Payment"))
        self.lbl_date_17.setText(_translate("purchaseWindow", "Balance"))
        self.btn_submit.setText(_translate("purchaseWindow", "Save"))
        self.btn_cancel.setText(_translate("purchaseWindow", "Cancel"))
        self.cb_net.setText(_translate("purchaseWindow", "Net"))
        self.cb_shortTerm.setText(_translate("purchaseWindow", "Short Term"))
        self.cb_lease.setText(_translate("purchaseWindow", "Lease"))
        self.lbl_date_20.setText(_translate("purchaseWindow", "Invoice"))
        self.planGB.setTitle(_translate("purchaseWindow", " Plan"))
        self.tab_plan.setTabText(self.tab_plan.indexOf(self.lease), _translate("purchaseWindow", "Plan"))
        # self.tab_plan.setTabText(self.tab_plan.indexOf(self.short_term), _translate("purchaseWindow", "Short Term"))
        self.btn_captureImage.setText(_translate("purchaseWindow", "Capture"))
        self.btn_browseImage.setText(_translate("purchaseWindow", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    purchaseWindow = QtWidgets.QMainWindow()
    ui = Ui_purchaseWindow()
    ui.setupUi(purchaseWindow)
    purchaseWindow.show()
    sys.exit(app.exec_())

