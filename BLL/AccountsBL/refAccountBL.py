from Forms.Accounts.RefAccount.refAccountForm import *
from Forms.Accounts.RefAccount.refAccountConfirmForm import *

from DLL.AccountsDL import refAccountDL

from Services.NotificationService import notification
from Services.ResetServices import formReset
from Services.RecallServices import formRecall

################################## open Forms from main Form ####################################################
def openReferenceAccountForm(self):
    self.refAccountWindow = QtWidgets.QMainWindow()
    self.ui = Ui_refAccountWindow()
    self.ui.refAccountSetupUi(self.refAccountWindow)
    self.ui.init()
    self.refAccountWindow.showMaximized()

################################## End Forms from main Form #####################################################\

def validateRefAccount(self, name,fatherName,cnic,mobile,gender,address,imageCode,filterList):
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
    elif(mobile == ''):
        notification.showWarning("Please Enter Mobile Number ","Warning")
        return
    elif(len(mobile)<11):
        notification.showWarning("Please Enter Complete Mobile Number","Warning")
        return

    for x in filterList:
        if(mobile == x[4]):
            notification.showWarning("This Mobile Number is Already Registered","Registered")
            return
        if(cnic == x[3]):
            notification.showWarning("This CNIC Number is Already Registered","Registered")
            return


    self.refAccountConfirmDialog = QtWidgets.QDialog()
    self.ui = Ui_refAccountConfirmDialog()
    self.ui.refAccountConfirmSetupUi(self.refAccountConfirmDialog)
    self.ui.setAccountFields( name,fatherName,cnic,mobile,gender,address,imageCode)
    self.refAccountConfirmDialog.show()

def confirmRefAccountValidation(name,fatherName,cnic,mobile,gender,address,imageCode):
    createdBy = globalVariables.Variables._userId
    refAccountDL.insertRefAccountToDB('NULL',name,fatherName,cnic,mobile,gender,address,imageCode,createdBy)
    formReset.Reset._resetRefAccountForm()
    formRecall.Recall._recallRefAccountList()


def getAllRefAccounts():
    result = refAccountDL.getAllRefAccounts()
    return result

def deleteAccount(self,accountId,name):
    confirm = notification.confirmPopup('Do You want to Delete '+str(name)+' Parmanently ', 'Deleting Account')
    if(confirm == 'OK'):
        refAccountDL.updateRefAccount(accountId,'','','','','','',1)
        formRecall.Recall._recallRefAccount()
        return
    else:
        return

