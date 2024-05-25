from TransportCompany.View.Admin.ViewRegistrationWorker import ViewRegistrationWorker
from TransportCompany.Model.Admin.ModelRegistrationWorker import ModelRegistrationWorker
from TransportCompany.Entities.Driver import Driver
from TransportCompany.Entities.Accountant import Accountant
from PyQt5 import QtWidgets
import sys

class ControllerRegistrationWorker:
    def __init__(self):
        self.model = ModelRegistrationWorker()
        self.view = ViewRegistrationWorker()
        self.SettingUI()
        self.view.pushButton_Back.clicked.connect(self.Back)
        self.view.pushButton_Registration.clicked.connect(self.Registration)

    def SettingUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.RegistrationWorker = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.RegistrationWorker)

    def RunViewRegistrationWorker(self):
        self.RegistrationWorker.show()

    def Back(self):
        from TransportCompany.Controller.Admin.ControllerWindowApplication import ControllerWindowApplication
        self.ControllerWinApp = ControllerWindowApplication()
        self.RegistrationWorker.close()
        self.ControllerWinApp.RunViewWindowApplication()

    def Registration(self):
        if self.view.comboBox_Worker.currentText() == "Бухгалтер":
            accountant = Accountant()
            accountant_ = self.FillingAccountant(accountant)
            if isinstance(accountant_, str):
                self.view.message("Информация", accountant_)
            else:
                self.model.RegistrationAccountant(accountant_)
                self.view.message("Информация", "Работник успешно добавлен")
                self.Back()
        elif self.view.comboBox_Worker.currentText() == "Водитель":
            driver = Driver()
            driver_ = self.FillingDriver(driver)
            if isinstance(driver_, str):
                self.view.message("Информация", driver_)
            else:
                self.model.RegistrationDriver(driver_)
                self.view.message("Информация", "Работник успешно добавлен")
                self.Back()

    def FillingAccountant(self, accountant: Accountant):
        accountant.FirstName = self.view.lineEdit_FirstName.text()
        accountant.LastName = self.view.lineEdit_LastName.text()
        accountant.Patronymic = self.view.lineEdit_Patronymic.text()
        accountant.NumberPhone = self.view.lineEdit_NumberPhone.text()
        accountant.Email = self.view.lineEdit_Email.text()
        accountant.Age = self.view.lineEdit_Age.text()
        accountant.Experience = self.view.lineEdit_Experience.text()
        if self.model.CheckEmail(accountant.Email) or self.model.CheckPhone(accountant.NumberPhone):
            return "Такой номер телефона или почта уже занята"
        elif (None in accountant.__dict__.values()) or "" in accountant.__dict__.values():
            return "Не все поля заполнены"
        else:
            return accountant

    def FillingDriver(self, driver: Driver):
        driver.FirstName = self.view.lineEdit_FirstName.text()
        driver.LastName = self.view.lineEdit_LastName.text()
        driver.Patronymic = self.view.lineEdit_Patronymic.text()
        driver.NumberPhone = self.view.lineEdit_NumberPhone.text()
        driver.Email = self.view.lineEdit_Email.text()
        driver.Age = self.view.lineEdit_Age.text()
        driver.Experience = self.view.lineEdit_Experience.text()
        values_driver = list(driver.__dict__.values())[1:-3]
        if self.model.CheckEmail(driver.Email) or self.model.CheckPhone(driver.NumberPhone):
            return "Такой номер телефона или почта уже занята"
        elif set([None, ""]).intersection(values_driver):
            return "Не все поля заполнены"
        else:
            return driver



