# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ApplicationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ViewApplicationWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1285, 545)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 721, 501))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.527094, y1:0, x2:0.502463, y2:1, stop:0 rgba(0, 231, 100, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget_TableApplication = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_TableApplication.setGeometry(QtCore.QRect(10, 10, 701, 441))
        self.tableWidget_TableApplication.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px")
        self.tableWidget_TableApplication.setObjectName("tableWidget_TableApplication")
        self.tableWidget_TableApplication.setColumnCount(4)
        self.tableWidget_TableApplication.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TableApplication.setItem(1, 3, item)

        self.tableWidget_TableApplication.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        header = self.tableWidget_TableApplication.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(9, 453, 701, 41))
        self.widget.setStyleSheet("/*background-color: rgb(170, 255, 127);*/\n"
"background-color: rgb(0, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 0, 481, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_ListNumberPages = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_ListNumberPages.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_ListNumberPages.setObjectName("horizontalLayout_ListNumberPages")
        self.pushButton_NextPage = QtWidgets.QPushButton(self.widget)
        self.pushButton_NextPage.setGeometry(QtCore.QRect(3, 5, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_NextPage.setFont(font)
        self.pushButton_NextPage.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_NextPage.setObjectName("pushButton_NextPage")
        self.pushButton_BackPage = QtWidgets.QPushButton(self.widget)
        self.pushButton_BackPage.setGeometry(QtCore.QRect(101, 5, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_BackPage.setFont(font)
        self.pushButton_BackPage.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_BackPage.setObjectName("pushButton_BackPage")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(740, 0, 521, 501))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.527094, y1:0, x2:0.502463, y2:1, stop:0 rgba(0, 231, 100, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_Updatetable = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_Updatetable.setGeometry(QtCore.QRect(30, 438, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Updatetable.setFont(font)
        self.pushButton_Updatetable.setStyleSheet("background-color: rgb(255, 251, 224);\n"
"border-radius: 10px")
        self.pushButton_Updatetable.setObjectName("pushButton_UpdateTable")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 501, 81))
        self.frame_3.setStyleSheet("background-color: rgb(255, 251, 224);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.dateEdit_Searchdate = QtWidgets.QDateEdit(self.frame_3)
        self.dateEdit_Searchdate.setGeometry(QtCore.QRect(10, 23, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.dateEdit_Searchdate.setFont(font)
        self.dateEdit_Searchdate.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.dateEdit_Searchdate.setObjectName("dateEdit_Searchdate")
        self.comboBox_Date = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_Date.setGeometry(QtCore.QRect(248, 23, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_Date.setFont(font)
        self.comboBox_Date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_Date.setObjectName("comboBox_Date")
        self.comboBox_Date.addItem("")
        self.comboBox_Date.addItem("")
        self.comboBox_Date.addItem("")
        self.comboBox_Date.addItem("")
        self.pushButton_Search_date = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_Search_date.setGeometry(QtCore.QRect(394, 23, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_Search_date.setFont(font)
        self.pushButton_Search_date.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-radius: 10px\n"
"")
        self.pushButton_Search_date.setObjectName("pushButton_Search_date")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(10, 100, 501, 81))
        self.frame_4.setStyleSheet("background-color: rgb(255, 251, 224);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.comboBox_Status = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Status.setGeometry(QtCore.QRect(10, 23, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_Status.setFont(font)
        self.comboBox_Status.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_Status.setObjectName("comboBox_Status")
        self.comboBox_Status.addItem("")
        self.comboBox_Status.addItem("")
        self.comboBox_Status.addItem("")
        self.comboBox_Status.addItem("")
        self.label_Status = QtWidgets.QLabel(self.frame_4)
        self.label_Status.setGeometry(QtCore.QRect(260, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_Status.setFont(font)
        self.label_Status.setObjectName("label_Status")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(10, 190, 501, 81))
        self.frame_5.setStyleSheet("background-color: rgb(255, 251, 224);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.comboBox_SortTable = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_SortTable.setGeometry(QtCore.QRect(10, 23, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_SortTable.setFont(font)
        self.comboBox_SortTable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_SortTable.setObjectName("comboBox_SortTable")
        self.comboBox_SortTable.addItem("")
        self.comboBox_SortTable.addItem("")
        self.label_text = QtWidgets.QLabel(self.frame_5)
        self.label_text.setGeometry(QtCore.QRect(260, 18, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_text.setFont(font)
        self.label_text.setObjectName("label_text")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(100, 280, 341, 81))
        self.frame_6.setStyleSheet("background-color: rgb(255, 251, 224);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_Quantity = QtWidgets.QLabel(self.frame_6)
        self.label_Quantity.setGeometry(QtCore.QRect(110, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_Quantity.setFont(font)
        self.label_Quantity.setObjectName("label_Quantity")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_6)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 29, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("color: rgb(0, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_BackFirstPage = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_BackFirstPage.setGeometry(QtCore.QRect(30, 380, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_BackFirstPage.setFont(font)
        self.pushButton_BackFirstPage.setStyleSheet("background-color: rgb(255, 251, 224);\n"
"border-radius: 10px")
        self.pushButton_BackFirstPage.setObjectName("pushButton_BackFirstPage")
        MainWindow.setCentralWidget(self.centralwidget)

        self.Button_Group = QtWidgets.QButtonGroup()
        self.Button_Group.setExclusive(False)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 21))
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
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.menu.addAction(self.action_profile)
        self.menu.addAction(self.action_SubmitApplication)
        self.menu.addAction(self.action_AboatProgram)
        self.menu.addAction(self.action_Exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget_TableApplication.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_TableApplication.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_TableApplication.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Пункт отправления"))
        item = self.tableWidget_TableApplication.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Пункт назначения"))
        item = self.tableWidget_TableApplication.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Описание груза"))
        item = self.tableWidget_TableApplication.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата подачи заявки"))
        __sortingEnabled = self.tableWidget_TableApplication.isSortingEnabled()
        self.tableWidget_TableApplication.setSortingEnabled(False)
        item = self.tableWidget_TableApplication.item(0, 0)
        item.setText(_translate("MainWindow", "Кемерово"))
        item = self.tableWidget_TableApplication.item(0, 1)
        item.setText(_translate("MainWindow", "Москва"))
        item = self.tableWidget_TableApplication.item(0, 2)
        item.setText(_translate("MainWindow", "Метал"))
        item = self.tableWidget_TableApplication.item(0, 3)
        item.setText(_translate("MainWindow", "13.10.2024"))
        item = self.tableWidget_TableApplication.item(1, 0)
        item.setText(_translate("MainWindow", "Москва"))
        item = self.tableWidget_TableApplication.item(1, 1)
        item.setText(_translate("MainWindow", "Кемерово"))
        item = self.tableWidget_TableApplication.item(1, 2)
        item.setText(_translate("MainWindow", "Дерево"))
        item = self.tableWidget_TableApplication.item(1, 3)
        item.setText(_translate("MainWindow", "13.11.2024"))
        self.tableWidget_TableApplication.setSortingEnabled(__sortingEnabled)
        self.pushButton_NextPage.setText(_translate("MainWindow", "Next >"))
        self.pushButton_BackPage.setText(_translate("MainWindow", "< Back"))
        self.pushButton_Updatetable.setText(_translate("MainWindow", "Убрать все фильтры"))
        self.dateEdit_Searchdate.setToolTip(_translate("MainWindow", "Измените дату"))
        self.comboBox_Date.setToolTip(_translate("MainWindow", "Выберите принцип поиска"))
        self.comboBox_Date.setItemText(0, _translate("MainWindow", "По полной дате"))
        self.comboBox_Date.setItemText(1, _translate("MainWindow", "По году"))
        self.comboBox_Date.setItemText(2, _translate("MainWindow", "По месяцу"))
        self.comboBox_Date.setItemText(3, _translate("MainWindow", "По дню"))
        self.pushButton_Search_date.setText(_translate("MainWindow", "Search:"))
        self.comboBox_Status.setToolTip(_translate("MainWindow", "Сортировка таблицы"))
        self.comboBox_Status.setItemText(0, _translate("MainWindow", "В пути"))
        self.comboBox_Status.setItemText(1, _translate("MainWindow", "Доставлен"))
        self.comboBox_Status.setItemText(2, _translate("MainWindow", "Отменён"))
        self.comboBox_Status.setItemText(3, _translate("MainWindow", "Сформирован"))
        self.label_Status.setText(_translate("MainWindow", "Статус"))
        self.comboBox_SortTable.setToolTip(_translate("MainWindow", "Сортировка таблицы"))
        self.comboBox_SortTable.setItemText(0, _translate("MainWindow", "По убывающей дате"))
        self.comboBox_SortTable.setItemText(1, _translate("MainWindow", "По возрастающей дате"))
        self.label_text.setText(_translate("MainWindow", "Сортировка таблицы"))
        self.label_Quantity.setText(_translate("MainWindow", "Количество заявок"))
        self.pushButton_BackFirstPage.setText(_translate("MainWindow", "Вернуться на первую страницу"))
        self.menu.setTitle(_translate("MainWindow", "Программа"))
        self.action_SubmitApplication.setText(_translate("MainWindow", "Подать заявку"))
        self.action_AboatProgram.setText(_translate("MainWindow", "О программе"))
        self.action_profile.setText(_translate("MainWindow", "Профиль "))
        self.action_Exit.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ViewApplicationWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())