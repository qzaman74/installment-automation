from Login.login import *


def openLoginForm(self):
    self.loginDialog = QtWidgets.QDialog()
    self.ui = Ui_loginDialog()
    self.ui.loginSetupUi(self.loginDialog)
    self.loginDialog.show()