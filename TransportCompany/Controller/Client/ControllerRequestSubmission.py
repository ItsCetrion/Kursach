from TransportCompany.Model.Client.ModelRequestSubmission import ModelRequestSubmission
from TransportCompany.View.Client.ViewRequestSubmission import ViewRequestSubmission
from TransportCompany.Entities.Request import Request
from PyQt5 import QtWidgets
import sys
class ControllerRequestSubmission:
    def __init__(self):
        self.model = ModelRequestSubmission()
        self.view = ViewRequestSubmission()
        self.SettingsUI()
        self.view.pushButton_CreateRequest.clicked.connect(self.ClickedCreateRequest)
        # self.view.pushButton_Back.clicked.connect(self.ClickedBack)


    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.RequestSubmission = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.RequestSubmission)

    def RunViewRequestSubmission(self):
        self.RequestSubmission.show()
        sys.exit(self.app.exec_())

    def ClickedCreateRequest(self):
        request = Request()
        request.FirstName = self.view.lineEdit_FirstName.text()
        request.LastName = self.view.lineEdit_LastName.text()
        request.Email = self.view.lineEdit_Email.text()
        request.NumberPhone = self.view.lineEdit_NumberPhone.text()
        request.PlaceDeparture = self.view.lineEdit_PlaceDispatch.text()
        request.PlaceDelivery = self.view.lineEdit_PlaceDelivery.text()
        request.CargoWeight = self.view.lineEdit_CargoWeight.text()
        request.CargoDescription = self.view.lineEdit_CargoDescription.text()

        if None in (list(request.__dict__.values()))[1:-1]:
            self.view.message("Информация", "Не все поля заполнены!")
        else:
            self.model.AddRequest(request)
            self.view.message("Информация", "Заявка отправлена, ждите рассмотрения!")

    def ClickedBack(self):
        pass


