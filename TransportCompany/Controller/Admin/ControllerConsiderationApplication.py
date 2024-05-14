from TransportCompany.Model.Admin.ModelConsiderationApplication import ModelConsiderationApplication
from TransportCompany.Model.Admin.ModelWindowApplication import ModelWindowApplication
from TransportCompany.View.Admin.ViewConsiderationApplication import ViewConsiderationApplication
from TransportCompany.Controller.Admin.ControllerConfirmOrder import ControllerConfirmOrder
from TransportCompany.Entities.Request import Request
from PyQt5 import QtWidgets
import sys

class ControllerConsiderationApplication():
    def __init__(self, parent):
        self.view = ViewConsiderationApplication()
        self.model = ModelConsiderationApplication()
        self.SettingsUI()
        self.parent = parent
        self.ConfirmOrder = None

        self.view.pushButton_Deny.clicked.connect(self.ClickedDeny)
        self.view.pushButton_Back.clicked.connect(self.ClickedBack)
        self.view.pushButton_MakeOrder.clicked.connect(self.ClickedMakeorder)
    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ConsiderationApplication = QtWidgets.QDialog()
        ui = self.view
        ui.setupUi(self.ConsiderationApplication)

    def FillingFields(self, request):
        self.request = request
        self.view.lineEdit_date.setText(request.DateRequest)
        self.view.textEdit_dispatch.setText(request.PlaceDeparture)
        self.view.textEdit_delivery.setText(request.PlaceDelivery)
        self.view.textEdit_description.setText(request.CargoDescription)
        self.view.lineEdit_weight.setText(str(request.CargoWeight))
        self.view.textEdit_FirstName.setText(request.FirstName)
        self.view.textEdit_LastName.setText(request.LastName)
        self.view.textEdit_Phone.setText(request.NumberPhone)
        self.view.textEdit_Email.setText(request.Email)

    def ClickedDeny(self):
        test = self.view.MessageQuestion()
        if test == QtWidgets.QMessageBox.Yes:
            ModelWindowApplication().DeleteRequest(self.request.ID)
            self.model.AddDenyRequest(self.request)
            self.view.MessageOK("Информация", "Заявка успешно отклонена!")
            self.ConsiderationApplication.destroy(destroyWindow=True)
            self.parent.DeleteRequestFromTable()

    def RunViewConsiderationApplication(self):
        self.ConsiderationApplication.show()

    def ClickedBack(self):
        self.ConsiderationApplication.destroy(destroyWindow=True)

    def ClickedMakeorder(self):
        if self.ConfirmOrder is None:
            self.ConfirmOrder = ControllerConfirmOrder(self)
            self.ConsiderationApplication.hide()
            self.ConfirmOrder.RunConfirmOrder()
        else:
            self.ConsiderationApplication.hide()
            self.ConfirmOrder.RunConfirmOrder()

    def Close(self):
        self.ConsiderationApplication.close()


