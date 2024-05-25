from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Client import Client
from pyodbc import ProgrammingError


class ClientRepository:


    def AddUser(self, user: Client):
        query = (f"""INSERT INTO Client(FirstName,LastName,Patronymic,NumberPhone,Email,PasswordProgram)
                     VALUES('{user.FirstName}','{user.LastName}','{user.Patronymic}','{user.NumberPhone}',
                     '{user.Email}','{user.Password}')""")
        self.__AUDI(query)

    def GetClient(self, IdClient):
        result = self.__request(f"""SELECT * FROM Client Where ID = {IdClient}""")
        return result

    def UpdatePhone(self, IdClient, Phone):
        query = (f"""UPDATE Client SET NumberPhone = '{Phone}' 
                                   WHERE ID = {IdClient}""")
        self.__AUDI(query)

    def UpdateEmail(self, IdClient, Email):
        query = (f"""UPDATE Client SET Email = '{Email}' 
                                           WHERE ID = {IdClient}""")
        self.__AUDI(query)

    def UpdatePassword(self, IdClient, Password):
        query = (f"""UPDATE Client SET PasswordProgram = '{Password}' 
                                                   WHERE ID = {IdClient}""")
        self.__AUDI(query)

    @staticmethod
    def __request(query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except ProgrammingError:
            raise "Ошибка"

    @staticmethod
    def __AUDI(query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            __context.connection.commit()
            __context.connection.close()
        except ProgrammingError:
            raise "Ошибка"