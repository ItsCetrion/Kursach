from TransportCompany.View.Accountant.ViewListDeliveredOrders import ViewListDeliveredOrders
from TransportCompany.Model.Accountant.ModelListDeliveredOrders import ModelListDeliveredOrders
from TransportCompany.Controller.Accountant.ControllerAccountantProfile import ControllerAccountantProfile
from TransportCompany.Entities.Accountant import Accountant
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QCoreApplication, Qt
from sys import argv


class ControllerListDeliveredOrders:
    def __init__(self, accountant: Accountant):
        self.view = ViewListDeliveredOrders()
        self.model = ModelListDeliveredOrders()
        self.accountant = accountant
        self.sort = "ASC"
        self.FlagSearch = False
        self.SettingsUI()
        self.FillingTable(self.model.GetAllCompletedOrders(sort=self.sort))

        self.view.comboBox_SortTable_2.currentTextChanged.connect(self.ChangeSort)
        self.view.pushButton_Search.clicked.connect(self.ClickedSearch)
        self.view.pushButton_ResetSearch.clicked.connect(self.ClickedResetSeacrch)
        self.view.action_profile.triggered.connect(self.ClickedProfile)
        self.view.action_Exit.triggered.connect(self.ClickedExit)

    def SettingsUI(self):
        self.app = QApplication(argv)
        self.ListDeliveredOrders = QMainWindow()
        ui = self.view
        ui.setupUi(self.ListDeliveredOrders)

    def RunViewListDeliveredOrders(self):
        self.ListDeliveredOrders.show()
        self.CheckHavePassword()
        # sys.exit(self.app.exec_())

    def CheckHavePassword(self):
        if self.accountant.Password is None:
            self.AccountantProfile = ControllerAccountantProfile(self.accountant, self)
            self.AccountantProfile.RunViewWindowApplication()
            self.ListDeliveredOrders.setEnabled(False)
            self.view.message("Информация", "Произведен первый запуск приложения.\nНеобходимо установить пароль")

    def FillingTable(self, orders: list):
        self.view.tableWidget_TableApplication.setRowCount(len(orders))
        self.view.lcdNumber.display(len(orders))
        _translate = QCoreApplication.translate
        RowTable = 0
        for request in orders:
            self.SetItem(RowTable)
            item = self.view.tableWidget_TableApplication.verticalHeaderItem(RowTable)
            item.setText(_translate("MainWindow", ""))
            item = self.view.tableWidget_TableApplication.item(RowTable, 0)
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(_translate("MainWindow", str(request[0])))
            item = self.view.tableWidget_TableApplication.item(RowTable, 1)
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(_translate("MainWindow", request[1]))
            item = self.view.tableWidget_TableApplication.item(RowTable, 2)
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(_translate("MainWindow", request[2]))
            RowTable += 1

    @staticmethod
    def NewItem():
        return QTableWidgetItem()

    def SetItem(self, index):
        self.view.tableWidget_TableApplication.setVerticalHeaderItem(index, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 0, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 1, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 2, self.NewItem())

    def ChangeSort(self, text):
        if text == "По убыванию":
            self.sort = "DESC"
        elif text == "По возрастанию":
            self.sort = "ASC"
        if not self.FlagSearch:
            self.FillingTable(self.model.GetAllCompletedOrders(self.sort))

    def ClickedSearch(self):
            NumberOrder = self.view.lineEdit_NumberOrder.text()
            if NumberOrder != "":
                NumberOrder = int(NumberOrder)
                order = self.model.GetOrderByIdOrder(NumberOrder)
                self.view.lcdNumber.display(len(order))
                self.view.tableWidget_TableApplication.clearContents()
                self.FillingTable(order)
                self.FlagSearch = True

    def ClickedResetSeacrch(self):
        self.view.tableWidget_TableApplication.clearContents()
        self.sort = "ASC"
        self.view.lineEdit_NumberOrder.clear()
        self.FlagSearch = False
        self.view.comboBox_SortTable_2.setCurrentIndex(0)
        self.FillingTable(self.model.GetAllCompletedOrders(sort=self.sort))

    def ClickedProfile(self):
        self.AccountantProfile = ControllerAccountantProfile(self.accountant, self)
        self.AccountantProfile.RunViewWindowApplication()
        self.ListDeliveredOrders.setEnabled(False)

    def ClickedExit(self):
        self.ListDeliveredOrders.close()
