# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_RequestSubmission.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class ViewRequestSubmission(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 685)
        MainWindow.setStyleSheet("/*background-color: rgb(0, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.pushButton_Back.setStyleSheet("background-color: rgb(129, 211, 255);")
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 70, 351, 581))
        font = QtGui.QFont()
        font.setItalic(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet("border-radius: 30px;\n"
"background-color: rgb(255, 170, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_CreateRequest = QtWidgets.QPushButton(self.frame)
        self.pushButton_CreateRequest.setGeometry(QtCore.QRect(40, 520, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CreateRequest.setFont(font)
        self.pushButton_CreateRequest.setStyleSheet("background-color: rgb(129, 211, 255);\n"
"border-radius: 10px")
        self.pushButton_CreateRequest.setObjectName("pushButton_CreateRequest")
        # self.pushButton_CreateRequest.setDisabled(True)
        self.lineEdit_FirstName = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_FirstName.setGeometry(QtCore.QRect(40, 100, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_FirstName.setFont(font)
        self.lineEdit_FirstName.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_FirstName.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_FirstName.setClearButtonEnabled(False)
        self.lineEdit_FirstName.setObjectName("lineEdit_FirstName")
        FirstNameRegx = QRegExp('^[а-яА-Я]+$')
        FirstNameValidator = QRegExpValidator(FirstNameRegx, self.lineEdit_FirstName)
        self.lineEdit_FirstName.setValidator(FirstNameValidator)
        self.lineEdit_LastName = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_LastName.setGeometry(QtCore.QRect(40, 150, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_LastName.setFont(font)
        self.lineEdit_LastName.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")
        LastNameRegx = QRegExp('^[а-яА-Я]+$')
        LastNameValidator = QRegExpValidator(LastNameRegx, self.lineEdit_LastName)
        self.lineEdit_LastName.setValidator(LastNameValidator)
        self.lineEdit_Email = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Email.setGeometry(QtCore.QRect(40, 200, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_Email.setFont(font)
        self.lineEdit_Email.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_Email.setText("")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.lineEdit_NumberPhone = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_NumberPhone.setGeometry(QtCore.QRect(40, 250, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_NumberPhone.setFont(font)
        self.lineEdit_NumberPhone.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_NumberPhone.setObjectName("lineEdit_NumberPhone")
        NumberPhoneRegx = QRegExp('\d{11}')
        NumberPhoneValidator = QRegExpValidator(NumberPhoneRegx, self.lineEdit_NumberPhone)
        self.lineEdit_NumberPhone.setValidator(NumberPhoneValidator)
        self.lineEdit_PlaceDispatch = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_PlaceDispatch.setGeometry(QtCore.QRect(40, 300, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_PlaceDispatch.setFont(font)
        self.lineEdit_PlaceDispatch.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_PlaceDispatch.setText("")
        self.lineEdit_PlaceDispatch.setObjectName("lineEdit_PlaceDispatch")
        self.lineEdit_PlaceDelivery = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_PlaceDelivery.setGeometry(QtCore.QRect(40, 350, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_PlaceDelivery.setFont(font)
        self.lineEdit_PlaceDelivery.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_PlaceDelivery.setObjectName("lineEdit_PlaceDelivery")
        self.lineEdit_CargoWeight = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_CargoWeight.setGeometry(QtCore.QRect(40, 400, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_CargoWeight.setFont(font)
        self.lineEdit_CargoWeight.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_CargoWeight.setObjectName("lineEdit_CargoWeight")

        CargoWeightRegx = QRegExp('\d{4}')
        CargoWeightValidator = QRegExpValidator(CargoWeightRegx, self.lineEdit_CargoWeight)
        self.lineEdit_CargoWeight.setValidator(CargoWeightValidator)

        self.label_Logo = QtWidgets.QLabel(self.frame)
        self.label_Logo.setGeometry(QtCore.QRect(140, 20, 71, 61))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap("C:/Users/79951/Documents/GitHub/Kursach/TransportCompany/Resources/Logo.png"))
        self.label_Logo.setObjectName("label_Logo")
        self.lineEdit_CargoDescription = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_CargoDescription.setGeometry(QtCore.QRect(40, 450, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_CargoDescription.setFont(font)
        self.lineEdit_CargoDescription.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_CargoDescription.setObjectName("lineEdit_CargoDescription")
        self.label_Info = QtWidgets.QLabel(self.centralwidget)
        self.label_Info.setGeometry(QtCore.QRect(90, 40, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_Info.setFont(font)
        self.label_Info.setObjectName("label_Info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.pushButton_CreateRequest.setText(_translate("MainWindow", "Подать заявку"))
        self.lineEdit_FirstName.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit_FirstName.setPlaceholderText(_translate("MainWindow", "Имя:"))
        self.lineEdit_LastName.setPlaceholderText(_translate("MainWindow", "Фамилия:"))
        self.lineEdit_Email.setPlaceholderText(_translate("MainWindow", "Почта:"))
        self.lineEdit_NumberPhone.setPlaceholderText(_translate("MainWindow", "Номер телефона:"))
        self.lineEdit_PlaceDispatch.setPlaceholderText(_translate("MainWindow", "Адрес отправления:"))
        self.lineEdit_PlaceDelivery.setPlaceholderText(_translate("MainWindow", "Адрес прибытия:"))
        self.lineEdit_CargoWeight.setPlaceholderText(_translate("MainWindow", "Вес груза(кг):"))
        self.lineEdit_CargoDescription.setPlaceholderText(_translate("MainWindow", "Описание груза:"))
        self.label_Info.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_Info.setText(_translate("MainWindow", "Форма подачи заявки"))

    @staticmethod
    def message(title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ViewRequestSubmission()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())