from Forms.Reports.SaleReports.saleReportByDate import *

from DLL.ReportsDL.SaleReportsDL import saleReportByDateDL
from DLL.MiscDL import billDL





################################## open Forms from main Form ####################################################
def openSaleReportByDateForm(self):
    self.saleReportByDateWindow = QtWidgets.QMainWindow()
    self.srui = Ui_saleReportByDateWindow()
    self.srui.saleReportByDateSetupUi(self.saleReportByDateWindow)
    self.srui.init()
    self.saleReportByDateWindow.showMaximized()
################################## End Forms from main Form #####################################################


def validateSaleReportDates(startDate, endDate):
    result = saleReportByDateDL.getSaleReportByDates(startDate, endDate)
    return result

def validateSaleBillByDate(startDate, endDate, billType):
    result = billDL.getBillByDate(startDate, endDate, billType)
    return result
