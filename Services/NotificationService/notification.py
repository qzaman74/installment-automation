from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Globals import globalVariables

def showRight(message,title):

    msgBox = QMessageBox()
    #msgBox.move(1150,600)
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
    msgBox.setWindowIcon(QtGui.QIcon(windowIcon))

    timeout = 1500

    def doNothing():
        msgBox.close()
    QtCore.QTimer().singleShot(timeout, doNothing)
    msgBox.exec_()



def showWarning(message,title):

    msgBox = QMessageBox()
    #msgBox.move(1150,600)
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
    msgBox.setWindowIcon(QtGui.QIcon(windowIcon))

    timeout = 1500

    def doNothing():
        msgBox.close()
    QtCore.QTimer().singleShot(timeout, doNothing)
    msgBox.exec_()


def showInformative(message,title):

    msgBox = QMessageBox()
    #msgBox.move(1150,600)
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
    msgBox.setWindowIcon(QtGui.QIcon(windowIcon))

    timeout = 2000

    def doNothing():
        msgBox.close()
    QtCore.QTimer().singleShot(timeout, doNothing)
    msgBox.exec_()

def showPopup(message,title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
    msgBox.setWindowIcon(QtGui.QIcon(windowIcon))
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.setEscapeButton(QMessageBox.Close)
    msgBox.exec_()

def confirmPopup(message,title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)

    windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
    msgBox.setWindowIcon(QtGui.QIcon(windowIcon))
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.setEscapeButton(QMessageBox.Close)

    result = msgBox.exec_()
    if result == QMessageBox.Ok:
        return 'OK'

    # self.lbl_image = QtWidgets.QLabel(self.centralwidget)
    # self.lbl_image.setGeometry(QtCore.QRect(90, 500, 200, 140))
    # self.lbl_image.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon + 'invoice.png'))
    # self.lbl_image.setScaledContents(True)
    # self.lbl_image.setObjectName("lbl_image")


def showWaitingPopUp():

    msg = QMessageBox()
    # create Label
    msg.setIconPixmap(QtGui.QPixmap(globalVariables.Variables._icon + 'waiting.gif').scaledToWidth(40))
    icon_label = msg.findChild(QtWidgets.QLabel, "qt_msgboxex_icon_label")
    movie = QtGui.QMovie(globalVariables.Variables._icon + 'waiting.gif')
    # avoid garbage collector
    setattr(msg, 'icon_label', movie)
    icon_label.setMovie(movie)
    movie.start()
    msg.setModal(False)

    msg.show()
    msg.exec_()