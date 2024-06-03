from TransportCompany.View.Admin.ViewRegistrationWorker import ViewRegistrationWorker
from TransportCompany.Model.Admin.ModelRegistrationWorker import ModelRegistrationWorker
from TransportCompany.Entities.Driver import Driver
from TransportCompany.Entities.Accountant import Accountant
from PyQt5 import QtWidgets
import sys

class ControllerRegistrationWorker:
    def __init__(self):
        self.__model = ModelRegistrationWorker()
        self.view = ViewRegistrationWorker()
        self.__SettingUI()
        self.view.pushButton_Back.clicked.connect(self.__Back)
        self.view.pushButton_Registration.clicked.connect(self.__Registration)

    def __SettingUI(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__RegistrationWorker = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.__RegistrationWorker)

    def RunViewRegistrationWorker(self):
        self.__RegistrationWorker.show()

    def __Back(self):
        from TransportCompany.Controller.Admin.ControllerWindowApplication import ControllerWindowApplication
        self.__ControllerWinApp = ControllerWindowApplication()
        self.__RegistrationWorker.close()
        self.__ControllerWinApp.RunViewWindowApplication()

    def __Registration(self):
        if self.__isCheckAgeAndExperience():
            if self.view.comboBox_Worker.currentText() == "Бухгалтер":
                accountant = Accountant()
                accountant_ = self.__FillingAccountant(accountant)
                if isinstance(accountant_, str):
                    self.view.message("Информация", accountant_)
                else:
                    self.__model.RegistrationAccountant(accountant_)
                    self.view.message("Информация", "Работник успешно добавлен")
                    self.__Back()
            elif self.view.comboBox_Worker.currentText() == "Водитель":
                driver = Driver()
                driver_ = self.__FillingDriver(driver)
                if isinstance(driver_, str):
                    self.view.message("Информация", driver_)
                else:
                    self.__model.RegistrationDriver(driver_)
                    self.view.message("Информация", "Работник успешно добавлен")
                    self.__Back()

    def __isCheckAgeAndExperience(self):
        try:
            if int(self.view.lineEdit_Age.text()) < 18:
                self.view.message("Информация", "Нельзя назначит сотрудника младше 18 лет!")
                return False
            if int(self.view.lineEdit_Age.text()) - int(self.view.lineEdit_Experience.text()) < 16:
                self.view.message("Информация", "Неправильный стаж!")
                return False
            else:
                return True
        except ValueError:
            self.view.message("Информация", "Какое-то из полей не заполнено!")
            return False

    def __FillingAccountant(self, accountant: Accountant):
        accountant.FirstName = self.view.lineEdit_FirstName.text()
        accountant.LastName = self.view.lineEdit_LastName.text()
        accountant.Patronymic = self.view.lineEdit_Patronymic.text()
        accountant.NumberPhone = self.view.lineEdit_NumberPhone.text()
        accountant.Email = self.view.lineEdit_Email.text()
        accountant.Age = self.view.lineEdit_Age.text()
        accountant.Experience = self.view.lineEdit_Experience.text()
        values_driver = list(accountant.__dict__.values())[1:-2]
        if self.__model.CheckEmail(accountant.Email) or self.__model.CheckPhone(accountant.NumberPhone):
            return "Такой номер телефона или почта уже занята"
        elif set([None, ""]).intersection(values_driver):
            return "Не все поля заполнены"
        else:
            return accountant

    def __FillingDriver(self, driver: Driver):
        driver.FirstName = self.view.lineEdit_FirstName.text()
        driver.LastName = self.view.lineEdit_LastName.text()
        driver.Patronymic = self.view.lineEdit_Patronymic.text()
        driver.NumberPhone = self.view.lineEdit_NumberPhone.text()
        driver.Email = self.view.lineEdit_Email.text()
        driver.Age = self.view.lineEdit_Age.text()
        driver.Experience = self.view.lineEdit_Experience.text()
        values_driver = list(driver.__dict__.values())[2:-3]
        if self.__model.CheckEmail(driver.Email) or self.__model.CheckPhone(driver.NumberPhone):
            return "Такой номер телефона или почта уже занята"
        elif set([None, ""]).intersection(values_driver):
            return "Не все поля заполнены"
        else:
            return driver




