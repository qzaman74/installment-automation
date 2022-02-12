from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import os, sys, time
from Globals import globalVariables
from Login.login import *

class ThreadProgress(QThread):
    mysignal = pyqtSignal(int)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
    def run(self):
        i = 0
        while i<101:
            time.sleep(0.000000000000003)
            self.mysignal.emit(i)
            i += 1

FROM_SPLASH,_ = loadUiType(os.path.join(os.path.dirname(__file__),"splash.ui"))
        
class Splash(QMainWindow, FROM_SPLASH):
    def __init__(self, parent = None):
        super(Splash, self).__init__(parent)
        QMainWindow.__init__(self)

        self.setupUi(self)
        self.splash_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'splash.png').scaled(450, 300))
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progress)
        progress.start()
        
    @pyqtSlot(int)
    def progress(self, i):
        self.progressBar.setValue(i)
        if i == 0:
            self.lbl_splash.setText("Collecting Data ")
        if i == 25:
            self.lbl_splash.setText("Setting up Software ")
        if i == 50:
            self.lbl_splash.setText("Collecting User Information")
        if i == 75:
            self.lbl_splash.setText("Starting Software")
        if i == 100:

            self.hide()
            self.loginDialog = QtWidgets.QDialog()
            self.ui = Ui_loginDialog()
            self.ui.loginSetupUi(self.loginDialog)
            self.loginDialog.show()


def splashMain():
    app = QtWidgets.QApplication(sys.argv)
    window = Splash()
    window.show()
    app.exec_()

if __name__ == '__main__':
    try:
        splashMain()
    except Exception as why:
        print(why)



