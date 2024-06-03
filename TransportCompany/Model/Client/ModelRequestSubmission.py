from TransportCompany.Repositories.RequestRepository import RequestRepository
from TransportCompany.Entities.Request import Request


class ModelRequestSubmission:

    @staticmethod
    def AddRequest(request: Request):
        RequestRepository().AddRequest(request)