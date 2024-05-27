from TransportCompany.View.Driver.ViewDriverProfile import ViewDriverProfile
from TransportCompany.Model.Driver.ModelDriverProfile import ModelDriverProfile
from TransportCompany.Entities.Driver import Driver
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication, Qt
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordStats
from hashlib import md5
from sys import argv

class ControllerDriverProfile:
    def __init__(self, driver: Driver, parent):
        self.view = ViewDriverProfile()
        self.model = ModelDriverProfile()
        self.driver = driver
        self.parent = parent
        self.SettingsUI()
        self.DriverProfile.closeEvent = self.closeEvent

        self.view.lineEdit_FirstName.setText(self.driver.FirstName)
        self.view.lineEdit_LastName.setText(self.driver.LastName)
        self.view.lineEdit_Patronymic.setText(self.driver.Patronymic)
        self.view.textEdit_Phone.setText(self.driver.NumberPhone)
        self.view.textEdit_Email.setText(self.driver.Email)
        if self.driver.Password is None:
            self.view.textEdit_OldPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", ""))
            self.view.textEdit_OldPassword.setEnabled(False)
        self.view.pushButton_EditPhone.clicked.connect(self.ClickedEditPhone)
        self.view.pushButton_EditEmail.clicked.connect(self.ClickedEditEmail)
        self.view.pushButton_EditPassword.clicked.connect(self.ClickedEditPassword)
        self.view.pushButton_Back.clicked.connect(self.ClickedBack)

    def SettingsUI(self):
        self.app = QApplication(argv)
        self.DriverProfile = QMainWindow()
        ui = self.view
        ui.setupUi(self.DriverProfile)

    def RunViewDriverProfile(self):
        self.DriverProfile.show()

    def ClickedEditPhone(self):
        phone = self.view.textEdit_Phone.toPlainText()
        if self.isCheckPhone(phone):
            self.view.message("Информация", "Успешно изменено")
            self.model.UpdatePhone(self.driver.ID, phone)
            self.driver.NumberPhone = phone

    def isCheckPhone(self, phone) -> bool:
        if phone == self.driver.NumberPhone: return False
        if len(phone) != 11:
            self.view.message("Информация", "Номер телефона состоит из 11 цифр")
            return False
        else: return True

    def ClickedEditEmail(self) -> None:
        email = self.view.textEdit_Email.toPlainText()
        if self.isCheckEmail(email):
            self.view.message("Информация", "Успешно изменено")
            self.model.UpdateEmail(self.driver.ID, email)
            self.driver.Email = email

    def isCheckEmail(self, email):
        if email == self.driver.Email: return False
        try:
            validate_email(email, check_deliverability=False)
            return True
        except EmailNotValidError:
            self.view.message("Информация", "Почта указана некорректно")
            return False

    def ClickedEditPassword(self):
        if self.driver.Password is None:
            NewPassword = self.view.textEdit_NewPassword.toPlainText()
            if self.isCheckPassword(None, NewPassword):
                self.view.message("Информация", "Успешно изменено")
                NewPassword = md5(NewPassword.encode()).hexdigest()
                self.model.UpdatePassword(self.driver.ID, NewPassword)
                self.driver.Password = NewPassword
                self.view.textEdit_OldPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", "Введите старый пароль"))
                self.view.textEdit_OldPassword.setEnabled(True)
        else:
            NewPassword = self.view.textEdit_NewPassword.toPlainText()
            OldPassword = self.view.textEdit_OldPassword.toPlainText()
            OldPassword = md5(OldPassword.encode()).hexdigest()
            if self.isCheckPassword(OldPassword, NewPassword):
                self.view.message("Информация", "Успешно изменено")
                NewPassword = md5(NewPassword.encode()).hexdigest()
                self.model.UpdatePassword(self.driver.ID, NewPassword)
                self.driver.Password = NewPassword

    def isCheckPassword(self, OldPassword, NewPassword):
        if OldPassword != self.driver.Password and OldPassword is not None:
            self.view.message("Информация", "Старый пароль указан неверно")
            return False
        if NewPassword == "":
            self.view.message("Информация", "Поле нового пароля пусто")
            return False
        if 0 <= PasswordStats(NewPassword).strength() <= 0.2:
            self.view.message("Информация", "Новый пароль недостаточно надежен")
            return False
        else: return True

    def closeEvent(self, event):
        if self.driver.Password is None:
            self.view.message("Информация", "При первом запуске необходимо установить пароль")
            event.ignore()
        else:
            self.parent.driver = self.driver
            self.parent.MainWindow.setEnabled(True)
            event.accept()

    def ClickedBack(self):
        self.DriverProfile.close()