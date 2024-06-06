from pyodbc import ProgrammingError
from DBcontext.DBContext import DBContext
from Entities.Request import Request


class RequestRepository:
    def AddRequest(self, request: Request):

        self.__UID("""INSERT INTO Request(FirstName,LastName,Email,NumberPhone,PlaceDeparture,PlaceDelivery,CargoWeight,
                     CargoDescription, IdClient)
                     VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""", (request.FirstName, request.LastName, request.Email,
                                                            request.NumberPhone, request.PlaceDeparture,
                                                            request.PlaceDelivery, request.CargoWeight,
                                                            request.CargoDescription, request.IdClient))

    def DeleteRequest(self, id: int):
        self.__UID("DELETE FROM Request WHERE ID = ?", id)

    def Get11RequestByDate(self, date: str, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                 FROM Request WHERE DateRequest = ?
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""", date)
        return result

    def Get11RequestByYearAndMonth(self, year: int, month: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest 
                                 FROM Request 
                                 WHERE DATEPART(MONTH, DateRequest) = ? and DATEPART(YEAR, DateRequest) = ?
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""", (month, year))
        return result

    def Get11RequestByYearAndDay(self, year: int, day: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                 FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = ? and DATEPART(YEAR, DateRequest) = ?
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""", (day, year))
        return result

    def Get11RequestByMonthAndDay(self, month: int, day: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                 FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = ? and DATEPART(MONTH, DateRequest) = ?
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""", (day, month))
        return result

    def Get11RequestByYear(self, year: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                   PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                   FROM Request WHERE DATEPART(YEAR, DateRequest) = ?
                                   Order By {ParameterSort} {sort}, ID DESC
                                     OFFSET {StartIndex} ROWS
                                     FETCH NEXT 11 ROWS ONLY""", year)
        return result

    def Get11RequestByMonth(self, month: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                 FROM Request WHERE DATEPART(MONTH, DateRequest) = ?
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""", month)
        return result

    def Get11RequestByDay(self, day: int, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                 FROM Request WHERE DATEPART(DAY, DateRequest) = ?
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""", day)
        return result

    def Get11RequestByFirstName(self, PartFirstName: str, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                 From Request WHERE FirstName LIKE ?
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""", PartFirstName + '%')
        return result

    def Get11RequestByLastName(self, PartLastName: str, StartIndex: int, ParameterSort: str, reverse=False):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                 From Request WHERE LastName LIKE ?
                                 Order By {ParameterSort} {sort}, ID DESC
                                    OFFSET {StartIndex} ROWS
                                    FETCH NEXT 11 ROWS ONLY""", PartLastName + '%')
        return result

    def Get11RequestClients(self, StartIndex: int, ParameterSort: str, reverse):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                  PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                  FROM Request 
                                  Order By {ParameterSort} {sort}, ID DESC
                                     OFFSET {StartIndex} ROWS
                                     FETCH NEXT 11 ROWS ONLY""")

        return result

    def Get11RequestClient(self, StartIndex: int, reverse, IdClient):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                   PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateRequest
                                   FROM Request Where IdClient = ?
                                   Order By DateRequest {sort}, ID DESC
                                     OFFSET {StartIndex} ROWS
                                     FETCH NEXT 11 ROWS ONLY""", IdClient)
        return result

    def GetAllQuantityRequest(self):
        result = self.__Demand("SELECT COUNT(*) FROM Request")
        return result[0][0]

    def GetQuantityRequestByDate(self, date: str):
        result = self.__Demand("""SELECT COUNT(*) FROM Request 
                                 WHERE DateRequest = ?""", date)
        return result[0][0]

    def GetQuantityRequestByYearAndMonth(self, year: int, month: int):
        result = self.__Demand("""SELECT COUNT(*) FROM Request 
                                  WHERE DATEPART(MONTH, DateRequest) = ? and DATEPART(YEAR, DateRequest) = ?""", (month, year))
        return result[0][0]

    def GetQuantityRequestByYearAndDay(self, year: int, day: int):
        result = self.__Demand("""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = ? and DATEPART(YEAR, DateRequest) = ?""", (day, year))
        return result[0][0]

    def GetQuantityRequestByMonthAndDay(self, month: int, day: int):
        result = self.__Demand("""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = ? and DATEPART(MONTH, DateRequest) = ?""", (day, month))
        return result[0][0]

    def GetQuantityRequestByYear(self, year: int):
        result = self.__Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(YEAR, DateRequest) = ?""", year)
        return result[0][0]

    def GetQuantityRequestByMonth(self, month: int):
        result = self.__Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(MONTH, DateRequest) = ?""", month)
        return result[0][0]

    def GetQuantityRequestByDay(self, day: int):
        result = self.__Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE DATEPART(DAY, DateRequest) = ?""", day)
        return result[0][0]

    def GetQuantityRequestByFirstName(self, PartFirstName: str):
        result = self.__Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE FirstName LIKE ?""", PartFirstName + '%')
        return result[0][0]

    def GetQuantityRequestByLastName(self, PartLastName: str):
        result = self.__Demand(f"""SELECT COUNT(*) FROM Request 
                                 WHERE LastName LIKE ?""", PartLastName + '%')
        return result[0][0]

    def GetQuantityRequestClient(self, IdClient: int):
        result = self.__Demand(f"""SELECT COUNT(*) FROM Request WHERE IdClient = ?""", IdClient)
        return result[0][0]

    @staticmethod
    def __Demand(query: str, list_param: [tuple, int, str] = ()):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query, list_param)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except ProgrammingError as error:
            raise error

    @staticmethod
    def __UID(query: str, list_param: [tuple, int, str] = ()):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query, list_param)
            __context.connection.commit()
            __context.connection.close()
        except ProgrammingError as error:
            raise error


