from TransportCompany.View.ViewLogin import ViewLogin
from TransportCompany.Model.ModelLogin import ModelLogin
from TransportCompany.Controller.ControllerRegistration import ControllerRegister
from TransportCompany.Controller.Admin.ControllerWindowApplication import ControllerWindowApplication
from PyQt5 import QtWidgets
import hashlib
import sys


class ControllerLogin:
    def __init__(self):
        self.model = ModelLogin()
        self.view = ViewLogin()
        self.ControllerReg = ControllerRegister()
        self.WindowApplication = ControllerWindowApplication()
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
        role = self.model.GetUserRole(email, password)
        if role != '':
            self.Login(role)
        else:
            self.view.message("Информация", "Вы не верно ввели логин или пароль")

    def Login(self, role):
        self.LoginWindow.close()
        if role == "Администратор":
            self.WindowApplication.RunViewWindowApplication()

    def FunctionSignUp(self):
        self.LoginWindow.close()                      # Понять как полноценно уничтожить окно
        self.ControllerReg.RunViewRegister()

