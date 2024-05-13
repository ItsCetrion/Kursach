import pyodbc

from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Request import Request


class RequestRepository:
    @staticmethod
    def AddRequest(request: Request):
        context = DBContext()
        cursor = context.cursor
        query = (f"""INSERT INTO Request(FirstName,LastName,Email,NumberPhone,PlaceDeparture,PlaceDelivery,CargoWeight,
                     CargoDescription)
                         VALUES('{request.FirstName}','{request.LastName}','{request.Email}','{request.NumberPhone}',
                         '{request.PlaceDeparture}','{request.PlaceDelivery}',
                         '{request.CargoWeight}', '{request.CargoDescription}')""")
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

    def Get11RequestByDate(self, date: str, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest
                                 FROM Request WHERE DateRequest = '{date}'
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""")
        return result

    def Get11RequestByYearAndMonth(self, year: int, month: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest 
                                 FROM Request 
                                 WHERE DATEPART(MONTH, DateRequest) = {month} and DATEPART(YEAR, DateRequest) = {year}
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""")
        return result

    def Get11RequestByYearAndDay(self, year: int, day: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest
                                 FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = {day} and DATEPART(YEAR, DateRequest) = {year}
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""")
        return result

    def Get11RequestByMonthAndDay(self, month: int, day: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest
                                 FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = {day} and DATEPART(MONTH, DateRequest) = {month}
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""")
        return result

    def Get11RequestByYear(self, year: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest
                             FROM Request WHERE DATEPART(YEAR, DateRequest) = {year}
                             Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""")
        return result

    def Get11RequestByMonth(self, month: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest
                                 FROM Request WHERE DATEPART(MONTH, DateRequest) = {month}
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""")
        return result

    def Get11RequestByDay(self, day: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest
                                 FROM Request WHERE DATEPART(DAY, DateRequest) = {day}
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""")
        return result

    def Get11RequestByFirstName(self, PartFirstName: str, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest
                                 From Request WHERE FirstName LIKE '{PartFirstName}%'
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""")
        return result

    def Get11RequestByLastName(self, PartLastName: str, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest
                                 From Request WHERE LastName LIKE '{PartLastName}%'
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""")
        return result


    def GetAllQuantityRequest(self):
        result = self.Demand("SELECT COUNT(*) FROM Request"
                             "")
        return result[0][0]

    def GetQuantityRequestByDate(self, date: str):
        result = self.Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DateRequest = '{date}'""")
        return result[0][0]

    def GetQuantityRequestByYearAndMonth(self, year: int, month: int):
        result = self.Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(MONTH, DateRequest) = {month} and DATEPART(YEAR, DateRequest) = {year}""")
        return result[0][0]

    def GetQuantityRequestByYearAndDay(self, year: int, day: int):
        result = self.Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = {day} and DATEPART(YEAR, DateRequest) = {year}""")
        return result[0][0]

    def GetQuantityRequestByMonthAndDay(self, month: int, day: int):
        result = self.Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = {day} and DATEPART(MONTH, DateRequest) = {month}""")
        return result[0][0]

    def GetQuantityRequestByYear(self, year: int):
        result = self.Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(YEAR, DateRequest) = {year}""")
        return result[0][0]

    def GetQuantityRequestByMonth(self, month: int):
        result = self.Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(MONTH, DateRequest) = {month}""")
        return result[0][0]

    def GetQuantityRequestByDay(self, day: int):
        result = self.Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = {day}""")
        return result[0][0]

    def GetQuantityRequestByFirstName(self, PartFirstName: str):
        result = self.Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE FirstName LIKE '{PartFirstName}%'""")
        return result[0][0]

    def GetQuantityRequestByLastName(self, PartLastName: str):
        result = self.Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE LastName LIKE '{PartLastName}%'""")
        return result[0][0]



    def Get11Request(self, StartIndex: int, ParameterSort: str, reverse):
        sort = "ASC" if reverse is False else "DESC"
        result = self.Demand(f"""SELECT FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateRequest
                                    FROM Request Order By {ParameterSort} {sort}, ID DESC
                                                    OFFSET {StartIndex} ROWS
                                                    FETCH NEXT 11 ROWS ONLY""")
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


