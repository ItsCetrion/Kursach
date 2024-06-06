from Model.Driver.ModelMainWindow import ModelMainWindow
from View.Driver.ViewMainWindow import ViewMainWindow
from Entities.Driver import Driver
from Entities.DeliveredRequest import DeliveredRequest
from Controller.Driver.ControllerMap import ControllerMap
from Controller.Driver.ControllerDriverProfile import ControllerDriverProfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, \
    QTextEdit, QLineEdit, QPushButton, QTableWidgetItem
from PyQt5.QtCore import QRect, QCoreApplication
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from PyQt5.QtGui import QFont
from sys import argv


class ControllerMainWindow:
    def __init__(self, driver: Driver):
        self.view = ViewMainWindow()
        self.__model = ModelMainWindow()
        self.__driver = driver
        self.__SettingsUI()
        self.__CreateActiveOrder()
        self.__FirstFillingTable()

        self.view.action_Profile.triggered.connect(self.__ClickedProfile)
        self.view.action_Exit.triggered.connect(self.__ClickedExit)

    def __SettingsUI(self):
        self.__app = QApplication(argv)
        self.MainWindow = QMainWindow()
        ui = self.view
        ui.setupUi(self.MainWindow)

    def RunMainWindow(self):
        self.MainWindow.show()
        self.__CheckHavePassword()

    def __CheckHavePassword(self):
        if self.__driver.Password is None:
            self.__DriverProfile = ControllerDriverProfile(self.__driver, self)
            self.__DriverProfile.RunViewDriverProfile()
            self.MainWindow.setEnabled(False)
            self.view.message("Информация", "Произведен первый запуск приложения.\nНеобходимо установить пароль")

    def __FirstFillingTable(self):
        ListCompletedOrder = self.__model.GetCompletedOrders(self.__driver.ID) # Если буду делать сортировку, то убрать от сюда
        self.view.tableWidget.setRowCount(len(ListCompletedOrder))
        _translate = QCoreApplication.translate
        RowTable = 0
        for request in ListCompletedOrder:
            self.__SetItem(RowTable)
            item = self.view.tableWidget.verticalHeaderItem(RowTable)
            item.setText(_translate("MainWindow", ""))
            item = self.view.tableWidget.item(RowTable, 0)
            item.setText(_translate("MainWindow", str(request[0])))
            item = self.view.tableWidget.item(RowTable, 1)
            item.setText(_translate("MainWindow", request[1]))
            item = self.view.tableWidget.item(RowTable, 2)
            item.setText(_translate("MainWindow", request[2]))
            item = self.view.tableWidget.item(RowTable, 3)
            item.setText(_translate("MainWindow", str(request[3])))
            RowTable += 1

    @staticmethod
    def __NewItem():
        return QTableWidgetItem()

    def __SetItem(self, index):
        self.view.tableWidget.setVerticalHeaderItem(index, self.__NewItem())
        self.view.tableWidget.setItem(index, 0, self.__NewItem())
        self.view.tableWidget.setItem(index, 1, self.__NewItem())
        self.view.tableWidget.setItem(index, 2, self.__NewItem())
        self.view.tableWidget.setItem(index, 3, self.__NewItem())

    def __CreateActiveOrder(self):
        if self.__driver.IdOrderClient is not None:
            self.__CreateBtnOpenMap(self.view.frame)
            self.__CreateBtnCloseOrder(self.view.frame)
            frame = self.__CreateFrame(self.view.frame)
            self.__CreateTextEdits(frame)
            self.__FillingTextEdits()
            self.__CreateLineEdits(frame)

    def __CreateFrame(self, parent: QWidget) -> QWidget:
        self.view.frame_2 = QFrame(parent)
        self.view.frame_2.setGeometry(QRect(20, 50, 351, 351))
        self.view.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.view.frame_2.setFrameShape(QFrame.StyledPanel)
        self.view.frame_2.setFrameShadow(QFrame.Raised)
        self.view.frame_2.setObjectName("frame_2")
        return self.view.frame_2

    def __CreateTextEdits(self, parent: QWidget):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        self.view.textEdit_IDCargo = QTextEdit(parent)
        self.view.textEdit_IDCargo.setGeometry(QRect(140, 20, 191, 31))
        self.view.textEdit_IDCargo.setFont(font)
        self.view.textEdit_IDCargo.setStyleSheet("background-color: rgb(221, 248, 214);")
        self.view.textEdit_IDCargo.setReadOnly(True)
        self.view.textEdit_IDCargo.setObjectName("textEdit_IDCargo")

        self.view.textEdit_cargo = QTextEdit(parent)
        self.view.textEdit_cargo.setGeometry(QRect(140, 60, 191, 31))
        self.view.textEdit_cargo.setFont(font)
        self.view.textEdit_cargo.setStyleSheet("background-color: rgb(221, 248, 214);")
        self.view.textEdit_cargo.setReadOnly(True)
        self.view.textEdit_cargo.setObjectName("textEdit_cargo")

        self.view.textEdit_FirstNameClient = QTextEdit(parent)
        self.view.textEdit_FirstNameClient.setGeometry(QRect(140, 100, 191, 31))
        self.view.textEdit_FirstNameClient.setFont(font)
        self.view.textEdit_FirstNameClient.setStyleSheet("background-color: rgb(221, 248, 214);")
        self.view.textEdit_FirstNameClient.setReadOnly(True)
        self.view.textEdit_FirstNameClient.setObjectName("textEdit_FirstNameClient")

        self.view.textEdit_LastNameClient = QTextEdit(parent)
        self.view.textEdit_LastNameClient.setGeometry(QRect(140, 140, 191, 31))
        self.view.textEdit_LastNameClient.setFont(font)
        self.view.textEdit_LastNameClient.setStyleSheet("background-color: rgb(221, 248, 214);")
        self.view.textEdit_LastNameClient.setReadOnly(True)
        self.view.textEdit_LastNameClient.setObjectName("textEdit_LastNameClient")

        self.view.textEdit_PlaceDeparture = QTextEdit(parent)
        self.view.textEdit_PlaceDeparture.setGeometry(QRect(140, 180, 191, 31))
        self.view.textEdit_PlaceDeparture.setFont(font)
        self.view.textEdit_PlaceDeparture.setStyleSheet("background-color: rgb(221, 248, 214);")
        self.view.textEdit_PlaceDeparture.setReadOnly(True)
        self.view.textEdit_PlaceDeparture.setObjectName("textEdit_PlaceDeparture")

        self.view.textEdit_PlaceDelivery = QTextEdit(parent)
        self.view.textEdit_PlaceDelivery.setGeometry(QRect(140, 220, 191, 31))
        self.view.textEdit_PlaceDelivery.setFont(font)
        self.view.textEdit_PlaceDelivery.setStyleSheet("background-color: rgb(221, 248, 214);")
        self.view.textEdit_PlaceDelivery.setReadOnly(True)
        self.view.textEdit_PlaceDelivery.setObjectName("textEdit_PlaceDelivery")

        self.view.textEdit_CargoWight = QTextEdit(parent)
        self.view.textEdit_CargoWight.setGeometry(QRect(140, 260, 191, 31))
        self.view.textEdit_CargoWight.setFont(font)
        self.view.textEdit_CargoWight.setStyleSheet("background-color: rgb(221, 248, 214);")
        self.view.textEdit_CargoWight.setReadOnly(True)
        self.view.textEdit_CargoWight.setObjectName("textEdit_CargoWight")

        self.view.textEdit_Distance = QTextEdit(parent)
        self.view.textEdit_Distance.setGeometry(QRect(140, 300, 191, 31))
        self.view.textEdit_Distance.setFont(font)
        self.view.textEdit_Distance.setStyleSheet("background-color: rgb(221, 248, 214);")
        self.view.textEdit_Distance.setReadOnly(True)
        self.view.textEdit_Distance.setObjectName("textEdit_Distance")


    def __FillingTextEdits(self):
        self.ActiveOrder = self.__model.GetActiveOrder(self.__driver.ID)
        distance = self.__CalculatorDistance(self.ActiveOrder[4], self.ActiveOrder[5])
        self.view.textEdit_IDCargo.setText(str(self.ActiveOrder[0]))
        self.view.textEdit_cargo.setText(self.ActiveOrder[1])
        self.view.textEdit_FirstNameClient.setText(self.ActiveOrder[2])
        self.view.textEdit_LastNameClient.setText(self.ActiveOrder[3])
        self.view.textEdit_PlaceDeparture.setText(self.ActiveOrder[4])
        self.view.textEdit_PlaceDelivery.setText(self.ActiveOrder[5])
        self.view.textEdit_CargoWight.setText(str(self.ActiveOrder[6]))
        self.view.textEdit_Distance.setText(str(distance))

    @staticmethod
    def __CalculatorDistance(PlaceDeparture, PlaceDelivery):
        locator = Nominatim(user_agent="myapp")
        start_latlng = locator.geocode(PlaceDeparture)
        end_latlng = locator.geocode(PlaceDelivery)
        if start_latlng is None or end_latlng is None:
            return "ошибка расстояния"
        start_coordinates = (start_latlng.latitude, start_latlng.longitude)
        end_coordinates = (end_latlng.latitude, end_latlng.longitude)
        return f"{round(geodesic(start_coordinates, end_coordinates).km, 2)} км"

    def __CreateLineEdits(self, parent: QWidget):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        _translate = QCoreApplication.translate

        self.view.lineEdit_IDCargo = QLineEdit(parent)
        self.view.lineEdit_IDCargo.setGeometry(QRect(10, 25, 71, 22))
        self.view.lineEdit_IDCargo.setFont(font)
        self.view.lineEdit_IDCargo.setStyleSheet("border: 0px")
        self.view.lineEdit_IDCargo.setReadOnly(True)
        self.view.lineEdit_IDCargo.setObjectName("lineEdit_IDCargo")
        self.view.lineEdit_IDCargo.setText(_translate("MainWindow", "ID товара"))

        self.view.lineEdit_Cargo = QLineEdit(parent)
        self.view.lineEdit_Cargo.setGeometry(QRect(10, 63, 41, 22))
        self.view.lineEdit_Cargo.setFont(font)
        self.view.lineEdit_Cargo.setStyleSheet("border: 0px")
        self.view.lineEdit_Cargo.setReadOnly(True)
        self.view.lineEdit_Cargo.setObjectName("lineEdit_Cargo")
        self.view.lineEdit_Cargo.setText(_translate("MainWindow", "Груз"))

        self.view.lineEdit_FirstNameClient = QLineEdit(parent)
        self.view.lineEdit_FirstNameClient.setGeometry(QRect(10, 100, 91, 22))
        self.view.lineEdit_FirstNameClient.setFont(font)
        self.view.lineEdit_FirstNameClient.setStyleSheet("border: 0px")
        self.view.lineEdit_FirstNameClient.setReadOnly(True)
        self.view.lineEdit_FirstNameClient.setObjectName("lineEdit_FirstNameClient")
        self.view.lineEdit_FirstNameClient.setText(_translate("MainWindow", "Имя клиента"))

        self.view.lineEdit_LastNameClient = QLineEdit(parent)
        self.view.lineEdit_LastNameClient.setGeometry(QRect(10, 140, 111, 22))
        self.view.lineEdit_LastNameClient.setFont(font)
        self.view.lineEdit_LastNameClient.setStyleSheet("border: 0px")
        self.view.lineEdit_LastNameClient.setReadOnly(True)
        self.view.lineEdit_LastNameClient.setObjectName("lineEdit_LastNameClient")
        self.view.lineEdit_LastNameClient.setText(_translate("MainWindow", "Фамилия клиента"))

        self.view.lineEdit_PlaceDeparture = QLineEdit(parent)
        self.view.lineEdit_PlaceDeparture.setGeometry(QRect(10, 180, 121, 22))
        self.view.lineEdit_PlaceDeparture.setFont(font)
        self.view.lineEdit_PlaceDeparture.setStyleSheet("border: 0px")
        self.view.lineEdit_PlaceDeparture.setReadOnly(True)
        self.view.lineEdit_PlaceDeparture.setObjectName("lineEdit_PlaceDeparture")
        self.view.lineEdit_PlaceDeparture.setText(_translate("MainWindow", "Место отправления"))

        self.view.lineEdit_PlaceDelivery = QLineEdit(parent)
        self.view.lineEdit_PlaceDelivery.setGeometry(QRect(10, 220, 121, 22))
        self.view.lineEdit_PlaceDelivery.setFont(font)
        self.view.lineEdit_PlaceDelivery.setStyleSheet("border: 0px")
        self.view.lineEdit_PlaceDelivery.setReadOnly(True)
        self.view.lineEdit_PlaceDelivery.setObjectName("lineEdit_PlaceDelivery")
        self.view.lineEdit_PlaceDelivery.setText(_translate("MainWindow", "Место прибытия"))

        self.view.lineEdit_CargoWight = QLineEdit(parent)
        self.view.lineEdit_CargoWight.setGeometry(QRect(10, 260, 121, 22))
        self.view.lineEdit_CargoWight.setFont(font)
        self.view.lineEdit_CargoWight.setStyleSheet("border: 0px")
        self.view.lineEdit_CargoWight.setReadOnly(True)
        self.view.lineEdit_CargoWight.setObjectName("lineEdit_PlaceDelivery")
        self.view.lineEdit_CargoWight.setText(_translate("MainWindow", "Вес груза"))

        self.view.lineEdit_Distance = QLineEdit(parent)
        self.view.lineEdit_Distance.setGeometry(QRect(10, 300, 121, 22))
        self.view.lineEdit_Distance.setFont(font)
        self.view.lineEdit_Distance.setStyleSheet("border: 0px")
        self.view.lineEdit_Distance.setReadOnly(True)
        self.view.lineEdit_Distance.setObjectName("lineEdit_Distance")
        self.view.lineEdit_Distance.setText(_translate("MainWindow", "Расстояние"))

    def __CreateBtnOpenMap(self, parent: QWidget):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        _translate = QCoreApplication.translate

        self.view.pushButton_Map = QPushButton(parent)
        self.view.pushButton_Map.setFont(font)
        self.view.pushButton_Map.setGeometry(QRect(20, 415, 351, 28))
        self.view.pushButton_Map.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "border-radius: 10px")
        self.view.pushButton_Map.setObjectName("pushButton_Map")
        self.view.pushButton_Map.setText(_translate("MainWindow", "Показать на карте"))
        self.view.pushButton_Map.clicked.connect(self.__ClickedMap)

    def __ClickedMap(self):
        if self.view.textEdit_Distance.toPlainText() != "ошибка расстояния":
            self.map = ControllerMap(self.ActiveOrder[4], self.ActiveOrder[5], self)
            self.map.RunViewMap()
            self.MainWindow.setEnabled(False)
        else:
            self.view.message("Информация", "Извините, видимо указанный город, не существует")

    def __CreateBtnCloseOrder(self, parent: QWidget):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        _translate = QCoreApplication.translate

        self.view.pushButton_CloseOrder = QPushButton(parent)
        self.view.pushButton_CloseOrder.setFont(font)
        self.view.pushButton_CloseOrder.setGeometry(QRect(20, 450, 351, 28))
        self.view.pushButton_CloseOrder.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "border-radius: 10px")
        self.view.pushButton_CloseOrder.setObjectName("pushButton_CloseOrder")
        self.view.pushButton_CloseOrder.setText(_translate("MainWindow", "Закрыть заказ"))
        self.view.pushButton_CloseOrder.clicked.connect(self.__ClickedCloseOrder)

    def __ClickedCloseOrder(self):
        IdOrder = self.ActiveOrder[0]
        IdDrivers = self.__model.GetIdDriverByIdOrder(IdOrder)
        Request = self.__model.GetAcceptRequest(IdOrder)
        Request = self.__FillingDeliveredRequest(Request)
        self.__model.DeleteAcceptRequest(IdOrder)
        for id_driver in IdDrivers:
            Request.IdDriver = id_driver[0]
            self.__model.AddDeliveredRequest(Request)
        self.__driver.IdOrderClient = None
        self.__ClearActiveOrder()
            # self.AddRequestInTable(Request)

    def __ClearActiveOrder(self):
        self.view.frame_2.close()
        self.view.pushButton_CloseOrder.close()
        self.view.pushButton_Map.close()

    def __AddRequestInTable(self, Request: DeliveredRequest):
        _translate = QCoreApplication.translate
        rowCount = self.view.tableWidget.rowCount()
        self.view.tableWidget.setRowCount(rowCount + 1)
        self.__SetItem(rowCount)
        item = self.view.tableWidget.verticalHeaderItem(rowCount)
        item.setText(_translate("MainWindow", ""))
        item = self.view.tableWidget.item(rowCount, 0)
        item.setText(_translate("MainWindow", str(Request.ID)))
        item = self.view.tableWidget.item(rowCount, 1)
        item.setText(_translate("MainWindow",  Request.PlaceDeparture))
        item = self.view.tableWidget.item(rowCount, 2)
        item.setText(_translate("MainWindow",  Request.PlaceDelivery))
        item = self.view.tableWidget.item(rowCount, 3)
        item.setText(_translate("MainWindow",  str(Request.Revenue)))

    def __FillingDeliveredRequest(self, AcceptRequest):
        deliveredRequest = DeliveredRequest()
        deliveredRequest.ID = AcceptRequest[0]
        deliveredRequest.FirstName = AcceptRequest[1]
        deliveredRequest.LastName = AcceptRequest[2]
        deliveredRequest.Email = AcceptRequest[3]
        deliveredRequest.NumberPhone = AcceptRequest[4]
        deliveredRequest.PlaceDeparture = AcceptRequest[5]
        deliveredRequest.PlaceDelivery = AcceptRequest[6]
        deliveredRequest.CargoWeight = AcceptRequest[7]
        deliveredRequest.CargoDescription = AcceptRequest[8]
        deliveredRequest.IdClient = AcceptRequest[9]
        return deliveredRequest

    def __ClickedProfile(self):
        self.__DriverProfile = ControllerDriverProfile(self.__driver, self)
        self.__DriverProfile.RunViewDriverProfile()
        self.MainWindow.setEnabled(False)

    def __ClickedExit(self):
        self.MainWindow.close()

