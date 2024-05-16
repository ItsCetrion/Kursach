from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Request import Request

class AcceptRequestRepository:
    def AddAcceptRequest(self, request: Request):
        context = DBContext()
        cursor = context.cursor
        query = (f"""INSERT INTO AcceptRequest(ID,FirstName,LastName,Email,NumberPhone,PlaceDeparture,PlaceDelivery,
                                             CargoWeight,CargoDescription)
                                 VALUES('{request.ID}','{request.FirstName}','{request.LastName}',
                                 '{request.Email}','{request.NumberPhone}','{request.PlaceDeparture}',
                                 '{request.PlaceDelivery}', '{request.CargoWeight}',
                                 '{request.CargoDescription}')""")
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()