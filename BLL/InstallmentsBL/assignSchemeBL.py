from Forms.InstallmentPlan.assignScheme.assignSchemeForm import *
from Forms.InstallmentPlan.assignScheme.assignSchemeConfirmForm import *
from DLL.InstallmentDL import assignSchemeDL,schemeDL
from DLL.AccountsDL import accountDL
from Services.NotificationService import notification

################################## open Forms from main Form ####################################################
def openAssignSchemeForm(self):
    self.assignSchemeWindow = QtWidgets.QMainWindow()
    self.asui = Ui_assignSchemeWindow()
    self.asui.assignSchemeSetupUi(self.assignSchemeWindow)
    self.asui.init()
    self.assignSchemeWindow.showMaximized()
################################## End Forms from main Form #####################################################

def getAccountByType(accountType):
    result = accountDL.getAccountByTypeFromDB(accountType)
    return result

def getAccountInfo(accountID):
    result = accountDL.getAccountData(accountID)
    return result

def getSchemeList():
    result = schemeDL.getAllSchemesFromDB()
    return result

def getSchemeInfo(schemeID):
    result = schemeDL.getSchemeData(schemeID)
    return result

def getAllAssignedSchemes(accountId):
    result = assignSchemeDL.getAllAssignedSchemesById(accountId)
    return result

def validateAssginScheme(self,accountID, schemeID, name, cnic, cellno, scheme, amount, remarks):
    if(accountID == 0 ):
        notification.showInformative('Please Select Account', 'Account')
        return
    elif(schemeID == 0):
        notification.showInformative('Please Select Scheme', 'Scheme')
        return
    elif(amount == ''):
        notification.showInformative('Please Enter Amount', 'Amount')
        return

    self.assignSchemeConfirmDialog = QtWidgets.QDialog()
    self.asui = Ui_assignSchemeConfirmDialog()
    self.asui.assignSchemeConfirmSetupUi(self.assignSchemeConfirmDialog)
    self.asui.setAssignSchemeFields(accountID, schemeID, name, cnic, cellno, scheme, amount, remarks)
    self.assignSchemeConfirmDialog.show()

def confirmAssignScheme(schemeId, accountId):
    id = 'NULL'
    createdBy = globalVariables.Variables._userId

    assignSchemeDL.insertAssignScheme(id,schemeId,accountId,createdBy)