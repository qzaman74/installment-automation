from Forms.Accounts.CreateAccount.accountForm import *
from Forms.Accounts.CreateAccount.accountConfirmForm import *
from Forms.Accounts.CreateAccount.accountImageForm import *
from Forms.Accounts.CreateAccount.accountUpdateForm import *

from DLL.AccountsDL import accountDL

from Services.NotificationService import notification
from Services.ResetServices import formReset
from Services.RecallServices import formRecall


################################## open Forms from main Form ####################################################
def openAccountForm(self):
    self.accountWindow = QtWidgets.QMainWindow()
    self.aui = Ui_accountWindow()
    self.aui.accountSetupUi(self.accountWindow)
    self.aui.init()
    self.accountWindow.showMaximized()

################################## End Forms from main Form #####################################################\

def validateAccount(self, name, fatherName, cnic, mobileNo, gender, address, accountType, accountStatus, balance, imageCode,filterList ):
    if(name == ''):
        notification.showWarning("Please Enter Name","Warning")
        return

    elif(len(name) < 3):
        notification.showWarning("Please Enter Minimum 3 Character Name","Warning")
        return

    elif(fatherName != ''):
        if (len(fatherName) < 3):
            notification.showWarning("Please Enter Minimum 3 Character Father Name", "Warning")
            return

    elif(cnic != ''):
        if(len(cnic)<13):
            notification.showWarning("Please Enter Complete CNIC","Warning")
            return

        for x in filterList:
            if (cnic == x[3]):
                notification.showWarning("This CNIC Number is Already Registered", "Registered")
                return

    elif(mobileNo == ''):
        notification.showWarning("Please Enter Mobile Number ","Warning")
        return

    elif(mobileNo != ''):
        for x in filterList:
            if (mobileNo == x[4]):
                notification.showWarning("This Mobile Number is Already Registered", "Registered")
                return

    elif(len(mobileNo)<11):
        notification.showWarning("Please Enter Complete Mobile Number","Warning")
        return


    self.accountConfirmDialog = QtWidgets.QDialog()
    self.acui = Ui_accountConfirmDialog()
    self.acui.accountConfirmSetupUi(self.accountConfirmDialog)
    self.acui.setAccountConfirmFields( name, fatherName, cnic, mobileNo, gender, address, accountType, accountStatus, balance, imageCode )
    self.accountConfirmDialog.show()


def confirmAccount(self, name, fatherName, cnic, mobileNo, gender, address,accountType, accountStatus, balance, imageCode ):
    id = 'NULL'
    createdBy = globalVariables.Variables._userId
    accountDL.insertAccountToDB(id, name, fatherName, cnic, mobileNo,  gender, address, accountType, accountStatus,
                                balance, 'NULL', createdBy )
    formRecall.Recall._recallQuickAccount
    formReset.Reset._resetAccountForm()



### get accountData from DL for Display in AccountsForm Table
def getAllAccounts():
    result = accountDL.getAllAccountsFromDB()
    return result


### get image from DL and show in imageDailog
def validateImage(self,accountID):
    result = accountDL.getAccountImage(accountID)
    if(result != ''):
        self.imageDialog = QtWidgets.QDialog()
        self.iui = Ui_imageDialog()
        self.iui.imageSetupUi(self.imageDialog)
        self.imageDialog.show()
        self.iui.getImage(result)

def deleteAccount(self, accountID, name):
    if(int(accountID) == 1):
        notification.showInformative("Sorry You Don't Remove This Account","UnSuccess")
        return

    confirm = notification.confirmPopup('Do You want to Delete '+str(name)+' Parmanently ', 'Deleting Account')
    if(confirm == 'OK'):
        accountDL.updateAccount(accountID,'','','','','','','','','',1)
        self.getAccounts()
        return
    else:
        return

def validateUpdate(self,accountID):
    result = accountDL.getAccountData(accountID)
    if(len(result)>0):
        self.accountUpdateForm = QtWidgets.QDialog()
        self.auui = Ui_accountUpdateForm()
        self.auui.accountUpdateSetupUi(self.accountUpdateForm)
        self.auui.setAccountUpdateFields(result)
        self.accountUpdateForm.show()

def updateAccountForm(accountId, cellNo, address, accountType, accountStatus):
    confirm = notification.confirmPopup('Do You want to Save Changes ', 'Confirm')
    if(confirm == 'OK'):
        accountDL.updateAccount(accountId, 0, '', '', '', cellNo, '', address, accountType, accountStatus, '', 0)
        return
    else:
        return
