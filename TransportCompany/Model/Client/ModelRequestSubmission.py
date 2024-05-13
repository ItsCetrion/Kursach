from TransportCompany.Repositories.RequestRepository import RequestRepository
from TransportCompany.Entities.Request import Request

class ModelRequestSubmission:

    def AddRequest(self, request: Request):
        RequestRepository().AddRequest(request)