from Forms.Purchase.purchaseForm import *
from Forms.Purchase.purchaseConfirmForm import *

from BLL.SetupBL import companyBL,productBL
from BLL.AccountsBL import accountFormBL

from DLL.AccountsDL import accountDL
from DLL.SetupDL import companyDL,productDL
from DLL.MiscDL import billDL,transectionDL, policyDL,paymentDL
from DLL.PurchaseDL import purchaseDL

from Services.NotificationService import notification
from Services.MiscService import dateTime
from Services.ResetServices import formReset
from Services.RecallServices import formRecall



################################## open Forms from main Form ####################################################
def openPurchaseForm(self):
	self.purchaseWindow = QtWidgets.QMainWindow()
	self.ui = Ui_purchaseWindow()
	self.ui.purchaseSetupUi(self.purchaseWindow)
	self.ui.init()
	self.purchaseWindow.showMaximized()

################################## End Forms from main Form #####################################################

def getAccountByType(accountType):
    result = accountDL.getAccountByTypeFromDB(accountType)
    return result

def getCompany():
    result = companyDL.getCompanyFromDB()
    return result

def getProduct(companyID):
    result = productDL.getProductByCompanyIDFromDB(companyID)
    return result

def validateAddItem(companyId, companyName, productId, productName, productType, engine, chessis, registration,
                    costPrice, salePrice, discountAmount, totalPrice, remarks):
    if(companyName == 'SELECT'):
        notification.showInformative("Please Select Company","Missing...!")
        return
    elif(productName == 'SELECT'):
        notification.showInformative("Please Select Product","Missing...!")
        return
    elif(productType == ''):
        notification.showInformative("Please Select Product Type ","Missing...!")
        return
    elif(engine == ''):
        notification.showInformative("Please Enter Engine Number","Missing...!")
        return
    elif(chessis == ''):
        notification.showInformative("Please Enter Chessis Number","Missing...!")
        return
    elif(costPrice == ''):
        notification.showInformative("Please Enter Cost Price","Missing...!")
        return
    elif(salePrice == ''):
        notification.showInformative("Please Enter Sale Price","Missing...!")
        return
    elif(registration == ''):
        registration = 0

    itemList = [companyId, companyName, productId, productName, productType, engine, chessis, registration,
                costPrice, salePrice, discountAmount, totalPrice, remarks]
    Ui_purchaseWindow._cartItemList.append(itemList)
    formReset.Reset._resetPurchaseItem()


def removeItemFromCart(itemIndex):
        del (Ui_purchaseWindow._cartItemList[itemIndex])



def validatePurchase(self, date, accountId, accountName,invoice, amount, discount, netAmount, payment,balance,
                     imageCode, itemList, policyType, policyList ):
    if(accountName == ''):
        notification.showInformative('Please Select the Account ', 'Account Missing !')
        return
    elif(len(itemList)< 1):
        notification.showInformative('Please Enter Atleast One Product ', 'Product Missing !')
        return
    elif(policyType == globalVariables.Variables._net):
        if(int(balance) < 0 ):
            notification.showInformative('You Are Paying Over Due Amount ', 'Over Amount !')
            return
        if(int(balance) > 0 ):
            notification.showInformative('You Are Paying Under Due Amount ', 'Under Amount !')
            return

    elif(policyType == globalVariables.Variables._lease or policyType == globalVariables.Variables._shortTerm ):
        if(len(policyList)< 1):
            notification.showInformative('Please Enter Atleast One Installment Policy ', 'Installment Missing !')
            return
        elif(int(balance) < 0 ):
            notification.showInformative('You Are Paying Over Due Amount ', 'Over Amount !')
            return

    self.purchaseConfirmForm = QtWidgets.QDialog()
    self.ui = Ui_purchaseConfirmForm()
    self.ui.purchaseConfirmFormSetupUi(self.purchaseConfirmForm)
    self.ui.setPurchaseFields( date, accountId, accountName,invoice, amount, discount, netAmount, payment, balance,
                               imageCode, itemList, policyType, policyList )
    self.purchaseConfirmForm.show()





def confirmPurchase(date, accountId,invoice, amount, discount, netAmount, payment,balance, imageCode, itemList, policyType, policyList ):
    id = 'NULL'
    billId = '(SELECT MAX(bill_id) FROM bill)'

    date = dateTime.getStartDateWithoutTimes(date)
    billType = globalVariables.Variables._purchase
    withDrawalTransection = globalVariables.Variables._withDrawal
    payableTransection = globalVariables.Variables._payable
    createdBy = globalVariables.Variables._userId


    if(policyType == globalVariables.Variables._net):

        billDL.insertBillToDB(id, accountId, id, date, '', '', invoice, billType, 0,
                              amount, discount, netAmount, payment, balance, 'NO', 'NULL', createdBy)

        for item in itemList:
            purchaseDL.insertPurchaseToDB(id, billId, accountId, item[0], item[2], item[4],item[5], item[6], item[7],
                                          item[8],item[9],item[10],item[11],1,item[12],createdBy)

        accountDL.updateAccount(1, '', '', '', '', '', '', '', '', ('balance-'+str(payment)), 0)
        transectionDL.insertTransectionToDB(id, 1, billId, billType, withDrawalTransection, 0, payment, 0, 'PAID FOR PURCHASE', createdBy)


    if(policyType == globalVariables.Variables._shortTerm or policyType == globalVariables.Variables._lease):

        billDL.insertBillToDB(id, accountId, id, date, '', '', invoice, billType, 1,
                              amount, discount, netAmount, payment, balance, 'NO', 'NULL', createdBy)

        for item in itemList:
            purchaseDL.insertPurchaseToDB(id, billId, accountId, item[0], item[2], item[4],item[5], item[6], item[7],
                                          item[8],item[9],item[10],item[11],1,item[12],createdBy)

        accountDL.updateAccount(1,'','','','','','','','',('balance-'+str(payment)),0)
        accountDL.updateAccount(accountId,'','','','','','','','', ('balance-' + str(balance)),0)

        transectionDL.insertTransectionToDB(id, 1, billId, billType, withDrawalTransection, 0, payment, 0,
                                            'PAID FOR PURCHASE', createdBy)
        transectionDL.insertTransectionToDB(id, accountId, billId, billType, payableTransection, 0, balance, 0,
                                            'PAYABLE AGAINST PURCHASE', createdBy)

        for x in policyList:
            x = str(x)
            x = x.split(',')
            policyDL.insertPolicyToDB(id, billId, policyType, x[0], x[1], x[2], 0, createdBy)

        # paymentDL.insertPaymentToDB(id, billId, billType, date, payment, balance, 'DOWN PAYMENT AGAINST SALE', createdBy)


    notification.showRight("Purchased Successfully",'Success !')
    formReset.Reset._resetPurchaseForm()
    formRecall.Recall._recallDashboard()



def getBill(accountId,billType):
    result = billDL.getBillByAccountID(accountId,billType)
    return result

def validateOpenQuickAccount(self):
    accountFormBL.openAccountForm(self)

def validateOpenQuickCompany(self):
    companyBL.openCompanyForm(self)

def validateOpenQuickProduct(self):
    productBL.openProductForm(self)