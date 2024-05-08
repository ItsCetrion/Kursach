from TransportCompany.Entities.User import User
from TransportCompany.UserRepository.UserRepository import UserRepository
from TransportCompany.View.ViewRegistration import Ui_RegWindow
from TransportCompany.Model.ModelRegistration import ModelRegistration
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordStats
from PyQt5 import QtWidgets
import sys
import hashlib


class ControllerRegister:
    def __init__(self):
        self.model = ModelRegistration()
        self.view = Ui_RegWindow()
        self.SettingsUI()
        self.view.pushButton_SignUp.clicked.connect(self.functionsSignUp)
        self.view.pushButton_Back.clicked.connect(self.functionsBack)
        self.view.lineEdit_FirstName.textChanged.connect(self.ColorGrenFirstName)
        self.view.lineEdit_LastName.textChanged.connect(self.ColorGrenLastName)
        self.view.lineEdit_Patronymic.textChanged.connect(self.ColorGrenPatronymic)
        self.view.lineEdit_NumberPhone.textChanged.connect(self.CheckNumderPhone)
        self.view.lineEdit_Email.textChanged.connect(self.CheckEmail)
        self.view.lineEdit_Password.textChanged.connect(self.CheckPassword)
        self.view.lineEdit_AgainPassword.textChanged.connect(self.CheckAgainPassword)

    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.RegisterWindow = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.RegisterWindow)

    def RunViewRegister(self):
        self.RegisterWindow.show()
        # sys.exit(self.app.exec_())

    def ColorGrenFirstName(self):
        self.view.lineEdit_FirstName.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                   "border-radius: 10px")

    def ColorGrenLastName(self):
        self.view.lineEdit_LastName.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                  "border-radius: 10px")

    def ColorGrenPatronymic(self):
        self.view.lineEdit_Patronymic.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                    "border-radius: 10px")

    def CheckNumderPhone(self):
        if self.model.CheckPhone(self.view.lineEdit_NumberPhone.text()) or len(self.view.lineEdit_NumberPhone.text()) < 11:
            self.view.lineEdit_NumberPhone.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                    "border-radius: 10px")
        else:
            self.view.lineEdit_NumberPhone.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                    "border-radius: 10px")

    def CheckEmail(self):
        try:
            email = self.view.lineEdit_Email.text()
            validate_email(email, check_deliverability=False)
        except EmailNotValidError:
            self.view.lineEdit_Email.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                    "border-radius: 10px")
        else:
            if UserRepository.CheckEmail(email):
                self.view.lineEdit_Email.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                        "border-radius: 10px")
            else:
                self.view.lineEdit_Email.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                        "border-radius: 10px")

    def CheckPassword(self):
        password = self.view.lineEdit_Password.text()
        if len(password) == 0:
            self.view.lineEdit_Password.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                 "border-radius: 10px")
        else:
            stats = PasswordStats(password)
            if 0 <= stats.strength() <= 0.2:
                self.view.lineEdit_Password.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                     "border-radius: 10px")
            elif 0.2 < stats.strength() <= 0.66:
                self.view.lineEdit_Password.setStyleSheet("background-color: rgb(255, 170, 0);"
                                                     "border-radius: 10px")
            elif 0.66 < stats.strength() <= 0.99:
                self.view.lineEdit_Password.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                     "border-radius: 10px")

    def CheckAgainPassword(self):
        if self.view.lineEdit_AgainPassword.text() != self.view.lineEdit_Password.text():
            self.view.lineEdit_AgainPassword.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                      "border-radius: 10px")
        else:
            self.view.lineEdit_AgainPassword.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                      "border-radius: 10px")

    def functionsSignUp(self):
        if self.CheckColor():
            user = User()
            user.FirstName = self.view.lineEdit_FirstName.text()
            user.LastName = self.view.lineEdit_LastName.text()
            user.Patronymic = self.view.lineEdit_Patronymic.text()
            user.NumberPhone = self.view.lineEdit_NumberPhone.text()
            user.Email = self.view.lineEdit_Email.text()
            password = self.view.lineEdit_Password.text()
            user.Password = hashlib.md5(password.encode()).hexdigest()
            user.Email = self.view.lineEdit_Email.text()
            user.Role = "Клиент"
            self.model.UserRigistation(user)
            self.view.message("Информация", "Успешно")
            self.functionsBack()
        else:
            self.view.message("Информация", "Не все поля заполнены корректно или вовсе незаполненны")

    def CheckColor(self):
        for LineEdit in self.RegisterWindow.findChildren(QtWidgets.QLineEdit):
            hexcolor = LineEdit.palette().color(LineEdit.backgroundRole()).name()
            if hexcolor == "#aa0000" or hexcolor == "#ffffff" or len(LineEdit.text()) < 2:
                return False
        else:
            return True

    def functionsBack(self):
        from TransportCompany.Controller.ControllerLogin import ControllerLogin
        self.ControllerLogin = ControllerLogin()
        self.RegisterWindow.close()
        self.ControllerLogin.RunViewLogin()