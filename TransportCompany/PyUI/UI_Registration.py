from PyQt5 import QtCore, QtGui, QtWidgets
from TransportCompany.Entities.User import User
from TransportCompany.Registation import Register
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from TransportCompany.UserRepository.UserRepository import UserRepository
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordStats
# import UI_Login





class Ui_RegWindow(object):

    # def __init__(self):
    #     self.WindowLogin = UI_Login.test1()

    def setupUi(self, RegWindow):
        RegWindow.setObjectName("MainWindow")
        RegWindow.resize(552, 485)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        RegWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(RegWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_FirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_FirstName.setGeometry(QtCore.QRect(50, 90, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_FirstName.setFont(font)
        self.lineEdit_FirstName.setObjectName("lineEdit_FirstName")
        FirstNameRegx = QRegExp('^[а-яА-Я]+$')
        FirstNameValidator = QRegExpValidator(FirstNameRegx, self.lineEdit_FirstName)
        self.lineEdit_FirstName.setValidator(FirstNameValidator)
        self.lineEdit_LastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_LastName.setGeometry(QtCore.QRect(50, 130, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_LastName.setFont(font)
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")
        LastNameRegx = QRegExp('^[а-яА-Я]+$')
        LastNameValidator = QRegExpValidator(LastNameRegx, self.lineEdit_LastName)
        self.lineEdit_LastName.setValidator(LastNameValidator)
        self.label_Logo = QtWidgets.QLabel(self.centralwidget)
        self.label_Logo.setGeometry(QtCore.QRect(240, 10, 71, 71))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap("C:/Users/79951/Documents/GitHub/Kursach/TransportCompany/Resources/Logo.png"))
        self.label_Logo.setObjectName("label_Logo")
        self.pushButton_SignUp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SignUp.setGeometry(QtCore.QRect(100, 380, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_SignUp.setFont(font)
#         self.pushButton_SignUp.setStyleSheet("color: rgb(255, 255, 255);\n"
# "background-color: rgb(85, 170, 255);\n"
# "border-radius: 10px")
        self.pushButton_SignUp.setObjectName("pushButton_SignUp")
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setStyleSheet("background-color: rgb(115, 115, 115);")
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.lineEdit_Patronymic = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Patronymic.setGeometry(QtCore.QRect(50, 170, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_Patronymic.setFont(font)
        self.lineEdit_Patronymic.setObjectName("lineEdit_Patronymic")
        PatronymicRegx = QRegExp('^[а-яА-Я]+$')
        PatronymicValidator = QRegExpValidator(PatronymicRegx, self.lineEdit_LastName)
        self.lineEdit_Patronymic.setValidator(PatronymicValidator)
        self.lineEdit_NumberPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_NumberPhone.setGeometry(QtCore.QRect(50, 210, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_NumberPhone.setFont(font)
        self.lineEdit_NumberPhone.setObjectName("lineEdit_NumberPhone")
        NumberPhoneRegx = QRegExp('\d{11}')
        NumberPhoneValidator = QRegExpValidator(NumberPhoneRegx, self.lineEdit_NumberPhone)
        self.lineEdit_NumberPhone.setValidator(NumberPhoneValidator)
        self.lineEdit_Email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Email.setGeometry(QtCore.QRect(50, 250, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_Email.setFont(font)
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        # EmailRegx = QRegExp('([a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?\.)')
        # EmailValidator = QRegExpValidator(EmailRegx, self.lineEdit_Email)
        # self.lineEdit_Email.setValidator(EmailValidator)
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(50, 290, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_Password.setFont(font)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.lineEdit_AgainPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_AgainPassword.setGeometry(QtCore.QRect(50, 330, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lineEdit_AgainPassword.setFont(font)
        self.lineEdit_AgainPassword.setObjectName("lineEdit_AgainPassword")
        RegWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 21))
        self.menubar.setObjectName("menubar")
        RegWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegWindow)
        self.statusbar.setObjectName("statusbar")
        RegWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegWindow)
        QtCore.QMetaObject.connectSlotsByName(RegWindow)

        self.SignUP()
        self.lineEdit_FirstName.textChanged.connect(self.ColorGrenFirstName)
        self.lineEdit_LastName.textChanged.connect(self.ColorGrenLastName)
        self.lineEdit_Patronymic.textChanged.connect(self.ColorGrenPatronymic)
        self.lineEdit_NumberPhone.textChanged.connect(self.CheckNumderPhone)
        self.lineEdit_Email.textChanged.connect(self.CheckEmail)
        self.lineEdit_Password.textChanged.connect(self.CheckPassword)
        self.lineEdit_AgainPassword.textChanged.connect(self.CheckAgainPassword)
        # self.Back()

    def retranslateUi(self, RegWindow):
        _translate = QtCore.QCoreApplication.translate
        RegWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_FirstName.setPlaceholderText(_translate("MainWindow", "FirstName"))
        self.lineEdit_LastName.setPlaceholderText(_translate("MainWindow", "LastName"))
        self.pushButton_SignUp.setText(_translate("MainWindow", "Sign up"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.lineEdit_Patronymic.setPlaceholderText(_translate("MainWindow", "Patronymic"))
        self.lineEdit_NumberPhone.setPlaceholderText(_translate("MainWindow", "NumberPhone"))
        self.lineEdit_Email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.lineEdit_Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_AgainPassword.setPlaceholderText(_translate("MainWindow", "Again Password"))

    def ColorGrenFirstName(self):
        self.lineEdit_FirstName.setStyleSheet("background-color: rgb(0, 255, 127);"
                                              "border-radius: 10px")

    def ColorGrenLastName(self):
        self.lineEdit_LastName.setStyleSheet("background-color: rgb(0, 255, 127);"
                                             "border-radius: 10px")

    def ColorGrenPatronymic(self):
        self.lineEdit_Patronymic.setStyleSheet("background-color: rgb(0, 255, 127);"
                                               "border-radius: 10px")

    def CheckNumderPhone(self):
        if UserRepository.CheckPhoneInDB(self.lineEdit_NumberPhone.text()) or len(self.lineEdit_NumberPhone.text()) < 11:
            self.lineEdit_NumberPhone.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                    "border-radius: 10px")
        else:
            self.lineEdit_NumberPhone.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                    "border-radius: 10px")

    def CheckEmail(self):
        try:
            email = self.lineEdit_Email.text()
            validate_email(email, check_deliverability=False)
        except EmailNotValidError:
            self.lineEdit_Email.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                    "border-radius: 10px")
        else:
            if UserRepository.CheckEmailInDB(email):
                self.lineEdit_Email.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                        "border-radius: 10px")
            else:
                self.lineEdit_Email.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                        "border-radius: 10px")

    def CheckPassword(self):
        password = self.lineEdit_Password.text()
        if len(password) == 0:
            self.lineEdit_Password.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                 "border-radius: 10px")
        else:
            stats = PasswordStats(password)
            if 0 <= stats.strength() <= 0.2:
                self.lineEdit_Password.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                     "border-radius: 10px")
            elif 0.2 < stats.strength() <= 0.66:
                self.lineEdit_Password.setStyleSheet("background-color: rgb(255, 170, 0);"
                                                     "border-radius: 10px")
            elif 0.66 < stats.strength() <= 0.99:
                self.lineEdit_Password.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                     "border-radius: 10px")

    def CheckAgainPassword(self):
        if self.lineEdit_AgainPassword.text() != self.lineEdit_Password.text():
            self.lineEdit_AgainPassword.setStyleSheet("background-color: rgb(170, 0, 0);"
                                                      "border-radius: 10px")
        else:
            self.lineEdit_AgainPassword.setStyleSheet("background-color: rgb(0, 255, 127);"
                                                      "border-radius: 10px")

    def CheckColor(self):
        for LineEdit in RegisterWindow.findChildren(QtWidgets.QLineEdit):
            hexcolor = LineEdit.palette().color(LineEdit.backgroundRole()).name()
            if hexcolor == "#aa0000" or hexcolor == "#ffffff" or len(LineEdit.text()) < 2:
                return False
        else:
            return True

    def SignUP(self):
        self.pushButton_SignUp.clicked.connect(self.functionsSignUp)

    @staticmethod
    def message(title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()

    def functionsSignUp(self):
        if self.CheckColor():
            user = User()
            user.FirstName = self.lineEdit_FirstName.text()
            user.LastName = self.lineEdit_LastName.text()
            user.Patronymic = self.lineEdit_Patronymic.text()
            user.NumberPhone = self.lineEdit_NumberPhone.text()
            user.Email = self.lineEdit_Email.text()
            user.Password = self.lineEdit_Password.text()
            user.Email = self.lineEdit_Email.text()
            user.Role = "Клиент"
            Register(user).UserRigistation()
            self.message("Информация", "Успешно")
        else:
            self.message("Информация", "Не все поля заполнены корректно или вовсе незаполненны")
        # self.WindowLogin.show()

    # def Back(self):
    #     self.pushButton_Back.clicked.connect(self.FunctionBack)

    # def FunctionBack(self):
    #     # RegisterWindow.destroy()
    #     # self.WindowLogin.show()
    #     buffer = self.lineEdit_FirstName.palette().color(self.lineEdit_FirstName.backgroundRole())
    #     self.message("ff", f"{buffer.name()}")








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())
