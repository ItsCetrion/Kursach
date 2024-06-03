from TransportCompany.Repositories.DenyRequestRepository import DenyRequestRepository
from TransportCompany.Entities.DenyRequest import DenyRequest


class ModelConsiderationApplication:
    @staticmethod
    def AddDenyRequest(deny_request: DenyRequest):
        DenyRequestRepository().AddDenyRequest(deny_request)