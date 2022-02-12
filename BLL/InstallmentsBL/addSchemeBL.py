from Forms.InstallmentPlan.addScheme.addSchemeForm import *
from Forms.InstallmentPlan.addScheme.addSchemeConformForm import *
from Services.NotificationService import notification
from DLL.InstallmentDL import schemeDL


################################## open Forms from main Form ####################################################
def openAddSchemeFormForm(self):
    self.schemeWindow = QtWidgets.QMainWindow()
    self.sui = Ui_schemeWindow()
    self.sui.schemeSetupUi(self.schemeWindow)
    self.sui.init()
    self.schemeWindow.showMaximized()
################################## End Forms from main Form #####################################################

def validateScheme(self, scheme, startDate, endDate, dueDate, installments, amount, remarks):
    if (scheme == ''):
        notification.showInformative('Please Add Scheme Title  ', 'Scheme Title !')
        return
    elif (startDate == ''):
        notification.showInformative('Please Select The Start Date  ', 'Start Date !')
        return
    elif (endDate == ''):
        notification.showInformative('Please Select The End Date  ', 'End Date !')
        return
    elif (dueDate == ''):
        notification.showInformative('Please Select The Due Date  ', 'Due Date !')
        return
    elif (installments == '' or int(installments) < 1):
        notification.showInformative('Please Add the Total Installment   ', 'Installment !')
        return
    elif (amount == '' or int(amount) < 1 ):
        notification.showInformative('Please Select The Installment Amount  ', 'Installment Amount !')
        return

    self.schemeConformDialog = QtWidgets.QDialog()
    self.scui = Ui_schemeConformDialog()
    self.scui.schemeConformSetupUi(self.schemeConformDialog)
    self.schemeConformDialog.show()
    self.scui.setSchemeField(scheme, startDate, endDate, dueDate, installments, amount, remarks)


def confirmAddScheme(scheme, startDate, endDate, dueDate, installments, amount, remarks):
    id = 'NULL'
    startDate = dateTime.getStartDateWithoutTimes(startDate)
    endDate = dateTime.getStartDateWithoutTimes(endDate)
    createdBy = globalVariables.Variables._userId
    schemeDL.insertScheme(id,scheme,startDate,endDate,dueDate,installments,amount,remarks,createdBy)


def getAllSchemes():
    result = schemeDL.getAllSchemesFromDB()
    return result

def deleteScheme(self,schemeId,title):
    confirm = notification.confirmPopup('Do You want to Delete "'+str(title)+'" Parmanently ', 'Deleting Scheme')
    if(confirm == 'OK'):
        schemeDL.updateScheme(schemeId,'','','','','','','',1)
        return
    else:
        return

