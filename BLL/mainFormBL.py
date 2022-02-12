
from Forms.mainForm import *
from Globals import globalVariables

from DLL.AccountsDL import accountDL
from DLL.MiscDL import transectionDL,billDL
from Services.MiscService import dateTime


def openMainForm(self):
    self.mainForm = QtWidgets.QMainWindow()
    self.ui = Ui_mainForm()
    self.ui.mainFormSetupUi(self.mainForm)
    self.ui.init()
    self.mainForm.showMaximized()

def setDashboard():
    purchaseType = globalVariables.Variables._purchase
    saleType = globalVariables.Variables._sale

    startDate = dateTime.getCurrentStartDate()
    endDate = dateTime.getCurrentEndDate()

    sale = billDL.getCurrentBill(saleType,startDate,endDate)
    purchase = billDL.getCurrentBill(purchaseType,startDate,endDate)
    cashIn = transectionDL.getCurrentCashIn(startDate,endDate)
    cashOut = transectionDL.getCurrentCashOut(startDate,endDate)



    return sale, purchase, cashIn, cashOut
