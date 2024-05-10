from TransportCompany.Entities.Request import Request
from TransportCompany.Repositories.RequestRepository import RequestRepository
class ModelWindowApplication:
    def __init__(self):
        self.RequestRepository = RequestRepository()

    def AddRequest(self, request: Request):
        self.RequestRepository.AddRequest(request)

    def GetRequestByDate(self, data: str):
        return self.RequestRepository.GetRequestByDate(data)

    def GetRequestByYearAndMonth(self, year: int, month: int):
        return self.RequestRepository.GetRequestByYearAndMonth(year, month)

    def GetRequestByYearAndDay(self, year: int, day: int):
        return self.RequestRepository.GetRequestByYearAndDay(year, day)

    def GetRequestByMonthAndDay(self, month: int, day: int):
        return self.RequestRepository.GetRequestByMonthAndDay(month,day)

    def GetRequestByYear(self, year: int):
        return self.RequestRepository.GetRequestByYear(year)

    def GetRequestByMonth(self, month: int):
        return self.RequestRepository.GetRequestByMonth(month)

    def GetRequestByDay(self, day):
        return self.RequestRepository.GetRequestByDay(day)

    def GetRequestByFirstName(self, PartFirstName):
        return self.RequestRepository.GetRequestByFirstName(PartFirstName)

    def GetRequestByLastName(self, PartLastName):
        return self.RequestRepository.GetRequestByLastName(PartLastName)

    def GetSortByDecreaseDate(self):
        return self.RequestRepository.GetSortByDecreaseDate()

    def GetSortByEscalatingDate(self):
        return self.RequestRepository.GetSortByEscalatingDate()

    def GetSortByAlphabeticalOrder(self):
        return self.RequestRepository.GetSortByAlphabeticalOrder()

    def GetSortReverseAlphabeticalOrder(self):
        return self.RequestRepository.GetSortReverseAlphabeticalOrder()

    def GetAll(self):
        return self.RequestRepository.GetAll()

