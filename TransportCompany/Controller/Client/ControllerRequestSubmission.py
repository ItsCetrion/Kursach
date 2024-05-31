from TransportCompany.Model.Client.ModelRequestSubmission import ModelRequestSubmission
from TransportCompany.View.Client.ViewRequestSubmission import ViewRequestSubmission
from TransportCompany.Entities.Request import Request
from TransportCompany.Entities.Client import Client
from PyQt5 import QtWidgets
import sys
class ControllerRequestSubmission:
    def __init__(self, client: Client):
        self.model = ModelRequestSubmission()
        self.view = ViewRequestSubmission()
        self.SettingsUI()
        self.Client = client
        self.FillingFields()
        self.RequestSubmission.closeEvent = self.closeEvent

        self.view.pushButton_CreateRequest.clicked.connect(self.ClickedCreateRequest)
        self.view.pushButton_Back.clicked.connect(self.ClickedBack)


    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.RequestSubmission = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.RequestSubmission)

    def RunViewRequestSubmission(self):
        self.RequestSubmission.show()
        # sys.exit(self.app.exec_())

    def FillingFields(self):
        self.view.lineEdit_FirstName.setText(str(self.Client.FirstName))
        self.view.lineEdit_LastName.setText(str(self.Client.LastName))
        self.view.lineEdit_Email.setText(str(self.Client.Email))
        self.view.lineEdit_NumberPhone.setText(str(self.Client.NumberPhone))


    def ClickedCreateRequest(self):
        if self.isCheckWight():
            request = self.FillingRequest()
            values_request = list(request.__dict__.values())[1:-1]
            if len(set([None, ""]).intersection(values_request)) != 0:
                self.view.message("Информация", "Не все поля заполнены!")
            else:
                self.model.AddRequest(request)
                self.view.message("Информация", "Заявка отправлена, ждите рассмотрения!")
                self.RequestSubmission.close()

    def isCheckWight(self):
        try:
            if int(self.view.lineEdit_CargoWeight.text()) > 20000:
                self.view.message("Информация", "Извините, грузы тяжелее чем 20 тонн, компания не перевозит!")
                return False
            else:
                return True
        except ValueError:
            self.view.message("Информация", "Не указан вес грузу!")
            return False

    def FillingRequest(self):
        request = Request()
        request.IdClient = self.Client.ID
        request.FirstName = self.Client.FirstName
        request.LastName = self.Client.LastName
        request.Email = self.Client.Email
        request.NumberPhone = self.Client.NumberPhone
        request.PlaceDeparture = self.view.lineEdit_PlaceDispatch.text()
        request.PlaceDelivery = self.view.lineEdit_PlaceDelivery.text()
        request.CargoWeight = self.view.lineEdit_CargoWeight.text()
        request.CargoDescription = self.view.lineEdit_CargoDescription.text()
        return request



    def ClickedBack(self):
        self.RequestSubmission.close()

    def closeEvent(self, event):
        self.view.lineEdit_PlaceDispatch.clear()
        self.view.lineEdit_PlaceDelivery.clear()
        self.view.lineEdit_CargoDescription.clear()
        self.view.lineEdit_CargoWeight.clear()
        event.accept()

