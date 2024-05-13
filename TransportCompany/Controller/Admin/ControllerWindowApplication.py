from TransportCompany.Model.Admin.ModelWindowApplication import ModelWindowApplication
from TransportCompany.View.Admin.ViewWindowApplication import ViewWindowApplication
from TransportCompany.Controller.Admin.ControllerRegistrationWorker import ControllerRegistrationWorker
from TransportCompany.Controller.Admin.ControllerConsiderationApplication import ControllerConsiderationApplication
from TransportCompany.Entities.Request import Request
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QCoreApplication
import sys
from math import ceil

class ControllerWindowApplication:
    def __init__(self):
        self.model = ModelWindowApplication()
        self.view = ViewWindowApplication()
        self.ControllerRegWorker = ControllerRegistrationWorker()
        self._translate = QCoreApplication.translate
        self.QuantityRequest = self.model.GetAllQuantityReauest()
        self.ListRequest = []
        self.CursorPage = 1
        self.ParameterSort = "DateRequest"
        self.reverse = True
        self.SaveRequest(self.model.Get11Request(StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))
        self.SettingsUI()
        self.FillingTable(NumberPage=1)
        self.CreateButtonsPage()
        self.IsFilterDate = False
        self.IsFilterClient = False
        self.FilterDate = None
        self.FilterClient = None
        self.ConsiderationApplication = None

        self.view.comboBox_SortTable.currentIndexChanged.connect(self.IdexChangeSortTable)
        self.view.pushButton_Search_date.clicked.connect(self.SearchDate)
        self.view.pushButton_Search_Client.clicked.connect(self.SearchClient)
        self.view.pushButton_UpdateTable.clicked.connect(self.UpdateTable)
        self.view.action_exit.triggered.connect(self.Exit)
        self.view.action_RegistrationWorker.triggered.connect(self.OpenRegistrationWorker)
        self.view.tableWidget_TableApplication.clicked.connect(self.test)
        self.view.lcdNumber.display(self.QuantityRequest)
        self.view.Button_Group.buttonClicked.connect(self.ClickedButtonPage)
        self.view.pushButton_NextPage.clicked.connect(self.ClickedNext)
        self.view.pushButton_BackPage.clicked.connect(self.ClickedBack)
        self.view.pushButton_BackFirstPage.clicked.connect(self.ClickedBackFirstPage)
        self.view.pushButton_UpdateTable.clicked.connect(self.ClickedUpdateTable)


    def ClickedUpdateTable(self):
        self.QuantityRequest = self.model.GetAllQuantityReauest()
        self.UpdateTable()
        self.BackBeginning()

    def ClickedBackFirstPage(self):
        self.BackBeginning()
    def ClickedNext(self):
        if self.CursorPage != (ceil(self.QuantityRequest / 11)):
            self.ClickedButtonPage(self.view.Button_Group.button(self.CursorPage + 1))

    def ClickedBack(self):
        if self.CursorPage != 1:
            self.ClickedButtonPage(self.view.Button_Group.button(self.CursorPage - 1))

    def CreateButtonsPage(self):
        if self.QuantityRequest <= 55:  #55 - это 5 отображаемых страниц(на 1-ой странице по 11 заявок)
            self.CreateButton(ceil(self.QuantityRequest / 11))
        else:
            self.CreateButton(5)
            self.CreateButton(QuantityButton=1, ButtonText="...")
            self.CreateButton(QuantityButton=1, ButtonText=str(ceil(self.QuantityRequest / 11)))

    def CreateButton(self, QuantityButton, ButtonText = None):
        if ButtonText is None:
            for page in range(1, QuantityButton + 1):
                name_btn = f"PushButton{page}"
                exec(f"self.view.{name_btn} = QtWidgets.QPushButton(self.view.horizontalLayoutWidget)")
                exec(f"self.view.{name_btn}.setMinimumSize(QtCore.QSize(0, 25))")
                exec(f"self.view.{name_btn}.setStyleSheet('background-color: rgb(255, 255, 255); border: 2px solid gray;')")
                exec(f"self.view.{name_btn}.setObjectName('{name_btn}')")
                exec(f"self.view.horizontalLayout_ListNumberPages.addWidget(self.view.{name_btn})")
                exec(f'self.view.{name_btn}.setText(self._translate("MainWindow", str(page)))')
                exec(f'self.view.Button_Group.addButton(self.view.{name_btn}, page)')
            if self.view.PushButton1 in self.view.Button_Group.buttons():
                self.view.PushButton1.setStyleSheet('background-color: rgb(85, 255, 127); border: 2px solid gray;')
        elif ButtonText is not None:
            text = ButtonText
            if ButtonText == "...": ButtonText = "PushButtonEllipsis"
            elif ButtonText.isdigit(): ButtonText = "PushButton_Number"
            exec(f"self.view.{ButtonText} = QtWidgets.QPushButton(self.view.horizontalLayoutWidget)")
            exec(f"self.view.{ButtonText}.setMinimumSize(QtCore.QSize(0, 25))")
            exec(f"self.view.{ButtonText}.setStyleSheet('background-color: rgb(255, 255, 255); border: 2px solid gray;')")
            exec(f"self.view.{ButtonText}.setObjectName('{ButtonText}')")
            exec(f"self.view.horizontalLayout_ListNumberPages.addWidget(self.view.{ButtonText})")
            exec(f'self.view.{ButtonText}.setText(self._translate("MainWindow", "{text}"))')
            if ButtonText != 'PushButtonEllipsis': exec(f'self.view.Button_Group.addButton(self.view.{ButtonText}, int(text))')

    def test(self):
        index = self.view.tableWidget_TableApplication.currentRow()
        request = self.ListRequest[index]

        if self.ConsiderationApplication is None:
            self.ConsiderationApplication = ControllerConsiderationApplication(self)
            self.ConsiderationApplication.FillingFields(request)
            self.ConsiderationApplication.ConsiderationApplication.show()
        else:
            self.ConsiderationApplication.FillingFields(request)
            self.ConsiderationApplication.ConsiderationApplication.show()

    def ClickedButtonPage(self, button):
        if int(button.text()) != self.CursorPage:
            index_button = self.IdentifyClickedButton(button)
            self.last_cursor = self.CursorPage
            self.CursorPage = int(button.text())
            index = (int(button.text()) - 1) * 11
            self.ListRequest.clear()
            self.SaveRequest(self.СhoiceSaveRequest(index))
            self.FillingTable(int(button.text()))
            if 0 <= index_button <= 1:
                self.StepBack(button)
            elif 3 <= index_button <= 4:
                self.StepFrot(button)

            self.view.Button_Group.button(self.last_cursor).setStyleSheet("background-color: rgb(255, 255, 255);"
                                                                     "border: 2px solid gray;")
            self.view.Button_Group.button(self.CursorPage).setStyleSheet('background-color: rgb(85, 255, 127); '
                                                                         'border: 2px solid gray;')
            del self.last_cursor

    def СhoiceSaveRequest(self, index):
        if self.IsFilterDate:
            return self.ChoiceFunctionDate(index)
        elif self.IsFilterClient:
            return self.ChoiceFunctionClient(index)
        else:
            return self.model.Get11Request(StartIndex=index, ParameterSort=self.ParameterSort, reverse=self.reverse)



    def StepFrot(self, button):
        if self.MaxStepFront() == 1:
            self.EditStepFront(1)
            if self.last_cursor != int(self.view.Button_Group.buttons()[-1].text()):
                self.last_cursor += 1
        elif self.MaxStepFront() >= 2:
            quantity = self.QuantityStepsFront(button)
            self.EditStepFront(quantity)
            if self.last_cursor != int(self.view.Button_Group.buttons()[-1].text()):
                self.last_cursor += quantity

    def StepBack(self, button):
        if self.MaxstepBack() == 1:
            self.EditStepBack(1)
            if self.last_cursor != int(self.view.Button_Group.buttons()[-1].text()):
                self.last_cursor -= 1
        elif self.MaxstepBack() >= 2:
            quantity = self.QuantityStepsBack(button)
            self.EditStepBack(quantity)
            if self.last_cursor != int(self.view.Button_Group.buttons()[-1].text()):
                self.last_cursor -= quantity

    def QuantityStepsFront(self, button) -> int:
        index = self.IdentifyClickedButton(button)
        if index == 3: return 1
        if index == 4: return 2

    def QuantityStepsBack(self, button) -> int:
        index = self.IdentifyClickedButton(button)
        if index == 0: return 2
        if index == 1: return 1

    def MaxStepFront(self) -> int:
        list_button = self.view.Button_Group.buttons()
        return int(list_button[5].text()) - (int(list_button[4].text()) + 1)

    def MaxstepBack(self) -> int:
        list_button = self.view.Button_Group.buttons()
        return int(list_button[0].text()) - 1

    def IdentifyClickedButton(self, Button) -> int:
        for index, button in enumerate(self.view.Button_Group.buttons()):
            if button == Button:
                return index

    def EditStepFront(self, step):
        BtnGroup = self.view.Button_Group
        for index, button in enumerate(BtnGroup.buttons()[:-1]):
            BtnGroup.setId(button, BtnGroup.id(button) + step)
            button.setText(self._translate("MainWindow", str(int(button.text()) + step)))

    def EditStepBack(self, step):
        BtnGroup = self.view.Button_Group
        for index, button in enumerate(BtnGroup.buttons()[:-1]):
            BtnGroup.setId(button, BtnGroup.id(button) - step)
            button.setText(self._translate("MainWindow", str(int(button.text()) - step)))

    def BackBeginning(self):
        btn_group = self.view.Button_Group.buttons()
        step = int(btn_group[0].text()) - 1
        LastCursor = self.CursorPage - step if self.CursorPage != int(self.view.Button_Group.buttons()[-1].text()) else self.CursorPage
        self.EditStepBack(step)
        self.ListRequest.clear()
        self.SaveRequest(self.СhoiceSaveRequest(index=0))
        self.FillingTable(1)
        self.view.Button_Group.button(LastCursor).setStyleSheet("background-color: rgb(255, 255, 255);"
                                                                            "border: 2px solid gray;")
        self.CursorPage = 1
        self.view.Button_Group.button(self.CursorPage).setStyleSheet("background-color: rgb(85, 255, 127);"
                                                                     "border: 2px solid gray;")

    def SaveRequest(self, requests):
        for request in requests:
            req = Request()
            req.FirstName = request[0]
            req.LastName = request[1]
            req.Email = request[2]
            req.NumberPhone = request[3]
            req.PlaceDeparture = request[4]
            req.PlaceDelivery = request[5]
            req.CargoWeight = request[6]
            req.CargoDescription = request[7]
            req.DateRequest = str(request[8]).replace("-", ".")
            self.ListRequest.append(req)


    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.WindowApplication = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.WindowApplication)

    def RunViewWindowApplication(self):
        self.WindowApplication.show()
        sys.exit(self.app.exec_())

    def FillingTable(self, NumberPage):
        self.view.tableWidget_TableApplication.setRowCount(len(self.ListRequest))
        RowTable = ((int(NumberPage) - 1) / 11)
        for index, request in enumerate(self.ListRequest, start=((int(NumberPage) - 1) * 11) + 1):
            self.SetItem(RowTable)
            item = self.view.tableWidget_TableApplication.verticalHeaderItem(RowTable)
            item.setText(self._translate("MainWindow", str(index)))
            item = self.view.tableWidget_TableApplication.item(RowTable, 0)
            item.setText(self._translate("MainWindow", request.FirstName))
            item = self.view.tableWidget_TableApplication.item(RowTable, 1)
            item.setText(self._translate("MainWindow", request.LastName))
            item = self.view.tableWidget_TableApplication.item(RowTable, 2)
            item.setText(self._translate("MainWindow", request.DateRequest))
            RowTable += 1

    def NewItem(self):
        return QtWidgets.QTableWidgetItem()

    def SetItem(self, index):
        self.view.tableWidget_TableApplication.setVerticalHeaderItem(index, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 0, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 1, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 2, self.NewItem())

    def IdexChangeSortTable(self):
        if self.view.comboBox_SortTable.currentText() == "По убывающей дате":
            self.ParameterSort = "DateRequest"
            self.reverse = True
            self.BackBeginning()
        elif self.view.comboBox_SortTable.currentText() == "По возрастающей дате":
            self.ParameterSort = "DateRequest"
            self.reverse = False
            self.BackBeginning()
        elif self.view.comboBox_SortTable.currentText() == "В алфавитном порядке":
            self.ParameterSort = "FirstName"
            self.reverse = False
            self.BackBeginning()
        elif self.view.comboBox_SortTable.currentText() == "В обратном алфавитном порядке":
            self.ParameterSort = "FirstName"
            self.reverse = True
            self.BackBeginning()
        pass

    def ChoiceFunctionDate(self, index):
        if self.view.comboBox_Date.currentText() == "По полной дате":
            date = self.view.dateEdit_Searchdate.text()
            return self.model.Get11RequestByDate(date, StartIndex=index, ParameterSort=self.ParameterSort, reverse=self.reverse)
        elif self.view.comboBox_Date.currentText() == "По году и месяцу":
            return self.model.Get11RequestByYearAndMonth(self.FilterDate[2], self.FilterDate[1], StartIndex=index, ParameterSort=self.ParameterSort,reverse=self.reverse)
        elif self.view.comboBox_Date.currentText() == "По году и дню":
            return self.model.Get11RequestByYearAndDay(self.FilterDate[2], self.FilterDate[0], StartIndex=index, ParameterSort=self.ParameterSort,reverse=self.reverse)
        elif self.view.comboBox_Date.currentText() == "По месяцу и дню":
            return self.model.Get11RequestByMonthAndDay(self.FilterDate[1], self.FilterDate[0], StartIndex=index, ParameterSort=self.ParameterSort,reverse=self.reverse)
        elif self.view.comboBox_Date.currentText() == "По году":
            return self.model.Get11RequestByYear(self.FilterDate[2], StartIndex=index, ParameterSort=self.ParameterSort, reverse=self.reverse)
        elif self.view.comboBox_Date.currentText() == "По месяцу":
            return self.model.Get11RequestByMonth(self.FilterDate[1], StartIndex=index, ParameterSort=self.ParameterSort, reverse=self.reverse)
        elif self.view.comboBox_Date.currentText() == "По дню":
            return self.model.Get11RequestByDay(self.FilterDate[0], StartIndex=index, ParameterSort=self.ParameterSort, reverse=self.reverse)

    def ChoiceFunctionClient(self, index):
        if self.view.comboBox_Client.currentText() == "По имени":
            return self.model.Get11RequestByFirstName(self.FilterClient, StartIndex=index, ParameterSort=self.ParameterSort,reverse=self.reverse)
        elif self.view.comboBox_Client.currentText() == "По фамилии":
            return self.model.Get11RequestByLastName(self.FilterClient, StartIndex=index, ParameterSort=self.ParameterSort,reverse=self.reverse)
    def ChoiceParameterDate(self, date: str):
        ComponentsDate = list(map(int, date.split(".")))
        self.FilterDate = ComponentsDate
        year = ComponentsDate[2]
        month = ComponentsDate[1]
        day = ComponentsDate[0]
        if self.view.comboBox_Date.currentText() == "По полной дате":
            self.QuantityRequest = self.model.GetQuantityRequestByDate(date)
            self.TableFilter(self.model.Get11RequestByDate(date, StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))
        elif self.view.comboBox_Date.currentText() == "По году и месяцу":
            self.QuantityRequest = self.model.GetQuantityRequestByYearAndMonth(year, month)
            self.TableFilter(self.model.Get11RequestByYearAndMonth(year, month, StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))
        elif self.view.comboBox_Date.currentText() == "По году и дню":
            self.QuantityRequest = self.model.GetQuantityRequestByYearAndDay(year, day)
            self.TableFilter(self.model.Get11RequestByYearAndDay(year, day, StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))
        elif self.view.comboBox_Date.currentText() == "По месяцу и дню":
            self.QuantityRequest = self.model.GetQuantityRequestByMonthAndDay(month, day)
            self.TableFilter(self.model.Get11RequestByMonthAndDay(month, day, StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))
        elif self.view.comboBox_Date.currentText() == "По году":
            self.QuantityRequest = self.model.GetQuantityRequestByYear(year)
            self.TableFilter(self.model.Get11RequestByYear(year, StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))
        elif self.view.comboBox_Date.currentText() == "По месяцу":
            self.QuantityRequest = self.model.GetQuantityRequestByMonth(month)
            self.TableFilter(self.model.Get11RequestByMonth(month, StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))
        elif self.view.comboBox_Date.currentText() == "По дню":
            self.QuantityRequest = self.model.GetQuantityRequestByDay(day)
            self.TableFilter(self.model.Get11RequestByDay(day, StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))

    def ChoiceParameterClient(self, text):
        self.FilterClient = text
        if self.view.comboBox_Client.currentText() == "По имени":
            self.QuantityRequest = self.model.GetQuantityRequestByFirstName(text)
            self.TableFilter(self.model.Get11RequestByFirstName(text, StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))
        elif self.view.comboBox_Client.currentText() == "По фамилии":
            self.QuantityRequest = self.model.GetQuantityRequestByLastName(text)
            self.TableFilter(self.model.Get11RequestByLastName(text, StartIndex=0, ParameterSort=self.ParameterSort, reverse=self.reverse))

    def TableFilter(self, requests: list):
        self.view.lcdNumber.display(self.QuantityRequest)
        self.ListRequest.clear()
        self.SaveRequest(requests)
        self.FillingTable(1)
        self.ClearLayout_ListNumberPages()
        self.CreateButtonsPage()
        self.CursorPage = 1
        # self.BackBeginning()

    def SearchDate(self):
        date = self.view.dateEdit_Searchdate.text()
        self.IsFilterClient = False
        self.IsFilterDate = True
        self.ChoiceParameterDate(date)

    def SearchClient(self):
        text = self.view.lineEdit_SearchClient.text()
        self.IsFilterDate = False
        self.IsFilterClient = True
        self.ChoiceParameterClient(text)

    def UpdateTable(self):
        lastQuantityRequest = self.QuantityRequest
        self.IsFilterClient = False
        self.IsFilterDate = False
        self.QuantityRequest = self.model.GetAllQuantityReauest()
        self.view.lcdNumber.display(self.QuantityRequest)
        if ceil(lastQuantityRequest / 11) < ceil(self.QuantityRequest / 11):
            self.ClearLayout_ListNumberPages()
            self.CreateButtonsPage()
            self.CursorPage = 1

        if ceil(lastQuantityRequest / 11) > ceil(self.QuantityRequest / 11):
            self.ClearLayout_ListNumberPages()
            self.CreateButtonsPage()
            self.CursorPage = 1


    def ClearLayout_ListNumberPages(self):
        while self.view.horizontalLayout_ListNumberPages.count():
            child = self.view.horizontalLayout_ListNumberPages.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def Exit(self):
        self.WindowApplication.close()

    def OpenRegistrationWorker(self):
        self.WindowApplication.close()
        self.ControllerRegWorker.RunViewRegistrationWorker()





