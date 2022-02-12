from Forms.ActivationKey.activationForm import *

from Services.NotificationService import notification
from DLL.ActivationKeyDL import activationDL
from Services.CloseServices import formClose


def openActivationForm(self):
    self.activationDialog = QtWidgets.QDialog()
    self.akui = Ui_activationDialog()
    self.akui.activationSetupUi(self.activationDialog)
    self.akui.init()
    self.activationDialog.show()


def validateActivationKey(key, key1, key2):
    if(key == '' or key1 == '' or key2 == ''):
        notification.showInformative("Please Enter key","Missing Key")
        return
    elif(len(key) > 4 or len(key1) > 5 or len(key2) > 4):
        notification.showInformative("Please Enter Complete key","Missing Key")
        return

    expiryKey = key + key1 + key2
    activationDL.updateActivationKey(expiryKey)
    formClose.Close._closeActivationForm()
