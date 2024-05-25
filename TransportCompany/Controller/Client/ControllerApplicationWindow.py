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
        self.model = ModelApplicationWindow()
        self.view = ViewApplicationWindow()
        self.SettingsUI()
        self.RequestSubmission = None
        self.client = client
        self._translate = QApplication.translate
        self.ListRequest = []
        self.CursorPage = 1
        self.reverse = True
        self.IsFilterDate = False
        self.DataDate = None
        self.Status = "В пути"
        self.QuantityRequest = self.model.GetQuantityRequest(self.CurrentTable(), self.client.ID)
        self.SaveRequest(self.model.Get11Request(0, self.reverse, self.CurrentTable(), self.client.ID), AcceptRequest)
        self.FillingTable(NumberPage=1)
        self.CreateButtonsPage()
        
        self.view.pushButton_BackFirstPage.clicked.connect(self.ClickedBackFirstPage)
        self.view.pushButton_Updatetable.clicked.connect(self.ClickedUpdatetable)
        self.view.pushButton_Search_date.clicked.connect(self.ClickedSearchDate)
        self.view.comboBox_SortTable.currentTextChanged.connect(self.TextChangedSortTable)
        self.view.comboBox_Status.currentTextChanged.connect(self.TextChangedStatus)
        self.view.lcdNumber.display(self.QuantityRequest)
        self.view.Button_Group.buttonClicked.connect(self.ClickedButtonPage)
        self.view.action_profile.triggered.connect(self.ClickedProfile)
        self.view.action_SubmitApplication.triggered.connect(self.ClickedSubmitApplication)
        self.view.action_Exit.triggered.connect(self.ClickedExit)

    def SettingsUI(self):
        self.app = QApplication(sys.argv)
        self.ApplicationWindow = QMainWindow()
        ui = self.view
        ui.setupUi(self.ApplicationWindow)

    def RunViewApplicationWindow(self):
        self.ApplicationWindow.show()
        # sys.exit(self.app.exec_())

    def CurrentEntities(self):
        if self.Status == "В пути": return AcceptRequest
        if self.Status == "Отменён": return DenyRequest
        if self.Status == "Сформирован": return Request
        if self.Status == "Доставлен":
            return DeliveredRequest
        else:
            raise "ошибка статуса"

    def CurrentTable(self):
        if self.Status == "В пути": return "AcceptRequest"
        if self.Status == "Отменён": return "DenyRequest"
        if self.Status == "Сформирован": return "Request"
        if self.Status == "Доставлен": return "DeliveredRequest"
        else: raise "ошибка статуса"

    def TextChangedSortTable(self, text):
        if text == "По убывающей дате":
            self.reverse = True
            self.BackBeginning()
        elif text == "По возрастающей дате":
            self.reverse = False
            self.BackBeginning()

    def TextChangedStatus(self, text):
        if text == "В пути":
            self.Status = "В пути"
            self.UpdateTable()
            if len(self.view.Button_Group.buttons()) > 0: self.BackBeginning()
        elif text == "Доставлен":
            self.Status = "Доставлен"
            self.UpdateTable()
            if len(self.view.Button_Group.buttons()) > 0: self.BackBeginning()
        elif text == "Отменён":
            self.Status = "Отменён"
            self.UpdateTable()
            if len(self.view.Button_Group.buttons()) > 0: self.BackBeginning()
        elif text == "Сформирован":
            self.Status = "Сформирован"
            self.UpdateTable()
            if len(self.view.Button_Group.buttons()) > 0: self.BackBeginning()

    # def Test(self):
    #     self.QuantityRequest = self.model.GetQuantityRequest(self.CurrentTable(), self.client.ID)
    #     self.ClearLayout_ListNumberPages()
    #     self.CreateButtonsPage()
    #     self.ListRequest.clear()
    #     self.SaveRequest(self.ChoiceSaveRequest(index=0), self.CurrentEntities())
    #     self.FillingTable(1)

    def ClickedSearchDate(self):
        date = self.view.dateEdit_Searchdate.text()
        self.IsFilterDate = True
        self.ChoiceParameterDate(date)

    def ChoiceParameterDate(self, date: str):
        ComponentsDate = list(map(int, date.split(".")))
        self.DataDate = ComponentsDate
        year = ComponentsDate[2]
        month = ComponentsDate[1]
        day = ComponentsDate[0]
        if self.view.comboBox_Date.currentText() == "По полной дате":
            self.QuantityRequest = self.model.GetQuantityByDate(date, self.CurrentTable(), self.client.ID)
            self.TableFilter(self.model.Get11RequestByDate(0, self.reverse, self.CurrentTable(), date, self.client.ID))
        elif self.view.comboBox_Date.currentText() == "По году":
            self.QuantityRequest = self.model.GetQuantityByYear(year, self.CurrentTable(), self.client.ID)
            self.TableFilter(self.model.Get11RequestByYear(0, self.reverse, self.CurrentTable(), year, self.client.ID))
        elif self.view.comboBox_Date.currentText() == "По месяцу":
            self.QuantityRequest = self.model.GetQuantityByMonth(month, self.CurrentTable(), self.client.ID)
            self.TableFilter(self.model.Get11RequestByMonth(0, self.reverse, self.CurrentTable(), month, self.client.ID))
        elif self.view.comboBox_Date.currentText() == "По дню":
            self.QuantityRequest = self.model.GetQuantityByDay(day, self.CurrentTable(), self.client.ID)
            self.TableFilter(self.model.Get11RequestByDay(0, self.reverse, self.CurrentTable(), day, self.client.ID))

    def TableFilter(self, requests: list):
        self.view.lcdNumber.display(self.QuantityRequest)
        self.ListRequest.clear()
        self.SaveRequest(requests, self.CurrentEntities())
        self.FillingTable(1)
        self.ClearLayout_ListNumberPages()
        self.CreateButtonsPage()
        self.CursorPage = 1

    def ClearLayout_ListNumberPages(self):
        while self.view.horizontalLayout_ListNumberPages.count():
            child = self.view.horizontalLayout_ListNumberPages.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def SaveRequest(self, list_requests, request: [Request, AcceptRequest, DenyRequest]):
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
            self.ListRequest.append(req)

    def FillingTable(self, NumberPage):
        self.view.tableWidget_TableApplication.setRowCount(len(self.ListRequest))
        RowTable = ((int(NumberPage) - 1) / 11)
        for index, request in enumerate(self.ListRequest, start=((int(NumberPage) - 1) * 11) + 1):
            self.SetItem(RowTable)
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

    def SetItem(self, index):
        self.view.tableWidget_TableApplication.setVerticalHeaderItem(index, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 0, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 1, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 2, self.NewItem())
        self.view.tableWidget_TableApplication.setItem(index, 3, self.NewItem())

    def NewItem(self):
        return QTableWidgetItem()

    def CreateButtonsPage(self):
        if self.QuantityRequest == 0:
            pass
        elif self.QuantityRequest <= 55:  #55 - это 5 отображаемых страниц(на 1-ой странице по 11 заявок)
            self.CreateButton(ceil(self.QuantityRequest / 11))
        else:
            self.CreateButton(5)
            self.CreateButton(QuantityButton=1, ButtonText="...")
            self.CreateButton(QuantityButton=1, ButtonText=str(ceil(self.QuantityRequest / 11)))

    def CreateButton(self, QuantityButton, ButtonText=None):
        if ButtonText is None:
            for page in range(1, QuantityButton + 1):
                name_btn = f"PushButton{page}"
                self.FunctionalCreateButton(name_btn, str(page))
                exec(f'self.view.Button_Group.addButton(self.view.{name_btn}, page)')
            if 'PushButton1' in self.view.__dict__.keys():
                self.view.PushButton1.setStyleSheet('background-color: rgb(85, 255, 127); border: 2px solid gray;')
        elif ButtonText is not None:
            ButtonName = ButtonText
            text = ButtonText
            if ButtonName == "...": ButtonName = "PushButtonEllipsis"
            elif ButtonName.isdigit(): ButtonName = "PushButton_Number"
            self.FunctionalCreateButton(ButtonName, text)
            if ButtonText == 'PushButton_Number':
                exec(f'self.view.Button_Group.addButton(self.view.{ButtonName}, int(text))')

    def FunctionalCreateButton(self, NameButton, TextButton):
        exec(f"self.view.{NameButton} = QPushButton(self.view.horizontalLayoutWidget)")
        exec(f"self.view.{NameButton}.setMinimumSize(QSize(0, 25))")
        exec(
            f"self.view.{NameButton}.setStyleSheet('background-color: rgb(255, 255, 255); border: 2px solid gray;')")
        exec(f"self.view.{NameButton}.setObjectName('{NameButton}')")
        exec(f"self.view.horizontalLayout_ListNumberPages.addWidget(self.view.{NameButton})")
        exec(f'self.view.{NameButton}.setText(self._translate("MainWindow", str(TextButton)))')

    def ClickedSubmitApplication(self):
        if self.RequestSubmission == None:
            self.RequestSubmission = ControllerRequestSubmission(self.client)
            self.RequestSubmission.RunViewRequestSubmission()
        else:
            self.RequestSubmission.RunViewRequestSubmission()

    def ClickedBackFirstPage(self):
        self.BackBeginning()

    def ClickedUpdatetable(self):
        self.IsFilterDate = False
        self.view.comboBox_Date.setCurrentIndex(0)
        self.Status = "В пути"
        # self.QuantityRequest = self.model.GetQuantityRequestPositionWay(self.client.ID)
        self.view.comboBox_Status.setCurrentIndex(0)
        self.reverse = True
        self.view.comboBox_SortTable.setCurrentIndex(0)
        self.UpdateTable()
        self.BackBeginning()

    def UpdateTable(self):
        lastQuantityRequest = self.QuantityRequest
        self.QuantityRequest = self.model.GetQuantityRequest(self.CurrentTable(), self.client.ID)
        self.view.lcdNumber.display(self.QuantityRequest)
        if ceil(lastQuantityRequest / 11) < ceil(self.QuantityRequest / 11):
            self.ClearLayout_ListNumberPages()
            self.CreateButtonsPage()
            self.CursorPage = 1

        if ceil(lastQuantityRequest / 11) > ceil(self.QuantityRequest / 11):
            self.ClearLayout_ListNumberPages()
            self.CreateButtonsPage()
            self.CursorPage = 1

    def BackBeginning(self):
        btn_group = self.view.Button_Group.buttons()
        step = int(btn_group[0].text()) - 1
        LastCursor = self.CursorPage - step if self.CursorPage != int(self.view.Button_Group.buttons()[-1].text()) else self.CursorPage
        self.EditStepBack(step)
        self.ListRequest.clear()
        self.SaveRequest(self.ChoiceSaveRequest(index=0), self.CurrentEntities())
        self.FillingTable(1)
        self.view.Button_Group.button(LastCursor).setStyleSheet("background-color: rgb(255, 255, 255);"
                                                                            "border: 2px solid gray;")
        self.CursorPage = 1
        self.view.Button_Group.button(self.CursorPage).setStyleSheet("background-color: rgb(85, 255, 127);"
                                                                     "border: 2px solid gray;")

    def ChoiceSaveRequest(self, index):
        if self.IsFilterDate:
            return self.ChoiceFunctionDate(index)
        else:
            return self.model.Get11Request(index, self.reverse, self.CurrentTable(), self.client.ID)

    def ChoiceFunctionDate(self, index):
        if self.view.comboBox_Date.currentText() == "По полной дате":
            date = self.view.dateEdit_Searchdate.text()
            return self.model.Get11RequestByDate(index, self.reverse, self.CurrentTable(), date, self.client.ID)
        if self.view.comboBox_Date.currentText() == "По году":
            return self.model.Get11RequestByYear(index, self.reverse, self.CurrentTable(), self.DataDate[2], self.client.ID)
        if self.view.comboBox_Date.currentText() == "По месяцу":
            return self.model.Get11RequestByMonth(index, self.reverse, self.CurrentTable(), self.DataDate[1], self.client.ID)
        if self.view.comboBox_Date.currentText() == "По дню":
            return self.model.Get11RequestByDay(index, self.reverse, self.CurrentTable(), self.DataDate[0], self.client.ID)

    def ClickedButtonPage(self, button):
        if int(button.text()) != self.CursorPage:
            index_button = self.IdentifyClickedButton(button)
            self.last_cursor = self.CursorPage
            self.CursorPage = int(button.text())
            index = (int(button.text()) - 1) * 11
            self.ListRequest.clear()
            self.SaveRequest(self.ChoiceSaveRequest(index), self.CurrentEntities())
            self.FillingTable(int(button.text()))
            if 0 <= index_button <= 1:
                self.StepBack(button)
            elif 3 <= index_button <= 4:
                self.StepFront(button)

            self.view.Button_Group.button(self.last_cursor).setStyleSheet("background-color: rgb(255, 255, 255);"
                                                                     "border: 2px solid gray;")
            self.view.Button_Group.button(self.CursorPage).setStyleSheet('background-color: rgb(85, 255, 127); '
                                                                         'border: 2px solid gray;')
            del self.last_cursor

    def StepFront(self, button):
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

    def ClickedProfile(self):
        self.UserProfile = ControllerUserProfile(self.client, self)
        self.UserProfile.RunViewUserProfile()
        self.ApplicationWindow.setEnabled(False)

    def ClickedExit(self):
        self.ApplicationWindow.close()