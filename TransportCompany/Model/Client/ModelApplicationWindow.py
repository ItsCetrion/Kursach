from TransportCompany.Repositories.AllRequestRepository import AllRequestRepository
class ModelApplicationWindow:
    def Get11Request(self, StartIndex: int, reverse: bool, table: str, IdClient: int):
        return AllRequestRepository().Get11Request(StartIndex, reverse, table, IdClient)

    def Get11RequestByDate(self, StartIndex: int, reverse: bool, table: str, date: str, IdClient: int):
        return AllRequestRepository().Get11RequestByDate(StartIndex, reverse, table, date, IdClient)

    def Get11RequestByYear(self, StartIndex: int, reverse: bool, table: str, year: int, IdClient: int):
        return AllRequestRepository().Get11RequestByYear(StartIndex, reverse, table, year, IdClient)

    def Get11RequestByMonth(self, StartIndex: int, reverse: bool, table: str, mouth: int, IdClient: int):
        return AllRequestRepository().Get11RequestByMonth(StartIndex, reverse, table, mouth, IdClient)

    def Get11RequestByDay(self, StartIndex: int, reverse: bool, table: str, day: int, IdClient: int):
        return AllRequestRepository().Get11RequestByDay(StartIndex, reverse, table, day, IdClient)

    def GetQuantityRequest(self, table: str, IdClient: int):
        return AllRequestRepository().GetQuantityRequest(table, IdClient)

    def GetQuantityByDate(self, date: str, table: str, IdClient: int):
        return AllRequestRepository().GetQuantityByDate(date, table, IdClient)

    def GetQuantityByYear(self, year: int, table: str, IdClient: int):
        return AllRequestRepository().GetQuantityByYear(year, table, IdClient)

    def GetQuantityByMonth(self, month: int, table: str, IdClient: int):
        return AllRequestRepository().GetQuantityByMonth(month, table, IdClient)

    def GetQuantityByDay(self, day: int, table: str, IdClient: int):
        return AllRequestRepository().GetQuantityByDay(day, table, IdClient)
