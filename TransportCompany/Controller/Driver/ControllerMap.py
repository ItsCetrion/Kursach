from TransportCompany.View.Driver.ViewMap import ViewMap
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout
from pyqtlet2 import L, MapWidget
from geopy.geocoders import Nominatim
class ControllerMap:
    def __init__(self, PlaceDeparture, PlaceDelivery, parent):
        self.view = ViewMap()
        self.PlaceDeparture = PlaceDeparture
        self.PlaceDelivery = PlaceDelivery
        self.parent = parent
        self.SettingsUI()
        self.CreateMap()
        self.view.closeEvent = self.closeEvent
    def SettingsUI(self):
        self.app = QApplication(sys.argv)

    def RunViewMap(self):
        self.view.showMaximized()

    def CreateMap(self):
        self.view.mapWidget = MapWidget()
        self.view.layout = QVBoxLayout()
        self.view.layout.addWidget(self.view.mapWidget)
        self.view.setLayout(self.view.layout)
        coordinates = self.CreateCoordinates()
        self.view.map = L.map(self.view.mapWidget)
        self.view.map.setView([coordinates[0][0], coordinates[0][1]], 15)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.view.map)
        self.view.marker1 = L.marker([coordinates[0][0], coordinates[0][1]])
        self.view.marker1.bindPopup('Начало')
        self.view.map.addLayer(self.view.marker1)
        self.view.marker2 = L.marker([coordinates[1][0], coordinates[1][1]])
        self.view.marker2.bindPopup("Конец")
        self.view.map.addLayer(self.view.marker2)

    def CreateCoordinates(self):
        locator = Nominatim(user_agent="myapp")
        start_latlng = locator.geocode(self.PlaceDeparture)
        end_latlng = locator.geocode(self.PlaceDelivery)
        del self.PlaceDelivery
        del self.PlaceDeparture
        return [(start_latlng.latitude, start_latlng.longitude), (end_latlng.latitude, end_latlng.longitude)]

    def closeEvent(self, event):
        self.parent.MainWindow.setEnabled(True)
        event.accept()