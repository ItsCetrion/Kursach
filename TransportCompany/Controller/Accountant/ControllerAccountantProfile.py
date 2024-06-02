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
        self.__view = ViewAccountantProfile()
        self.__model = ModelAccountantProfile()
        self.__accountant = accountant
        self.__parent = parent
        self.__SettingsUI()
        self.__AccountantProfile.closeEvent = self.__closeEvent

        self.__view.lineEdit_FirstName.setText(self.__accountant.FirstName)
        self.__view.lineEdit_LastName.setText(self.__accountant.LastName)
        self.__view.lineEdit_Patronymic.setText(self.__accountant.Patronymic)
        self.__view.textEdit_Phone.setText(self.__accountant.NumberPhone)
        self.__view.textEdit_Email.setText(self.__accountant.Email)
        if self.__accountant.Password is None:
            self.__view.textEdit_OldPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", ""))
            self.__view.textEdit_OldPassword.setEnabled(False)
        self.__view.pushButton_EditPhone.clicked.connect(self.__ClickedEditPhone)
        self.__view.pushButton_EditEmail.clicked.connect(self.__ClickedEditEmail)
        self.__view.pushButton_EditPassword.clicked.connect(self.__ClickedEditPassword)
        self.__view.pushButton_Back.clicked.connect(self.__ClickedBack)
    def __SettingsUI(self):
        self.__app = QApplication(argv)
        self.__AccountantProfile = QMainWindow()
        ui = self.__view
        ui.setupUi(self.__AccountantProfile)

    def RunViewWindowApplication(self):
        self.__AccountantProfile.show()

    def __ClickedEditPhone(self):
        phone = self.__view.textEdit_Phone.toPlainText()
        if self.__isCheckPhone(phone):
            self.__view.message("Информация", "Успешно изменено")
            self.__model.UpdatePhone(self.__accountant.ID, phone)
            self.__accountant.NumberPhone = phone

    def __isCheckPhone(self, phone) -> bool:
        if phone == self.__accountant.NumberPhone: return False
        if len(phone) != 11:
            self.__view.message("Информация", "Номер телефона состоит из 11 цифр")
            return False
        else: return True

    def __ClickedEditEmail(self) -> None:
        email = self.__view.textEdit_Email.toPlainText()
        if self.__isCheckEmail(email):
            self.__view.message("Информация", "Успешно изменено")
            self.__model.UpdateEmail(self.__accountant.ID, email)
            self.__accountant.Email = email

    def __isCheckEmail(self, email):
        if email == self.__accountant.Email: return False
        try:
            validate_email(email, check_deliverability=False)
            return True
        except EmailNotValidError:
            self.__view.message("Информация", "Почта указана некорректно")
            return False

    def __ClickedEditPassword(self):
        if self.__accountant.Password is None:
            NewPassword = self.__view.textEdit_NewPassword.toPlainText()
            if self.__isCheckPassword(None, NewPassword):
                self.__view.message("Информация", "Успешно изменено")
                NewPassword = md5(NewPassword.encode()).hexdigest()
                self.__model.UpdatePassword(self.__accountant.ID, NewPassword)
                self.__accountant.Password = NewPassword
                self.__view.textEdit_OldPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", "Введите старый пароль"))
                self.__view.textEdit_OldPassword.setEnabled(True)
        else:
            NewPassword = self.__view.textEdit_NewPassword.toPlainText()
            OldPassword = self.__view.textEdit_OldPassword.toPlainText()
            OldPassword = md5(OldPassword.encode()).hexdigest()
            if self.__isCheckPassword(OldPassword, NewPassword):
                self.__view.message("Информация", "Успешно изменено")
                NewPassword = md5(NewPassword.encode()).hexdigest()
                self.__model.UpdatePassword(self.__accountant.ID, NewPassword)
                self.__accountant.Password = NewPassword

    def __isCheckPassword(self, OldPassword, NewPassword):
        if OldPassword != self.__accountant.Password and OldPassword is not None:
            self.__view.message("Информация", "Старый пароль указан неверно")
            return False
        if NewPassword == "":
            self.__view.message("Информация", "Поле нового пароля пусто")
            return False
        if 0 <= PasswordStats(NewPassword).strength() <= 0.2:
            self.__view.message("Информация", "Новый пароль недостаточно надежен")
            return False
        else: return True

    def __closeEvent(self, event):
        if self.__accountant.Password is None:
            self.__view.message("Информация", "При первом запуске необходимо установить пароль")
            event.ignore()
        else:
            self.__parent.__accountant = self.__accountant
            self.__parent.ListDeliveredOrders.setEnabled(True)
            event.accept()

    def __ClickedBack(self):
        self.__AccountantProfile.close()