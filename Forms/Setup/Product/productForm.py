
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

from Globals import globalList,globalVariables

from Services.ImgService import image,browseImage,camera
from Services.ResetServices import formReset
from Services.RecallServices import formRecall

from BLL.SetupBL import productBL


class Ui_productWindow(object):
    _companyId = 0
    _imageCode = ''
    _productList = None


    def init(self):
        self.setCompany()
        self.getProduct()

    def setCompany(self):
        self.cb_company.clear()
        self.cb_company.addItem("SELECT")
        companyList = productBL.getCompany()
        for id, name, code, representative, contact, location in companyList:
            self.cb_company.addItem(name,id)

    def onChangeCompany(self):
        if(self.cb_company.currentIndex()>0):
            self._companyId = self.cb_company.currentData()
        self.cb_type.setFocus()

    def onChangeProductType(self):
        self.le_name.setFocus()

    def onEnterProduct(self):
        self.le_code.setFocus()

    def onEnterCode(self):
        self.te_remarks.setFocus()

    def capture(self):
        try:
            base64Img = camera.capture()
            self._imageCode = base64Img
            self.lbl_productImage.setPixmap(image.getPixmap(base64Img))
        except:
            pass

    def browse(self):
        try:
            base64Img = browseImage.getImagePath(self.__init__())
            self._imageCode = base64Img
            self.lbl_productImage.setPixmap(image.getPixmap(base64Img))
        except:
            pass

    def onSubmit(self):
        companyId = self.cb_company.currentData()
        companyName = self.cb_company.currentText()
        productType = self.cb_type.currentText()
        name = self.le_name.text()
        code = self.le_code.text()
        remarks = self.te_remarks.toPlainText()
        imageCode = self._imageCode
        productList = self._productList


        formReset.Reset._resetProductForm = self.onClear
        productBL.validateProduct(self, companyId,companyName,productType,name,code,remarks, imageCode, productList)


    def onClear(self):
        self.le_name.setText('')
        self.le_code.setText('')
        self.te_remarks.setText('')
        self.getProduct()

    def onCancel(self):
        self.cb_company.setCurrentIndex(0)
        self.cb_type.setCurrentIndex(0)
        self.onClear()


    def showProductImage(self):
        button = self.tbl_product.sender()
        index = self.tbl_product.indexAt(button.pos())
        if index.isValid():
            productID = self.tbl_product.model().index(index.row(), 0).data()
            #productBL.validateProductImage(self,productID)

    def editProduct(self):
        formRecall.Recall._recallProductForm = self.getProduct()
        button = self.tbl_product.sender()
        index = self.tbl_product.indexAt(button.pos())
        if index.isValid():
            productId = self.tbl_product.model().index(index.row(), 0).data()
            productBL.updateProduct(self,productId)

    def removeProduct(self):
        button = self.tbl_product.sender()
        index = self.tbl_product.indexAt(button.pos())
        if index.isValid():
            productID = self.tbl_product.model().index(index.row(), 0).data()
            name = self.tbl_product.model().index(index.row(), 3).data()
            formRecall.Recall._recallProductForm = self.getProduct()
            productBL.deleteProduct(productID, name)


    def getProduct(self):
        result = productBL.getProducts()
        self.showProducts(result)

        self._productList = productBL.getProducts().fetchall().copy()

    def showProducts(self,result):

        self.tbl_product.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tbl_product.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tbl_product.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data).upper()))

                self.btn_image = QPushButton('Image')
                imageIcon = QtGui.QPixmap(globalVariables.Variables._icon+'imageIcon.png')
                self.btn_image.setIcon(QtGui.QIcon(imageIcon))
                self.tbl_product.setCellWidget(row_number,6, self.btn_image)
                self.btn_image.clicked.connect(self.showProductImage)

                self.btn_edit = QPushButton('Edit')
                settingIcon = QtGui.QPixmap(globalVariables.Variables._icon+'settingIcon.png')
                self.btn_edit.setIcon(QtGui.QIcon(settingIcon))
                self.tbl_product.setCellWidget(row_number,7, self.btn_edit)
                self.btn_edit.clicked.connect(self.editProduct)

                self.btn_remove = QPushButton('Delete')
                removeIcon = QtGui.QPixmap(globalVariables.Variables._icon+'deleteIcon.jpg')
                self.btn_remove.setIcon(QtGui.QIcon(removeIcon))
                self.tbl_product.setCellWidget(row_number,8, self.btn_remove)
                self.btn_remove.clicked.connect(self.removeProduct)


    def filterFunc(self,item):
        company = self.le_filterByCompanyName.text()
        productType = self.le_filterByCompanyType.text()
        product = self.le_filterByProductName.text()
        code = self.le_filterByProductCode.text()
        remarks = self.le_filterByProductRemarks.text()

        if (str(item[1].lower()).startswith(company) and str(item[2].lower()).startswith(productType) and
            str(item[3].lower()).startswith(product) and str(item[4].lower()).startswith(code)  and
            str(item[5].lower()).startswith(remarks)  ):
            return True
        else:
            return False

    def filterProduct(self):
        result = list(filter(self.filterFunc, self._productList))
        self.showProducts(result)




    def productSetupUi(self, productWindow):
        productWindow.setObjectName("productWindow")
        productWindow.resize(1365, 700)

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        productWindow.setWindowIcon(QtGui.QIcon(windowIcon))

        productWindow.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        productWindow.setAutoFillBackground(True)

        intRegex=QtCore.QRegExp("[0-9_]+")
        self.onlyInt = QtGui.QRegExpValidator(intRegex)

        charRegex=QtCore.QRegExp("[a-z-A-Z _]+")
        self.onlyChar = QtGui.QRegExpValidator(charRegex)

        self.centralwidget = QtWidgets.QWidget(productWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addProductGB = QtWidgets.QGroupBox(self.centralwidget)
        self.addProductGB.setGeometry(QtCore.QRect(10, 0, 291, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addProductGB.sizePolicy().hasHeightForWidth())
        self.addProductGB.setSizePolicy(sizePolicy)
        self.addProductGB.setObjectName("addProductGB")

        self.cb_company = QtWidgets.QComboBox(self.addProductGB)
        self.cb_company.setGeometry(QtCore.QRect(80, 30, 200, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_company.setFont(font)
        self.cb_company.setObjectName("cb_company")

        self.label_10 = QtWidgets.QLabel(self.addProductGB)
        self.label_10.setGeometry(QtCore.QRect(10, 30, 63, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.cb_type = QtWidgets.QComboBox(self.addProductGB)
        self.cb_type.setGeometry(QtCore.QRect(80, 70, 200, 28))
        self.cb_type.addItems(globalList.List._productTypeList)
        self.cb_type.setObjectName("cb_type")
        self.cb_type.activated.connect(self.onChangeProductType)

        self.le_name = QtWidgets.QLineEdit(self.addProductGB)
        self.le_name.setEnabled(True)
        self.le_name.setGeometry(QtCore.QRect(80, 110, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_name.setFont(font)
        self.le_name.setPlaceholderText("Enter Product Name")
        self.le_name.setMaxLength(100)
        self.le_name.setObjectName("le_name")
        self.le_name.returnPressed.connect(self.onEnterProduct)

        self.label_6 = QtWidgets.QLabel(self.addProductGB)
        self.label_6.setGeometry(QtCore.QRect(10, 145, 63, 28))
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
        self.label_5 = QtWidgets.QLabel(self.addProductGB)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 63, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.le_code = QtWidgets.QLineEdit(self.addProductGB)
        self.le_code.setEnabled(True)
        self.le_code.setGeometry(QtCore.QRect(80, 145, 200, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_code.sizePolicy().hasHeightForWidth())
        self.le_code.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_code.setFont(font)
        self.le_code.setPlaceholderText("Enter Product Code")
        self.le_code.setMaxLength(32)
        self.le_code.setValidator(self.onlyInt)
        self.le_code.setObjectName("le_code")
        self.le_code.returnPressed.connect(self.onEnterCode)

        self.label_7 = QtWidgets.QLabel(self.addProductGB)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 63, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.addProductGB)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 63, 28))
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
        self.label_9 = QtWidgets.QLabel(self.addProductGB)
        self.label_9.setGeometry(QtCore.QRect(10, 260, 63, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lbl_productImage = QtWidgets.QLabel(self.addProductGB)
        self.lbl_productImage.setGeometry(QtCore.QRect(80, 270, 200, 200))
        self.lbl_productImage.setText("")
        self.lbl_productImage.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon + 'product.png'))
        self.lbl_productImage.setScaledContents(True)
        self.lbl_productImage.setObjectName("lbl_productImage")

        self.btn_capture = QtWidgets.QPushButton(self.addProductGB)
        self.btn_capture.setGeometry(QtCore.QRect(180, 480, 100, 28))
        captureIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cameraIcon.png')
        self.btn_capture.setIcon(QtGui.QIcon(captureIcon))
        self.btn_capture.setObjectName("btn_capture")
        # self.btn_capture.clicked.connect(self.capture)

        self.btn_submit = QtWidgets.QPushButton(self.addProductGB)
        self.btn_submit.setGeometry(QtCore.QRect(80, 640, 100, 28))
        submitIcon = QtGui.QPixmap(globalVariables.Variables._icon+'rightIcon.png')
        self.btn_submit.setIcon(QtGui.QIcon(submitIcon))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.onSubmit)

        self.btn_cancel = QtWidgets.QPushButton(self.addProductGB)
        self.btn_cancel.setGeometry(QtCore.QRect(180, 640, 100, 28))
        cancelIcon = QtGui.QPixmap(globalVariables.Variables._icon+'cancelIcon.png')
        self.btn_cancel.setIcon(QtGui.QIcon(cancelIcon))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.onCancel)

        self.btn_browse = QtWidgets.QPushButton(self.addProductGB)
        self.btn_browse.setGeometry(QtCore.QRect(80, 480, 100, 28))
        browseIcon = QtGui.QPixmap(globalVariables.Variables._icon+'browseIcon.png')
        self.btn_browse.setIcon(QtGui.QIcon(browseIcon))
        self.btn_browse.setObjectName("btn_browse")
        # self.btn_browse.clicked.connect(self.browse)

        self.te_remarks = QtWidgets.QTextEdit(self.addProductGB)
        self.te_remarks.setGeometry(QtCore.QRect(80, 180, 200, 70))
        self.te_remarks.setPlaceholderText("Enter Remarks")
        self.te_remarks.setObjectName("te_remarks")

        self.productGB = QtWidgets.QGroupBox(self.centralwidget)
        self.productGB.setGeometry(QtCore.QRect(310, 0, 1051, 681))
        self.productGB.setObjectName("productGB")
        self.tbl_product = QtWidgets.QTableWidget(self.productGB)
        self.tbl_product.setGeometry(QtCore.QRect(10, 60, 1031, 611))
        self.tbl_product.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_product.setRowCount(19)
        self.tbl_product.setColumnCount(9)
        self.tbl_product.setHorizontalHeaderLabels(['ID', 'Company', 'Product Type', 'Product',
                                                    'Code', 'Remarks', 'Image', 'Setting', 'Remove'])
        self.tbl_product.setColumnHidden(0, True)
        self.tbl_product.setColumnWidth(1, 140)
        self.tbl_product.setColumnWidth(3, 150)
        self.tbl_product.setColumnWidth(5, 200)
        self.tbl_product.setObjectName("tbl_product")

        self.filterGB = QtWidgets.QGroupBox(self.productGB)
        self.filterGB.setGeometry(QtCore.QRect(10, 15, 1021, 41))
        self.filterGB.setObjectName("filterGB")

        self.le_filterByCompanyName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompanyName.setGeometry(QtCore.QRect(0, 20, 160, 20))
        self.le_filterByCompanyName.setValidator(self.onlyChar)
        self.le_filterByCompanyName.setPlaceholderText("Filter By Company")
        self.le_filterByCompanyName.setObjectName("le_filterByCompanyName")
        self.le_filterByCompanyName.textChanged.connect(self.filterProduct)

        self.le_filterByCompanyType = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByCompanyType.setGeometry(QtCore.QRect(160, 20, 100, 20))
        self.le_filterByCompanyType.setValidator(self.onlyChar)
        self.le_filterByCompanyType.setPlaceholderText("Filter By Type")
        self.le_filterByCompanyType.setObjectName("le_filterByCompanyType")
        self.le_filterByCompanyType.textChanged.connect(self.filterProduct)

        self.le_filterByProductName = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByProductName.setGeometry(QtCore.QRect(260, 20, 150, 20))
        self.le_filterByProductName.setPlaceholderText("Filter By Product")
        self.le_filterByProductName.setObjectName("le_filterByProductName")
        self.le_filterByProductName.textChanged.connect(self.filterProduct)

        self.le_filterByProductCode = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByProductCode.setGeometry(QtCore.QRect(410, 20, 100, 20))
        self.le_filterByProductCode.setValidator(self.onlyInt)
        self.le_filterByProductCode.setPlaceholderText("Filter By Code")
        self.le_filterByProductCode.setObjectName("le_filterByProductCode")
        self.le_filterByProductCode.textChanged.connect(self.filterProduct)

        self.le_filterByProductRemarks = QtWidgets.QLineEdit(self.filterGB)
        self.le_filterByProductRemarks.setGeometry(QtCore.QRect(510, 20, 100, 20))
        self.le_filterByProductRemarks.setPlaceholderText("Filter By Remarks")
        self.le_filterByProductRemarks.setObjectName("le_filterByProductRemarks")
        self.le_filterByProductRemarks.textChanged.connect(self.filterProduct)

        self.btn_refresh = QtWidgets.QPushButton(self.filterGB)
        self.btn_refresh.setGeometry(QtCore.QRect(920, 10, 100, 28))
        refreshIcon = QtGui.QPixmap(globalVariables.Variables._icon+'refreshIcon.png')
        self.btn_refresh.setIcon(QtGui.QIcon(refreshIcon))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.getProduct)

        productWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(productWindow)
        self.statusbar.setObjectName("statusbar")
        productWindow.setStatusBar(self.statusbar)

        self.retranslateUi(productWindow)
        QtCore.QMetaObject.connectSlotsByName(productWindow)

    def retranslateUi(self, productWindow):
        _translate = QtCore.QCoreApplication.translate
        productWindow.setWindowTitle(_translate("productWindow", "Product Window"))
        self.addProductGB.setTitle(_translate("productWindow", "Add New Product"))
        self.label_10.setText(_translate("productWindow", "Comapny"))
        self.label_6.setText(_translate("productWindow", "Code"))
        self.label_5.setText(_translate("productWindow", "Product"))
        self.label_7.setText(_translate("productWindow", "Remarks"))
        self.label_11.setText(_translate("productWindow", "Type"))
        self.label_9.setText(_translate("productWindow", "Image"))
        self.btn_capture.setText(_translate("productWindow", "Capture"))
        self.btn_submit.setText(_translate("productWindow", "Submit"))
        self.btn_cancel.setText(_translate("productWindow", "Cancel"))
        self.btn_browse.setText(_translate("productWindow", "Browse"))
        self.productGB.setTitle(_translate("productWindow", "All Products"))
        self.filterGB.setTitle(_translate("productWindow", "Filter Product"))
        self.btn_refresh.setText(_translate("productWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    productWindow = QtWidgets.QMainWindow()
    ui = Ui_productWindow()
    ui.productSetupUi(productWindow)
    productWindow.show()
    sys.exit(app.exec_())

