from Model.Admin.ModelConsiderationApplication import ModelConsiderationApplication
from Model.Admin.ModelWindowApplication import ModelWindowApplication
from View.Admin.ViewConsiderationApplication import ViewConsiderationApplication
from Controller.Admin.ControllerConfirmOrder import ControllerConfirmOrder
from PyQt5 import QtWidgets
import sys


class ControllerConsiderationApplication:
    def __init__(self, parent):
        self.view = ViewConsiderationApplication()
        self.__model = ModelConsiderationApplication()
        self.__SettingsUI()
        self.__parent = parent
        self.__ConfirmOrder = None

        self.view.pushButton_Deny.clicked.connect(self.__ClickedDeny)
        self.view.pushButton_Back.clicked.connect(self.__ClickedBack)
        self.view.pushButton_MakeOrder.clicked.connect(self.ClickedMakeorder)
    def __SettingsUI(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__ConsiderationApplication = QtWidgets.QDialog()
        ui = self.view
        ui.setupUi(self.__ConsiderationApplication)

    def RunViewConsiderationApplication(self):
        self.__ConsiderationApplication.show()

    def FillingFields(self, request):
        self.__request = request
        self.view.lineEdit_date.setText(request.DateRequest)
        self.view.textEdit_dispatch.setText(request.PlaceDeparture)
        self.view.textEdit_delivery.setText(request.PlaceDelivery)
        self.view.textEdit_description.setText(request.CargoDescription)
        self.view.lineEdit_weight.setText(str(request.CargoWeight))
        self.view.textEdit_FirstName.setText(request.FirstName)
        self.view.textEdit_LastName.setText(request.LastName)
        self.view.textEdit_Phone.setText(request.NumberPhone)
        self.view.textEdit_Email.setText(request.Email)

    def __ClickedDeny(self):
        test = self.view.MessageQuestion()
        if test == QtWidgets.QMessageBox.Yes:
            ModelWindowApplication().DeleteRequest(self.__request.ID)
            self.__model.AddDenyRequest(self.__request)
            self.view.MessageOK("Информация", "Заявка успешно отклонена!")
            self.__ConsiderationApplication.destroy(destroyWindow=True)
            self.DeleteRequestFromTable()

    def DeleteRequestFromTable(self):
        self.__parent.DeleteRequestFromTable()

    def __ClickedBack(self):
        self.__ConsiderationApplication.destroy(destroyWindow=True)

    def ClickedMakeorder(self):
        if self.__ConfirmOrder is None:
            self.__ConfirmOrder = ControllerConfirmOrder(self)
            self.__ConfirmOrder.FillingFields(self.__request)
            self.__ConsiderationApplication.hide()
            self.__ConfirmOrder.RunConfirmOrder()
        else:
            self.__ConsiderationApplication.hide()
            self.__ConfirmOrder.FillingFields(self.__request)
            self.__ConfirmOrder.RunConfirmOrder()

    def Close(self):
        self.__ConsiderationApplication.close()


