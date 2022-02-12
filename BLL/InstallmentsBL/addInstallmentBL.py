from Forms.InstallmentPlan.addInstallment.addInstallmentForm import *
from Forms.InstallmentPlan.addInstallment.installmentConfirmForm import *
from DLL.InstallmentDL import assignSchemeDL,schemeDL,addInstallmentDL
from DLL.AccountsDL import accountDL
from Services.NotificationService import notification

################################## open Forms from main Form ####################################################
def openAddInstallmentForm(self):
    self.addInstallmentWindow = QtWidgets.QMainWindow()
    self.aiui = Ui_addInstallmentWindow()
    self.aiui.addInstallmentSetupUi(self.addInstallmentWindow)
    self.aiui.init()
    self.addInstallmentWindow.showMaximized()

################################## End Forms from main Form #####################################################

def getSchemeList(accountId):
    result = assignSchemeDL.getAssignedSchemesById(accountId)
    return result

def getSchemeInfo(customerSchemeID):
    result = schemeDL.getSchemeDataByCSID(customerSchemeID)
    return result

def validateAddInstallment(self, date, name, cellno, address,  customerSchemeID,  scheme, installment, balance, amount, remarks):
    if(customerSchemeID == 0):
        notification.showInformative("Please Select Scheme","Scheme Missing !")
        return
    elif(amount == '' or int(amount) < 0 ):
        notification.showInformative("Please Enter Amount","Amount Missing !")
        return

    self.conformInstallmentDialog = QtWidgets.QDialog()
    self.ciui = Ui_conformInstallmentDialog()
    self.ciui.conformInstallmentSetupUi(self.conformInstallmentDialog)
    self.ciui.setInstallmentConfirmFields(date, name, cellno, address,  customerSchemeID,  scheme, installment, balance, amount, remarks)
    self.conformInstallmentDialog.show()


def confirmInstallment(customerSchemeID, date, balance, amount, remarks):
    id = 'NULL'
    createdBy = globalVariables.Variables._userId
    date = dateTime.getStartDateWithoutTimes(date)
    balance = int(amount) + int(balance)

    addInstallmentDL.insertInstallmentLog(id,customerSchemeID,date,amount,balance,remarks,createdBy)

def getInstallmentHistory(accountId, customerSchemeId):
    result = addInstallmentDL.getInstallmentHistoryFromDB(accountId, customerSchemeId)
    return result


def getAccountByType(accountType):
    result = accountDL.getAccountByTypeFromDB(accountType)
    return result

def getAccountInfo(accountID):
    result = accountDL.getAccountData(accountID)
    return result