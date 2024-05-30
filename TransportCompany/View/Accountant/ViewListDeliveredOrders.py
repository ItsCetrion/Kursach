# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ListDeliveredOrders.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class ViewListDeliveredOrders(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 405)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 501, 361))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"border-radius: 20px;\n"
"border: 2px solid black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget_TableApplication = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_TableApplication.setGeometry(QtCore.QRect(10, 10, 481, 340))
        self.tableWidget_TableApplication.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 0px")
        self.tableWidget_TableApplication.setObjectName("tableWidget_TableApplication")
        self.tableWidget_TableApplication.setColumnCount(3)
        self.tableWidget_TableApplication.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setHorizontalHeaderItem(2, item)

        self.tableWidget_TableApplication.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        header = self.tableWidget_TableApplication.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(520, 0, 521, 361))
        self.frame_2.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"border-radius: 20px;\n"
"border: 2px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_ResetSearch = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_ResetSearch.setGeometry(QtCore.QRect(40, 290, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ResetSearch.setFont(font)
        self.pushButton_ResetSearch.setStyleSheet("background-color: rgb(255, 251, 224);\n"
"border-radius: 10px")
        self.pushButton_ResetSearch.setObjectName("pushButton_ResetSearch")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(10, 20, 501, 81))
        self.frame_4.setStyleSheet("background-color: rgb(255, 251, 224);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_NumberOrder = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_NumberOrder.setGeometry(QtCore.QRect(10, 25, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit_NumberOrder.setFont(font)
        self.lineEdit_NumberOrder.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_NumberOrder.setObjectName("lineEdit_NumberOrder")
        NumberOrderRegx = QRegExp('\d{11}')
        NumberOrderValidator = QRegExpValidator(NumberOrderRegx, self.lineEdit_NumberOrder)
        self.lineEdit_NumberOrder.setValidator(NumberOrderValidator)
        self.pushButton_Search = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_Search.setGeometry(QtCore.QRect(254, 25, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_Search.setFont(font)
        self.pushButton_Search.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(10, 120, 501, 81))
        self.frame_7.setStyleSheet("background-color: rgb(255, 251, 224);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.comboBox_SortTable_2 = QtWidgets.QComboBox(self.frame_7)
        self.comboBox_SortTable_2.setGeometry(QtCore.QRect(10, 23, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_SortTable_2.setFont(font)
        self.comboBox_SortTable_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px")
        self.comboBox_SortTable_2.setObjectName("comboBox_SortTable_2")
        self.comboBox_SortTable_2.addItem("")
        self.comboBox_SortTable_2.addItem("")
        self.label_text_2 = QtWidgets.QLabel(self.frame_7)
        self.label_text_2.setGeometry(QtCore.QRect(220, 18, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_text_2.setFont(font)
        self.label_text_2.setStyleSheet("border: 0px")
        self.label_text_2.setObjectName("label_text_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(90, 225, 341, 41))
        self.frame_6.setStyleSheet("background-color: rgb(255, 251, 224);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_Quantity = QtWidgets.QLabel(self.frame_6)
        self.label_Quantity.setGeometry(QtCore.QRect(110, 10, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_Quantity.setFont(font)
        self.label_Quantity.setStyleSheet("border: 0px")
        self.label_Quantity.setObjectName("label_Quantity")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_6)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 10, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: 0px")
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_SubmitApplication = QtWidgets.QAction(MainWindow)
        self.action_SubmitApplication.setObjectName("action_SubmitApplication")
        self.action_AboatProgram = QtWidgets.QAction(MainWindow)
        self.action_AboatProgram.setObjectName("action_AboatProgram")
        self.action_profile = QtWidgets.QAction(MainWindow)
        self.action_profile.setObjectName("action_profile")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.menu.addAction(self.action_profile)
        self.menu.addAction(self.action_Exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget_TableApplication.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер заказа"))
        item = self.tableWidget_TableApplication.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Место отправления"))
        item = self.tableWidget_TableApplication.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Место прибытия"))
        __sortingEnabled = self.tableWidget_TableApplication.isSortingEnabled()
        self.tableWidget_TableApplication.setSortingEnabled(False)
        self.tableWidget_TableApplication.setSortingEnabled(__sortingEnabled)
        self.pushButton_ResetSearch.setText(_translate("MainWindow", "Сбросить поиск"))
        self.lineEdit_NumberOrder.setPlaceholderText(_translate("MainWindow", "Поиск по номеру заказа:"))
        self.pushButton_Search.setText(_translate("MainWindow", "Поиск"))
        self.comboBox_SortTable_2.setToolTip(_translate("MainWindow", "Сортировка таблицы"))
        self.comboBox_SortTable_2.setItemText(0, _translate("MainWindow", "По возрастанию"))
        self.comboBox_SortTable_2.setItemText(1, _translate("MainWindow", "По убыванию"))
        self.label_text_2.setText(_translate("MainWindow", "Сортировка по номеру заказа"))
        self.label_Quantity.setText(_translate("MainWindow", "Количество заявок"))
        self.menu.setTitle(_translate("MainWindow", "Программа"))
        self.action_profile.setText(_translate("MainWindow", "Профиль "))
        self.action_Exit.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ViewListDeliveredOrders()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
