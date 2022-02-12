from Forms.Reports.StockReport.stocklevelReport import *
from DLL.MiscDL import stockDL


################################## open Forms from main Form ####################################################
def openStockLevelReportForm(self):
    self.stockLevelWindow = QtWidgets.QMainWindow()
    self.ui = Ui_stockLevelWindow()
    self.ui.stockLevelSetupUi(self.stockLevelWindow)
    self.ui.init()
    self.stockLevelWindow.show()

################################## End Forms from main Form #####################################################

def getStockLevel():
    result = stockDL.getStockLevelFromDB()
    return result