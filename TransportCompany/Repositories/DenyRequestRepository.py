from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.DenyRequest import DenyRequest


class DenyRequestRepository:

    def AddDenyRequest(self, deny_request: DenyRequest):
        context = DBContext()
        cursor = context.cursor
        query = (f"""INSERT INTO DenyRequest(ID,FirstName,LastName,Email,NumberPhone,PlaceDeparture,PlaceDelivery,
                                             CargoWeight,CargoDescription)
                                 VALUES('{deny_request.ID}','{deny_request.FirstName}','{deny_request.LastName}',
                                 '{deny_request.Email}','{deny_request.NumberPhone}','{deny_request.PlaceDeparture}',
                                 '{deny_request.PlaceDelivery}', '{deny_request.CargoWeight}',
                                 '{deny_request.CargoDescription}')""")
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

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