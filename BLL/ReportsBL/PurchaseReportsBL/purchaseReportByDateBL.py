from Forms.Reports.PurchaseReports.purchaseReportByDate import *

from DLL.ReportsDL.PurchaseReportsDL import purchaseReportByDateDL
from DLL.MiscDL import billDL

################################## open Forms from main Form ####################################################
def openPurchaseReportByDateForm(self):
    self.purchaseReportByDateWindow = QtWidgets.QMainWindow()
    self.prui = Ui_purchaseReportByDateWindow()
    self.prui.purchaseReportByDateSetupUi(self.purchaseReportByDateWindow)
    self.prui.init()
    self.purchaseReportByDateWindow.showMaximized()

################################## End Forms from main Form #####################################################


def validatePurchaseReportDates(startDate, endDate):
    result = purchaseReportByDateDL.getPurchasesReportByDates(startDate, endDate)
    return result

def validatePurchaseBillByDate(startDate, endDate, billType):
    result = billDL.getBillByDate(startDate, endDate, billType)
    return result
