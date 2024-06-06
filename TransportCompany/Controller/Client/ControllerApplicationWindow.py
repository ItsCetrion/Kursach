from TransportCompany.Model.Client.ModelApplicationWindow import ModelApplicationWindow
from TransportCompany.View.Client.ViewApplicationWindow import ViewApplicationWindow
from TransportCompany.Controller.Client.ControllerRequestSubmission import ControllerRequestSubmission
from TransportCompany.Controller.Client.ControllerUserProfile import ControllerUserProfile
from TransportCompany.Entities.DenyRequest import DenyRequest
from TransportCompany.Entities.AcceptRequest import AcceptRequest
from TransportCompany.Entities.Request import Request
from TransportCompany.Entities.DeliveredRequest import DeliveredRequest
from TransportCompany.Entities.Client import Client
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QCoreApplication
from math import ceil
import sys


class ControllerApplicationWindow:
    def __init__(self, client: Client):
        self.__model = ModelApplicationWindow()
        self.view = ViewApplicationWindow()
        self.__SettingsUI()
        self.__RequestSubmission = None
        self.__client = client
        self._translate = QApplication.translate
        self.__ListRequest = []
        self.__CursorPage = 1
        self.__reverse = True
        self.__IsFilterDate = False
        self.__DataDate = None
        self.__Status = "В пути"
        self.__QuantityRequest = self.__model.GetQuantityRequest(self.__CurrentTable(), self.__client.ID)
        self.__SaveRequest(self.__model.Get11Request(0, self.__reverse, self.__CurrentTable(), self.__client.ID), AcceptRequest)
        self.__FillingTable(NumberPage=1)
        self.__CreateButtonsPage()
        
        self.view.pushButton_BackFirstPage.clicked.connect(self.__ClickedBackFirstPage)
        self.view.pushButton_Updatetable.clicked.connect(self.__ClickedUpdatetable)
        self.view.pushButton_Search_date.clicked.connect(self.__ClickedSearchDate)
        self.view.comboBox_SortTable.currentTextChanged.connect(self.__TextChangedSortTable)
        self.view.comboBox_Status.currentTextChanged.connect(self.__TextChangedStatus)
        self.view.lcdNumber.display(self.__QuantityRequest)
        self.view.Button_Group.buttonClicked.connect(self.__ClickedButtonPage)
        self.view.action_profile.triggered.connect(self.__ClickedProfile)
        self.view.action_SubmitApplication.triggered.connect(self.__ClickedSubmitApplication)
        self.view.action_Exit.triggered.connect(self.__ClickedExit)

    def __SettingsUI(self):
        self.__app = QApplication(sys.argv)
        self.ApplicationWindow = QMainWindow()
        ui = self.view
        ui.setupUi(self.ApplicationWindow)

    def RunViewApplicationWindow(self):
        self.ApplicationWindow.show()

    def __CurrentEntities(self):
        if self.__Status == "В пути": return AcceptRequest
        if self.__Status == "Отменён": return DenyRequest
        if self.__Status == "Сформирован": return Request
        if self.__Status == "Доставлен":
            return DeliveredRequest
        else:
            raise "ошибка статуса"

    def __CurrentTable(self):
        if self.__Status == "В пути": return "AcceptRequest"
        if self.__Status == "Отменён": return "DenyRequest"
        if self.__Status == "Сформирован": return "Request"
        if self.__Status == "Доставлен": return "DeliveredRequest"
        else: raise "ошибка статуса"

    def __TextChangedSortTable(self, text):
        if text == "По убывающей дате":
            self.__reverse = True
            self.__BackBeginning()
        elif text == "По возрастающей дате":
            self.__reverse = False
            self.__BackBeginning()

    def __TextChangedStatus(self, text):
        if text == "В пути":
            self.__OperationStatus("В пути")
        elif text == "Доставлен":
            self.__OperationStatus("Доставлен")
        elif text == "Отменён":
            self.__OperationStatus("Отменён")
        elif text == "Сформирован":
            self.__OperationStatus("Сформирован")

    def __OperationStatus(self, status: str):
        self.__Status = status
        self.__UpdateTable()
        if len(self.view.Button_Group.buttons()) > 0: self.__BackBeginning()

    def __ClickedSearchDate(self):
        date = self.view.dateEdit_Searchdate.text()
        self.__IsFilterDate = True
        self.__ChoiceParameterDate(date)

    def __ChoiceParameterDate(self, date: str):
        ComponentsDate = list(map(int, date.split(".")))
        self.__DataDate = ComponentsDate
        year = ComponentsDate[2]
        month = ComponentsDate[1]
        day = ComponentsDate[0]
        if self.view.comboBox_Date.currentText() == "По полной дате":
            self.__QuantityRequest = self.__model.GetQuantityByDate(date, self.__CurrentTable(), self.__client.ID)
            self.__TableFilter(self.__model.Get11RequestByDate(0, self.__reverse, self.__CurrentTable(), date, self.__client.ID))
        elif self.view.comboBox_Date.currentText() == "По году":
            self.__QuantityRequest = self.__model.GetQuantityByYear(year, self.__CurrentTable(), self.__client.ID)
            self.__TableFilter(self.__model.Get11RequestByYear(0, self.__reverse, self.__CurrentTable(), year, self.__client.ID))
        elif self.view.comboBox_Date.currentText() == "По месяцу":
            self.__QuantityRequest = self.__model.GetQuantityByMonth(month, self.__CurrentTable(), self.__client.ID)
            self.__TableFilter(self.__model.Get11RequestByMonth(0, self.__reverse, self.__CurrentTable(), month, self.__client.ID))
        elif self.view.comboBox_Date.currentText() == "По дню":
            self.__QuantityRequest = self.__model.GetQuantityByDay(day, self.__CurrentTable(), self.__client.ID)
            self.__TableFilter(self.__model.Get11RequestByDay(0, self.__reverse, self.__CurrentTable(), day, self.__client.ID))

    def __TableFilter(self, requests: list):
        self.view.lcdNumber.display(self.__QuantityRequest)
        self.__ListRequest.clear()
        self.__SaveRequest(requests, self.__CurrentEntities())
        self.__FillingTable(1)
        self.__ClearLayout_ListNumberPages()
        self.__CreateButtonsPage()
        self.__CursorPage = 1

    def __ClearLayout_ListNumberPages(self):
        while self.view.horizontalLayout_ListNumberPages.count():
            child = self.view.horizontalLayout_ListNumberPages.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def __SaveRequest(self, list_requests, request: [Request, AcceptRequest, DenyRequest]):
        for request_ in list_requests:
            req = request()
            req.ID = request_[0]
            req.FirstName = request_[1]
            req.LastName = request_[2]
            req.Email = request_[3]
            req.NumberPhone = request_[4]
            req.PlaceDeparture = request_[5]
            req.PlaceDelivery = request_[6]
            req.CargoWeight = request_[7]
            req.CargoDescription = request_[8]
            req.IdClient = request_[9]
            if isinstance(req, Request):
                req.DateRequest = str(request_[10]).replace("-", ".")
            elif isinstance(req, AcceptRequest):
                req.DateAccept = str(request_[10]).replace("-", ".")
            elif isinstance(req, DenyRequest):
                req.DateDeny = str(request_[10]).replace("-", ".")
            elif isinstance(req, DeliveredRequest):
                req.DateDelivered = str(request_[10]).replace("-", ".")
            self.__ListRequest.append(req)

    def __FillingTable(self, NumberPage):
        self.view.tableWidget_TableApplication.setRowCount(len(self.__ListRequest))
        RowTable = ((int(NumberPage) - 1) / 11)
        for index, request in enumerate(self.__ListRequest, start=((int(NumberPage) - 1) * 11) + 1):
            self.__SetItem(RowTable)
            item = self.view.tableWidget_TableApplication.verticalHeaderItem(RowTable)
            item.setText(self._translate("MainWindow", str(index)))
            item = self.view.tableWidget_TableApplication.item(RowTable, 0)
            item.setText(self._translate("MainWindow", request.PlaceDeparture))
            item = self.view.tableWidget_TableApplication.item(RowTable, 1)
            item.setText(self._translate("MainWindow", request.PlaceDelivery))
            item = self.view.tableWidget_TableApplication.item(RowTable, 2)
            item.setText(self._translate("MainWindow", request.CargoDescription))
            item = self.view.tableWidget_TableApplication.item(RowTable, 3)
            if isinstance(request, Request):
                item.setText(self._translate("MainWindow", request.DateRequest))
            elif isinstance(request, AcceptRequest):
                item.setText(self._translate("MainWindow", request.DateAccept))
            elif isinstance(request, DenyRequest):
                item.setText(self._translate("MainWindow", request.DateDeny))
            elif isinstance(request, DeliveredRequest):
                item.setText(self._translate("MainWindow", request.DateDelivered))
            RowTable += 1

    def __SetItem(self, index):
        self.view.tableWidget_TableApplication.setVerticalHeaderItem(index, self.__NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 0, self.__NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 1, self.__NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 2, self.__NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 3, self.__NewItem())

    def __NewItem(self):
        return QTableWidgetItem()

    def __CreateButtonsPage(self):
        if self.__QuantityRequest == 0:
            self.__CreateButton(1)
        elif self.__QuantityRequest <= 55:  #55 - это 5 отображаемых страниц(на 1-ой странице по 11 заявок)
            self.__CreateButton(ceil(self.__QuantityRequest / 11))
        else:
            self.__CreateButton(5)
            self.__CreateButton(QuantityButton=1, ButtonText="...")
            self.__CreateButton(QuantityButton=1, ButtonText=str(ceil(self.__QuantityRequest / 11)))

    def __CreateButton(self, QuantityButton, ButtonText=None):
        if ButtonText is None:
            for page in range(1, QuantityButton + 1):
                name_btn = f"PushButton{page}"
                self.__FunctionalCreateButton(name_btn, str(page))
                exec(f'self.view.Button_Group.addButton(self.view.{name_btn}, page)')
            if 'PushButton1' in self.view.__dict__.keys():
                self.view.PushButton1.setStyleSheet('background-color: rgb(85, 255, 127); border: 2px solid gray;')
        elif ButtonText is not None:
            ButtonName = ButtonText
            text = ButtonText
            if ButtonName == "...": ButtonName = "PushButtonEllipsis"
            elif ButtonName.isdigit(): ButtonName = "PushButton_Number"
            self.__FunctionalCreateButton(ButtonName, text)
            if ButtonText == 'PushButton_Number':
                exec(f'self.view.Button_Group.addButton(self.view.{ButtonName}, int(text))')

    def __FunctionalCreateButton(self, NameButton, TextButton):
        exec(f"self.view.{NameButton} = QPushButton(self.view.horizontalLayoutWidget)")
        exec(f"self.view.{NameButton}.setMinimumSize(QSize(0, 25))")
        exec(
            f"self.view.{NameButton}.setStyleSheet('background-color: rgb(255, 255, 255); border: 2px solid gray;')")
        exec(f"self.view.{NameButton}.setObjectName('{NameButton}')")
        exec(f"self.view.horizontalLayout_ListNumberPages.addWidget(self.view.{NameButton})")
        exec(f'self.view.{NameButton}.setText(self._translate("MainWindow", str(TextButton)))')

    def __ClickedSubmitApplication(self):
        if self.__RequestSubmission == None:
            self.__RequestSubmission = ControllerRequestSubmission(self.__client)
            self.__RequestSubmission.RunViewRequestSubmission()
        else:
            self.__RequestSubmission.RunViewRequestSubmission()

    def __ClickedBackFirstPage(self):
        self.__BackBeginning()

    def __ClickedUpdatetable(self):
        self.__IsFilterDate = False
        self.view.comboBox_Date.setCurrentIndex(0)
        self.__Status = "В пути"
        self.view.comboBox_Status.setCurrentIndex(0)
        self.__reverse = True
        self.view.comboBox_SortTable.setCurrentIndex(0)
        self.__UpdateTable()
        self.__BackBeginning()

    def __UpdateTable(self):
        lastQuantityRequest = self.__QuantityRequest
        self.__QuantityRequest = self.__model.GetQuantityRequest(self.__CurrentTable(), self.__client.ID)
        self.view.lcdNumber.display(self.__QuantityRequest)
        if ceil(lastQuantityRequest / 11) < ceil(self.__QuantityRequest / 11):
            self.__ClearLayout_ListNumberPages()
            self.__CreateButtonsPage()
            self.__CursorPage = 1

        if ceil(lastQuantityRequest / 11) > ceil(self.__QuantityRequest / 11):
            self.__ClearLayout_ListNumberPages()
            self.__CreateButtonsPage()
            self.__CursorPage = 1

    def __BackBeginning(self):
        btn_group = self.view.Button_Group.buttons()
        try:
            step = int(btn_group[0].text()) - 1
        except IndexError:
            step = 0
        LastCursor = self.__CursorPage - step if self.__CursorPage != int(self.view.Button_Group.buttons()[-1].text()) else self.__CursorPage
        self.__EditStepBack(step)
        self.__ListRequest.clear()
        self.__SaveRequest(self.__ChoiceSaveRequest(index=0), self.__CurrentEntities())
        self.__FillingTable(1)
        self.view.Button_Group.button(LastCursor).setStyleSheet("background-color: rgb(255, 255, 255);"
                                                                            "border: 2px solid gray;")
        self.__CursorPage = 1
        self.view.Button_Group.button(self.__CursorPage).setStyleSheet("background-color: rgb(85, 255, 127);"
                                                                     "border: 2px solid gray;")

    def __ChoiceSaveRequest(self, index):
        if self.__IsFilterDate:
            return self.__ChoiceFunctionDate(index)
        else:
            return self.__model.Get11Request(index, self.__reverse, self.__CurrentTable(), self.__client.ID)

    def __ChoiceFunctionDate(self, index):
        if self.view.comboBox_Date.currentText() == "По полной дате":
            date = self.view.dateEdit_Searchdate.text()
            return self.__model.Get11RequestByDate(index, self.__reverse, self.__CurrentTable(), date, self.__client.ID)
        if self.view.comboBox_Date.currentText() == "По году":
            return self.__model.Get11RequestByYear(index, self.__reverse, self.__CurrentTable(), self.__DataDate[2], self.__client.ID)
        if self.view.comboBox_Date.currentText() == "По месяцу":
            return self.__model.Get11RequestByMonth(index, self.__reverse, self.__CurrentTable(), self.__DataDate[1], self.__client.ID)
        if self.view.comboBox_Date.currentText() == "По дню":
            return self.__model.Get11RequestByDay(index, self.__reverse, self.__CurrentTable(), self.__DataDate[0], self.__client.ID)

    def __ClickedButtonPage(self, button):
        if int(button.text()) != self.__CursorPage:
            index_button = self.__IdentifyClickedButton(button)
            self.last_cursor = self.__CursorPage
            self.__CursorPage = int(button.text())
            index = (int(button.text()) - 1) * 11
            self.__ListRequest.clear()
            self.__SaveRequest(self.__ChoiceSaveRequest(index), self.__CurrentEntities())
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

    def __ClickedProfile(self):
        self.__UserProfile = ControllerUserProfile(self.__client, self)
        self.__UserProfile.RunViewUserProfile()
        self.ApplicationWindow.setEnabled(False)

    def __ClickedExit(self):
        self.ApplicationWindow.close()