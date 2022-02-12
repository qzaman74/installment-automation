from Splash import splashForm
from BLL.ActivationKeyBL import activationBL
from BLL.LoginBL import loginBL
from PyQt5 import QtWidgets
from DLL.MiscDL import expiryDL
from Globals import globalVariables,config
from Services.MiscService import gernateKey
from Services.NotificationService import notification
from Services.RecallServices import formRecall
from Services.MiscService import mac


class Main(object):



    def openSplashScreen(self):
        # loginBL.openLoginForm(self)
        # splashBL.openSplashScreen(self)
        splashForm.splashMain()


    def openActivationForm(self):
        formRecall.Recall._activationForm = Main
        activationBL.openActivationForm(self)

    def checkValidation(self):
        expiryDate = gernateKey.decodeKey(expiryDL.getExpiryFromDB()[0])
        currentDate = float(globalVariables.Variables._createdOn)
        localMac = mac.getMac()

        try:
            if (config.Config._mac != localMac):
                notification.showPopup("Your PC is not registered !", "Unregistered Software !")
                sys.exit()


            elif not (currentDate <= expiryDate):
                notification.showPopup("Your Software Has Been Expired !", "Software Expired !")
                self.openActivationForm()


            else:
                try:
                    self.openSplashScreen()

                except(Exception):
                    sys.exit()

        except(Exception):
            notification.showPopup("Invalid Key Found !", "Software Expired !")
            self.openActivationForm()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.checkValidation()
    sys.exit(app.exec_())