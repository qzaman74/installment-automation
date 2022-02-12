from Forms.Sale.NetSale.netSaleForm import *
from Forms.Sale.NetSale.netSaleConfirmForm import *

from BLL.SetupBL import companyBL, productBL
from BLL.AccountsBL import accountFormBL

from DLL.AccountsDL import accountDL
from DLL.SaleDL import saleDL
from DLL.PurchaseDL import purchaseDL
from DLL.SetupDL import companyDL,productDL
from DLL.MiscDL import billDL,transectionDL

from Services.NotificationService import notification
from Services.ResetServices import formReset

################################## open Forms from main Form ####################################################
def openSaleForm(self):
    self.saleWindow = QtWidgets.QMainWindow()
    self.ui = Ui_netSaleWindow()
    self.ui.netSaleSetupUi(self.saleWindow)
    self.ui.init()
    self.saleWindow.showMaximized()

################################## End Forms from main Form #####################################################

def getAccountByType(accountType):
    result = accountDL.getAccountByTypeFromDB(accountType)
    return result

def getAccountData(accountId):
    result = accountDL.getAccountData(accountId)
    return result

def getCompany():
    result = companyDL.getCompanyFromDB()
    return result

def getProduct(companyID):
    result = productDL.getProductByCompanyIDFromDB(companyID)
    return result

def getBill(accountId,billType):
    result = billDL.getBillByAccountID(accountId,billType)
    return result

def getProductDetail(productId):
    if(productId!=0):
        result = purchaseDL.getPurchaseByProductID(productId)
        return result
    else:
        pass

def setProductDetail(purchaseId):
    result = purchaseDL.getPurchaseByPurchaseID(purchaseId)
    return result

def validateAddItem(accountId,companyId,companyName,productId,productName,purchaseId,engine,chassis,quantity,
                    salePrice,discount,totalPrice,remarks):
    if(accountId == None):
        notification.showInformative("Please Select Account","Missing...!")
        return
    elif (companyName == 'SELECT'):
        notification.showInformative("Please Select Company", "Missing...!")
        return
    elif(productName == 'SELECT'):
        notification.showInformative("Please Select Product","Missing...!")
        return
    elif(salePrice == ''):
        notification.showInformative("Please Enter Sale Price","Missing...!")
        return

    itemList = [accountId,companyId,companyName,productId,productName,purchaseId,engine,chassis,quantity,salePrice,
                discount,totalPrice,remarks]
    Ui_netSaleWindow._cartItemList.append(itemList)
    formReset.Reset._resetSaleItem

def removeItemFromCart(itemIndex):
    del (Ui_netSaleWindow._cartItemList[itemIndex])

def validateSale(self, date, accountId, accountName, accountCnic, accountMobile, accountAddress,
                 company, product, engine,chassis, amount, discount,netAmount, payment, balance, imageCode, itemList):
    if(len(itemList)< 1):
        notification.showInformative('Please Add Atleast One Product ', 'Product Missing !')
        return
    if(int(balance)>0):
        notification.showInformative('Payment is less ', 'Less Payment !')
        return
    if(int(balance)<0):
        notification.showInformative('Payment is High ', 'Over Payment !')
        return


    invoice = billDL.getMaxBillId()

    self.confirmSaleDialog = QtWidgets.QDialog()
    self.ui = Ui_confirmSaleDialog()
    self.ui.confirmSaleSetupUi(self.confirmSaleDialog)
    self.ui.setConfirmSaleFields( date, invoice, accountId, accountName, accountCnic, accountMobile, accountAddress,
                                  company, product, engine,chassis, amount, discount,netAmount, payment, balance,
                                  imageCode, itemList)
    self.confirmSaleDialog.show()

def confirmSale(accountId,date,totalBill,discount,netBill,payment,balance,imageCode,itemList):
    id = 'NULL'
    billId = '(SELECT MAX(bill_id) FROM bill)'
    date = dateTime.getStartDateWithoutTimes(date)
    billType = globalVariables.Variables._sale
    transectionType = globalVariables.Variables._deposit
    createdBy = globalVariables.Variables._userId

    billDL.insertBillToDB(id,accountId,id,date,'','',0,billType,0,totalBill,discount,netBill,payment,balance,'no','NULL',createdBy)

    for item in itemList:
        saleDL.insertSaleToDB(id, billId, item[0], item[1], item[5], item[8], item[9], item[10], item[11], item[12], createdBy)
        purchaseDL.updatePurchase(item[5], '', '', '', '', '', '', '', '', '', '', ('quantity_log-' + str(item[8])), '', 0)

    accountDL.updateAccount(1, '', '', '', '', '', '', '', '', ('balance+' + str(payment)), 0)
    transectionDL.insertTransectionToDB(id,1,billId,billType,transectionType,payment,0,0,
                                        'Received from Sale',createdBy)

    if(int(balance)>0):
        accountDL.updateAccount(accountId,'','','','','','','','',('balance+'+str(balance)),0)
        transectionDL.insertTransectionToDB(id,accountId,billId,billType,'NULL',balance,0,0,
                                            'Received from Sale',createdBy)

    if (int(balance) < 0):
        accountDL.updateAccount(accountId, '', '', '', '', '', '', '', '', ('balance-' + str(int(balance)*-1)), 0)
        transectionDL.insertTransectionToDB(id, accountId, billId, billType, 'NULL',balance, 0, 0,
                                            'remaing receiveable for purchase', createdBy)

    notification.showInformative("Sale Successfully.!","Success")
    formReset.Reset._resetSaleForm()




def validateOpenQuickAccount(self):
    accountFormBL.openAccountForm(self)

def validateOpenQuickCompany(self):
    companyBL.openCompanyForm(self)

def validateOpenQuickProduct(self):
    productBL.openProductForm(self)