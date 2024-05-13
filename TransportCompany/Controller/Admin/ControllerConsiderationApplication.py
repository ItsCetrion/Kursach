from TransportCompany.Model.Admin.ModelConsiderationApplication import ModelConsiderationApplication
from TransportCompany.View.Admin.ViewConsiderationApplication import ViewConsiderationApplication
from TransportCompany.Entities.Request import Request
from PyQt5 import QtWidgets
import sys

class ControllerConsiderationApplication():
    def __init__(self, parentwindow):
        self.view = ViewConsiderationApplication()
        self.model = ModelConsiderationApplication()
        self.parentwindow = parentwindow
        self.SettingsUI()

        self.view.pushButton_Back.clicked.connect(self.ClickedBack)
    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ConsiderationApplication = QtWidgets.QDialog()
        ui = self.view
        ui.setupUi(self.ConsiderationApplication)

    def FillingFields(self, request):
        self.view.lineEdit_date.setText(request.DateRequest)
        self.view.textEdit_dispatch.setText(request.PlaceDeparture)
        self.view.textEdit_delivery.setText(request.PlaceDelivery)
        self.view.textEdit_description.setText(request.CargoDescription)
        self.view.lineEdit_weight.setText(str(request.CargoWeight))
        self.view.textEdit_FirstName.setText(request.FirstName)
        self.view.textEdit_LastName.setText(request.LastName)
        self.view.textEdit_Phone.setText(request.NumberPhone)
        self.view.textEdit_Email.setText(request.Email)

    def RunViewConsiderationApplication(self):
        self.ConsiderationApplication.show()

    def ClickedBack(self):
        self.ConsiderationApplication.destroy(destroyWindow=True)


