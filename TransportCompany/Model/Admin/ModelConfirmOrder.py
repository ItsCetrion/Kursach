from Repositories.DriverRepository import DriverRepository
from Repositories.AcceptRequestRepository import AcceptRequestRepository
from Entities.Request import Request


class ModelConfirmOrder:
    @staticmethod
    def Get5Driver():
        return DriverRepository().Get5Driver()

    @staticmethod
    def Get5DriverWithException(id: int):
        return DriverRepository().Get5DriverWithException(id)

    @staticmethod
    def AddAcceptRequest(request: Request):
        AcceptRequestRepository().AddAcceptRequest(request)

    @staticmethod
    def UpdateDriver(IdRequest, IdDriver):
        DriverRepository().UpdateDriver(IdRequest, IdDriver)