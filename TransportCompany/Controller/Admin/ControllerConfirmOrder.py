from TransportCompany.Model.Admin.ModelConfirmOrder import ModelConfirmOrder
from TransportCompany.View.Admin.ViewConfirmOrder import ViewConfirmOrder
from TransportCompany.Model.Admin.ModelWindowApplication import ModelWindowApplication
from PyQt5 import QtWidgets
from TransportCompany.Entities.Request import Request
from TransportCompany.Entities.Driver import Driver
import sys
class ControllerConfirmOrder:
    def __init__(self, parent):
        self.model = ModelConfirmOrder()
        self.view = ViewConfirmOrder()
        self.SettingsUI()
        self.parent = parent

        self.view.pushButton_Back.clicked.connect(self.ClickedBack)
        self.view.pushButton_Confirm.clicked.connect(self.ClickedConfirm)
        self.FillinComboBoxDriver(self.view.comboBox_1Driver, self.model.Get5Driver())
        self.view.radioButton_Change2Driver.clicked.connect(self.ClickedChange2Driver)

    def ClickedChange2Driver(self):
        if self.view.radioButton_Change2Driver.isChecked():
            self.view.comboBox_2Driver.setEnabled(True)
            text = self.view.comboBox_1Driver.currentText()
            quantity = self.view.comboBox_1Driver.count()
            if text != "Нет свободных водителей" and quantity > 1:
                self.FillinComboBoxDriver(self.view.comboBox_2Driver,
                                          self.model.Get5DriverWithException(self.view.comboBox_1Driver.itemData(self.view.comboBox_1Driver.currentIndex())))
            else:
                self.view.comboBox_2Driver.addItem("Нет свободных водителей")
        else:
            self.view.comboBox_2Driver.setEnabled(False)
            self.view.comboBox_2Driver.clear()
    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ConfirmOrder = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.ConfirmOrder)

    def RunConfirmOrder(self):
        self.ConfirmOrder.show()

    def FillingFields(self, request: Request):
        self.request = request
        self.view.textEdit_Dispatch.setText(request.PlaceDeparture)
        self.view.textEdit_Delivery.setText(request.PlaceDelivery)
        self.view.textEdit_Cargoinfo.setText(f"Описание: {request.CargoDescription}\nВес(кг): {request.CargoWeight}")


    def FillinComboBoxDriver(self, combobox,  drivers):
        # DriversInfo = []
        if len(drivers) == 0:
            combobox.addItem("Нет свободных водителей")
        for DriverInfo in drivers:
            FIO = f"{DriverInfo[0]} {DriverInfo[1]} {DriverInfo[2]} " \
                  f"(стаж: {DriverInfo[3]} {'года' if DriverInfo[3] < 5 else 'лет'})"
            combobox.addItem(FIO, DriverInfo[4])


    def ClickedBack(self):
        self.ConfirmOrder.close()
        self.parent.RunViewConsiderationApplication()

    def CheckParameters(self) -> bool:
        if self.view.comboBox_1Driver.currentText() == "Нет свободных водителей": return False
        if self.view.radioButton_Change2Driver.isChecked() \
                and self.view.comboBox_2Driver.currentText() == "Нет свободных водителей": return False
        if self.view.comboBox_1Driver.currentText() == self.view.comboBox_2Driver.currentText(): return False
        else: return True
    def ClickedConfirm(self):
        if self.CheckParameters():
            ModelWindowApplication().DeleteRequest(self.request.ID)
            self.model.AddAcceptRequest(self.request)
            IdDriver1 = self.view.comboBox_1Driver.itemData(self.view.comboBox_1Driver.currentIndex())
            self.model.UpdateDriver(self.request.ID, IdDriver1)
            if self.view.radioButton_Change2Driver.isChecked():
                IdDriver2 = self.view.comboBox_2Driver.itemData(self.view.comboBox_2Driver.currentIndex())
                self.model.UpdateDriver(self.request.ID, IdDriver2)
            self.view.message("Информация", "Заказ оформлен!")
            self.parent.DeleteRequestFromTable()
            self.ConfirmOrder.close()
            self.parent.Close()

        else:
            self.view.message("Информация", "Ошибка назначения водителя!")