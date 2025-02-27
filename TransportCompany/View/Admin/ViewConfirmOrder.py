# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ConfirmOrder.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ViewConfirmOrder(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(455, 575)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 416, 531))
        self.frame.setStyleSheet("background-color: rgb(170, 170, 0);\n"
"border-radius: 30px;\n"
"border: 2px solid gray")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit_Dispatch = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Dispatch.setGeometry(QtCore.QRect(55, 50, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textEdit_Dispatch.setFont(font)
        self.textEdit_Dispatch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.textEdit_Dispatch.setObjectName("textEdit_Dispatch")
        self.textEdit_Delivery = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Delivery.setGeometry(QtCore.QRect(55, 140, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textEdit_Delivery.setFont(font)
        self.textEdit_Delivery.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.textEdit_Delivery.setObjectName("textEdit_Delivery")
        self.textEdit_Cargoinfo = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Cargoinfo.setGeometry(QtCore.QRect(55, 230, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textEdit_Cargoinfo.setFont(font)
        self.textEdit_Cargoinfo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.textEdit_Cargoinfo.setObjectName("textEdit_Cargoinfo")
        self.label_c = QtWidgets.QLabel(self.frame)
        self.label_c.setGeometry(QtCore.QRect(150, 20, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_c.setFont(font)
        self.label_c.setStyleSheet("border: 0px\n"
"")
        self.label_c.setObjectName("label_c")
        self.label_Delivery = QtWidgets.QLabel(self.frame)
        self.label_Delivery.setGeometry(QtCore.QRect(150, 110, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Delivery.setFont(font)
        self.label_Delivery.setStyleSheet("border: 0px\n"
"")
        self.label_Delivery.setObjectName("label_Delivery")
        self.label_CargoInfo = QtWidgets.QLabel(self.frame)
        self.label_CargoInfo.setGeometry(QtCore.QRect(130, 200, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_CargoInfo.setFont(font)
        self.label_CargoInfo.setStyleSheet("border: 0px\n"
"")
        self.label_CargoInfo.setObjectName("label_CargoInfo")
        self.comboBox_1Driver = QtWidgets.QComboBox(self.frame)
        self.comboBox_1Driver.setGeometry(QtCore.QRect(60, 331, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.comboBox_1Driver.setFont(font)
        self.comboBox_1Driver.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_1Driver.setObjectName("comboBox_1Driver")
        self.radioButton_Change2Driver = QtWidgets.QRadioButton(self.frame)
        self.radioButton_Change2Driver.setGeometry(QtCore.QRect(90, 380, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_Change2Driver.setFont(font)
        self.radioButton_Change2Driver.setStyleSheet("border: 0px")
        self.radioButton_Change2Driver.setObjectName("radioButton_Change2Driver")
        self.comboBox_2Driver = QtWidgets.QComboBox(self.frame)
        self.comboBox_2Driver.setGeometry(QtCore.QRect(60, 420, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.comboBox_2Driver.setFont(font)
        self.comboBox_2Driver.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2Driver.setObjectName("comboBox_2Driver")
        self.comboBox_2Driver.setEnabled(False)
        self.pushButton_Back = QtWidgets.QPushButton(self.frame)
        self.pushButton_Back.setGeometry(QtCore.QRect(210, 480, 181, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Confirm = QtWidgets.QPushButton(self.frame)
        self.pushButton_Confirm.setGeometry(QtCore.QRect(30, 480, 181, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Confirm.setFont(font)
        self.pushButton_Confirm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.pushButton_Confirm.setObjectName("pushButton_Confirm")
        self.label_Driver = QtWidgets.QLabel(self.frame)
        self.label_Driver.setGeometry(QtCore.QRect(165, 290, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Driver.setFont(font)
        self.label_Driver.setStyleSheet("border: 0px\n"
"")
        self.label_Driver.setObjectName("label_Driver")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 26))
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
        self.textEdit_Dispatch.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Москва</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_Delivery.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\">dsfsdfdsfsd</span></p></body></html>"))
        self.textEdit_Cargoinfo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\">dsfsdfdsfsd</span></p></body></html>"))
        self.label_c.setText(_translate("MainWindow", "Пункт отправки"))
        self.label_Delivery.setText(_translate("MainWindow", "Пункт доставки"))
        self.label_CargoInfo.setText(_translate("MainWindow", "Информация о грузе"))
        self.radioButton_Change2Driver.setText(_translate("MainWindow", "Добавить второго водителя"))
        self.pushButton_Back.setText(_translate("MainWindow", "Назад"))
        self.pushButton_Confirm.setText(_translate("MainWindow", "Подтвердить"))
        self.label_Driver.setText(_translate("MainWindow", "Водитель"))

    @staticmethod
    def message(title, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox().Information)
        msg.setDefaultButton(QtWidgets.QMessageBox().Ok)
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ViewConfirmOrder()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
