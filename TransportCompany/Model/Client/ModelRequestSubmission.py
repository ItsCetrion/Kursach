from Repositories.RequestRepository import RequestRepository
from Entities.Request import Request


class ModelRequestSubmission:

    @staticmethod
    def AddRequest(request: Request):
        RequestRepository().AddRequest(request)