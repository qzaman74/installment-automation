
from Forms.Accounts.CashTransection.conformCashTransectionForm import *
from Forms.Accounts.CashTransection.cashTransectionForm import *

from DLL.AccountsDL import accountDL
from DLL.MiscDL import transectionDL

from Services.NotificationService import notification
from Services.RecallServices import formRecall
from Services.ResetServices import formReset

################################## open Forms from main Form ####################################################
def openCashTransectionForm(self):
    self.cashTransectionWindow = QtWidgets.QMainWindow()
    self.ui = Ui_cashTransectionWindow()
    self.ui.cashTransectionSetupUi(self.cashTransectionWindow)
    self.ui.init()
    self.cashTransectionWindow.showMaximized()

################################## End Forms from main Form #####################################################\


def getAccountByType(accountType):
    result = accountDL.getAccountByTypeFromDB(accountType)
    return result

def getAccountDataById(accountId):
    result = accountDL.getAccountData(accountId)
    return result

def validateCashTransection(self, acID, amountType, remarks, amount, name, mob, balance):
    if (amount == ''):
        notification.showPopup('Please the Amount ', 'Amount !')
        return

    elif (acID == None):
        notification.showPopup('Please the Account ', 'Account !')
        return

    if(amountType == globalVariables.Variables._deposit):
        balance = str(int(balance) - int(amount))

    elif (amountType == globalVariables.Variables._withDrawal):
        balance = str(int(balance) + int(amount))

    self.conformCashTransectionWindow = QtWidgets.QDialog()
    self.cui = Ui_conformCashTransectionWindow()
    self.cui.conformCashTransectionSetupUi(self.conformCashTransectionWindow)
    self.cui.setConfirmField(acID, amountType, remarks, amount, name, mob, balance)
    self.conformCashTransectionWindow.show()

def confirmCashTransection(acID, _type, remarks, amount, balance):
    createdBy = globalVariables.Variables._userId

    if(_type == globalVariables.Variables._withDrawal):
        accountDL.updateAccount(1,"","","","","","","","","balance-"+str(amount)+"",0)
        accountDL.updateAccount(acID,"","","","","","","","","balance+"+str(amount)+"",0)
        transectionDL.insertTransectionToDB('NULL', 1,'NULL','', _type, 0,amount,0,remarks,createdBy)
        transectionDL.insertTransectionToDB('NULL',acID,'NULL','',_type,amount,0,0,remarks,createdBy)
    else:
        accountDL.updateAccount(1,"","","","","","","","","balance+"+amount+"",0)
        accountDL.updateAccount(acID,"","","","","","","","","balance-"+amount+"",0)
        transectionDL.insertTransectionToDB('NULL', 1,'NULL','', _type, amount,0,0,remarks,createdBy)
        transectionDL.insertTransectionToDB('NULL',acID,'NULL','',_type,0,amount,0,remarks,createdBy)

    notification.showInformative("Transection Done Successfully","Success")

    formReset.Reset._resetCashTranectionForm()
    formRecall.Recall._recallDashboard()

def getCashTransectionByAccountId(accountId):
    result = transectionDL.getTransetionByAccountId(accountId)
    return result