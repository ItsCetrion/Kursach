from TransportCompany.Entities.Client import Client
from TransportCompany.Repositories.ClientRepository import ClientRepository
from TransportCompany.View.ViewRegistration import ViewRigistration
from TransportCompany.Model.ModelRegistration import ModelRegistration
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordStats
from PyQt5 import QtWidgets
import sys
import hashlib


class ControllerRegister:
    def __init__(self):
        self.__model = ModelRegistration()
        self.__view = ViewRigistration()
        self.__SettingsUI()

        self.__view.pushButton_SignUp.clicked.connect(self.__functionsSignUp)
        self.__view.pushButton_Back.clicked.connect(self.__functionsBack)
        self.__view.lineEdit_FirstName.textChanged.connect(self.__ColorGrenFirstName)
        self.__view.lineEdit_LastName.textChanged.connect(self.__ColorGrenLastName)
        self.__view.lineEdit_Patronymic.textChanged.connect(self.__ColorGrenPatronymic)
        self.__view.lineEdit_NumberPhone.textChanged.connect(self.__CheckNumderPhone)
        self.__view.lineEdit_Email.textChanged.connect(self.__CheckEmail)
        self.__view.lineEdit_Password.textChanged.connect(self.__CheckPassword)
        self.__view.lineEdit_AgainPassword.textChanged.connect(self.__CheckAgainPassword)

    def __SettingsUI(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__RegisterWindow = QtWidgets.QMainWindow()
        ui = self.__view
        ui.setupUi(self.__RegisterWindow)

    def RunViewRegister(self):
        self.__RegisterWindow.show()

    def __ColorGrenFirstName(self):
        self.__view.lineEdit_FirstName.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                   "border-radius: 10px")

    def __ColorGrenLastName(self):
        self.__view.lineEdit_LastName.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                  "border-radius: 10px")

    def __ColorGrenPatronymic(self):
        self.__view.lineEdit_Patronymic.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                    "border-radius: 10px")

    def __CheckNumderPhone(self):
        if self.__model.CheckPhone(self.__view.lineEdit_NumberPhone.text()) or len(self.__view.lineEdit_NumberPhone.text()) < 11:
            self.__view.lineEdit_NumberPhone.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                    "border-radius: 10px")
        else:
            self.__view.lineEdit_NumberPhone.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                    "border-radius: 10px")

    def __CheckEmail(self):
        try:
            email = self.__view.lineEdit_Email.text()
            validate_email(email, check_deliverability=False)
        except EmailNotValidError:
            self.__view.lineEdit_Email.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                    "border-radius: 10px")
        else:
            if self.__model.CheckEmail(email):
                self.__view.lineEdit_Email.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                        "border-radius: 10px")
            else:
                self.__view.lineEdit_Email.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                        "border-radius: 10px")

    def __CheckPassword(self):
        password = self.__view.lineEdit_Password.text()
        if len(password) == 0:
            self.__view.lineEdit_Password.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                 "border-radius: 10px")
        else:
            stats = PasswordStats(password)
            if 0 <= stats.strength() <= 0.2:
                self.__view.lineEdit_Password.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                     "border-radius: 10px")
            elif 0.2 < stats.strength() <= 0.66:
                self.__view.lineEdit_Password.setStyleSheet("background-color: rgb(255, 170, 0);"
                                                     "border-radius: 10px")
            elif 0.66 < stats.strength() <= 0.99:
                self.__view.lineEdit_Password.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                     "border-radius: 10px")

    def __CheckAgainPassword(self):
        if self.__view.lineEdit_AgainPassword.text() != self.__view.lineEdit_Password.text():
            self.__view.lineEdit_AgainPassword.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                      "border-radius: 10px")
        else:
            self.__view.lineEdit_AgainPassword.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                      "border-radius: 10px")

    def __functionsSignUp(self):
        if self.__CheckColor():
            user = Client()
            user.FirstName = self.__view.lineEdit_FirstName.text()
            user.LastName = self.__view.lineEdit_LastName.text()
            user.Patronymic = self.__view.lineEdit_Patronymic.text()
            user.NumberPhone = self.__view.lineEdit_NumberPhone.text()
            user.Email = self.__view.lineEdit_Email.text()
            password = self.__view.lineEdit_Password.text()
            user.Password = hashlib.md5(password.encode()).hexdigest()
            self.__model.UserRigistation(user)
            self.__view.message("Информация", "Успешно")
            self.__functionsBack()
        else:
            self.__view.message("Информация", "Не все поля заполнены корректно или вовсе незаполненны")

    def __CheckColor(self):
        for LineEdit in self.__RegisterWindow.findChildren(QtWidgets.QLineEdit):
            hexcolor = LineEdit.palette().color(LineEdit.backgroundRole()).name()
            if hexcolor == "#aa0000" or hexcolor == "#ffffff" or len(LineEdit.text()) < 2:
                return False
        else:
            return True

    def __functionsBack(self):
        from TransportCompany.Controller.ControllerLogin import ControllerLogin
        self.ControllerLogin = ControllerLogin()
        self.__RegisterWindow.close()
        self.ControllerLogin.RunViewLogin()