from TransportCompany.Repositories.DriverRepository import DriverRepository
from TransportCompany.Repositories.AcceptRequestRepository import AcceptRequestRepository
from TransportCompany.Repositories.DeliveredRequestRepositories import DeliveredRequestRepositories
from TransportCompany.Entities.DeliveredRequest import DeliveredRequest


class ModelMainWindow:
    @staticmethod
    def GetCompletedOrders(Id_driver):
        return DeliveredRequestRepositories().GetCompletedOrders(Id_driver)

    @staticmethod
    def GetActiveOrder(Id_driver):
        return DriverRepository().GetActiveOrder(Id_driver)

    @staticmethod
    def GetAcceptRequest(IdRequest):
        return AcceptRequestRepository(). GetAcceptRequest(IdRequest)

    @staticmethod
    def GetIdDriverByIdOrder(IdOrder):
        return DriverRepository().GetIdDriverByIdOrder(IdOrder)

    @staticmethod
    def DeleteAcceptRequest(IdRequest):
        DriverRepository().DeleteIdOrder(IdRequest)
        AcceptRequestRepository().DeleteAcceptRequest(IdRequest)

    @staticmethod
    def AddDeliveredRequest(request: DeliveredRequest):
        DeliveredRequestRepositories().AddDeliveredRequest(request)

