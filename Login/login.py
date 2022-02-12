
from Services.NotificationService import notification
from Services.DBService import DBConnection
from Services.ResetServices import formReset

from BLL import mainFormBL

from Globals import globalVariables
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginDialog(object):

    def onLogin(self):
        mainFormBL.openMainForm(self)
        formReset.Reset._closeLogin()


    # def onLogin(self):
    #
    #     if(self.le_userName.text() == ''):
    #         notification.showRight('Empty Username \n Please Try Again  ', 'Username')
    #         return
    #     elif(self.le_password.text() == ''):
    #         notification.showRight('Empty Password \n Please Try Again  ', 'Password')
    #         return
    #     else:
    #         userName = self.le_userName.text()
    #         password = self.le_password.text()
    #
    #         connection = DBConnection.DBConnectivity._connection
    #         qry = " SELECT * FROM account WHERE user_name=? AND password=? AND is_deleted=0 "
    #         result = connection.execute(qry,( userName, password))
    #         data = result.fetchall()
    #         if(len(data)> 0 ):
    #             for x in data:
    #                 self.userID = x[0]
    #                 globalVariables._userId = x[0]
    #
    #             mainFormBL.openMainForm(self)
    #             formReset.Reset._closeLogin()
    #
    #         else:
    #             notification.showRight("InCorrect LogIn","Try Again..!")

    def onEnterUserName(self):
        if(self.le_userName.text() != ''):
            self.le_password.setFocus()


    def loginSetupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(398, 304)
        # loginDialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        # loginDialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        formReset.Reset._closeLogin = loginDialog.accept

        windowIcon = QtGui.QPixmap(globalVariables.Variables._icon+'logo.png')
        loginDialog.setWindowIcon(QtGui.QIcon(windowIcon))

        loginDialog.setStyleSheet(open(globalVariables.Variables._style,'r').read())
        loginDialog.setAutoFillBackground(True)

        self.lbl_backgroundImage = QtWidgets.QLabel(loginDialog)
        self.lbl_backgroundImage.setGeometry(QtCore.QRect(5, 5, 395, 300))
        self.lbl_backgroundImage.setObjectName("lbl_backgroundImage")

        self.lbl_backgroundImage = QtWidgets.QLabel(loginDialog)
        self.lbl_backgroundImage.setGeometry(QtCore.QRect(5, 5, 395, 300))
        self.lbl_backgroundImage.setText("")
        self.lbl_backgroundImage.setPixmap(QtGui.QPixmap(globalVariables.Variables._icon+'main.jpg'))
        self.lbl_backgroundImage.setScaledContents(True)
        self.lbl_backgroundImage.setObjectName("lbl_backgroundImage")

        self.le_userName = QtWidgets.QLineEdit(loginDialog)
        self.le_userName.setGeometry(QtCore.QRect(150, 80, 200, 26))
        self.le_userName.setMaxLength(32)
        self.le_userName.setObjectName("le_userName")
        self.le_userName.returnPressed.connect(self.onEnterUserName)

        self.le_password = QtWidgets.QLineEdit(loginDialog)
        self.le_password.setGeometry(QtCore.QRect(150, 110, 200, 26))
        self.le_password.setMaxLength(32)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.le_password.returnPressed.connect(self.onLogin)

        self.btn_logIn = QtWidgets.QPushButton(loginDialog)
        self.btn_logIn.setGeometry(QtCore.QRect(150, 160, 100, 26))
        self.btn_logIn.setObjectName("btn_logIn")
        self.btn_logIn.clicked.connect(self.onLogin)
        # self.btn_logIn.clicked.connect(loginDialog.accept)

        self.btn_cancel = QtWidgets.QPushButton(loginDialog)
        self.btn_cancel.setGeometry(QtCore.QRect(250, 160, 100, 26))
        self.btn_cancel.setObjectName("btn_cancel")
        # self.btn_cancel.clicked.connect(loginDialog.reject)

        self.label = QtWidgets.QLabel(loginDialog)
        self.label.setGeometry(QtCore.QRect(60, 80, 91, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(loginDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 91, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

    def retranslateUi(self, loginDialog):
        _translate = QtCore.QCoreApplication.translate
        loginDialog.setWindowTitle(_translate("loginDialog", "Log In"))
        self.btn_logIn.setText(_translate("loginDialog", "LogIn"))
        self.btn_cancel.setText(_translate("loginDialog", "Cancel"))
        self.label.setText(_translate("loginDialog", "User Name"))
        self.label_2.setText(_translate("loginDialog", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginDialog = QtWidgets.QDialog()
    ui = Ui_loginDialog()
    ui.loginSetupUi(loginDialog)
    loginDialog.show()
    sys.exit(app.exec_())

