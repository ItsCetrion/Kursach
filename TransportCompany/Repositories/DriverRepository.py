from DBcontext.DBContext import DBContext
from Entities.Driver import Driver
from pyodbc import ProgrammingError


class DriverRepository:
    def RegistrationDriver(self, driver: Driver):

        self.__UID(f"""INSERT INTO Driver(Firstname,Lastname,Patronymic,NumberPhone,Email,Age,Experience)
                           VALUES(?, ?, ?, ?, ?, ?, ?)""", (driver.FirstName, driver.LastName, driver.Patronymic,
                                                            driver.NumberPhone, driver.Email, driver.Age,
                                                            driver.Experience))

    def UpdateDriver(self, IdRequest, IdDriver):
        self.__UID(f"""UPDATE Driver
                     SET IdOrderClient=?, Condition='Занят'
                     WHERE ID = ?""", (IdRequest, IdDriver))

    def DeleteIdOrder(self, IdRequest):
        self.__UID(f"""Update Driver SET IdOrderClient = NULL,Condition='Свободен' WHERE IdOrderClient = ?""", IdRequest)

    def UpdatePhone(self, IdDriver, phone):
        self.__UID(f"""Update Driver SET NumberPhone = ? WHERE ID = ?""", (phone, IdDriver))

    def UpdateEmail(self, IdDriver, email):
        self.__UID(f"""Update Driver SET Email = ? WHERE ID = ?""", (email, IdDriver))

    def UpdatePassword(self, IdDriver, password):
        self.__UID(f"""Update Driver SET PasswordProgram = ? WHERE ID = ?""", (password, IdDriver))

    def GetDriver(self, IdDriver):
        result = self.__Demand(f"""SELECT * FROM Driver WHERE ID = ?""", IdDriver)
        return result

    def GetActiveOrder(self, IdDriver):
        result = self.__Demand(f"""SELECT AcceptRequest.ID, CargoDescription, AcceptRequest.FirstName, 
                                   AcceptRequest.LastName, PlaceDeparture, PlaceDelivery, CargoWeight 
                                   FROM AcceptRequest JOIN Driver ON AcceptRequest.ID = Driver.IdOrderClient
                                   WHERE Driver.ID = ?""", IdDriver)
        return result[0]

    def Get5Driver(self):
        result = self.__Demand(f"""SELECT Lastname, Firstname, Patronymic, Experience, ID From Driver Where Condition = 'Свободен'
                                 Order By ID
                                    OFFSET 0 ROWS
                                    FETCH NEXT 5 ROWS ONLY""")
        return result

    def Get5DriverWithException(self, id: int):
        result = self.__Demand(f"""SELECT Lastname, Firstname, Patronymic, 
                                 Experience, ID From Driver Where Condition = 'Свободен' and ID != ?
                                 Order By ID
                                    OFFSET 0 ROWS
                                    FETCH NEXT 5 ROWS ONLY""", id)
        return result

    def GetIdDriverByIdOrder(self, IdOrder):
        result = self.__Demand(f"""SELECT ID FROM Driver WHERE IdOrderClient = ?""", IdOrder)
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
    def __UID(query: str, list_param: [tuple, int, str] = ()):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query, list_param)
            __context.connection.commit()
            __context.connection.close()
        except ProgrammingError as error:
            raise error