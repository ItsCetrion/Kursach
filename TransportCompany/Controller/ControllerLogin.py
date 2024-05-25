from TransportCompany.View.ViewLogin import ViewLogin
from TransportCompany.Model.ModelLogin import ModelLogin
from TransportCompany.Controller.ControllerRegistration import ControllerRegister
from TransportCompany.Controller.Admin.ControllerWindowApplication import ControllerWindowApplication
from TransportCompany.Controller.Client.ControllerApplicationWindow import ControllerApplicationWindow
from TransportCompany.Entities.Client import Client
from TransportCompany.Entities.Driver import Driver
from TransportCompany.Entities.Administrator import Administrator
from TransportCompany.Entities.Accountant import Accountant
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

        self.view.lineEdit_Login.setText("test@mail.ru") #Потом удалить
        self.view.lineEdit_Password.setText("1234567890") #Потом удалить

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
        user = self.model.GetEntity(email, password)
        if len(user) == 0:
            self.view.message("Информация", "Вы не верно ввели логин или пароль")
        else:
            InfoEntity = [*(self.model.GetEntity(email, password)[0])]
            self.Login(InfoEntity)

    def Login(self, InfoEntity):
        id = InfoEntity[0]
        role = InfoEntity[-1]
        if role == "Администратор":
            entity = self.FillingEntity(self.model.GetAdmin(id), Administrator)
            self.WindowApplication = ControllerWindowApplication() #передать сущность администратор
            self.WindowApplication.RunViewWindowApplication()
            self.LoginWindow.close()
        elif role == "Клиент":
            entity = self.FillingEntity([*(self.model.GetClient(id)[0])], Client)
            self.ApplicationWindow = ControllerApplicationWindow(entity)
            self.ApplicationWindow.RunViewApplicationWindow()
            self.LoginWindow.close()

    def FillingEntity(self, InfoEntity: list, Entity : [Client, Driver, Administrator, Accountant]):
        entity = Entity()
        if isinstance(entity, (Accountant, Driver, Administrator, Client)):
            entity.ID = InfoEntity[0]
            entity.FirstName = InfoEntity[1]
            entity.LastName = InfoEntity[2]
            entity.Patronymic = InfoEntity[3]
            entity.NumberPhone = InfoEntity[4]
            entity.Email = InfoEntity[5]
            entity.Password = InfoEntity[6]
            if isinstance(entity, (Accountant, Driver)):
                entity.Age = InfoEntity[6]
                entity.Experience = InfoEntity[7]
            if isinstance(entity, Driver):
                entity.IdOrderClient = InfoEntity[8]
                entity.Condition = InfoEntity[9]
            entity.Role = InfoEntity[-1]
        return entity

    def FunctionSignUp(self):
        self.LoginWindow.close()                      # Понять как полноценно уничтожить окно
        self.ControllerReg.RunViewRegister()

