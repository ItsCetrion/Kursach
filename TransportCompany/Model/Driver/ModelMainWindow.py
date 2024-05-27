from TransportCompany.Repositories.DriverRepository import DriverRepository
from TransportCompany.Repositories.AcceptRequestRepository import AcceptRequestRepository
from TransportCompany.Repositories.DeliveredRequestRepositories import DeliveredRequestRepositories
from TransportCompany.Entities.DeliveredRequest import DeliveredRequest
class ModelMainWindow:
    def GetCompletedOrders(self, Id_driver):
        return DeliveredRequestRepositories().GetCompletedOrders(Id_driver)

    def GetActiveOrder(self, Id_driver):
        return DriverRepository().GetActiveOrder(Id_driver)

    def GetAcceptRequest(self, IdRequest):
        return AcceptRequestRepository(). GetAcceptRequest(IdRequest)

    def DeleteAcceptRequest(self, IdRequest):
        DriverRepository().DeleteIdOrder(IdRequest)
        AcceptRequestRepository().DeleteAcceptRequest(IdRequest)

    def AddDeliveredRequest(self, request: DeliveredRequest):
        DeliveredRequestRepositories().AddDeliveredRequest(request)

