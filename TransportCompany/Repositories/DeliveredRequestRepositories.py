from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.DeliveredRequest import DeliveredRequest
from pyodbc import ProgrammingError


class DeliveredRequestRepositories:

    def AddDeliveredRequest(self, request: DeliveredRequest):
        self.__UID(f"""INSERT INTO DeliveredRequest(ID,FirstName,LastName,Email,NumberPhone,PlaceDeparture,
                       PlaceDelivery,CargoWeight,CargoDescription, IdClient, IdDriver)
                       VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (request.ID, request.FirstName, request.LastName,
                                                                    request.Email, request.NumberPhone,
                                                                    request.PlaceDeparture, request.PlaceDelivery,
                                                                    request.CargoWeight, request.CargoDescription,
                                                                    request.IdClient, request.IdDriver))

    def UpdateRevenue(self, IdDriver: int, IdOrder: int, revenue: float):
        self.__UID(f"""UPDATE DeliveredRequest SET Revenue = ?
                       WHERE IdDriver = ? and ID = ?""", (revenue, IdDriver, IdOrder))

    def GetCompletedOrders(self, IdDriver: int):
        result = self.__Demand(f"""SELECT ID, PlaceDeparture, PlaceDelivery, Revenue
                                   FROM DeliveredRequest WHERE IdDriver = ? and Revenue is not NULL""", IdDriver)
        return result

    def GetAllCompletedOrders(self, sort: str):
        result = self.__Demand(f"""SELECT ID, PlaceDeparture, PlaceDelivery 
                                   FROM DeliveredRequest WHERE Revenue is NULL
                                   GROUP BY ID, PlaceDeparture, PlaceDelivery
                                   ORDER BY ID {sort}""")
        return result

    def GetOrderByIdOrder(self, IdOrder):
        result = self.__Demand(f"""SELECT ID, PlaceDeparture, PlaceDelivery
                                   FROM DeliveredRequest WHERE ID = ? and Revenue is NULL
                                   GROUP BY ID, PlaceDeparture, PlaceDelivery""", IdOrder)
        return result

    def GetInfoOrderAndDriver(self, IdOrder):
        result = self.__Demand(f"""SELECT Driver.ID, Driver.FirstName,  Driver.LastName, Patronymic,  Driver.Email,
                                   Experience, PlaceDeparture, PlaceDelivery, CargoWeight
                                   FROM DeliveredRequest JOIN Driver ON DeliveredRequest.IdDriver = Driver.ID
                                   WHERE DeliveredRequest.ID = ?""", IdOrder)
        return result

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
    def __UID(query: str, list_param: [tuple, int, str, float] = ()):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query, list_param)
            __context.connection.commit()
            __context.connection.close()
        except ProgrammingError as error:
            raise error