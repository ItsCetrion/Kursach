from TransportCompany.Model.Admin.ModelConfirmOrder import ModelConfirmOrder
from TransportCompany.View.Admin.ViewConfirmOrder import ViewConfirmOrder
from PyQt5 import QtWidgets
import sys
class ControllerConfirmOrder:
    def __init__(self, parent):
        self.model = ModelConfirmOrder()
        self.view = ViewConfirmOrder()
        self.SettingsUI()
        self.parent = parent
        self.view.pushButton_Back.clicked.connect(self.ClickedBack)
        self.view.pushButton_Confirm.clicked.connect(self.ClickedConfirm)


    def SettingsUI(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ConfirmOrder = QtWidgets.QMainWindow()
        ui = self.view
        ui.setupUi(self.ConfirmOrder)

    def RunConfirmOrder(self):
        self.ConfirmOrder.show()

    def ClickedBack(self):
        self.ConfirmOrder.close()
        self.parent.RunViewConsiderationApplication()

    def ClickedConfirm(self):
        self.ConfirmOrder.close()
        self.parent.Close()