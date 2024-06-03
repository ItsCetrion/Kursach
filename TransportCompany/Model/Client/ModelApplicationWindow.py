from TransportCompany.Repositories.AllRequestRepository import AllRequestRepository


class ModelApplicationWindow:
    @staticmethod
    def Get11Request(StartIndex: int, reverse: bool, table: str, IdClient: int):
        return AllRequestRepository().Get11Request(StartIndex, reverse, table, IdClient)

    @staticmethod
    def Get11RequestByDate(StartIndex: int, reverse: bool, table: str, date: str, IdClient: int):
        return AllRequestRepository().Get11RequestByDate(StartIndex, reverse, table, date, IdClient)

    @staticmethod
    def Get11RequestByYear(StartIndex: int, reverse: bool, table: str, year: int, IdClient: int):
        return AllRequestRepository().Get11RequestByYear(StartIndex, reverse, table, year, IdClient)

    @staticmethod
    def Get11RequestByMonth(StartIndex: int, reverse: bool, table: str, mouth: int, IdClient: int):
        return AllRequestRepository().Get11RequestByMonth(StartIndex, reverse, table, mouth, IdClient)

    @staticmethod
    def Get11RequestByDay(StartIndex: int, reverse: bool, table: str, day: int, IdClient: int):
        return AllRequestRepository().Get11RequestByDay(StartIndex, reverse, table, day, IdClient)

    @staticmethod
    def GetQuantityRequest(table: str, IdClient: int):
        return AllRequestRepository().GetQuantityRequest(table, IdClient)

    @staticmethod
    def GetQuantityByDate(date: str, table: str, IdClient: int):
        return AllRequestRepository().GetQuantityByDate(date, table, IdClient)

    @staticmethod
    def GetQuantityByYear(year: int, table: str, IdClient: int):
        return AllRequestRepository().GetQuantityByYear(year, table, IdClient)

    @staticmethod
    def GetQuantityByMonth(month: int, table: str, IdClient: int):
        return AllRequestRepository().GetQuantityByMonth(month, table, IdClient)

    @staticmethod
    def GetQuantityByDay(day: int, table: str, IdClient: int):
        return AllRequestRepository().GetQuantityByDay(day, table, IdClient)
