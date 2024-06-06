from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.DenyRequest import DenyRequest
from pyodbc import ProgrammingError


class DenyRequestRepository:

    def AddDenyRequest(self, deny_request: DenyRequest):
        self.__UID(f"""INSERT INTO DenyRequest(ID,FirstName,LastName,Email,NumberPhone,PlaceDeparture,PlaceDelivery,
                                             CargoWeight,CargoDescription, IdClient)
                                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (deny_request.ID, deny_request.FirstName,
                                                                           deny_request.LastName, deny_request.Email,
                                                                           deny_request.NumberPhone, deny_request.PlaceDeparture,
                                                                           deny_request.PlaceDelivery,  deny_request.CargoWeight,
                                                                           deny_request.CargoDescription, deny_request.IdClient))

    def Get11DenyRequest(self, StartIndex: int, reverse, IdClient: int):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                 PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateDeny
                                    FROM DenyRequest Where IdClient = ?
                                    Order By DateDeny {sort}, ID DESC
                                                    OFFSET {StartIndex} ROWS
                                                    FETCH NEXT 11 ROWS ONLY""", IdClient)
        return result

    def GetQuantityDenyRequest(self, IdClient: int):
        result = self.__Demand(f"""SELECT COUNT(*) FROM DenyRequest Where IdClient = ?""", IdClient)
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