from TransportCompany.Model.Admin.ModelWindowApplication import ModelWindowApplication
from TransportCompany.View.Admin.ViewWindowApplication import ViewWindowApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
import sys

class ControllerWindowApplication:
    def __init__(self):
        self.model = ModelWindowApplication()
        self.view = ViewWindowApplication()
        self._translate = QCoreApplication.translate
        self.SettingsUI()
        self.FillingTable(self.model.GetSortByDecreaseDate())
        self.view.comboBox_SortTable.currentIndexChanged.connect(self.IdexChangeSortTable)
        self.view.pushButton_Search_date.clicked.connect(self.SearchDate)
        self.view.pushButton_Search_Client.clicked.connect(self.SearchClient)
        self.view.pushButton_AllRequest.clicked.connect(self.AllRequest)
        self.view.action_exit.triggered.connect(self.Exit)
    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.WindowApplication = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.WindowApplication)

    def RunViewWindowApplication(self):
        self.WindowApplication.show()


    def FillingTable(self, values):
        self.view.tableWidget_TableApplication.setRowCount(len(values))
        for index, element in enumerate(values):
            self.SetItem(index)
            item = self.view.tableWidget_TableApplication.verticalHeaderItem(index)
            item.setText(self._translate("MainWindow", str(index + 1)))
            item = self.view.tableWidget_TableApplication.item(index, 0)
            item.setText(self._translate("MainWindow", values[index][0]))
            item = self.view.tableWidget_TableApplication.item(index, 1)
            item.setText(self._translate("MainWindow", values[index][1]))
            item = self.view.tableWidget_TableApplication.item(index, 2)
            item.setText(self._translate("MainWindow", str(values[index][2]).replace("-", ".")))

    def NewItem(self):
        return QtWidgets.QTableWidgetItem()

    def SetItem(self, index):
        self.view.tableWidget_TableApplication.setVerticalHeaderItem(index, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 0, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 1, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 2, self.NewItem())

    def IdexChangeSortTable(self):
        if self.view.comboBox_SortTable.currentText() == "По убывающей дате":
            self.FillingTable(self.model.GetSortByDecreaseDate())
        elif self.view.comboBox_SortTable.currentText() == "По возрастающей дате":
            self.FillingTable(self.model.GetSortByEscalatingDate())
        elif self.view.comboBox_SortTable.currentText() == "В алфавитном порядке":
            self.FillingTable(self.model.GetSortByAlphabeticalOrder())
        elif self.view.comboBox_SortTable.currentText() == "В обратном алфавитном порядке":
            self.FillingTable(self.model.GetSortReverseAlphabeticalOrder())
        pass

    def ChoiceParameterDate(self, date: str):
        ComponentsDate = list(map(int, date.split(".")))
        year = ComponentsDate[2]
        month = ComponentsDate[1]
        day = ComponentsDate[0]
        if self.view.comboBox_Date.currentText() == "По полной дате":
            self.FillingTable(self.model.GetRequestByDate(date))
        elif self.view.comboBox_Date.currentText() == "По году и месяцу":
            self.FillingTable(self.model.GetRequestByYearAndMonth(year, month))
        elif self.view.comboBox_Date.currentText() == "По году и дню":
            self.FillingTable(self.model.GetRequestByYearAndDay(year, day))
        elif self.view.comboBox_Date.currentText() == "По месяцу и дню":
            self.FillingTable(self.model.GetRequestByMonthAndDay(month, day))
        elif self.view.comboBox_Date.currentText() == "По году":
            self.FillingTable(self.model.GetRequestByYear(year))
        elif self.view.comboBox_Date.currentText() == "По месяцу":
            self.FillingTable(self.model.GetRequestByMonth(month))
        elif self.view.comboBox_Date.currentText() == "По дню":
            self.FillingTable(self.model.GetRequestByDay(day))

    def ChoiceParameterClient(self, text):
        if self.view.comboBox_Client.currentText() == "По имени":
            self.FillingTable(self.model.GetRequestByFirstName(text))
        elif self.view.comboBox_Client.currentText() == "По фамилии":
            self.FillingTable(self.model.GetRequestByLastName(text))


    def SearchDate(self):
        date = self.view.dateEdit_Searchdate.text()
        self.ChoiceParameterDate(date)

    def SearchClient(self):
        text = self.view.lineEdit_SearchClient.text()
        self.ChoiceParameterClient(text)

    def AllRequest(self):
        values = self.model.GetSortByDecreaseDate()
        self.FillingTable(values)

    def Exit(self):
        self.WindowApplication.close()





