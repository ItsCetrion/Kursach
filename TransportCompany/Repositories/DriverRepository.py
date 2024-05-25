from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Driver import Driver
from pyodbc import ProgrammingError

class DriverRepository:
    def RegistrationDriver(self, driver: Driver):
        context = DBContext()
        cursor = context.cursor
        query = f"""INSERT INTO Driver(Firstname,Lastname,Patronymic,NumberPhone,Email,Age,Experience)
                           VALUES('{driver.FirstName}','{driver.LastName}','{driver.Patronymic}',
                           '{driver.NumberPhone}','{driver.Email}',{driver.Age},{driver.Experience})"""
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

    def GetDriver(self, IdDriver):
        result = self.__Demand(f"""SELECT * FROM Driver WHERE ID = {IdDriver}""")
        return result

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

    def UpdateDriver(self, IdRequest, IdDriver):
        context = DBContext()
        cursor = context.cursor
        query = f"""UPDATE Driver
                     SET IdOrderClient={IdRequest}, Condition='Занят'
                     WHERE ID = {IdDriver}"""
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

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