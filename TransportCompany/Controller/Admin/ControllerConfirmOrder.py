from TransportCompany.Model.Admin.ModelConfirmOrder import ModelConfirmOrder
from TransportCompany.View.Admin.ViewConfirmOrder import ViewConfirmOrder
from TransportCompany.Model.Admin.ModelWindowApplication import ModelWindowApplication
from PyQt5 import QtWidgets
from TransportCompany.Entities.Request import Request
from TransportCompany.Entities.Driver import Driver
import sys


class ControllerConfirmOrder:
    def __init__(self, parent):
        self.__model = ModelConfirmOrder()
        self.view = ViewConfirmOrder()
        self.__SettingsUI()
        self.__parent = parent
        self.__ConfirmOrder.closeEvent = self.__closeEvent

        self.view.pushButton_Back.clicked.connect(self.__ClickedBack)
        self.view.pushButton_Confirm.clicked.connect(self.__ClickedConfirm)
        self.view.radioButton_Change2Driver.clicked.connect(self.__ClickedChange2Driver)

    def __ClickedChange2Driver(self):
        if self.view.radioButton_Change2Driver.isChecked():
            self.view.comboBox_2Driver.setEnabled(True)
            text = self.view.comboBox_1Driver.currentText()
            quantity = self.view.comboBox_1Driver.count()
            if text != "Нет свободных водителей" and quantity > 1:
                self.__FillinComboBoxDriver(self.view.comboBox_2Driver,
                                            self.__model.Get5DriverWithException(self.view.comboBox_1Driver.itemData(self.view.comboBox_1Driver.currentIndex())))
            else:
                self.view.comboBox_2Driver.addItem("Нет свободных водителей")
        else:
            self.view.comboBox_2Driver.setEnabled(False)
            self.view.comboBox_2Driver.clear()

    def __SettingsUI(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__ConfirmOrder = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.__ConfirmOrder)

    def RunConfirmOrder(self):
        self.__ConfirmOrder.show()

    def FillingFields(self, request: Request):
        self.request = request
        self.view.textEdit_Dispatch.setText(request.PlaceDeparture)
        self.view.textEdit_Delivery.setText(request.PlaceDelivery)
        self.view.textEdit_Cargoinfo.setText(f"Описание: {request.CargoDescription}\nВес(кг): {request.CargoWeight}")
        self.__FillinComboBoxDriver(self.view.comboBox_1Driver, self.__model.Get5Driver())

    def __FillinComboBoxDriver(self, combobox, drivers):
        # DriversInfo = []
        if len(drivers) == 0:
            combobox.addItem("Нет свободных водителей")
        for DriverInfo in drivers:
            FIO = f"{DriverInfo[0]} {DriverInfo[1]} {DriverInfo[2]} " \
                  f"(стаж: {DriverInfo[3]} {'года' if DriverInfo[3] < 5 else 'лет'})"
            combobox.addItem(FIO, DriverInfo[4])

    def __ClickedBack(self):
        self.__ConfirmOrder.close()

    def __CheckParameters(self) -> bool:
        if self.view.comboBox_1Driver.currentText() == "Нет свободных водителей": return False
        if self.view.radioButton_Change2Driver.isChecked() \
                and self.view.comboBox_2Driver.currentText() == "Нет свободных водителей": return False
        if self.view.comboBox_1Driver.currentText() == self.view.comboBox_2Driver.currentText(): return False
        else: return True

    def __ClickedConfirm(self):
        if self.__CheckParameters():
            ModelWindowApplication().DeleteRequest(self.request.ID)
            self.__model.AddAcceptRequest(self.request)
            IdDriver1 = self.view.comboBox_1Driver.itemData(self.view.comboBox_1Driver.currentIndex())
            self.__model.UpdateDriver(self.request.ID, IdDriver1)
            if self.view.radioButton_Change2Driver.isChecked():
                IdDriver2 = self.view.comboBox_2Driver.itemData(self.view.comboBox_2Driver.currentIndex())
                self.__model.UpdateDriver(self.request.ID, IdDriver2)
            self.view.message("Информация", "Заказ оформлен!")
            self.__parent.DeleteRequestFromTable()
            self.__ConfirmOrder.close()
            self.__parent.Close()

        else:
            self.view.message("Информация", "Ошибка назначения водителя!")

    def __closeEvent(self, event):
        self.view.comboBox_1Driver.clear()
        self.view.comboBox_2Driver.clear()
        self.view.radioButton_Change2Driver.setChecked(False)
        self.__parent.RunViewConsiderationApplication()
        event.accept()