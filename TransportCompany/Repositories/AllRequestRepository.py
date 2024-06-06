from DBcontext.DBContext import DBContext
from pyodbc import ProgrammingError


class AllRequestRepository:

    def Get11RequestByDate(self, StartIndex: int, reverse: bool, table: str, date: str, IdClient: int):
        sort = "ASC" if reverse is False else "DESC"
        NameDate = self.__NameDate(table)
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate}
                                   FROM {table} Where IdClient = ? and {NameDate} = ?
                                   Group by ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate}
                                   Order By {NameDate} {sort}, ID DESC
                                         OFFSET {StartIndex} ROWS
                                         FETCH NEXT 11 ROWS ONLY""", (IdClient, date))
        return result

    def Get11RequestByYear(self, StartIndex: int, reverse: bool, table: str, year: int, IdClient: int):
        sort = "ASC" if reverse is False else "DESC"
        NameDate = self.__NameDate(table)
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate} FROM {table} 
                                   Where IdClient = ? and DATEPART(YEAR, {NameDate}) = ?
                                   Group by ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate}
                                   Order By {NameDate} {sort}, ID DESC
                                         OFFSET {StartIndex} ROWS
                                         FETCH NEXT 11 ROWS ONLY""", (IdClient, year))
        return result

    def Get11RequestByMonth(self, StartIndex: int, reverse: bool, table: str, month: int, IdClient: int):
        sort = "ASC" if reverse is False else "DESC"
        NameDate = self.__NameDate(table)
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate} FROM {table} 
                                   Where IdClient = ? and DATEPART(MONTH, {NameDate}) = ?
                                   Group by ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate}
                                   Order By {NameDate} {sort}, ID DESC
                                         OFFSET {StartIndex} ROWS
                                         FETCH NEXT 11 ROWS ONLY""", (IdClient, month))
        return result

    def Get11RequestByDay(self, StartIndex: int, reverse: bool, table: str, day: int, IdClient: int):
        sort = "ASC" if reverse is False else "DESC"
        NameDate = self.__NameDate(table)
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate} FROM {table} 
                                   Where IdClient = ? and DATEPART(DAY, {NameDate}) = ?
                                   Group by ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate}
                                   Order By {NameDate} {sort}, ID DESC
                                         OFFSET {StartIndex} ROWS
                                         FETCH NEXT 11 ROWS ONLY""", (IdClient, day))
        return result

    def Get11Request(self, StartIndex: int, reverse: bool, table: str, IdClient: int):
        sort = "ASC" if reverse is False else "DESC"
        NameDate = self.__NameDate(table)
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate}
                                   FROM {table} Where IdClient = ?
                                   Group by ID, FirstName, LastName, Email, NumberPhone, PlaceDeparture, PlaceDelivery, 
                                   CargoWeight, CargoDescription, IdClient, {NameDate}
                                   Order By {NameDate} {sort}, ID DESC
                                        OFFSET {StartIndex} ROWS
                                        FETCH NEXT 11 ROWS ONLY""", IdClient)
        return result

    def GetQuantityByDate(self, date: str, table: str, IdClient: int):
        NameDate = self.__NameDate(table)
        result = self.__Demand(f"""SELECT DISTINCT COUNT(*) OVER () FROM {table} 
                                   Where IdClient = ? and {NameDate} = ?
                                   Group by ID""", (IdClient, date))
        return result[0][0] if len(result) != 0 else 0

    def GetQuantityByYear(self, year: int, table: str, IdClient: int):
        NameDate = self.__NameDate(table)
        result = self.__Demand(f"""SELECT DISTINCT COUNT(*) OVER () FROM {table} 
                                   Where IdClient = ? and DATEPART(YEAR, {NameDate}) = ?
                                   Group by ID""", (IdClient, year))
        return result[0][0] if len(result) != 0 else 0

    def GetQuantityByMonth(self, month: int, table: str, IdClient: int):
        NameDate = self.__NameDate(table)
        result = self.__Demand(f"""SELECT DISTINCT COUNT(*) OVER () FROM {table} 
                                   Where IdClient = ? and DATEPART(MONTH, {NameDate}) = ?
                                   Group by ID""", (IdClient, month))
        return result[0][0] if len(result) != 0 else 0

    def GetQuantityByDay(self, day: int, table: str, IdClient: int):
        NameDate = self.__NameDate(table)
        result = self.__Demand(f"""SELECT DISTINCT COUNT(*) OVER () FROM {table} 
                                   Where IdClient = ? and DATEPART(DAY, {NameDate}) = ?
                                   Group by ID""", (IdClient, day))
        return result[0][0] if len(result) != 0 else 0

    def GetQuantityRequest(self, table: str, IdClient: int):
        result = self.__Demand(f"""SELECT DISTINCT COUNT(*) OVER () FROM {table} Where IdClient = ?
                                   Group by ID""", IdClient)
        return result[0][0] if len(result) != 0 else 0

    @staticmethod
    def __NameDate(table):
        if table == "Request": return "DateRequest"
        if table == "DenyRequest": return "DateDeny"
        if table == "AcceptRequest": return "DateAccept"
        if table == "DeliveredRequest": return "DateDelivered"
        else: raise "таблицы не существует"

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
 