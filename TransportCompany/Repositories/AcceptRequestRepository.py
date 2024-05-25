from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Request import Request
from pyodbc import ProgrammingError

class AcceptRequestRepository:
    def AddAcceptRequest(self, request: Request):
        context = DBContext()
        cursor = context.cursor
        query = (f"""INSERT INTO AcceptRequest(ID,FirstName,LastName,Email,NumberPhone,PlaceDeparture,PlaceDelivery,
                                             CargoWeight,CargoDescription, IdClient)
                                 VALUES('{request.ID}','{request.FirstName}','{request.LastName}',
                                 '{request.Email}','{request.NumberPhone}','{request.PlaceDeparture}',
                                 '{request.PlaceDelivery}', '{request.CargoWeight}',
                                 '{request.CargoDescription}', {request.IdClient})""")
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

    def Get11AcceptRequest(self, StartIndex: int, reverse: bool, IdClient: int):
        sort = "ASC" if reverse is False else "DESC"
        result = self.__Demand(f"""SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                         PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, IdClient, DateAccept
                                            FROM AcceptRequest Where and IdClient = {IdClient}
                                            Order By DateAccept {sort}, ID DESC
                                                            OFFSET {StartIndex} ROWS
                                                            FETCH NEXT 11 ROWS ONLY""")
        return result

    def GetQuantityRequest(self, IdClient:int):
        result = self.__Demand(f"""SELECT COUNT(*) FROM AcceptRequest 
                                 Where IdClient = {IdClient}""")
        return result[0][0]

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