from Forms.Setup.Product.productForm import *
from Forms.Setup.Product.productConfirmForm import *
from Forms.Setup.Product.productUpdateForm import *

from DLL.SetupDL import companyDL,productDL

from Services.NotificationService import notification
from Services.ResetServices import formReset
from Services.RecallServices import formRecall

################################## open Forms from main Form ####################################################
def openProductForm(self):
	self.productWindow = QtWidgets.QMainWindow()
	self.ui = Ui_productWindow()
	self.ui.productSetupUi(self.productWindow)
	self.ui.init()
	self.productWindow.showMaximized()

################################## End Forms from main Form #####################################################
def getCompany():
    result = companyDL.getCompanyFromDB()
    return result

def validateProduct(self, companyId,companyName,productType,name,code,remarks,imageCode, productList):
    if(companyId == ''):
        notification.showInformative("Please Select Company","Missing")
        return
    elif(name == ''):
        notification.showInformative("Please Add Product","Missing")
        return
    for x in productList:
        if(code == x[4]):
            notification.showInformative('This Product With Same Code Already saved  ', 'Code Duplicate')
            return
        else:
            pass

    self.confirmProduct = QtWidgets.QDialog()
    self.ui = Ui_confirmProduct()
    self.ui.confirmProductSetupUi(self.confirmProduct)
    self.ui.setConfirmFiels(companyId,companyName,productType,name,code,remarks,imageCode)
    self.confirmProduct.show()

def confirmProduct(companyId,productType,name,code,remarks,imageCode):
    id = 'NULL'
    createdBy = globalVariables.Variables._userId

    productDL.insertProduct(id, companyId,productType,name,code,remarks,'NULL',createdBy)
    formReset.Reset._resetProductForm()


def getProducts():
    result = productDL.getProductFromDB()
    return result

def deleteProduct(productId, productName):
    confirm = notification.confirmPopup('Do You want to Delete '+str(productName)+' Parmanently ', 'Deleting Poduct')
    if(confirm == 'OK'):
        productDL.updateProduct(productId,'','','','','','',1)
        formRecall.Recall._recallProductForm
        return
    else:
        return

def updateProduct(self,productId):
    companyList =  companyDL.getCompanyFromDB()
    result = productDL.getProductByProductID(productId)
    if (result != ''):
        self.updateProduct = QtWidgets.QDialog()
        self.ui = Ui_updateProduct()
        self.ui.updateSetupUi(self.updateProduct)
        self.ui.setProductFields(result, companyList)
        self.updateProduct.show()

def confirmUpdate(productId, companyId,Type, product, code,remarks, imageCode):
    confirm = notification.confirmPopup('Do You want to Save Changes ', 'Update Poduct')
    if(confirm == 'OK'):
        productDL.updateProduct(productId,companyId,Type,product,code,remarks,'NULL',0)
        formRecall.Recall._recallProductForm
        return
    else:
        return