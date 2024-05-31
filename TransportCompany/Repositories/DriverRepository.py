from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Driver import Driver
from pyodbc import ProgrammingError


class DriverRepository:
    def RegistrationDriver(self, driver: Driver):

        self.__UID(f"""INSERT INTO Driver(Firstname,Lastname,Patronymic,NumberPhone,Email,Age,Experience)
                           VALUES('{driver.FirstName}','{driver.LastName}','{driver.Patronymic}',
                           '{driver.NumberPhone}','{driver.Email}',{driver.Age},{driver.Experience})""")

    def GetDriver(self, IdDriver):
        result = self.__Demand(f"""SELECT * FROM Driver WHERE ID = {IdDriver}""")
        return result

    def GetActiveOrder(self, IdDriver):
        result = self.__Demand(f"""SELECT AcceptRequest.ID, CargoDescription, AcceptRequest.FirstName, 
                                   AcceptRequest.LastName, PlaceDeparture, PlaceDelivery, CargoWeight 
                                   FROM AcceptRequest JOIN Driver ON AcceptRequest.ID = Driver.IdOrderClient
                                   WHERE Driver.ID = {IdDriver}""")
        return result[0]

    def Get5Driver(self):
        result = self.__Demand(f"""SELECT Lastname, Firstname, Patronymic, Experience, ID From Driver Where Condition = 'Свободен'
                                 Order By ID
                                    OFFSET 0 ROWS
                                    FETCH NEXT 5 ROWS ONLY""")
        return result

    def Get5DriverWithException(self, id: int):
        result = self.__Demand(f"""SELECT Lastname, Firstname, Patronymic, 
                                 Experience, ID From Driver Where Condition = 'Свободен' and ID != {id}
                                 Order By ID
                                    OFFSET 0 ROWS
                                    FETCH NEXT 5 ROWS ONLY""")
        return result

    def GetIdDriverByIdOrder(self, IdOrder):
        result = self.__Demand(f"""SELECT ID FROM Driver WHERE IdOrderClient = {IdOrder}""")
        return result

    def UpdateDriver(self, IdRequest, IdDriver):
        self.__UID(f"""UPDATE Driver
                     SET IdOrderClient={IdRequest}, Condition='Занят'
                     WHERE ID = {IdDriver}""")

    def DeleteIdOrder(self, IdRequest):
        self.__UID(f"""Update Driver SET IdOrderClient = NULL,Condition='Свободен' WHERE IdOrderClient = {IdRequest}""")

    def UpdatePhone(self, IdDriver, phone):
        self.__UID(f"""Update Driver SET NumberPhone = '{phone}' WHERE ID = {IdDriver}""")

    def UpdateEmail(self, IdDriver, email):
        self.__UID(f"""Update Driver SET Email = '{email}' WHERE ID = {IdDriver}""")

    def UpdatePassword(self, IdDriver, password):
        self.__UID(f"""Update Driver SET PasswordProgram = '{password}' WHERE ID = {IdDriver}""")

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