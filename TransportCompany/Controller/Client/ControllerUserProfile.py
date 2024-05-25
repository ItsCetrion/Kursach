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
        self.model = ModelUserProfile()
        self.view = ViewUserProfile()
        self.client = client
        self.SettingsUI()
        self.parent = parent

        self.UserProfile.closeEvent = self.closeEvent
        self.view.lineEdit_FirstName.setText(client.FirstName)
        self.view.lineEdit_LastName.setText(client.LastName)
        self.view.lineEdit_Patronymic.setText(client.Patronymic)
        self.view.lineEdit_Phone.setText(client.NumberPhone)
        self.view.textEdit_Email.setText(client.Email)
        self.view.pushButton_EditPhone.clicked.connect(self.ClickedEditPhone)
        self.view.pushButton_EditEmail.clicked.connect(self.ClickedEditEmail)
        self.view.pushButton_EditPassword.clicked.connect(self.ClickedEditPassword)

    def SettingsUI(self):
        self.app = QApplication(argv)
        self.UserProfile = QMainWindow()
        ui = self.view
        ui.setupUi(self.UserProfile)

    def RunViewUserProfile(self):
        self.UserProfile.show()
        # sys.exit(self.app.exec_())

    def ClickedEditPhone(self) -> None:
        phone = self.view.lineEdit_Phone.text()
        if self.isCheckPhone(phone):
            self.view.message("Информация", "Успешно изменено")
            self.model.UpdatePhone(self.client.ID, phone)
            self.client.NumberPhone = phone

    def isCheckPhone(self, phone) -> bool:
        if phone == self.client.NumberPhone: return False
        if len(phone) != 11:
            self.view.message("Информация", "Номер телефона состоит из 11 цифр")
            return False
        else: return True


    def ClickedEditEmail(self) -> None:
        email = self.view.textEdit_Email.toPlainText()
        if self.isCheckEmail(email):
            self.view.message("Информация", "Успешно изменено")
            self.model.UpdateEmail(self.client.ID, email)
            self.client.Email = email

    def isCheckEmail(self, email):
        if email == self.client.Email: return False
        try:
            validate_email(email, check_deliverability=False)
            return True
        except EmailNotValidError:
            self.view.message("Информация", "Почта указана не корректно")
            return False

    def ClickedEditPassword(self):
        NewPassword = self.view.textEdit_NewPassword.toPlainText()
        OldPassword = self.view.textEdit_OldPassword.toPlainText()
        OldPassword = md5(OldPassword.encode()).hexdigest()
        if self.isCheckPassword(OldPassword, NewPassword):
            self.view.message("Информация", "Успешно изменено")
            NewPassword = md5(NewPassword.encode()).hexdigest()
            self.model.UpdatePassword(self.client.ID, NewPassword)
            self.client.Password = NewPassword

    def isCheckPassword(self, OldPassword, NewPassword):
        if OldPassword != self.client.Password:
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
        self.parent.client = self.client
        self.parent.ApplicationWindow.setEnabled(True)
        event.accept()
