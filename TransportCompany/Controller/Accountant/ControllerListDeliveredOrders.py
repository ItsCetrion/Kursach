from TransportCompany.View.Accountant.ViewListDeliveredOrders import ViewListDeliveredOrders
from TransportCompany.Model.Accountant.ModelListDeliveredOrders import ModelListDeliveredOrders
from TransportCompany.Controller.Accountant.ControllerAccountantProfile import ControllerAccountantProfile
from TransportCompany.Controller.Accountant.ControllerCostCalculation import ControllerCostCalculation
from TransportCompany.Entities.Accountant import Accountant
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QCoreApplication, Qt
from sys import argv


class ControllerListDeliveredOrders:
    def __init__(self, accountant: Accountant):
        self.__view = ViewListDeliveredOrders()
        self.__model = ModelListDeliveredOrders()
        self.__accountant = accountant
        self.__sort = "ASC"
        self.__FlagSearch = False
        self.__SettingsUI()
        self.__FillingTable(self.__model.GetAllCompletedOrders(sort=self.__sort))
        self.__CostCalculation = None

        self.__view.comboBox_SortTable_2.currentTextChanged.connect(self.__ChangeSort)
        self.__view.pushButton_Search.clicked.connect(self.__ClickedSearch)
        self.__view.pushButton_ResetSearch.clicked.connect(self.__ClickedResetSeacrch)
        self.__view.action_profile.triggered.connect(self.__ClickedProfile)
        self.__view.action_Exit.triggered.connect(self.__ClickedExit)
        self.__view.tableWidget_TableApplication.clicked.connect(self.__ClickedRow)

    def __SettingsUI(self):
        self.__app = QApplication(argv)
        self.ListDeliveredOrders = QMainWindow()
        ui = self.__view
        ui.setupUi(self.ListDeliveredOrders)

    def RunViewListDeliveredOrders(self):
        self.ListDeliveredOrders.show()
        self.__CheckHavePassword()
        # sys.exit(self.app.exec_())

    def __CheckHavePassword(self):
        if self.__accountant.Password is None:
            self.AccountantProfile = ControllerAccountantProfile(self.__accountant, self)
            self.AccountantProfile.RunViewWindowApplication()
            self.ListDeliveredOrders.setEnabled(False)
            self.__view.message("Информация", "Произведен первый запуск приложения.\nНеобходимо установить пароль")

    def __FillingTable(self, orders: list):
        self.__view.tableWidget_TableApplication.setRowCount(len(orders))
        self.__view.lcdNumber.display(len(orders))
        _translate = QCoreApplication.translate
        RowTable = 0
        for request in orders:
            self.__SetItem(RowTable)
            item = self.__view.tableWidget_TableApplication.verticalHeaderItem(RowTable)
            item.setText(_translate("MainWindow", ""))
            item = self.__view.tableWidget_TableApplication.item(RowTable, 0)
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(_translate("MainWindow", str(request[0])))
            item = self.__view.tableWidget_TableApplication.item(RowTable, 1)
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(_translate("MainWindow", request[1]))
            item = self.__view.tableWidget_TableApplication.item(RowTable, 2)
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(_translate("MainWindow", request[2]))
            RowTable += 1

    @staticmethod
    def __NewItem():
        return QTableWidgetItem()

    def __SetItem(self, index):
        self.__view.tableWidget_TableApplication.setVerticalHeaderItem(index, self.__NewItem())
        self.__view.tableWidget_TableApplication.setItem(index, 0, self.__NewItem())
        self.__view.tableWidget_TableApplication.setItem(index, 1, self.__NewItem())
        self.__view.tableWidget_TableApplication.setItem(index, 2, self.__NewItem())

    def __ChangeSort(self, text):
        if text == "По убыванию":
            self.__sort = "DESC"
        elif text == "По возрастанию":
            self.__sort = "ASC"
        if not self.__FlagSearch:
            self.__FillingTable(self.__model.GetAllCompletedOrders(self.__sort))

    def __ClickedSearch(self):
            NumberOrder = self.__view.lineEdit_NumberOrder.text()
            if NumberOrder != "":
                NumberOrder = int(NumberOrder)
                order = self.__model.GetOrderByIdOrder(NumberOrder)
                self.__view.lcdNumber.display(len(order))
                self.__view.tableWidget_TableApplication.clearContents()
                self.__FillingTable(order)
                self.__FlagSearch = True

    def __ClickedResetSeacrch(self):
        self.__view.tableWidget_TableApplication.clearContents()
        self.__sort = "ASC"
        self.__view.lineEdit_NumberOrder.clear()
        self.__FlagSearch = False
        self.__view.comboBox_SortTable_2.setCurrentIndex(0)
        self.__FillingTable(self.__model.GetAllCompletedOrders(sort=self.__sort))

    def __ClickedProfile(self):
        self.AccountantProfile = ControllerAccountantProfile(self.__accountant, self)
        self.AccountantProfile.RunViewWindowApplication()
        self.ListDeliveredOrders.setEnabled(False)

    def __ClickedRow(self):
        row = self.__view.tableWidget_TableApplication.currentRow()
        id_order = self.__view.tableWidget_TableApplication.item(row, 0).text()
        InfoOrderAndDriver = self.__model.GetInfoOrderAndDriver(id_order)
        self.ListDeliveredOrders.setEnabled(False)
        if self.__CostCalculation is None:
            self.__CostCalculation = ControllerCostCalculation(self)
            self.__CostCalculation.FillingFields(InfoOrderAndDriver, id_order)
            self.__CostCalculation.RunViewCostCalculation()
        else:
            self.__CostCalculation.FillingFields(InfoOrderAndDriver, id_order)
            self.__CostCalculation.RunViewCostCalculation()

    def __ClickedExit(self):
        self.ListDeliveredOrders.close()
