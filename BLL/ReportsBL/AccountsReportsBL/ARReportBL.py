from Forms.Reports.AccountsReport.ARReport import *
from DLL.AccountsDL import accountDL



################################## open Forms from main Form ####################################################
def openARReportForm(self):
    self.ARReportWindow = QtWidgets.QMainWindow()
    self.arui = Ui_ARReportWindow()
    self.arui.ARReportSetupUi(self.ARReportWindow)
    self.arui.init()
    self.ARReportWindow.showMaximized()

################################## End Forms from main Form #####################################################

def getAccountsReceivable():
    result = accountDL.getAccountsReceivableFromDB()
    return result