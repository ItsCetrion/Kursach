
from PyQt5 import QtCore, QtGui, QtWidgets
from TransportCompany.Login import Login
from PyQt5.QtWidgets import QMessageBox



class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("Ui_LoginWindow")
        LoginWindow.resize(552, 423)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_Login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Login.setGeometry(QtCore.QRect(50, 110, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_Login.setFont(font)
        self.lineEdit_Login.setObjectName("lineEdit_Login")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(50, 160, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_Password.setFont(font)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.label_Logo = QtWidgets.QLabel(self.centralwidget)
        self.label_Logo.setGeometry(QtCore.QRect(250, 20, 71, 71))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap("C:/Users/79951/Documents/GitHub/Kursach/TransportCompany/Resources/Logo.png"))
        self.label_Logo.setObjectName("label_Logo")
        self.pushButton_SignIn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SignIn.setGeometry(QtCore.QRect(50, 210, 471, 28))
        self.pushButton_SignIn.setObjectName("pushButton_SignIn")
        self.pushButton_SignUp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SignUp.setGeometry(QtCore.QRect(100, 250, 371, 28))
        self.pushButton_SignUp.setObjectName("pushButton_SignUp")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 26))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.pushButton_SignIn.clicked.connect(self.FunctionSignIn)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_Login.setPlaceholderText(_translate("MainWindow", "Email"))
        self.lineEdit_Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_SignIn.setText(_translate("MainWindow", "Sign in"))
        self.pushButton_SignUp.setText(_translate("MainWindow", "Sign up"))

    @staticmethod
    def message(title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()

    def FunctionSignIn(self):
        email = self.lineEdit_Login.text()
        password = self.lineEdit_Password.text()
        if Login(email, password).CheckUserInDB():
            self.message("Информация", "Вы успешно вошли")
        else:
            self.message("Информация", "Вы не верно ввели логин или пароль")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())