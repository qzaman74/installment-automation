from Forms.Sale.saleForm import *
from Forms.Sale.saleConfirmForm import *

from BLL.SetupBL import companyBL, productBL
from BLL.AccountsBL import accountFormBL, refAccountBL

from DLL.AccountsDL import accountDL, refAccountDL
from DLL.SaleDL import saleDL
from DLL.PurchaseDL import purchaseDL
from DLL.SetupDL import companyDL, productDL
from DLL.MiscDL import billDL, transectionDL, paymentDL, policyDL

from Services.NotificationService import notification
from Services.ResetServices import formReset
from Services.RecallServices import formRecall

################################## open Forms from main Form ####################################################
def openSaleForm(self):
    self.saleWindow = QtWidgets.QMainWindow()
    self.ui = Ui_saleWindow()
    self.ui.saleSetupUi(self.saleWindow)
    self.ui.init()
    self.saleWindow.showMaximized()

################################## End Forms from main Form #####################################################

def getAccountByType(accountType):
    result = accountDL.getAccountByTypeFromDB(accountType)
    return result

def getAccountData(accountId):
    result = accountDL.getAccountData(accountId)
    return result

def getRefAccount():
    result = refAccountDL.getAllRefAccounts()
    return result

def openReferenceAccount(self):
    refAccountBL.openReferenceAccountForm(self)

def getCompany():
    result = companyDL.getCompanyFromDB()
    return result

def getProduct(companyID):
    result = productDL.getProductByCompanyIDFromDB(companyID)
    return result

def getBill(accountId,billType):
    result = billDL.getBillByAccountID(accountId,billType)
    return result

def getProductDetail(productId,productType):
    if(productId!=0):
        result = purchaseDL.getPurchaseByProductID(productId,productType)
        return result
    else:
        pass

def setProductDetail(purchaseId):
    result = purchaseDL.getPurchaseByPurchaseID(purchaseId)
    return result

def validateAddItem(accountId, refAccountId, companyId, companyName, productId, productName, purchaseId,
                    engine, chassis, registration, quantity, salePrice,discount,totalPrice,remarks):

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

    if(refAccountId == None):
        refAccountId = 0

    itemList = [accountId, refAccountId, companyId, companyName, productId, productName, purchaseId, engine, chassis, registration, quantity, salePrice,
                discount, totalPrice, remarks]
    Ui_saleWindow._cartItemList.append(itemList)
    formReset.Reset._resetSaleItem

def removeItemFromCart(itemIndex):
    del (Ui_saleWindow._cartItemList[itemIndex])

def validateSale(self, date, accountId, accountName, accountCnic, accountMobile, accountAddress, refAccountId, refAccount, company, product,
                 engine,chassis, amount, discount,netAmount, payment, balance, imageCode, itemList, policyType, policyList):

    if(accountName == ''):
        notification.showInformative('Please Select the Account ', 'Account Missing !')
        return

    elif(len(itemList)< 1):
        notification.showInformative('Please Add Atleast One Product ', 'Product Missing !')
        return

    elif(policyType == globalVariables.Variables._net):
        if(int(balance) < 0 ):
            notification.showInformative('You Are Paying Over Due Amount ', 'Over Amount !')
            return
        if(int(balance) > 0 ):
            notification.showInformative('You Are Paying Under Due Amount ', 'Under Amount !')
            return


    elif(policyType == globalVariables.Variables._lease or policyType == globalVariables.Variables._shortTerm ):
        if(int(balance) == 0 ):
            notification.showInformative('You Are Paying Full Amount ', 'Full Amount !')
            return
        elif(int(balance) < 0 ):
            notification.showInformative('You Are Paying Over Due Amount ', 'Over Amount !')
            return
        elif(len(policyList)< 1):
            notification.showInformative('Please Enter Atleast One Installment Policy ', 'Installment Missing !')
            return

    if(refAccountId == None ):
        refAccountId = 0



    invoice = billDL.getMaxBillId()

    self.confirmSaleDialog = QtWidgets.QDialog()
    self.ui = Ui_confirmSaleDialog()
    self.ui.confirmSaleSetupUi(self.confirmSaleDialog)
    self.ui.setConfirmSaleFields( date, invoice, accountId, accountName, accountCnic, accountMobile, accountAddress, refAccountId, refAccount,
                                  company, product, engine,chassis, amount, discount,netAmount, payment, balance,
                                  imageCode, itemList, policyType, policyList )
    self.confirmSaleDialog.show()


def confirmSale(accountId, refAccountId, date, totalBill, discount, netBill, payment, balance, imageCode, itemList, policyType, policyList ):

    id = 'NULL'
    billId = '(SELECT MAX(bill_id) FROM bill)'
    date = dateTime.getStartDateWithoutTimes(date)
    billType = globalVariables.Variables._sale
    depositTransection = globalVariables.Variables._deposit
    receivableTransection = globalVariables.Variables._receivable
    createdBy = globalVariables.Variables._userId


    if(policyType == globalVariables.Variables._net):
        billDL.insertBillToDB(id, accountId, refAccountId, date, '', '', 0, billType, 0, totalBill, discount, netBill,
                              payment, balance, 'NO', 'NULL', createdBy)

        for item in itemList:
            saleDL.insertSaleToDB(id, billId, item[0], item[2], item[6], item[10], item[11], item[12], item[13], item[14], createdBy)
            purchaseDL.updatePurchase(item[6], '', '', '', '', '', '', '', '', '', '', ('quantity_log-' + str(item[10])), '', 0)

        accountDL.updateAccount(1, '', '', '', '', '', '', '', '', ('balance+' + str(payment)), 0)
        transectionDL.insertTransectionToDB(id, 1, billId, billType, depositTransection, payment, 0, 0,
                                            'RECEIVED FROM SALE', createdBy)


    if(policyType == globalVariables.Variables._shortTerm or policyType == globalVariables.Variables._lease):
        billDL.insertBillToDB(id, accountId, refAccountId, date, '', '', 0, billType, 1, totalBill, discount, netBill,
                              payment, balance, 'NO', 'NULL', createdBy)

        for item in itemList:
            saleDL.insertSaleToDB(id, billId, item[0], item[2], item[6], item[10], item[11], item[12], item[13], item[14], createdBy)
            purchaseDL.updatePurchase(item[6], '', '', '', '', '', '', '', '', '', '', ('quantity_log-' + str(item[10])), '', 0)

        accountDL.updateAccount(1, '', '', '', '', '', '', '', '', ('balance+' + str(payment)), 0)
        accountDL.updateAccount(accountId, '', '', '', '', '', '', '', '', ('balance+' + str(balance)), 0)

        transectionDL.insertTransectionToDB(id, 1, billId, billType, depositTransection, payment, 0, 0,
                                            'RECEIVED FROM SALE', createdBy)
        transectionDL.insertTransectionToDB(id, accountId, billId, billType, receivableTransection, balance, 0, 0,
                                            'RECEIVABLE AGAINST SALE', createdBy)

        paymentDL.insertPaymentToDB(id, billId, billType, date, payment, balance, 'DOWN PAYMENT AGAINST SALE', createdBy)

        for x in policyList:
            x = str(x)
            x = x.split(',')
            policyDL.insertPolicyToDB(id, billId, policyType, x[0], x[1], x[2], 0, createdBy)



    notification.showInformative("Sale Successfully.!","Success")
    formReset.Reset._resetSaleForm()
    formRecall.Recall._recallDashboard()


def validateOpenQuickAccount(self):
    accountFormBL.openAccountForm(self)

def validateOpenQuickCompany(self):
    companyBL.openCompanyForm(self)

def validateOpenQuickProduct(self):
    productBL.openProductForm(self)