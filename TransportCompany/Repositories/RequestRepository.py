import pyodbc

from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Request import Request


class RequestRepository:
    @staticmethod
    def AddRequest(request: Request):
        context = DBContext()
        cursor = context.cursor
        query = (f"""INSERT INTO Request
                         VALUES('{request.FirstName}','{request.LastName}','{request.Email}','{request.NumberPhone}',
                         '{request.PlaceDeparture}','{request.PlaceDelivery}',
                         '{request.CargoWeight}', '{request.CargoDescription}')""")
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

    def GetRequestByDate(self, date: str):
        result = self.Demand(f"""SELECT FirstName,LastName,DateRequest FROM Request WHERE DateRequest = '{date}'""")
        return result

    def GetRequestByYearAndMonth(self, year: int, month: int):
        result = self.Demand(f"""SELECT FirstName,LastName,DateRequest FROM Request 
                                 WHERE DATEPART(MONTH, DateRequest) = {month} and DATEPART(YEAR, DateRequest) = {year}""")
        return result

    def GetRequestByYearAndDay(self, year: int, day: int):
        result = self.Demand(f"""SELECT FirstName,LastName,DateRequest FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = {day} and DATEPART(YEAR, DateRequest) = {year}""")
        return result

    def GetRequestByMonthAndDay(self, month: int, day: int):
        result = self.Demand(f"""SELECT FirstName,LastName,DateRequest FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = {day} and DATEPART(MONTH, DateRequest) = {month}""")
        return result
    def GetRequestByYear(self, year: int):
        result = self.Demand(f"""SELECT FirstName,LastName,DateRequest
                             FROM Request WHERE DATEPART(YEAR, DateRequest) = {year}""")
        return result

    def GetRequestByMonth(self, month: int):
        result = self.Demand(f"""SELECT FirstName,LastName,DateRequest
                                 FROM Request WHERE DATEPART(MONTH, DateRequest) = {month}""")
        return result

    def GetRequestByDay(self, day: int):
        result = self.Demand(f"""SELECT FirstName,LastName,DateRequest
                                        FROM Request WHERE DATEPART(DAY, DateRequest) = {day}""")
        return result

    def GetRequestByFirstName(self, PartFirstName):
        result = self.Demand(f"""SELECT FirstName,LastName,DateRequest
                                        From Request WHERE FirstName LIKE '{PartFirstName}%'""")
        return result

    def GetRequestByLastName(self, PartLastName):
        result = self.Demand(f"""SELECT FirstName,LastName,DateRequest
                                                From Request WHERE LastName LIKE '{PartLastName}%'""")
        return result

    def GetSortByDecreaseDate(self):
        result = self.Demand("""SELECT FirstName, LastName, DateRequest
                                From Request Order By DateRequest DESC""")
        return result

    def GetSortByEscalatingDate(self):
        result = self.Demand("""SELECT FirstName, LastName, DateRequest
                                From Request Order By DateRequest""")
        return result

    def GetSortByAlphabeticalOrder(self):
        result = self.Demand("""SELECT FirstName, LastName, DateRequest
                                 From Request Order By FirstName""")
        return result

    def GetSortReverseAlphabeticalOrder(self):
        result = self.Demand("""SELECT FirstName, LastName, DateRequest
                                         From Request Order By FirstName DESC""")
        return result

    def GetAll(self):
        result = self.Demand("""SELECT FirstName, LastName, DateRequest FROM Request""")
        return result

    def Demand(self, query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except pyodbc.ProgrammingError:
            raise "проблемы с подключением"


