
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

from Globals import globalVariables,globalList
from BLL.SaleBL import saleBL

from Services.ImgService import camera,image,browseImage
from Services.ResetServices import formReset
from Services.RecallServices import formRecall
from Services.MiscService import dateTime

class Ui_saleWindow(object):

    _cartItemList = []
    _policyList = []
    _filterList = []

    _imageCode = ''
    _purchaseId = 0

    _name = ''
    _mobile = ''
    _cnic = ''
    _address = ''

    _engine = None
    _chassis = None
    _registration = None

    _productType = globalVariables.Variables._newProduct

    def init(self):
        self.le_date.setText(self.cal_date.selectedDate().toString())
        self.cb_accountType.setCurrentIndex(1)
        self.onAccountTypeChange(self.cb_accountType.currentText())
        self.setCompany()
        self.setRefAccount()

    def showCalendar(self):
        if (self.cal_date.isHidden()):
            self.cal_date.show()
        else:
            self.cal_date.hide()

    def setDate(self, date):
        self.le_date.setText(date.toString())
        self.cal_date.hide()


    def onAccountTypeChange(self,text):
        if(self.cb_accountType.currentIndex()>0):
            self.setAccounts(text)
            self.cb_account.setFocus()

    def setAccounts(self,accountType):
        self.cb_account.clear()
        self.cb_account.addItem("",0)
        accountList = saleBL.getAccountByType(accountType)
        for id, name, mob in accountList:
            self.cb_account.addItem(mob+"-"+name.upper(),id)

    def onChangeAccount(self):
        self.getSale()
        accountId = self.cb_account.currentData()
        self.setAccountData(accountId)
        self.cb_company.setFocus()

    def setAccountData(self,accountId):
        result = saleBL.getAccountData(accountId)
        for item in result:
            self._name = item[1]
            self._cnic = item[4]
            self._mobile = item[5]
            self._address = item[7]

    def setRefAccount(self):
        self.cb_refAccount.clear()
        self.cb_refAccount.addItem("")
        refAccountList = saleBL.getRefAccount()
        for id, name, fatherName,cnic, mobile, gender, address in refAccountList:
            self.cb_refAccount.addItem(mobile+"-"+name,id)

    def onChangeRefAccount(self):
        self.cb_company.setFocus()



    def setCompany(self):
        self.cb_company.clear()
        self.cb_company.addItem("SELECT")
        companyList = saleBL.getCompany()
        for id, name, code, representative, contact, location in companyList:
            self.cb_company.addItem(name.upper(),id)

    def onChangeCompany(self):
        companyID = self.cb_company.currentData()
        if(self.cb_company.currentIndex()>0):
            self.setProduct(companyID)
            self.cb_product.setFocus()
        else:
            pass


    def setProduct(self,companyID):
        self.cb_product.clear()
        self.cb_product.addItem("SELECT")
        productList = saleBL.getProduct(companyID)
        for productId, companyId, productType, name, code, remarks in productList:
            self.cb_product.addItem(name.upper(),productId)

    def onChangeProduct(self):
        productId = self.cb_product.currentData()
        self.setProductDetail(productId)
        self.cb_productDetail.setFocus()

    def setProductDetail(self,productId):
        self.cb_productDetail.clear()
        self.cb_productDetail.addItem('SELECT')
        result = saleBL.getProductDetail(productId,self._productType)
        for id, engine, chassis, registration in result:
            self.cb_productDetail.addItem(engine+", "+chassis+", "+registration, id)

    def onChangeProductDetail(self):
        try:
            purchaseId = self.cb_productDetail.currentData()
            if(purchaseId!=None):
                result = saleBL.setProductDetail(purchaseId)
                for id, engine, chassis,registration, sp in result:
                    self._engine = engine
                    self._chassis = chassis
                    self._registration = registration
                    self.le_salePrice.setText(str(sp))
            else:
                self.le_salePrice.clear()
                self.le_itemDiscountAmount.setText("0")
                self.le_itemDiscountPercent.setText("0")
                self.le_totalPrice.clear()
                self.le_remarks.clear()
        except:
            pass


    def onChangeSalePrice(self):
        self.le_totalPrice.setText(self.le_salePrice.text())

    def onEnterSalePrice(self):
        self.le_itemDiscountPercent.setFocus()

    def onEnterItemDiscountPercent(self):
        self.le_itemDiscountAmount.setFocus()

    def onEnterItemDiscountAmount(self):
        self.le_remarks.setFocus()

    def onCheckNet(self):
        self.cb_net.setChecked(True)
        self.cb_shortTerm.setChecked(False)
        self.cb_lease.setChecked(False)
        self.tbl_plan.setEnabled(False)

    def onCheckShortTerm(self):
        self.cb_shortTerm.setChecked(True)
        self.cb_net.setChecked(False)
        self.cb_lease.setChecked(False)
        self.tbl_plan.setEnabled(True)

    def onCheckLease(self):
        self.cb_lease.setChecked(True)
        self.cb_shortTerm.setChecked(False)
        self.cb_net.setChecked(False)
        self.tbl_plan.setEnabled(True)



    def onAddItem(self):
        accountId = self.cb_account.currentData()
        refAccountId = self.cb_refAccount.currentData()
        companyId = self.cb_company.currentData()
        companyName = self.cb_company.currentText()
        productId = self.cb_product.currentData()
        productName = self.cb_product.currentText()
        purchaseId = self.cb_productDetail.currentData()
        engine = self._engine
        chassis = self._chassis
        registration = self._registration
        quantity = 1
        salePrice = self.le_salePrice.text()
        discount = self.le_itemDiscountAmount.text()
        totalPrice = self.le_totalPrice.text()
        remarks = self.le_remarks.text()
        formReset.Reset._resetSaleItem = self.clearItem()
        saleBL.validateAddItem(accountId, refAccountId, companyId, companyName, productId, productName, purchaseId,
                               engine, chassis, registration, quantity, salePrice, discount, totalPrice, remarks)
        self.showCartItem()

    def onSubmit(self):
        policyType = ''


        if(self.cb_net.isChecked() == True):
            policyType = globalVariables.Variables._net

        if(self.cb_shortTerm.isChecked() == True):
            policyType = globalVariables.Variables._shortTerm

            tblRows = self.tbl_plan.rowCount()
            for row in range(1, tblRows):
                twi0 = self.tbl_plan.item(row, 0).text()
                twi1 = self.tbl_plan.item(row, 1).text()
                twi2 = self.tbl_plan.item(row, 2).text()
                self._policyList.append(twi0 + ',' + twi1 + ',' + twi2)

        if(self.cb_lease.isChecked() == True):
            policyType = globalVariables.Variables._lease

            tblRows = self.tbl_plan.rowCount()
            for row in range(1, tblRows):
                twi0 = self.tbl_plan.item(row, 0).text()
                twi1 = self.tbl_plan.item(row, 1).text()
                twi2 = self.tbl_plan.item(row, 2).text()
                self._policyList.append(twi0 + ',' + twi1 + ',' + twi2)

        date = self.le_date.text()
        accountId = self.cb_account.currentData()
        accountName = self._name
        accountCnic = self._cnic
        accountMobile = self._mobile
        accountAddress = self._address
        refAccountId = self.cb_refAccount.currentData()
        refAccount = self.cb_refAccount.currentText()
        company = self.cb_company.currentText()
        product = self.cb_product.currentText()
        engine = self._engine
        chassis = self._chassis
        amount = self.le_totalBill.text()
        discount = self.le_billDiscountAmount.text()
        netAmount = self.le_netBill.text()
        payment = self.le_payment.text()
        balance = self.le_balance.text()
        imageCode = self._imageCode
        itemList = self._cartItemList
        policyList = self._policyList

        formReset.Reset._resetSaleForm = self.onCancel
        saleBL.validateSale(self, date, accountId, accountName, accountCnic, accountMobile, accountAddress, refAccountId, refAccount,
                            company, product, engine, chassis, amount, discount, netAmount, payment, balance,
                            imageCode, itemList, policyType, policyList)


    def removeItem(self):
        button = self.tbl_cart.sender()
        index = self.tbl_cart.indexAt(button.pos())
        itemIndex = int(str(index.row()))
        saleBL.removeItemFromCart(itemIndex)
        self.showCartItem()

    def showCartItem(self):
        totalBill = 0

        self.tbl_cart.setRowCount(0)
        for row_number, row_data in enumerate(self._cartItemList):
            self.tbl_cart.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tbl_cart.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                if(colum_number == 13):
                    totalBill += int(float(data))

                self.btn_deleteItem = QPushButton('')
                removeIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
                self.btn_deleteItem.setIcon(QtGui.QIcon(removeIcon))
                self.tbl_cart.setCellWidget(row_number,15, self.btn_deleteItem)
                self.btn_deleteItem.clicked.connect(self.removeItem)

        if(self.tbl_cart.rowCount()<14):
            self.tbl_cart.setRowCount(14)

        self.le_totalBill.setText(str(totalBill))
        self.le_netBill.setText(str(totalBill))
        self.le_balance.setText(str(totalBill))
        self.tbl_plan.setItem(0, 2, QtWidgets.QTableWidgetItem(str(totalBill)))

    def onChangePayment(self):
        payment = self.le_payment.text()
        netBill = self.le_netBill.text()
        if (netBill != '' and payment != ''):
            balance = int(netBill) - int(payment)
            self.le_balance.setText(str(balance))
            self.tbl_plan.setItem(0, 2, QtWidgets.QTableWidgetItem(str(balance)))
        else:
            self.le_balance.setText(netBill)
            self.tbl_plan.setItem(0, 2, QtWidgets.QTableWidgetItem(str(netBill)))



    def getSale(self):
        try:
            accountId = None
            accountId = self.cb_account.currentData()
            if(accountId != None):
                billType = globalVariables.Variables._sale
                result = saleBL.getBill(accountId, billType)
                self.showSale(result)
                self._filterList = saleBL.getBill(accountId, billType).fetchall().copy()
        except:
            pass


    def showSale(self,result):
        self.tbl_sale.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_sale.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                if (colum_number == 2):
                    self.tbl_sale.setItem(row_number, colum_number,
                                              QtWidgets.QTableWidgetItem(str(dateTime.getDateWithoutTime(data))))
                else:
                    self.tbl_sale.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

                self.btn_billImage = QPushButton('')
                imageIcon = QtGui.QPixmap(globalVariables.Variables._icon + 'imageIcon.png')
                self.btn_billImage.setIcon(QtGui.QIcon(imageIcon))
                self.tbl_sale.setCellWidget(row_number, 11, self.btn_billImage)

                self.btn_billDetail = QPushButton('')
                detailIcon = QtGui.QPixmap(globalVariables.Variables._icon + 'viewDetailIcon.png')
                self.btn_billDetail.setIcon(QtGui.QIcon(detailIcon))
                self.tbl_sale.setCellWidget(row_number, 12, self.btn_billDetail)

        if (self.tbl_sale.rowCount() < 19):
            self.tbl_sale.setRowCount(19)

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



    def clearItem(self):
        self.cb_productDetail.setCurrentIndex(0)
        self.le_salePrice.setText('')
        self.le_itemDiscountAmount.setText('0')
        self.le_itemDiscountPercent.setText('0')
        self.le_totalPrice.setText('')
        self.le_remarks.setText('')

    def onCancel(self):
        self.cb_account.setCurrentIndex(0)
        self.cb_company.setCurrentIndex(0)
        self.cb_product.clear()
        self.le_totalBill.setText('')
        self.le_netBill.setText('')
        self.le_billDiscountAmount.setText('0')
        self.le_billDiscountPercent.setText('0')
        self.le_payment.setText('0')
        self.le_balance.setText('0')
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'invoice.png'))

        del self._cartItemList[:]
        self.showCartItem()

        del self._policyList[:]
        self.tbl_plan.setRowCount(1)

        self.tbl_sale.setRowCount(0)
        self.tbl_sale.setRowCount(12)
        self.clearItem()



    def filterFunc(self,item):
        billId = self.le_filterByBillId.text()
        date = self.le_filterByDate.text()
        discount = self.le_filterByDiscount.text()
        netBill = self.le_filterByNetBill.text()
        payment = self.le_filterByPayment.text()
        balance = self.le_filterByBalance.text()

        if (str(item[0]).startswith(billId) and str(item[2]).startswith(date) and
            str(item[6]).startswith(discount) and str(item[7]).startswith(netBill)  and
            str(item[8]).startswith(payment) and str(item[9]).startswith(balance) ):
            return True
        else:
            return False

    def filter(self):
        result = list(filter(self.filterFunc, self._filterList))
        self.showSale(result)


    def calculateItemDiscountAmount(self):
        sp = self.le_salePrice.text()
        dp = self.le_itemDiscountPercent.text()
        da = 0
        try:
            if(dp != '' and sp != ''):
                da = ((int(sp) * int(dp)) / 100)
                amount = (int(sp) - da)
                self.le_itemDiscountAmount.setText(str(da))
                self.le_totalPrice.setText(str(amount))

            else:
                self.le_itemDiscountAmount.setText('')
                self.le_totalPrice.setText(sp)
        except:
            pass

    def calculateItemDiscountPercentage(self):
        sp = self.le_salePrice.text()
        da = self.le_itemDiscountAmount.text()
        dp = 0
        try:
            if(da != '' and sp != ''):
                dp = (int(da) * 100) / int(sp)
                amount = (int(sp) - int(da))
                self.le_itemDiscountPercent.setText(str(dp))
                self.le_totalPrice.setText(str(amount))
            else:
                self.le_itemDiscountPercent.setText('')
                self.le_totalPrice.setText(sp)
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


    def quickAccount(self):
        saleBL.validateOpenQuickAccount(self)

    def quickCompnay(self):
        saleBL.validateOpenQuickCompany(self)

    def quickProduct(self):
        saleBL.validateOpenQuickProduct(self)

    def openRefAccount(self):
        formRecall.Recall._recallRefAccountList = self.setRefAccount
        saleBL.openReferenceAccount(self)

    def onRbNewClicked(self):
        self._productType = globalVariables.Variables._newProduct
        self.clearItem()

    def onRbUsedClicked(self):
        self._productType = globalVariables.Variables._usedProduct
        self.clearItem()

    def onAddPlanRow(self):
        try:
            button = self.tbl_plan.sender()
            index = self.tbl_plan.indexAt(button.pos())
            row = index.row()
            if(int(self.tbl_plan.item(row,2).text()) > 0):
                self.tbl_plan.insertRow(row + 1)

                self.btn_addLease = QPushButton('')
                addIcon = QtGui.QPixmap(globalVariables.Variables._icon+'addIcon.png')
                self.btn_addLease.setIcon(QtGui.QIcon(addIcon))
                self.tbl_plan.setCellWidget(row + 1 , 3, self.btn_addLease)
                self.btn_addLease.clicked.connect(self.onAddPlanRow)

            self.btn_removeLease = QPushButton('')
            removeIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
            self.btn_removeLease.setIcon(QtGui.QIcon(removeIcon))
            self.tbl_plan.setCellWidget(row + 1, 4, self.btn_removeLease)
            self.btn_removeLease.clicked.connect(self.onRemovePlanRow)
        except:
            pass

    def onRemovePlanRow(self):
        button = self.tbl_plan.sender()
        index = self.tbl_plan.indexAt(button.pos())
        itemIndex = int(str(index.row()))
        if(itemIndex != 0 ):
            self.tbl_plan.removeRow(itemIndex)

    def changeTbl(self, item):
        try:
            balance  = 0
            row = item.row()
            col = item.column()

            if(row > 0 and col == 1 ):
                amount = self.tbl_plan.item(row,1).text()
                bal = self.tbl_plan.item(row - 1, 2).text()
                if( int(bal) > 0 ):
                    balance = str(int(bal)-int(amount))
                    self.tbl_plan.setItem(row, 2, QtWidgets.QTableWidgetItem(balance))
                if(amount == 0 ):
                    balance = self.le_payment
                    self.tbl_plan.setItem(row, 2, QtWidgets.QTableWidgetItem(balance))
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
            self.tbl_plan.setItem(self.planCalendarRow, 0, QtWidgets.QTableWidgetItem(date.toString()))
            self.planCalendar.hide()





    def saleSetupUi(self, saleWindow):
        saleWindow.setObjectName("saleWindow")
        saleWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        saleWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        saleWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        saleWindow.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        self.centralwidget = QtWidgets.QWidget(saleWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addSaleGB = QtWidgets.QGroupBox(self.centralwidget)
        self.addSaleGB.setGeometry(QtCore.QRect(10, 0, 281, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSaleGB.sizePolicy().hasHeightForWidth())
        self.addSaleGB.setSizePolicy(sizePolicy)
        self.addSaleGB.setObjectName("addSaleGB")
        self.btn_date = QtWidgets.QPushButton(self.addSaleGB)
        self.btn_date.setGeometry(QtCore.QRect(240, 15, 30, 28))
        dateIcon = QtGui.QPixmap(globalVariables.Variables._icon+'calendarIcon.png')
        self.btn_date.setIcon(QtGui.QIcon(dateIcon))
        self.btn_date.setObjectName("btn_date")
        self.btn_date.clicked.connect(self.showCalendar)

        self.le_date = QtWidgets.QLineEdit(self.addSaleGB)
        self.le_date.setEnabled(False)
        self.le_date.setGeometry(QtCore.QRect(90, 15, 150, 28))
        self.le_date.setObjectName("le_date")
        self.cb_account = QtWidgets.QComboBox(self.addSaleGB)
        self.cb_account.setGeometry(QtCore.QRect(90, 75, 180, 28))
        self.cb_account.setEditable(True)
        self.cb_account.setObjectName("cb_account")
        self.cb_account.activated.connect(self.onChangeAccount)
        
        self.cb_company = QtWidgets.QComboBox(self.addSaleGB)
        self.cb_company.setGeometry(QtCore.QRect(90, 160, 150, 28))
        self.cb_company.setObjectName("cb_company")
        self.cb_company.activated[str].connect(self.onChangeCompany)

        self.le_salePrice = QtWidgets.QLineEdit(self.addSaleGB)
        self.le_salePrice.setGeometry(QtCore.QRect(90, 250, 180, 28))
        self.le_salePrice.setMaxLength(32)
        self.le_salePrice.setObjectName("le_salePrice")
        self.le_salePrice.setValidator(self.onlyInt)
        self.le_salePrice.setObjectName("le_salePrice")
        self.le_salePrice.textChanged.connect(self.onChangeSalePrice)
        self.le_salePrice.returnPressed.connect(self.onEnterSalePrice)

        self.lbl_date_5 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_5.setGeometry(QtCore.QRect(10, 160, 75, 28))
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
        self.lbl_date_3 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_3.setGeometry(QtCore.QRect(10, 75, 75, 28))
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
        self.lbl_date_2 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_2.setGeometry(QtCore.QRect(10, 15, 75, 28))
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
        self.lbl_date_7 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_7.setGeometry(QtCore.QRect(10, 220, 75, 28))
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
        self.lbl_date_10 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_10.setGeometry(QtCore.QRect(10, 250, 75, 28))
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
        self.lbl_date_6 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_6.setGeometry(QtCore.QRect(10, 190, 75, 28))
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

        self.le_itemDiscountPercent = QtWidgets.QLineEdit(self.addSaleGB)
        self.le_itemDiscountPercent.setGeometry(QtCore.QRect(90, 280, 180, 28))
        self.le_itemDiscountPercent.setText('0')
        self.le_itemDiscountPercent.setValidator(self.onlyInt)
        self.le_itemDiscountPercent.setObjectName("le_itemDiscountPercent")
        self.le_itemDiscountPercent.textChanged.connect(self.calculateItemDiscountAmount)
        self.le_itemDiscountPercent.returnPressed.connect(self.onEnterItemDiscountPercent)

        self.le_itemDiscountAmount = QtWidgets.QLineEdit(self.addSaleGB)
        self.le_itemDiscountAmount.setGeometry(QtCore.QRect(90, 310, 180, 28))
        self.le_itemDiscountAmount.setText('0')
        self.le_itemDiscountAmount.setValidator(self.onlyInt)
        self.le_itemDiscountAmount.setObjectName("le_itemDiscountAmount")
        self.le_itemDiscountAmount.textChanged.connect(self.calculateItemDiscountPercentage)
        self.le_itemDiscountAmount.returnPressed.connect(self.onEnterItemDiscountAmount)

        self.btn_addItem = QtWidgets.QPushButton(self.addSaleGB)
        self.btn_addItem.setGeometry(QtCore.QRect(170, 450, 100, 28))
        addIcon = QtGui.QPixmap(globalVariables.Variables._icon+'addIcon.png')
        self.btn_addItem.setIcon(QtGui.QIcon(addIcon))
        self.btn_addItem.setObjectName("btn_addItem")
        self.btn_addItem.clicked.connect(self.onAddItem)

        self.le_totalPrice = QtWidgets.QLineEdit(self.addSaleGB)
        self.le_totalPrice.setEnabled(False)
        self.le_totalPrice.setGeometry(QtCore.QRect(90, 340, 180, 28))
        self.le_totalPrice.setMaxLength(32)
        self.le_totalPrice.setObjectName("le_totalPrice")
        self.lbl_date_11 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_11.setGeometry(QtCore.QRect(10, 340, 75, 28))
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
        self.lbl_date_18 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_18.setGeometry(QtCore.QRect(10, 280, 75, 28))
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
        self.lbl_date_19 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_19.setGeometry(QtCore.QRect(10, 310, 75, 28))
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
        self.cb_product = QtWidgets.QComboBox(self.addSaleGB)
        self.cb_product.setGeometry(QtCore.QRect(90, 190, 150, 28))
        self.cb_product.setObjectName("cb_product")
        self.cb_product.activated.connect(self.onChangeProduct)

        self.lbl_date_21 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_21.setGeometry(QtCore.QRect(10, 370, 75, 28))
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
        self.lbl_date_22 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_22.setGeometry(QtCore.QRect(10, 45, 75, 28))
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
        self.cb_accountType = QtWidgets.QComboBox(self.addSaleGB)
        self.cb_accountType.setGeometry(QtCore.QRect(90, 45, 150, 28))
        self.cb_accountType.addItem('SELECT')
        self.cb_accountType.addItems(globalList.List._accountTypeList)
        self.cb_accountType.setObjectName("cb_accountType")
        self.cb_accountType.activated[str].connect(self.onAccountTypeChange)

        self.btn_quickAccount = QtWidgets.QPushButton(self.addSaleGB)
        self.btn_quickAccount.setGeometry(QtCore.QRect(240, 45, 30, 28))
        acIcon = QtGui.QPixmap(globalVariables.Variables._icon+'user.png')
        self.btn_quickAccount.setIcon(QtGui.QIcon(acIcon))
        self.btn_quickAccount.setObjectName("btn_quickAccount")
        self.btn_quickAccount.clicked.connect(self.quickAccount)

        self.cb_productDetail = QtWidgets.QComboBox(self.addSaleGB)
        self.cb_productDetail.setGeometry(QtCore.QRect(90, 220, 180, 28))
        self.cb_productDetail.setObjectName("cb_productDetail")
        self.cb_productDetail.activated[str].connect(self.onChangeProductDetail)

        self.btn_quickCompany = QtWidgets.QPushButton(self.addSaleGB)
        self.btn_quickCompany.setGeometry(QtCore.QRect(240, 160, 30, 28))
        addIcon = QtGui.QPixmap(globalVariables.Variables._icon+'addIcon.png')
        self.btn_quickCompany.setIcon(QtGui.QIcon(addIcon))
        self.btn_quickCompany.setToolTip("Add Company Quickly")
        self.btn_quickCompany.setObjectName("btn_quickCompany")
        self.btn_quickCompany.clicked.connect(self.quickCompnay)

        self.btn_quickProduct = QtWidgets.QPushButton(self.addSaleGB)
        self.btn_quickProduct.setGeometry(QtCore.QRect(240, 190, 30, 28))
        addIcon = QtGui.QPixmap(globalVariables.Variables._icon+'addIcon.png')
        self.btn_quickProduct.setIcon(QtGui.QIcon(addIcon))
        self.btn_quickProduct.setToolTip("Add Product Quickly")
        self.btn_quickProduct.setObjectName("btn_quickProduct")
        self.btn_quickProduct.clicked.connect(self.quickProduct)

        self.btn_quickRefAccount = QtWidgets.QPushButton(self.addSaleGB)
        self.btn_quickRefAccount.setGeometry(QtCore.QRect(240, 105, 30, 28))
        acIcon = QtGui.QPixmap(globalVariables.Variables._icon+'user.png')
        self.btn_quickRefAccount.setIcon(QtGui.QIcon(acIcon))
        self.btn_quickRefAccount.setObjectName("btn_quickRefAccount")
        self.btn_quickRefAccount.clicked.connect(self.openRefAccount)

        self.lbl_date_23 = QtWidgets.QLabel(self.addSaleGB)
        self.lbl_date_23.setGeometry(QtCore.QRect(10, 105, 75, 28))
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

        self.cb_refAccount = QtWidgets.QComboBox(self.addSaleGB)
        self.cb_refAccount.setGeometry(QtCore.QRect(90, 105, 150, 28))
        self.cb_refAccount.setEditable(True)
        self.cb_refAccount.setObjectName("cb_refAccount")
        self.cb_refAccount.activated[str].connect(self.onChangeRefAccount)

        self.rb_new = QtWidgets.QRadioButton(self.addSaleGB)
        self.rb_new.setGeometry(QtCore.QRect(90, 133, 51, 28))
        self.rb_new.setObjectName("rb_new")
        self.rb_new.setChecked(True)
        self.rb_new.clicked.connect(self.onRbNewClicked)

        self.rb_used = QtWidgets.QRadioButton(self.addSaleGB)
        self.rb_used.setGeometry(QtCore.QRect(140, 133, 51, 28))
        self.rb_used.setObjectName("rb_used")
        self.rb_used.clicked.connect(self.onRbUsedClicked)

        self.le_remarks = QtWidgets.QLineEdit(self.addSaleGB)
        self.le_remarks.setEnabled(True)
        self.le_remarks.setGeometry(QtCore.QRect(90, 370, 180, 28))
        self.le_remarks.setMaxLength(32)
        self.le_remarks.setObjectName("le_remarks")
        self.cal_date = QtWidgets.QCalendarWidget(self.addSaleGB)
        self.cal_date.setGeometry(QtCore.QRect(0, 45, 281, 183))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cal_date.setFont(font)
        self.cal_date.setAcceptDrops(False)
        self.cal_date.setAutoFillBackground(True)
        self.cal_date.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.cal_date.setGridVisible(True)
        self.cal_date.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.cal_date.setObjectName("cal_date")
        self.cal_date.hide()
        self.cal_date.clicked[QtCore.QDate].connect(self.setDate)

        self.cartBillGB = QtWidgets.QGroupBox(self.centralwidget)
        self.cartBillGB.setGeometry(QtCore.QRect(10, 480, 1350, 200))
        self.cartBillGB.setObjectName("cartBillGB")
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

        self.lbl_image = QtWidgets.QLabel(self.cartBillGB)
        self.lbl_image.setGeometry(QtCore.QRect(90, 10, 200, 140))
        self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'invoice.png'))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")

        self.btn_capture = QtWidgets.QPushButton(self.cartBillGB)
        self.btn_capture.setGeometry(QtCore.QRect(190, 160, 100, 28))
        captureIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cameraIcon.png')
        self.btn_capture.setIcon(QtGui.QIcon(captureIcon))
        self.btn_capture.setObjectName("btn_capture")
        self.btn_capture.clicked.connect(self.capture)

        self.btn_browse = QtWidgets.QPushButton(self.cartBillGB)
        self.btn_browse.setGeometry(QtCore.QRect(90, 160, 100, 28))
        browseIcon = QtGui.QPixmap(globalVariables.Variables._icon+'browseIcon.png')
        self.btn_browse.setIcon(QtGui.QIcon(browseIcon))
        self.btn_browse.setObjectName("btn_browse")
        self.btn_browse.clicked.connect(self.browse)

        self.finalBillGB = QtWidgets.QGroupBox(self.cartBillGB)
        self.finalBillGB.setGeometry(QtCore.QRect(310, 10, 491, 190))
        self.finalBillGB.setObjectName("finalBillGB")
        self.le_totalBill = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_totalBill.setEnabled(False)
        self.le_totalBill.setGeometry(QtCore.QRect(10, 35, 150, 25))
        self.le_totalBill.setMaxLength(32)
        self.le_totalBill.setObjectName("le_totalBill")

        self.le_billDiscountPercent = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_billDiscountPercent.setGeometry(QtCore.QRect(10, 80, 150, 25))
        self.le_billDiscountPercent.setMaxLength(32)
        self.le_billDiscountPercent.setText('0')
        self.le_billDiscountPercent.setValidator(self.onlyInt)
        self.le_billDiscountPercent.setObjectName("le_billDiscountPercent")
        self.le_billDiscountPercent.textChanged.connect(self.calculateBillDiscountAmount)

        self.le_billDiscountAmount = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_billDiscountAmount.setGeometry(QtCore.QRect(10, 130, 150, 25))
        self.le_billDiscountAmount.setMaxLength(32)
        self.le_billDiscountAmount.setText('0')
        self.le_billDiscountAmount.setValidator(self.onlyInt)
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
        self.le_balance.setEnabled(False)
        self.le_balance.setGeometry(QtCore.QRect(170, 130, 150, 25))
        self.le_balance.setObjectName("le_balance")
        self.le_netBill = QtWidgets.QLineEdit(self.finalBillGB)
        self.le_netBill.setEnabled(False)
        self.le_netBill.setGeometry(QtCore.QRect(170, 35, 150, 25))
        self.le_netBill.setMaxLength(32)
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
        self.plan = QtWidgets.QWidget()
        self.plan.setObjectName("plan")
        self.tbl_plan = QtWidgets.QTableWidget(self.plan)
        self.tbl_plan.setGeometry(QtCore.QRect(5, 0, 515, 140))
        self.tbl_plan.setRowCount(1)
        self.tbl_plan.setColumnCount(5)
        self.tbl_plan.setHorizontalHeaderLabels(['Date', 'Amount','Balance','Add','Remove'])

        self.btn_addLease = QPushButton('')
        self.btn_addLease.setIcon(QtGui.QIcon(addIcon))
        self.tbl_plan.setCellWidget(0, 3, self.btn_addLease)
        self.btn_addLease.clicked.connect(self.onAddPlanRow)

        self.btn_removeLease = QPushButton('')
        removeIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
        self.btn_removeLease.setIcon(QtGui.QIcon(removeIcon))
        self.tbl_plan.setCellWidget(0, 4, self.btn_removeLease)
        self.btn_removeLease.clicked.connect(self.onRemovePlanRow)

        self.tbl_plan.setEnabled(False)
        self.tbl_plan.itemChanged.connect(self.changeTbl)
        self.tbl_plan.cellClicked.connect(self.showPlanCalendar)

        self.tbl_plan.setObjectName("tbl_plan")

        self.tab_plan.addTab(self.plan, "")
        self.planCalendar = QtWidgets.QCalendarWidget(self.planGB)
        self.planCalendar.setGeometry(QtCore.QRect(60, 10, 312, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.planCalendar.setFont(font)
        self.planCalendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.planCalendar.setObjectName("planCalendar")
        self.planCalendar.hide()
        self.planCalendar.clicked[QtCore.QDate].connect(self.setPlanDate)

        self.cartGB = QtWidgets.QGroupBox(self.centralwidget)
        self.cartGB.setGeometry(QtCore.QRect(300, 0, 511, 480))
        self.cartGB.setObjectName("cartGB")
        self.tbl_cart = QtWidgets.QTableWidget(self.cartGB)
        self.tbl_cart.setGeometry(QtCore.QRect(5, 15, 500, 461))
        self.tbl_cart.setTabKeyNavigation(True)
        self.tbl_cart.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_cart.setRowCount(13)
        self.tbl_cart.setColumnCount(16)
        self.tbl_cart.setHorizontalHeaderLabels(['accountId','refAccountId','companyId','Company','productId','Product','purchaseId',
                                                 'Engine','Chassis','Reg','quantity','salePrice','Discount','Total',
                                                 'remarks','Remove'])
        self.tbl_cart.setColumnHidden(0,True)
        self.tbl_cart.setColumnHidden(1,True)
        self.tbl_cart.setColumnHidden(2,True)
        self.tbl_cart.setColumnHidden(4,True)
        self.tbl_cart.setColumnHidden(6,True)
        self.tbl_cart.setColumnHidden(10,True)
        self.tbl_cart.setColumnHidden(12,True)
        self.tbl_cart.setColumnHidden(14,True)

        self.tbl_cart.setColumnWidth(3,70)
        self.tbl_cart.setColumnWidth(5,65)
        self.tbl_cart.setColumnWidth(7,60)
        self.tbl_cart.setColumnWidth(8,60)
        self.tbl_cart.setColumnWidth(9,60)
        self.tbl_cart.setColumnWidth(11,50)
        self.tbl_cart.setColumnWidth(12,50)
        self.tbl_cart.setColumnWidth(13,50)
        self.tbl_cart.setColumnWidth(15,50)
        self.tbl_cart.setObjectName("tbl_cart")
        self.saleGB = QtWidgets.QGroupBox(self.centralwidget)
        self.saleGB.setGeometry(QtCore.QRect(820, 0, 541, 480))
        self.saleGB.setObjectName("saleGB")
        self.tbl_sale = QtWidgets.QTableWidget(self.saleGB)
        self.tbl_sale.setGeometry(QtCore.QRect(10, 60, 521, 415))
        self.tbl_sale.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_sale.setRowCount(12)
        self.tbl_sale.setColumnCount(13)
        self.tbl_sale.setHorizontalHeaderLabels(['Bill No', 'accountId', 'Date', 'Invoice', 'type',
                                                 'Amount', 'Discount', 'Net Bill', 'Payment', 'Balance', 'remarks', 'Image','Detail'])
        self.tbl_sale.setColumnHidden(1,True)
        self.tbl_sale.setColumnHidden(3,True)
        self.tbl_sale.setColumnHidden(4,True)
        self.tbl_sale.setColumnHidden(5,True)
        self.tbl_sale.setColumnHidden(10,True)

        self.tbl_sale.setColumnWidth(0,70)
        self.tbl_sale.setColumnWidth(2,70)
        self.tbl_sale.setColumnWidth(6,65)
        self.tbl_sale.setColumnWidth(7,70)
        self.tbl_sale.setColumnWidth(8,70)
        self.tbl_sale.setColumnWidth(9,70)
        self.tbl_sale.setColumnWidth(11,37)
        self.tbl_sale.setColumnWidth(12,37)

        self.tbl_sale.setObjectName("tbl_sale")

        self.filterGB = QtWidgets.QGroupBox(self.saleGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 15, 521, 41))
        self.filterGB.setObjectName("filterGB")

        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(420, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getSale)

        self.le_filterByBillId = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByBillId.setGeometry(QtCore.QRect(0, 15, 100, 20))
        self.le_filterByBillId.setMaxLength(32)
        self.le_filterByBillId.setObjectName("le_filterByBillId")
        self.le_filterByDate = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDate.setGeometry(QtCore.QRect(100, 15, 70, 20))
        self.le_filterByDate.setMaxLength(32)
        self.le_filterByDate.setObjectName("le_filterByDate")
        self.le_filterByDiscount = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByDiscount.setGeometry(QtCore.QRect(170, 15, 65, 20))
        self.le_filterByDiscount.setMaxLength(32)
        self.le_filterByDiscount.setObjectName("le_filterByDiscount")
        self.le_filterByNetBill = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByNetBill.setGeometry(QtCore.QRect(235, 15, 70, 20))
        self.le_filterByNetBill.setMaxLength(32)
        self.le_filterByNetBill.setObjectName("le_filterByNetBill")
        self.le_filterByPayment = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByPayment.setGeometry(QtCore.QRect(305, 15, 70, 20))
        self.le_filterByPayment.setMaxLength(32)
        self.le_filterByPayment.setObjectName("le_filterByPayment")
        self.le_filterByBalance = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByBalance.setGeometry(QtCore.QRect(375, 15, 45, 20))
        self.le_filterByBalance.setMaxLength(32)
        self.le_filterByBalance.setObjectName("le_filterByBalance")
        saleWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(saleWindow)
        self.statusbar.setObjectName("statusbar")
        saleWindow.setStatusBar(self.statusbar)

        self.retranslateUi(saleWindow)
        self.tab_plan.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(saleWindow)

    def retranslateUi(self, saleWindow):
        _translate = QtCore.QCoreApplication.translate
        saleWindow.setWindowTitle(_translate("saleWindow", "Sale Window"))
        self.addSaleGB.setTitle(_translate("saleWindow", "Add Sale"))
        self.le_salePrice.setPlaceholderText(_translate("saleWindow", "Sale Price"))
        self.lbl_date_5.setText(_translate("saleWindow", "Company"))
        self.lbl_date_3.setText(_translate("saleWindow", "Account"))
        self.lbl_date_2.setText(_translate("saleWindow", "Date"))
        self.lbl_date_7.setText(_translate("saleWindow", "Detail"))
        self.lbl_date_10.setText(_translate("saleWindow", "Sale Price"))
        self.lbl_date_6.setText(_translate("saleWindow", "Product"))
        self.le_itemDiscountPercent.setPlaceholderText(_translate("saleWindow", "Item Discount Percentage"))
        self.le_itemDiscountAmount.setPlaceholderText(_translate("saleWindow", "Item Discount Amount"))
        self.btn_addItem.setText(_translate("saleWindow", "Add Item"))
        self.le_totalPrice.setPlaceholderText(_translate("saleWindow", "Item Total Price"))
        self.lbl_date_11.setText(_translate("saleWindow", "Total Price"))
        self.lbl_date_18.setText(_translate("saleWindow", "Discount %"))
        self.lbl_date_19.setText(_translate("saleWindow", "Discount Rs."))
        self.lbl_date_21.setText(_translate("saleWindow", "Remarks"))
        self.lbl_date_22.setText(_translate("saleWindow", "AC Type"))
        self.lbl_date_23.setText(_translate("saleWindow", "Ref - AC"))
        self.rb_new.setText(_translate("saleWindow", "NEW"))
        self.rb_used.setText(_translate("saleWindow", "USED"))
        self.le_remarks.setPlaceholderText(_translate("saleWindow", "Remarks"))
        self.cartBillGB.setTitle(_translate("saleWindow", "CART BILL"))
        self.lbl_date_20.setText(_translate("saleWindow", "Image"))
        self.btn_capture.setText(_translate("saleWindow", "Capture"))
        self.btn_browse.setText(_translate("saleWindow", "Browse"))
        self.finalBillGB.setTitle(_translate("saleWindow", "Calculation"))
        self.le_totalBill.setPlaceholderText(_translate("saleWindow", "Bill Before Discount"))
        self.le_billDiscountPercent.setPlaceholderText(_translate("saleWindow", "Bill Discount Percentage"))
        self.le_billDiscountAmount.setPlaceholderText(_translate("saleWindow", "Bill Discount Amount"))
        self.lbl_date_12.setText(_translate("saleWindow", "Total Bill"))
        self.lbl_date_13.setText(_translate("saleWindow", "Discount %"))
        self.lbl_date_14.setText(_translate("saleWindow", "Discount Rs."))
        self.le_payment.setPlaceholderText(_translate("saleWindow", "Paid Amount"))
        self.le_balance.setPlaceholderText(_translate("saleWindow", "Remaing Balance"))
        self.le_netBill.setPlaceholderText(_translate("saleWindow", "Bill After Discount"))
        self.lbl_date_15.setText(_translate("saleWindow", "Net Bill"))
        self.lbl_date_16.setText(_translate("saleWindow", "Payment"))
        self.lbl_date_17.setText(_translate("saleWindow", "Balance"))
        self.btn_submit.setText(_translate("saleWindow", "Save"))
        self.btn_cancel.setText(_translate("saleWindow", "Cancel"))
        self.cb_net.setText(_translate("saleWindow", "Net"))
        self.cb_shortTerm.setText(_translate("saleWindow", "Short Term"))
        self.cb_lease.setText(_translate("saleWindow", "Lease"))
        self.planGB.setTitle(_translate("saleWindow", " Plan"))
        self.tab_plan.setTabText(self.tab_plan.indexOf(self.plan), _translate("saleWindow", "Plan"))
        self.cartGB.setTitle(_translate("saleWindow", "Sale Cart"))
        self.tbl_cart.setSortingEnabled(True)
        self.saleGB.setTitle(_translate("saleWindow", "All Sale"))
        self.filterGB.setTitle(_translate("saleWindow", "Filter"))
        self.btn_refresh.setText(_translate("saleWindow", "Refresh"))
        self.le_filterByBillId.setPlaceholderText(_translate("saleWindow", "Filter "))
        self.le_filterByDate.setPlaceholderText(_translate("saleWindow", "Filter "))
        self.le_filterByDiscount.setPlaceholderText(_translate("saleWindow", "Filter "))
        self.le_filterByNetBill.setPlaceholderText(_translate("saleWindow", "Filter "))
        self.le_filterByPayment.setPlaceholderText(_translate("saleWindow", "Filter "))
        self.le_filterByBalance.setPlaceholderText(_translate("saleWindow", "Filter "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saleWindow = QtWidgets.QMainWindow()
    ui = Ui_saleWindow()
    ui.saleSetupUi(saleWindow)
    saleWindow.show()
    sys.exit(app.exec_())

