from TransportCompany.View.ViewLogin import ViewLogin
from TransportCompany.Model.ModelLogin import ModelLogin
from TransportCompany.Controller.ControllerRegistration import ControllerRegister
from PyQt5 import QtWidgets
import hashlib
import sys


class ControllerLogin:
    def __init__(self):
        self.model = ModelLogin()
        self.view = ViewLogin()
        self.ControllerReg = ControllerRegister()
        self.SettingsUI()
        self.view.pushButton_SignIn.clicked.connect(self.FunctionSignIn)
        self.view.pushButton_SignUp.clicked.connect(self.FunctionSignUp)

    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.LoginWindow = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.LoginWindow)
    def RunViewLogin(self):
        self.LoginWindow.show()

    def StartProgram(self):
        sys.exit(self.app.exec_())

    def FunctionSignIn(self):
        email = self.view.lineEdit_Login.text()
        password = self.view.lineEdit_Password.text()
        password = hashlib.md5(password.encode()).hexdigest()
        if self.model.CheckUserInDB(email, password):
            self.view.message("Информация", "Вы успешно вошли")
        else:
            self.view.message("Информация", "Вы не верно ввели логин или пароль")

    def FunctionSignUp(self):
        self.LoginWindow.close()                      # Понять как полноценно уничтожить окно
        self.ControllerReg.RunViewRegister()

