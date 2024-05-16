from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Repositories.DriverRepository import DriverRepository
from TransportCompany.Repositories.AcceptRequestRepository import AcceptRequestRepository
from TransportCompany.Entities.Request import Request
class ModelConfirmOrder:
    def Get5Driver(self):
        return DriverRepository().Get5Driver()

    def Get5DriverWithException(self, id: int):
        return DriverRepository().Get5DriverWithException(id)

    def AddAcceptRequest(self, request: Request):
        AcceptRequestRepository().AddAcceptRequest(request)

    def UpdateDriver(self, IdRequest, IdDriver):
        DriverRepository().UpdateDriver(IdRequest, IdDriver)