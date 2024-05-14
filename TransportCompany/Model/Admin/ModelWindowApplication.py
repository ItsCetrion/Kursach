from TransportCompany.Entities.Request import Request
from TransportCompany.Repositories.RequestRepository import RequestRepository
class ModelWindowApplication:
    def __init__(self):
        self.RequestRepository = RequestRepository()

    def AddRequest(self, request: Request):
        self.RequestRepository.AddRequest(request)

    def DeleteRequest(self, id: int):
        self.RequestRepository.DeleteRequest(id)

    def Get11RequestByDate(self, data: str, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11RequestByDate(data, StartIndex, ParameterSort, reverse)

    def Get11RequestByYearAndMonth(self, year: int, month: int, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11RequestByYearAndMonth(year, month, StartIndex, ParameterSort, reverse)

    def Get11RequestByYearAndDay(self, year: int, day: int, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11RequestByYearAndDay(year, day, StartIndex, ParameterSort, reverse)

    def Get11RequestByMonthAndDay(self, month: int, day: int, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11RequestByMonthAndDay(month, day, StartIndex, ParameterSort, reverse)

    def Get11RequestByYear(self, year: int, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11RequestByYear(year, StartIndex, ParameterSort, reverse)

    def Get11RequestByMonth(self, month: int, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11RequestByMonth(month, StartIndex, ParameterSort, reverse)

    def Get11RequestByDay(self, day: int, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11RequestByDay(day, StartIndex, ParameterSort, reverse)

    def Get11RequestByFirstName(self, PartFirstName: str, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11RequestByFirstName(PartFirstName, StartIndex, ParameterSort, reverse)

    def Get11RequestByLastName(self, PartLastName: str, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11RequestByLastName(PartLastName, StartIndex, ParameterSort, reverse)

    def GetAllQuantityReauest(self):
        return self.RequestRepository.GetAllQuantityRequest()

    def GetQuantityRequestByDate(self, date: str):
        return self.RequestRepository.GetQuantityRequestByDate(date)

    def GetQuantityRequestByYearAndMonth(self, year: int, month: int):
        return self.RequestRepository.GetQuantityRequestByYearAndMonth(year, month)

    def GetQuantityRequestByYearAndDay(self, year: int, day: int):
        return self.RequestRepository.GetQuantityRequestByYearAndDay(year, day)

    def GetQuantityRequestByMonthAndDay(self, month: int, day: int):
        return self.RequestRepository.GetQuantityRequestByMonthAndDay(month, day)

    def GetQuantityRequestByYear(self, year: int):
        return self.RequestRepository.GetQuantityRequestByYear(year)

    def GetQuantityRequestByMonth(self, month: int):
        return self.RequestRepository.GetQuantityRequestByMonth(month)

    def GetQuantityRequestByDay(self, day: int):
        return self.RequestRepository.GetQuantityRequestByDay(day)

    def GetQuantityRequestByFirstName(self, PartFirstName: str):
        return self.RequestRepository.GetQuantityRequestByFirstName(PartFirstName)

    def GetQuantityRequestByLastName(self, PartLastName: str):
        return self.RequestRepository.GetQuantityRequestByLastName(PartLastName)

    def Get11Request(self, StartIndex: int, ParameterSort: str, reverse=False):
        return self.RequestRepository.Get11Request(StartIndex, ParameterSort, reverse)

