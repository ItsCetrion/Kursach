from TransportCompany.View.ViewLogin import ViewLogin
from TransportCompany.Model.ModelLogin import ModelLogin
from TransportCompany.Controller.ControllerRegistration import ControllerRegister
from TransportCompany.Controller.Admin.ControllerWindowApplication import ControllerWindowApplication
from TransportCompany.Controller.Client.ControllerApplicationWindow import ControllerApplicationWindow
from TransportCompany.Controller.Driver.ControllerMainWindow import ControllerMainWindow
from TransportCompany.Controller.Accountant.ControllerListDeliveredOrders import ControllerListDeliveredOrders
from TransportCompany.Entities.Client import Client
from TransportCompany.Entities.Driver import Driver
from TransportCompany.Entities.Administrator import Administrator
from TransportCompany.Entities.Accountant import Accountant
from PyQt5 import QtWidgets
import hashlib
import sys


class ControllerLogin:
    def __init__(self):
        self.__model = ModelLogin()
        self.__view = ViewLogin()
        self.__ControllerReg = ControllerRegister()
        self.__SettingsUI()
        self.__view.pushButton_SignIn.clicked.connect(self.__FunctionSignIn)
        self.__view.pushButton_SignUp.clicked.connect(self.__FunctionSignUp)

        self.__view.lineEdit_Login.setText("test@mail.ru") #Потом удалить
        self.__view.lineEdit_Password.setText("1234567890") #Потом удалить

    def __SettingsUI(self) -> None:
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__LoginWindow = QtWidgets.QMainWindow()
        ui = self.__view
        ui.setupUi(self.__LoginWindow)

    def RunViewLogin(self) -> None:
        self.__LoginWindow.show()

    def StartProgram(self) -> None:
        sys.exit(self.__app.exec_())

    def __FunctionSignIn(self) -> None:
        email = self.__view.lineEdit_Login.text()
        password = self.__view.lineEdit_Password.text()
        if password == "":
            password = "Null"
        else:
            password = hashlib.md5(password.encode()).hexdigest()
        user = self.__model.GetEntity(email, password)
        if len(user) == 0:
            self.__view.message("Информация", "Вы не верно ввели логин или пароль")
        else:
            InfoEntity = [*(self.__model.GetEntity(email, password)[0])]
            self.__Login(InfoEntity)

    def __Login(self, InfoEntity) -> None:
        id = InfoEntity[0]
        role = InfoEntity[-1]
        if role == "Администратор":
            entity = self.__FillingEntity(self.__model.GetAdmin(id), Administrator)
            self.WindowApplication = ControllerWindowApplication() #передать сущность администратор
            self.WindowApplication.RunViewWindowApplication()
            self.__LoginWindow.close()
        elif role == "Клиент":
            entity = self.__FillingEntity([*(self.__model.GetClient(id)[0])], Client)
            self.ApplicationWindow = ControllerApplicationWindow(entity)
            self.ApplicationWindow.RunViewApplicationWindow()
            self.__LoginWindow.close()
        elif role == "Водитель":
            entity = self.__FillingEntity([*(self.__model.GetDriver(id)[0])], Driver)
            self.MainWindow = ControllerMainWindow(entity)
            self.MainWindow.RunMainWindow()
            self.__LoginWindow.close()
        elif role == "Бухгалтер":
            entity = self.__FillingEntity([*(self.__model.GetAccountant(id)[0])], Accountant)
            self.ListDeliveredOrders = ControllerListDeliveredOrders(entity)
            self.ListDeliveredOrders.RunViewListDeliveredOrders()
            self.__LoginWindow.close()

    def __FillingEntity(self, InfoEntity: list, Entity : [Client, Driver, Administrator, Accountant]) -> [Client, Driver, Administrator, Accountant]:
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
                entity.Age = InfoEntity[7]
                entity.Experience = InfoEntity[8]
            if isinstance(entity, Driver):
                entity.IdOrderClient = InfoEntity[9]
                entity.Condition = InfoEntity[10]
            entity.Role = InfoEntity[-1]
        return entity

    def __FunctionSignUp(self) -> None:
        self.__LoginWindow.close()                      # Понять как полноценно уничтожить окно
        self.__ControllerReg.RunViewRegister()

