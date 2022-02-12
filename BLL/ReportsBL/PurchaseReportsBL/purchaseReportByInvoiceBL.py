from Forms.Reports.PurchaseReports.purchaseReportByInvoice import *
from DLL.MiscDL import billDL
from DLL.PurchaseDL import purchaseDL
from Services.NotificationService import notification




################################## open Forms from main Form ####################################################
def openPurchaseReportByInvoiceForm(self):
    self.purchaseReportByInvoiceWindow = QtWidgets.QMainWindow()
    self.ui = Ui_purchaseReportByInvoiceWindow()
    self.ui.purchaseReportByInvoiceetupUi(self.purchaseReportByInvoiceWindow)
    self.ui.init()
    self.purchaseReportByInvoiceWindow.showMaximized()

################################## End Forms from main Form #####################################################



def validateBillInvoice(invoice,billType):
    if(invoice == ''):
        notification.showPopup('Please Enter the Invoice No. ', 'Invoice Missing!')
        return
    else:
        result = billDL.getBillByInvoice(invoice,billType)
        return result

def validatePurchaseInvoice(invoice,billType):
    if(invoice == ''):
        notification.showPopup('Please Enter the Invoice No. ', 'Invoice Missing!')
        return
    else:
        result = purchaseDL.getPurchaseByInvoice(invoice, billType)
        return result
