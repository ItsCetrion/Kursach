from Model.Client.ModelRequestSubmission import ModelRequestSubmission
from View.Client.ViewRequestSubmission import ViewRequestSubmission
from Entities.Request import Request
from Entities.Client import Client
from PyQt5 import QtWidgets
import sys


class ControllerRequestSubmission:
    def __init__(self, client: Client):
        self.__model = ModelRequestSubmission()
        self.view = ViewRequestSubmission()
        self.__SettingsUI()
        self.__Client = client
        self.__FillingFields()
        self.__RequestSubmission.closeEvent = self.__closeEvent

        self.view.pushButton_CreateRequest.clicked.connect(self.__ClickedCreateRequest)
        self.view.pushButton_Back.clicked.connect(self.__ClickedBack)


    def __SettingsUI(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__RequestSubmission = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.__RequestSubmission)

    def RunViewRequestSubmission(self):
        self.__RequestSubmission.show()

    def __FillingFields(self):
        self.view.lineEdit_FirstName.setText(str(self.__Client.FirstName))
        self.view.lineEdit_LastName.setText(str(self.__Client.LastName))
        self.view.lineEdit_Email.setText(str(self.__Client.Email))
        self.view.lineEdit_NumberPhone.setText(str(self.__Client.NumberPhone))

    def __ClickedCreateRequest(self):
        if self.__isCheckWight():
            request = self.__FillingRequest()
            values_request = list(request.__dict__.values())[1:-1]
            if len(set([None, ""]).intersection(values_request)) != 0:
                self.view.message("Информация", "Не все поля заполнены!")
            else:
                self.__model.AddRequest(request)
                self.view.message("Информация", "Заявка отправлена, ждите рассмотрения!")
                self.__RequestSubmission.close()

    def __isCheckWight(self):
        try:
            if int(self.view.lineEdit_CargoWeight.text()) > 20000:
                self.view.message("Информация", "Извините, грузы тяжелее чем 20 тонн, компания не перевозит!")
                return False
            else:
                return True
        except ValueError:
            self.view.message("Информация", "Не указан вес грузу!")
            return False

    def __FillingRequest(self):
        request = Request()
        request.IdClient = self.__Client.ID
        request.FirstName = self.__Client.FirstName
        request.LastName = self.__Client.LastName
        request.Email = self.__Client.Email
        request.NumberPhone = self.__Client.NumberPhone
        request.PlaceDeparture = self.view.lineEdit_PlaceDispatch.text()
        request.PlaceDelivery = self.view.lineEdit_PlaceDelivery.text()
        request.CargoWeight = self.view.lineEdit_CargoWeight.text()
        request.CargoDescription = self.view.lineEdit_CargoDescription.text()
        return request

    def __ClickedBack(self):
        self.__RequestSubmission.close()

    def __closeEvent(self, event):
        self.view.lineEdit_PlaceDispatch.clear()
        self.view.lineEdit_PlaceDelivery.clear()
        self.view.lineEdit_CargoDescription.clear()
        self.view.lineEdit_CargoWeight.clear()
        event.accept()

