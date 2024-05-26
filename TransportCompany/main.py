# from Controller.ControllerLogin import ControllerLogin
# from Controller.Admin.ControllerWindowApplication import ControllerWindowApplication
# from Controller.Client.ControllerRequestSubmission import ControllerRequestSubmission
# from Controller.Client.ControllerApplicationWindow import ControllerApplicationWindow
# from Entities.Client import Client
#
#
# def main(client):
#     app = ControllerLogin()
#     app.RunViewLogin()
#     app.StartProgram()
#
#     # app = ControllerWindowApplication()
#     # app.RunViewWindowApplication()
#
#     # app = ControllerRequestSubmission(client)
#     # app.RunViewRequestSubmission()
#
#     # app = ControllerApplicationWindow(1)
#     # app.RunViewApplicationWindow()
#
#
# if __name__ == "__main__":
#     client = Client()
#     # client.Id = 1
#     # client.FirstName = "Иван"
#     # client.LastName = "Иванов"
#     # client.Email = "test@mail.ru"
#     # client.NumberPhone = "79951622900"
#     main(client)

import sys
import io
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet2 import L, MapWidget
from geopy.geocoders import Nominatim


class MapWindow(QWidget):
    def __init__(self):
        # Setting up the widgets and layout
        super().__init__()
        self.mapWidget = MapWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)

        locator = Nominatim(user_agent="myapp")
        start_location = "Красноярск борисова 24"
        start_latlng = locator.geocode(start_location)
        end_location = "Кемерово"
        end_latlng = locator.geocode(end_location)
        loc = [(start_latlng.latitude, start_latlng.longitude),(end_latlng.latitude, end_latlng.longitude)]

        # Working with the maps with pyqtlet
        self.map = L.map(self.mapWidget)
        self.map.setView([start_latlng.latitude, start_latlng.longitude], 15)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)
        self.marker1 = L.marker([start_latlng.latitude, start_latlng.longitude])
        self.marker1.bindPopup('Начало')
        self.map.addLayer(self.marker1)
        self.marker2 = L.marker([end_latlng.latitude, end_latlng.longitude])
        self.marker2.bindPopup("Конец")

        self.map.addLayer(self.marker2)
        self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MapWindow()
    sys.exit(app.exec_())
