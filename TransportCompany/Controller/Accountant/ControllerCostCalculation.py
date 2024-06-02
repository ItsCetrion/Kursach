from TransportCompany.View.Accountant.ViewCostCalculation import ViewCostCalculation
from TransportCompany.Model.Accountant.ModelCostCalculation import ModelCostCalculation
from TransportCompany.SecondaryPyFile.CalculatingCostTrip import CostTrip
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from PyQt5.QtWidgets import QApplication, QMainWindow
from sys import argv

class ControllerCostCalculation:
    def __init__(self, parent):
        self.view = ViewCostCalculation()
        self.__model = ModelCostCalculation()
        self.__parent = parent
        self.__SettingsUI()
        self.__CostCalculation.closeEvent = self.__closeEvent

        self.view.radioButton_DangerousCargo.clicked.connect(self.__ClickedDangerousCargo)
        self.view.pushButton_Back.clicked.connect(self.__ClickedBack)
        self.view.pushButton_Confirm.clicked.connect(self.__ClickedConfirm)

    def __SettingsUI(self):
        self.__app = QApplication(argv)
        self.__CostCalculation = QMainWindow()
        ui = self.view
        ui.setupUi(self.__CostCalculation)

    def RunViewCostCalculation(self):
        self.__CostCalculation.show()

    def FillingFields(self, InfoOrderAndDriver, id_order):
        self.id_order = id_order
        self.InfoOrderAndDriver = InfoOrderAndDriver
        self.CountDriver = len(InfoOrderAndDriver)
        self.__FillingFieldDistance(InfoOrderAndDriver[0][6], InfoOrderAndDriver[0][7])
        self.__FillingFieldProfitCompany(InfoOrderAndDriver[0][8])
        if self.CountDriver == 1:
            self.__FillingFieldsDriver1(InfoOrderAndDriver[0])
        elif self.CountDriver == 2:
            self.__FillingFieldsDriver1(InfoOrderAndDriver[0])
            self.__FillingFieldsDriver2(InfoOrderAndDriver[1])

    def __FillingFieldsDriver1(self, InfoDriver):
        self.view.lineEdit_FirstName.setText(InfoDriver[1])
        self.view.lineEdit_LastName.setText(InfoDriver[2])
        self.view.lineEdit_Patronymic.setText(InfoDriver[3])
        self.view.lineEdit_Email.setText(InfoDriver[4])
        self.view.lineEdit_Experience.setText(str(InfoDriver[5]))
        ProfitDriver1 = self.__CalculationProfitDriver(InfoDriver[5], self.CountDriver)
        self.view.lineEdit_ProfitDriver.setText(ProfitDriver1)

        self.ProfitDriver1 = ProfitDriver1

    def __FillingFieldsDriver2(self, InfoDriver):
        self.view.lineEdit_FirstName2.setText(InfoDriver[1])
        self.view.lineEdit_LastName2.setText(InfoDriver[2])
        self.view.lineEdit_Patronymic2.setText(InfoDriver[3])
        self.view.lineEdit_Email2.setText(InfoDriver[4])
        self.view.lineEdit_Experience2.setText(str(InfoDriver[5]))
        ProfitDriver2 = self.__CalculationProfitDriver(InfoDriver[5], self.CountDriver)
        self.view.lineEdit_ProfitDriver2.setText(ProfitDriver2)

        self.ProfitDriver2 = ProfitDriver2

    def __CalculationProfitDriver(self, experience, CountDriver):
        IncomePerTrip = self.view.lineEdit_ProfitCompany.text()
        try:
            IncomePerTrip = float(IncomePerTrip)
            InterestRateDriver = self.__InterestRateDriver(experience)
            result = IncomePerTrip * InterestRateDriver
            return str(result // CountDriver)
        except ValueError:
            return "Доход не определен"

    @staticmethod
    def __InterestRateDriver(experience):
        if experience <= 2: return 0.1
        if experience <= 5: return 0.12
        if experience <= 10: return 0.15
        if experience <= 20: return 0.17
        if experience > 20: return 0.2

    def __FillingFieldDistance(self, StartLocation, EndLocation):
        distance = self.__CalculatingDistance(StartLocation, EndLocation)
        self.view.lineEdit_Distance.setText(str(distance))

    @staticmethod
    def __CalculatingDistance(StartLocation, EndLocation):
        locator = Nominatim(user_agent="myapp")
        start_latlng = locator.geocode(StartLocation)
        end_latlng = locator.geocode(EndLocation)
        if start_latlng is None or end_latlng is None:
            return "ошибка расстояния"
        start_coordinates = (start_latlng.latitude, start_latlng.longitude)
        end_coordinates = (end_latlng.latitude, end_latlng.longitude)
        return round(geodesic(start_coordinates, end_coordinates).km, 2)

    def __FillingFieldProfitCompany(self, wight):
        try:
            distance = float(self.view.lineEdit_Distance.text())
            profit = round(CostTrip().Calcilating(distance, int(wight)), 2)
            self.view.lineEdit_ProfitCompany.setText(str(profit))
        except ValueError:
            self.view.lineEdit_ProfitCompany.setText("Доход не определен.Один из адресов некорректен")
            self.view.pushButton_Confirm.setEnabled(False)

    def __ClickedDangerousCargo(self):
        try:
            if self.view.radioButton_DangerousCargo.isChecked():
                self.__NewProfit(self.view.lineEdit_ProfitDriver)
                if self.CountDriver == 2:
                    self.__NewProfit(self.view.lineEdit_ProfitDriver2)
            else:
                self.view.lineEdit_ProfitDriver.setText(self.ProfitDriver1)
                if self.CountDriver == 2:
                    self.view.lineEdit_ProfitDriver2.setText(self.ProfitDriver2)
        except ValueError:
            pass

    def __NewProfit(self, lineEdit):
        IncomePerTrip = float(self.view.lineEdit_ProfitCompany.text())
        OldProfitDriver = float(lineEdit.text())
        OldInterestRateDriver = (OldProfitDriver * 100) / IncomePerTrip
        NewProfitDriver = round(IncomePerTrip * ((OldInterestRateDriver + 10) / 100), 2)
        lineEdit.setText(str(NewProfitDriver))
        
    def __closeEvent(self, event):
        self.__parent.ListDeliveredOrders.setEnabled(True)
        event.accept()

    def __ClickedConfirm(self):
        try:
            if self.CountDriver == 2:
                self.__model.UpdateRevenue(self.InfoOrderAndDriver[0][0], self.id_order,
                                           float(self.view.lineEdit_ProfitDriver.text()))
                self.__model.UpdateRevenue(self.InfoOrderAndDriver[1][0], self.id_order,
                                           float(self.view.lineEdit_ProfitDriver2.text()))
            elif self.CountDriver == 1:
                self.__model.UpdateRevenue(self.InfoOrderAndDriver[0][0], self.id_order,
                                           float(self.view.lineEdit_ProfitDriver.text()))
            self.view.message("Информация", "Доход за поездку успешно назначен водителям")
            row = self.__parent.view.tableWidget_TableApplication.currentRow()
            self.__parent.view.tableWidget_TableApplication.removeRow(row)
            self.__parent.view.lcdNumber.display(self.__parent.view.lcdNumber.value() - 1)
            self.__CostCalculation.close()
        except ValueError:
            pass

    def __ClickedBack(self):
        self.__CostCalculation.close()
