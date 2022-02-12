from Forms.Sale.PaymentSale.paymentSaleForm import *
from Forms.Sale.PaymentSale.paymentConfirmForm import *

from Services.NotificationService import notification
from Services.ResetServices import formReset

from DLL.AccountsDL import accountDL
from DLL.MiscDL import billDL,paymentDL,transectionDL

################################## open Forms from main Form ####################################################
def openPaymentSaleForm(self):
    self.paymentWindow = QtWidgets.QMainWindow()
    self.ui = Ui_paymentSaleWindow()
    self.ui.paymentSaleSetupUi(self.paymentWindow)
    self.ui.init()
    self.paymentWindow.showMaximized()

################################## End Forms from main Form #####################################################


def getAccountByType(accountType):
    result = accountDL.getAccountByTypeFromDB(accountType)
    return result

def getAccountData(accountId):
    result = accountDL.getAccountData(accountId)
    return result

def getSaleItem(accountId):
    result = billDL.getSaleItemByAccountId(accountId)
    return result

def getSaleItemDetail(billId):
    result = billDL.getItemDetailById(billId)
    return result

def getPaymentLog(billId):
    result = paymentDL.getPaymentLogByBillId(billId)
    return result

def validatePayment(self,date,billId,billType,accountId, name, mobile,address,soldItem,amount,balance,remarks):
    if(soldItem == 'SELECT'):
        notification.showInformative("Please Select the Item","Missing !")
        return
    if(amount == ''):
        notification.showInformative("Please Enter the Amount","Missing !")
        return
    if(amount != ''):
        if(int(balance)<0):
            notification.showInformative("Paying Higher Amount","Over !")
            return


    self.confirmSaleDialog = QtWidgets.QDialog()
    self.ui = Ui_confirmSaleDialog()
    self.ui.confirmSaleSetupUi(self.confirmSaleDialog)
    self.ui.setConfirmSalePaymentFields(date,billId,billType,accountId,name, mobile,address,soldItem,amount,balance,remarks)
    self.confirmSaleDialog.show()

def confirmPaymentSale(accountId,billId,billType,date,amount,balance,remarks):
    id = 'NULL'
    createdBy = globalVariables.Variables._userId
    transectionType = globalVariables.Variables._deposit
    date = dateTime.getStartDateWithoutTimes(date)

    paymentDL.insertPaymentToDB(id,billId,billType,date,amount,balance,remarks,createdBy)

    transectionDL.insertTransectionToDB(id,1,billId,billType,transectionType,amount,0,0,'received Against Sale',createdBy)
    accountDL.updateAccount(1, '', '', '', '', '', '', '', '', ('balance+' + str(amount)), 0)

    transectionDL.insertTransectionToDB(id,accountId,billId,billType,transectionType,0,amount,0,'Payment Against Sale',createdBy)
    accountDL.updateAccount(accountId,'','','','','','','','',('balance-'+str(amount)),0)

    billDL.updateBill(billId,'','','','','','','','','','','',"payment+"+amount+"",balance,0)




    notification.showInformative("Payment Done Successfully ","Success")
    formReset.Reset._resetPaymentSaleForm()