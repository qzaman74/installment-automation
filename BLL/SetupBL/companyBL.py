from Forms.Setup.Company.companyForm import *
from Forms.Setup.Company.companyConfirmForm import *
from Forms.Setup.Company.companyUpdateForm import *

from Services.NotificationService import notification
from Services.ResetServices import formReset
from Services.RecallServices import formRecall

from DLL.SetupDL import companyDL
from DLL.MiscDL import imageDL

################################## open Forms from main Form ####################################################
def openCompanyForm(self):
	self.companyWindow = QtWidgets.QMainWindow()
	self.cui = Ui_companyWindow()
	self.cui.companySetupUi(self.companyWindow)
	self.cui.init()
	self.companyWindow.showMaximized()

################################## End Forms from main Form #####################################################


#################### validate data is according to policy #################

def validateCompany(self, name, code, agent, contact, location, imageCode, companyList):
    if(name == ''):
        notification.showInformative('Please Enter The Name ', 'Name')
        return
    elif(len(name) < 4):
        notification.showInformative('Please Enter The Complete Name ', 'Name')
        return
    elif(agent != ''):
        if(len(agent) < 4):
            notification.showInformative('Please Enter The Complete Company Representative ', 'Representative')
            return
    elif (contact == ''):
        if (len(contact) != 11):
            notification.showInformative('Please Enter The Complete company Contact ', 'Company Contact')
            return

    for x in companyList:
        if(name == x[1]):
            notification.showInformative('This Company With Same Name Already saved  ', 'Name Duplicate')
            return
        if(code == x[2]):
            notification.showInformative('This Company With Same Code Already saved  ', 'Code Duplicate')
            return
        else:
            pass

    self.conformDialog = QtWidgets.QDialog()
    self.ccui = Ui_conformDialog()
    self.ccui.conformSetupUi(self.conformDialog)
    self.conformDialog.show()
    self.ccui.setCompanyFields(name, code, agent, contact, location, imageCode)

#################### end validate data is according to policy #################

def confirmCompany(self, name, code, agent, contact, location, imageCode):
    id = 'NULL'
    createdBy = globalVariables.Variables._userId
    companyDL.insertCompany(id, name, code, agent, contact, location,'NULL', createdBy)
    formReset.Reset._resetCompanyForm()
    formRecall.Recall._recallCompanyListForPurchase()


def getCompanies():
    result = companyDL.getCompanyFromDB()
    return  result

def validateImage(self,companyID):
    pass
def validateUpdate(self, companyId):
    result = companyDL.getCompanyByID(companyId)
    if(len(result)>0):
        self.updateCompany = QtWidgets.QDialog()
        self.ui = Ui_updateCompany()
        self.ui.updateSetupUi(self.updateCompany)
        self.ui.setUpdateFields(result)
        self.updateCompany.show()

def confirmUpdate(companyId, name,code, agent ,contact,location, imageCode):
    if (name == ''):
        notification.showInformative('Please Enter The Name ', 'Name')
        return
    elif (len(name) < 4):
        notification.showInformative('Please Enter The Complete Name ', 'Name')
        return
    elif (agent == ''):
        notification.showInformative('Please Enter The Company Representative ', 'Representative')
        return
    elif (len(agent) < 4):
        notification.showInformative('Please Enter The Complete Company Representative ', 'Representative')
        return
    elif (contact == ''):
        notification.showInformative('Please Enter The company Contact ', 'Company Contact')
        return
    elif (len(contact) != 11):
        notification.showInformative('Please Enter The Complete company Contact ', 'Company Contact')
        return
    elif (location == ''):
        notification.showPopup('Please Select Company Location  ', 'Location')
        return

    confirm = notification.confirmPopup('Do You want to Save ', 'Confirm Update')
    if(confirm == 'OK'):
        companyDL.updateCompany(companyId,name,code,agent,contact,location,imageCode,0)
        notification.showInformative('changes Done ', 'Success')
        return
    else:
        return

def validateRemove(self, companyId, name):
    confirm = notification.confirmPopup('Do You want to Delete '+str(name)+' Parmanently ', 'Deleting Account')
    if(confirm == 'OK'):
        companyDL.updateCompany(companyId,'','','','','','',1)
        Ui_companyWindow.getCompany(self)
        return
    else:
        return