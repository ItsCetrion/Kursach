from TransportCompany.Model.Admin.ModelWindowApplication import ModelWindowApplication
from TransportCompany.View.Admin.ViewWindowApplication import ViewWindowApplication
from TransportCompany.Controller.Admin.ControllerRegistrationWorker import ControllerRegistrationWorker
from TransportCompany.Controller.Admin.ControllerConsiderationApplication import ControllerConsiderationApplication
from TransportCompany.Entities.Request import Request
from TransportCompany.Entities.Administrator import Administrator
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QSize
import sys
from math import ceil


class ControllerWindowApplication:
    def __init__(self, admin: Administrator):
        self.__model = ModelWindowApplication()
        self.view = ViewWindowApplication()
        self._translate = QCoreApplication.translate
        self.__QuantityRequest = self.__model.GetAllQuantityReauest()
        self.__admin = admin
        self.__ListRequest = []
        self.__CursorPage = 1
        self.__ParameterSort = "DateRequest"
        self.__reverse = True
        self.__SaveRequest(self.__model.Get11RequestClients(StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))
        self.__SettingsUI()
        self.__FillingTable(NumberPage=1)
        self.__CreateButtonsPage()
        self.__IsFilterDate = False
        self.__IsFilterClient = False
        self.__FilterDate = None
        self.__FilterClient = None
        self.__ConsiderationApplication = None

        self.view.comboBox_SortTable.currentIndexChanged.connect(self.__IdexChangeSortTable)
        self.view.pushButton_Search_date.clicked.connect(self.__SearchDate)
        self.view.pushButton_Search_Client.clicked.connect(self.__SearchClient)
        self.view.action_exit.triggered.connect(self.__Exit)
        self.view.action_RegistrationWorker.triggered.connect(self.__OpenRegistrationWorker)
        self.view.tableWidget_TableApplication.clicked.connect(self.__ClickedRow)
        self.view.lcdNumber.display(self.__QuantityRequest)
        self.view.Button_Group.buttonClicked.connect(self.__ClickedButtonPage)
        self.view.pushButton_NextPage.clicked.connect(self.__ClickedNext)
        self.view.pushButton_BackPage.clicked.connect(self.__ClickedBack)
        self.view.pushButton_BackFirstPage.clicked.connect(self.__ClickedBackFirstPage)
        self.view.pushButton_UpdateTable.clicked.connect(self.__ClickedUpdateTable)

    def __SettingsUI(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.WindowApplication = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.WindowApplication)

    def RunViewWindowApplication(self):
        self.WindowApplication.show()

    def DeleteRequestFromTable(self):
        if ceil((self.__QuantityRequest - 1) / 11) == ceil(self.__QuantityRequest / 11) or \
                ceil((self.__QuantityRequest - 1) / 11) == 0:
            self.__QuantityRequest -= 1
            self.__ListRequest.clear()
            self.__SaveRequest(self.__СhoiceSaveRequest((self.__CursorPage - 1) * 11))
            self.__FillingTable(self.__CursorPage)
        elif ceil((self.__QuantityRequest - 1) / 11) < ceil(self.__QuantityRequest / 11):
            self.__QuantityRequest -= 1
            self.__CursorPage = 1 if self.__CursorPage - 1 == 0 else self.__CursorPage - 1
            self.__ClearLayout_ListNumberPages()
            self.__CreateButtonsPage()
            self.__ListRequest.clear()
            self.__SaveRequest(self.__СhoiceSaveRequest((self.__CursorPage - 1) * 11))
            self.__FillingTable(self.__CursorPage)

    def __ClickedUpdateTable(self):
        self.__QuantityRequest = self.__model.GetAllQuantityReauest()
        self.__UpdateTable()
        self.__BackBeginning()

    def __ClickedBackFirstPage(self):
        self.__BackBeginning()

    def __ClickedNext(self):
        if self.__CursorPage != (ceil(self.__QuantityRequest / 11)):
            self.__ClickedButtonPage(self.view.Button_Group.button(self.__CursorPage + 1))

    def __ClickedBack(self):
        if self.__CursorPage != 1:
            self.__ClickedButtonPage(self.view.Button_Group.button(self.__CursorPage - 1))

    def __CreateButtonsPage(self):
        if self.__QuantityRequest <= 55:  #55 - это 5 отображаемых страниц(на 1-ой странице по 11 заявок)
            self.__CreateButton(ceil(self.__QuantityRequest / 11))
        else:
            self.__CreateButton(5)
            self.__CreateButton(QuantityButton=1, ButtonText="...")
            self.__CreateButton(QuantityButton=1, ButtonText=str(ceil(self.__QuantityRequest / 11)))

    def __CreateButton(self, QuantityButton, ButtonText = None):
        if ButtonText is None:
            for page in range(1, QuantityButton + 1):
                name_btn = f"PushButton{page}"
                exec(f"self.view.{name_btn} = QtWidgets.QPushButton(self.view.horizontalLayoutWidget)")
                exec(f"self.view.{name_btn}.setMinimumSize(QSize(0, 25))")
                exec(f"self.view.{name_btn}.setStyleSheet('background-color: rgb(255, 255, 255); border: 2px solid gray;')")
                exec(f"self.view.{name_btn}.setObjectName('{name_btn}')")
                exec(f"self.view.horizontalLayout_ListNumberPages.addWidget(self.view.{name_btn})")
                exec(f'self.view.{name_btn}.setText(self._translate("MainWindow", str(page)))')
                exec(f'self.view.Button_Group.addButton(self.view.{name_btn}, page)')
            if 'PushButton1' in self.view.__dict__.keys():
                self.view.PushButton1.setStyleSheet('background-color: rgb(85, 255, 127); border: 2px solid gray;')
        elif ButtonText is not None:
            text = ButtonText
            if ButtonText == "...": ButtonText = "PushButtonEllipsis"
            elif ButtonText.isdigit(): ButtonText = "PushButton_Number"
            exec(f"self.view.{ButtonText} = QtWidgets.QPushButton(self.view.horizontalLayoutWidget)")
            exec(f"self.view.{ButtonText}.setMinimumSize(QSize(0, 25))")
            exec(f"self.view.{ButtonText}.setStyleSheet('background-color: rgb(255, 255, 255); border: 2px solid gray;')")
            exec(f"self.view.{ButtonText}.setObjectName('{ButtonText}')")
            exec(f"self.view.horizontalLayout_ListNumberPages.addWidget(self.view.{ButtonText})")
            exec(f'self.view.{ButtonText}.setText(self._translate("MainWindow", "{text}"))')
            if ButtonText != 'PushButtonEllipsis': exec(f'self.view.Button_Group.addButton(self.view.{ButtonText}, int(text))')

    def __ClickedRow(self):
        index = self.view.tableWidget_TableApplication.currentRow()
        request = self.__ListRequest[index]

        if self.__ConsiderationApplication is None:
            self.__ConsiderationApplication = ControllerConsiderationApplication(self)
            self.__ConsiderationApplication.FillingFields(request)
            self.__ConsiderationApplication.RunViewConsiderationApplication()
        else:
            self.__ConsiderationApplication.FillingFields(request)
            self.__ConsiderationApplication.RunViewConsiderationApplication()

    def __ClickedButtonPage(self, button):
        if int(button.text()) != self.__CursorPage:
            index_button = self.__IdentifyClickedButton(button)
            self.last_cursor = self.__CursorPage
            self.__CursorPage = int(button.text())
            index = (int(button.text()) - 1) * 11
            self.__ListRequest.clear()
            self.__SaveRequest(self.__СhoiceSaveRequest(index))
            self.__FillingTable(int(button.text()))
            if 0 <= index_button <= 1:
                self.__StepBack(button)
            elif 3 <= index_button <= 4:
                self.__StepFront(button)

            self.view.Button_Group.button(self.last_cursor).setStyleSheet("background-color: rgb(255, 255, 255);"
                                                                     "border: 2px solid gray;")
            self.view.Button_Group.button(self.__CursorPage).setStyleSheet('background-color: rgb(85, 255, 127); '
                                                                         'border: 2px solid gray;')
            del self.last_cursor

    def __СhoiceSaveRequest(self, index):
        if self.__IsFilterDate:
            return self.__ChoiceFunctionDate(index)
        elif self.__IsFilterClient:
            return self.__ChoiceFunctionClient(index)
        else:
            return self.__model.Get11RequestClients(StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)

    def __StepFront(self, button):
        if self.__MaxStepFront() == 1:
            self.__EditStepFront(1)
            if self.last_cursor != int(self.view.Button_Group.buttons()[-1].text()):
                self.last_cursor += 1
        elif self.__MaxStepFront() >= 2:
            quantity = self.__QuantityStepsFront(button)
            self.__EditStepFront(quantity)
            if self.last_cursor != int(self.view.Button_Group.buttons()[-1].text()):
                self.last_cursor += quantity

    def __StepBack(self, button):
        if self.__MaxstepBack() == 1:
            self.__EditStepBack(1)
            if self.last_cursor != int(self.view.Button_Group.buttons()[-1].text()):
                self.last_cursor -= 1
        elif self.__MaxstepBack() >= 2:
            quantity = self.__QuantityStepsBack(button)
            self.__EditStepBack(quantity)
            if self.last_cursor != int(self.view.Button_Group.buttons()[-1].text()):
                self.last_cursor -= quantity

    def __QuantityStepsFront(self, button) -> int:
        index = self.__IdentifyClickedButton(button)
        if index == 3: return 1
        if index == 4: return 2

    def __QuantityStepsBack(self, button) -> int:
        index = self.__IdentifyClickedButton(button)
        if index == 0: return 2
        if index == 1: return 1

    def __MaxStepFront(self) -> int:
        list_button = self.view.Button_Group.buttons()
        return int(list_button[5].text()) - (int(list_button[4].text()) + 1)

    def __MaxstepBack(self) -> int:
        list_button = self.view.Button_Group.buttons()
        return int(list_button[0].text()) - 1

    def __IdentifyClickedButton(self, Button) -> int:
        for index, button in enumerate(self.view.Button_Group.buttons()):
            if button == Button:
                return index

    def __EditStepFront(self, step):
        BtnGroup = self.view.Button_Group
        for index, button in enumerate(BtnGroup.buttons()[:-1]):
            BtnGroup.setId(button, BtnGroup.id(button) + step)
            button.setText(self._translate("MainWindow", str(int(button.text()) + step)))

    def __EditStepBack(self, step):
        BtnGroup = self.view.Button_Group
        for index, button in enumerate(BtnGroup.buttons()[:-1]):
            BtnGroup.setId(button, BtnGroup.id(button) - step)
            button.setText(self._translate("MainWindow", str(int(button.text()) - step)))

    def __BackBeginning(self):
        btn_group = self.view.Button_Group.buttons()
        step = int(btn_group[0].text()) - 1
        LastCursor = self.__CursorPage - step if self.__CursorPage != int(self.view.Button_Group.buttons()[-1].text()) else self.__CursorPage
        self.__EditStepBack(step)
        self.__ListRequest.clear()
        self.__SaveRequest(self.__СhoiceSaveRequest(index=0))
        self.__FillingTable(1)
        self.view.Button_Group.button(LastCursor).setStyleSheet("background-color: rgb(255, 255, 255);"
                                                                            "border: 2px solid gray;")
        self.__CursorPage = 1
        self.view.Button_Group.button(self.__CursorPage).setStyleSheet("background-color: rgb(85, 255, 127);"
                                                                     "border: 2px solid gray;")

    def __SaveRequest(self, requests):
        for request in requests:
            req = Request()
            req.ID = request[0]
            req.FirstName = request[1]
            req.LastName = request[2]
            req.Email = request[3]
            req.NumberPhone = request[4]
            req.PlaceDeparture = request[5]
            req.PlaceDelivery = request[6]
            req.CargoWeight = request[7]
            req.CargoDescription = request[8]
            req.IdClient = request[9]
            req.DateRequest = str(request[10]).replace("-", ".")
            self.__ListRequest.append(req)

    def __FillingTable(self, NumberPage):
        self.view.tableWidget_TableApplication.setRowCount(len(self.__ListRequest))
        RowTable = ((int(NumberPage) - 1) / 11)
        for index, request in enumerate(self.__ListRequest, start=((int(NumberPage) - 1) * 11) + 1):
            self.__SetItem(RowTable)
            item = self.view.tableWidget_TableApplication.verticalHeaderItem(RowTable)
            item.setText(self._translate("MainWindow", str(index)))
            item = self.view.tableWidget_TableApplication.item(RowTable, 0)
            item.setText(self._translate("MainWindow", request.FirstName))
            item = self.view.tableWidget_TableApplication.item(RowTable, 1)
            item.setText(self._translate("MainWindow", request.LastName))
            item = self.view.tableWidget_TableApplication.item(RowTable, 2)
            item.setText(self._translate("MainWindow", request.DateRequest))
            RowTable += 1

    def __NewItem(self):
        return QtWidgets.QTableWidgetItem()

    def __SetItem(self, index):
        self.view.tableWidget_TableApplication.setVerticalHeaderItem(index, self.__NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 0, self.__NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 1, self.__NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 2, self.__NewItem())

    def __IdexChangeSortTable(self):
        if self.view.comboBox_SortTable.currentText() == "По убывающей дате":
            self.__ParameterSort = "DateRequest"
            self.__reverse = True
            self.__BackBeginning()
        elif self.view.comboBox_SortTable.currentText() == "По возрастающей дате":
            self.__ParameterSort = "DateRequest"
            self.__reverse = False
            self.__BackBeginning()
        elif self.view.comboBox_SortTable.currentText() == "В алфавитном порядке":
            self.__ParameterSort = "FirstName"
            self.__reverse = False
            self.__BackBeginning()
        elif self.view.comboBox_SortTable.currentText() == "В обратном алфавитном порядке":
            self.__ParameterSort = "FirstName"
            self.__reverse = True
            self.__BackBeginning()
        pass

    def __ChoiceFunctionDate(self, index):
        if self.view.comboBox_Date.currentText() == "По полной дате":
            date = self.view.dateEdit_Searchdate.text()
            return self.__model.Get11RequestByDate(date, StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)
        elif self.view.comboBox_Date.currentText() == "По году и месяцу":
            return self.__model.Get11RequestByYearAndMonth(self.__FilterDate[2], self.__FilterDate[1], StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)
        elif self.view.comboBox_Date.currentText() == "По году и дню":
            return self.__model.Get11RequestByYearAndDay(self.__FilterDate[2], self.__FilterDate[0], StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)
        elif self.view.comboBox_Date.currentText() == "По месяцу и дню":
            return self.__model.Get11RequestByMonthAndDay(self.__FilterDate[1], self.__FilterDate[0], StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)
        elif self.view.comboBox_Date.currentText() == "По году":
            return self.__model.Get11RequestByYear(self.__FilterDate[2], StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)
        elif self.view.comboBox_Date.currentText() == "По месяцу":
            return self.__model.Get11RequestByMonth(self.__FilterDate[1], StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)
        elif self.view.comboBox_Date.currentText() == "По дню":
            return self.__model.Get11RequestByDay(self.__FilterDate[0], StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)

    def __ChoiceFunctionClient(self, index):
        if self.view.comboBox_Client.currentText() == "По имени":
            return self.__model.Get11RequestByFirstName(self.__FilterClient, StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)
        elif self.view.comboBox_Client.currentText() == "По фамилии":
            return self.__model.Get11RequestByLastName(self.__FilterClient, StartIndex=index, ParameterSort=self.__ParameterSort, reverse=self.__reverse)

    def __ChoiceParameterDate(self, date: str):
        ComponentsDate = list(map(int, date.split(".")))
        self.__FilterDate = ComponentsDate
        year = ComponentsDate[2]
        month = ComponentsDate[1]
        day = ComponentsDate[0]
        if self.view.comboBox_Date.currentText() == "По полной дате":
            self.__QuantityRequest = self.__model.GetQuantityRequestByDate(date)
            self.__TableFilter(self.__model.Get11RequestByDate(date, StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))
        elif self.view.comboBox_Date.currentText() == "По году и месяцу":
            self.__QuantityRequest = self.__model.GetQuantityRequestByYearAndMonth(year, month)
            self.__TableFilter(self.__model.Get11RequestByYearAndMonth(year, month, StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))
        elif self.view.comboBox_Date.currentText() == "По году и дню":
            self.__QuantityRequest = self.__model.GetQuantityRequestByYearAndDay(year, day)
            self.__TableFilter(self.__model.Get11RequestByYearAndDay(year, day, StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))
        elif self.view.comboBox_Date.currentText() == "По месяцу и дню":
            self.__QuantityRequest = self.__model.GetQuantityRequestByMonthAndDay(month, day)
            self.__TableFilter(self.__model.Get11RequestByMonthAndDay(month, day, StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))
        elif self.view.comboBox_Date.currentText() == "По году":
            self.__QuantityRequest = self.__model.GetQuantityRequestByYear(year)
            self.__TableFilter(self.__model.Get11RequestByYear(year, StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))
        elif self.view.comboBox_Date.currentText() == "По месяцу":
            self.__QuantityRequest = self.__model.GetQuantityRequestByMonth(month)
            self.__TableFilter(self.__model.Get11RequestByMonth(month, StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))
        elif self.view.comboBox_Date.currentText() == "По дню":
            self.__QuantityRequest = self.__model.GetQuantityRequestByDay(day)
            self.__TableFilter(self.__model.Get11RequestByDay(day, StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))

    def __ChoiceParameterClient(self, text):
        self.__FilterClient = text
        if self.view.comboBox_Client.currentText() == "По имени":
            self.__QuantityRequest = self.__model.GetQuantityRequestByFirstName(text)
            self.__TableFilter(self.__model.Get11RequestByFirstName(text, StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))
        elif self.view.comboBox_Client.currentText() == "По фамилии":
            self.__QuantityRequest = self.__model.GetQuantityRequestByLastName(text)
            self.__TableFilter(self.__model.Get11RequestByLastName(text, StartIndex=0, ParameterSort=self.__ParameterSort, reverse=self.__reverse))

    def __TableFilter(self, requests: list):
        self.view.lcdNumber.display(self.__QuantityRequest)
        self.__ListRequest.clear()
        self.__SaveRequest(requests)
        self.__FillingTable(1)
        self.__ClearLayout_ListNumberPages()
        self.__CreateButtonsPage()
        self.__CursorPage = 1
        # self.BackBeginning()

    def __SearchDate(self):
        date = self.view.dateEdit_Searchdate.text()
        self.__IsFilterClient = False
        self.__IsFilterDate = True
        self.__ChoiceParameterDate(date)

    def __SearchClient(self):
        text = self.view.lineEdit_SearchClient.text()
        self.__IsFilterDate = False
        self.__IsFilterClient = True
        self.__ChoiceParameterClient(text)

    def __UpdateTable(self):
        lastQuantityRequest = self.__QuantityRequest
        self.__IsFilterClient = False
        self.__IsFilterDate = False
        self.__QuantityRequest = self.__model.GetAllQuantityReauest()
        self.view.lcdNumber.display(self.__QuantityRequest)
        if ceil(lastQuantityRequest / 11) < ceil(self.__QuantityRequest / 11):
            self.__ClearLayout_ListNumberPages()
            self.__CreateButtonsPage()
            self.__CursorPage = 1

        if ceil(lastQuantityRequest / 11) > ceil(self.__QuantityRequest / 11):
            self.__ClearLayout_ListNumberPages()
            self.__CreateButtonsPage()
            self.__CursorPage = 1

    def __ClearLayout_ListNumberPages(self):
        while self.view.horizontalLayout_ListNumberPages.count():
            child = self.view.horizontalLayout_ListNumberPages.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def __Exit(self):
        self.WindowApplication.close()

    def __OpenRegistrationWorker(self):
        self.__ControllerRegWorker = ControllerRegistrationWorker(self)
        self.WindowApplication.setEnabled(False)
        self.__ControllerRegWorker.RunViewRegistrationWorker()





