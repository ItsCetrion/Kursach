from TransportCompany.View.Client.ViewUserProfile import ViewUserProfile
from TransportCompany.Model.Client.ModelUserProfile import ModelUserProfile
from TransportCompany.Entities.Client import Client
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordStats
from PyQt5.QtWidgets import QApplication, QMainWindow
from sys import argv
from hashlib import md5


class ControllerUserProfile:
    def __init__(self, client: Client, parent):
        self.__model = ModelUserProfile()
        self.view = ViewUserProfile()
        self.__client = client
        self.__SettingsUI()
        self.__parent = parent

        self.__UserProfile.closeEvent = self.__closeEvent
        self.view.lineEdit_FirstName.setText(client.FirstName)
        self.view.lineEdit_LastName.setText(client.LastName)
        self.view.lineEdit_Patronymic.setText(client.Patronymic)
        self.view.lineEdit_Phone.setText(client.NumberPhone)
        self.view.textEdit_Email.setText(client.Email)
        self.view.pushButton_EditPhone.clicked.connect(self.__ClickedEditPhone)
        self.view.pushButton_EditEmail.clicked.connect(self.__ClickedEditEmail)
        self.view.pushButton_EditPassword.clicked.connect(self.__ClickedEditPassword)

    def __SettingsUI(self):
        self.__app = QApplication(argv)
        self.__UserProfile = QMainWindow()
        ui = self.view
        ui.setupUi(self.__UserProfile)

    def RunViewUserProfile(self):
        self.__UserProfile.show()

    def __ClickedEditPhone(self) -> None:
        phone = self.view.lineEdit_Phone.text()
        if self.__isCheckPhone(phone):
            self.view.message("Информация", "Успешно изменено")
            self.__model.UpdatePhone(self.__client.ID, phone)
            self.__client.NumberPhone = phone

    def __isCheckPhone(self, phone) -> bool:
        if phone == self.__client.NumberPhone: return False
        if len(phone) != 11:
            self.view.message("Информация", "Номер телефона состоит из 11 цифр")
            return False
        else: return True

    def __ClickedEditEmail(self) -> None:
        email = self.view.textEdit_Email.toPlainText()
        if self.__isCheckEmail(email):
            self.view.message("Информация", "Успешно изменено")
            self.__model.UpdateEmail(self.__client.ID, email)
            self.__client.Email = email

    def __isCheckEmail(self, email):
        if email == self.__client.Email: return False
        try:
            validate_email(email, check_deliverability=False)
            return True
        except EmailNotValidError:
            self.view.message("Информация", "Почта указана некорректно")
            return False

    def __ClickedEditPassword(self):
        NewPassword = self.view.textEdit_NewPassword.toPlainText()
        OldPassword = self.view.textEdit_OldPassword.toPlainText()
        OldPassword = md5(OldPassword.encode()).hexdigest()
        if self.__isCheckPassword(OldPassword, NewPassword):
            self.view.message("Информация", "Успешно изменено")
            NewPassword = md5(NewPassword.encode()).hexdigest()
            self.__model.UpdatePassword(self.__client.ID, NewPassword)
            self.__client.Password = NewPassword

    def __isCheckPassword(self, OldPassword, NewPassword):
        if OldPassword != self.__client.Password:
            self.view.message("Информация", "Старый пароль указан неверно")
            return False
        if NewPassword == "":
            self.view.message("Информация", "Поле нового пароля пусто")
            return False
        if 0 <= PasswordStats(NewPassword).strength() <= 0.2:
            self.view.message("Информация", "Новый пароль недостаточно надежен")
            return False
        else: return True

    def __closeEvent(self, event):
        self.__parent.__client = self.__client
        self.__parent.ApplicationWindow.setEnabled(True)
        event.accept()
