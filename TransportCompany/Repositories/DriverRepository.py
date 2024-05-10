from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Driver import Driver

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