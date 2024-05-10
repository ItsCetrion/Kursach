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
            self.model.RegistrationAccountant(self.FillingAccountant(accountant))
            self.view.message("Информация", "Работник успешно добавлен")
            self.Back()
        elif self.view.comboBox_Worker.currentText() == "Водитель":
            driver = Driver()
            self.model.RegistrationDriver(self.FillingDriver(driver))
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
            self.view.message("Информация", "Такой номер телефона или почта уже занята")
        elif None in accountant.__dict__.values():
            self.view.message("Информация", "Не все поля заполнены")
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
        if self.model.CheckEmail(driver.Email) or self.model.CheckPhone(driver.NumberPhone):
            self.view.message("Информация", "Такой номер телефона или почта уже занята")
        elif None in driver.__dict__.values():
            self.view.message("Информация", "Не все поля заполнены")
        else:
            return driver



