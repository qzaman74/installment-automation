from Forms.Reports.SaleReports.saleReportByInvoice import *
from DLL.MiscDL import billDL
from DLL.SaleDL import saleDL
from Services.NotificationService import notification




################################## open Forms from main Form ####################################################
def openSaleReportByInvoiceForm(self):
    self.saleReportByInvoiceWindow = QtWidgets.QMainWindow()
    self.ui = Ui_saleReportByInvoiceWindow()
    self.ui.saleReportByInvoiceSetupUi(self.saleReportByInvoiceWindow)
    self.ui.init()
    self.saleReportByInvoiceWindow.showMaximized()

################################## End Forms from main Form #####################################################



def validateBillInvoice(invoice,billType):
    if(invoice == ''):
        notification.showInformative('Please Enter the Invoice No. ', 'Invoice Missing!')
        return
    else:
        result = billDL.getBillByInvoice(invoice,billType)
        return result

def validateSaleInvoice(invoice,billType):
    if(invoice == ''):
        notification.showInformative('Please Enter the Invoice No. ', 'Invoice Missing!')
        return
    else:
        result = saleDL.getSaleByInvoice(invoice, billType)
        return result
