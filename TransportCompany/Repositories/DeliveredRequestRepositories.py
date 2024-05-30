from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.DeliveredRequest import DeliveredRequest
from pyodbc import ProgrammingError


class DeliveredRequestRepositories:

    def AddDeliveredRequest(self, request: DeliveredRequest):
        self.__UID(f"""INSERT INTO DeliveredRequest(ID,FirstName,LastName,Email,NumberPhone,PlaceDeparture,
                       PlaceDelivery,CargoWeight,CargoDescription, IdClient, IdDriver)
                       VALUES('{request.ID}','{request.FirstName}','{request.LastName}',
                       '{request.Email}','{request.NumberPhone}','{request.PlaceDeparture}',
                       '{request.PlaceDelivery}', '{request.CargoWeight}',
                       '{request.CargoDescription}', {request.IdClient}, {request.IdDriver})""")

    def GetCompletedOrders(self, IdDriver):
        result = self.__Demand(f"""SELECT ID, PlaceDeparture, PlaceDelivery, Revenue
                                   FROM DeliveredRequest WHERE IdDriver = {IdDriver}""")
        return result

    def GetAllCompletedOrders(self, sort: str):
        result = self.__Demand(f"""SELECT ID, PlaceDeparture, PlaceDelivery 
                                   FROM DeliveredRequest WHERE Revenue is NULL
                                   ORDER BY ID {sort}""")
        return result

    def GetOrderByIdOrder(self, IdOrder):
        result = self.__Demand(f"""SELECT ID, PlaceDeparture, PlaceDelivery
                                   FROM DeliveredRequest WHERE ID = {IdOrder}""")
        return result

    def __Demand(self, query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except ProgrammingError:
            raise "проблемы с подключением"

    def __UID(self, query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            __context.connection.commit()
            __context.connection.close()
        except ProgrammingError:
            raise "проблемы с подключением"