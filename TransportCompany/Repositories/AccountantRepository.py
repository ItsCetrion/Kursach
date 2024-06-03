from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Accountant import Accountant
from pyodbc import ProgrammingError


class AccountantRepository:

    def RegistrationAccountant(self, accountant: Accountant):
        self.__UID(f"""INSERT INTO Accountant(Firstname,Lastname,Patronymic,NumberPhone,Email,Age,Experience)
                   VALUES('{accountant.FirstName}','{accountant.LastName}','{accountant.Patronymic}',
                   '{accountant.NumberPhone}','{accountant.Email}',{accountant.Age},{accountant.Experience})""")

    def UpdatePhone(self, IdAccountant: int, phone: str):
        self.__UID(f"""Update Accountant SET NumberPhone = '{phone}' WHERE ID = {IdAccountant}""")

    def UpdateEmail(self, IdAccountant: int, email: str):
        self.__UID(f"""Update Accountant SET Email = '{email}' WHERE ID = {IdAccountant}""")

    def UpdatePassword(self, IdAccountant: int, password: str):
        self.__UID(f"""Update Accountant SET PasswordProgram = '{password}' WHERE ID = {IdAccountant}""")

    def GetAccountant(self, IdAccountant):
        result = self.__Demand(f"""SELECT * FROM Accountant WHERE ID = {IdAccountant}""")
        return result

    @staticmethod
    def __Demand(query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except ProgrammingError:
            raise "проблемы с подключением"

    @staticmethod
    def __UID(query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            __context.connection.commit()
            __context.connection.close()
        except ProgrammingError:
            raise "проблемы с подключением"