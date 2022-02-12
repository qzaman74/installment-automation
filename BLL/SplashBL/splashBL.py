from Splash.splash import *
from Login.login import *

def openSplashScreen(self):
    self.MainWindow = QtWidgets.QMainWindow()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self.MainWindow)
    self.MainWindow.show()
    self.MainWindow.raise_()