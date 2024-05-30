from TransportCompany.Model.Accountant.ModelAccountantProfile import ModelAccountantProfile
from TransportCompany.View.Accountant.ViewAccountantProfile import ViewAccountantProfile
from TransportCompany.Entities.Accountant import Accountant
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordStats
from hashlib import md5
from sys import argv



class ControllerAccountantProfile:
    def __init__(self, accountant: Accountant, parent):
        self.view = ViewAccountantProfile()
        self.model = ModelAccountantProfile()
        self.accountant = accountant
        self.parent = parent
        self.SettingsUI()
        self.AccountantProfile.closeEvent = self.closeEvent

        self.view.lineEdit_FirstName.setText(self.accountant.FirstName)
        self.view.lineEdit_LastName.setText(self.accountant.LastName)
        self.view.lineEdit_Patronymic.setText(self.accountant.Patronymic)
        self.view.textEdit_Phone.setText(self.accountant.NumberPhone)
        self.view.textEdit_Email.setText(self.accountant.Email)
        if self.accountant.Password is None:
            self.view.textEdit_OldPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", ""))
            self.view.textEdit_OldPassword.setEnabled(False)
        self.view.pushButton_EditPhone.clicked.connect(self.ClickedEditPhone)
        self.view.pushButton_EditEmail.clicked.connect(self.ClickedEditEmail)
        self.view.pushButton_EditPassword.clicked.connect(self.ClickedEditPassword)
        self.view.pushButton_Back.clicked.connect(self.ClickedBack)
    def SettingsUI(self):
        self.app = QApplication(argv)
        self.AccountantProfile = QMainWindow()
        ui = self.view
        ui.setupUi(self.AccountantProfile)

    def RunViewWindowApplication(self):
        self.AccountantProfile.show()

    def ClickedEditPhone(self):
        phone = self.view.textEdit_Phone.toPlainText()
        if self.isCheckPhone(phone):
            self.view.message("Информация", "Успешно изменено")
            self.model.UpdatePhone(self.accountant.ID, phone)
            self.accountant.NumberPhone = phone

    def isCheckPhone(self, phone) -> bool:
        if phone == self.accountant.NumberPhone: return False
        if len(phone) != 11:
            self.view.message("Информация", "Номер телефона состоит из 11 цифр")
            return False
        else: return True

    def ClickedEditEmail(self) -> None:
        email = self.view.textEdit_Email.toPlainText()
        if self.isCheckEmail(email):
            self.view.message("Информация", "Успешно изменено")
            self.model.UpdateEmail(self.accountant.ID, email)
            self.accountant.Email = email

    def isCheckEmail(self, email):
        if email == self.accountant.Email: return False
        try:
            validate_email(email, check_deliverability=False)
            return True
        except EmailNotValidError:
            self.view.message("Информация", "Почта указана некорректно")
            return False

    def ClickedEditPassword(self):
        if self.accountant.Password is None:
            NewPassword = self.view.textEdit_NewPassword.toPlainText()
            if self.isCheckPassword(None, NewPassword):
                self.view.message("Информация", "Успешно изменено")
                NewPassword = md5(NewPassword.encode()).hexdigest()
                self.model.UpdatePassword(self.accountant.ID, NewPassword)
                self.accountant.Password = NewPassword
                self.view.textEdit_OldPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", "Введите старый пароль"))
                self.view.textEdit_OldPassword.setEnabled(True)
        else:
            NewPassword = self.view.textEdit_NewPassword.toPlainText()
            OldPassword = self.view.textEdit_OldPassword.toPlainText()
            OldPassword = md5(OldPassword.encode()).hexdigest()
            if self.isCheckPassword(OldPassword, NewPassword):
                self.view.message("Информация", "Успешно изменено")
                NewPassword = md5(NewPassword.encode()).hexdigest()
                self.model.UpdatePassword(self.accountant.ID, NewPassword)
                self.accountant.Password = NewPassword

    def isCheckPassword(self, OldPassword, NewPassword):
        if OldPassword != self.accountant.Password and OldPassword is not None:
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
        if self.accountant.Password is None:
            self.view.message("Информация", "При первом запуске необходимо установить пароль")
            event.ignore()
        else:
            self.parent.accountant = self.accountant
            self.parent.ListDeliveredOrders.setEnabled(True)
            event.accept()

    def ClickedBack(self):
        self.AccountantProfile.close()