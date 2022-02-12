from Forms.Reports.AccountsReport.APReport import *
from DLL.AccountsDL import accountDL



################################## open Forms from main Form ####################################################
def openAPReportForm(self):
    self.APReportWindow = QtWidgets.QMainWindow()
    self.apui = Ui_APReportWindow()
    self.apui.APReportSetupUi(self.APReportWindow)
    self.apui.init()
    self.APReportWindow.showMaximized()

################################## End Forms from main Form #####################################################

def getAccountsPayable():
    result = accountDL.getAccountsPayableFromDB()
    return result