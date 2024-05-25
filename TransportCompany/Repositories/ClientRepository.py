from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Client import Client
from pyodbc import ProgrammingError


class ClientRepository:

    @staticmethod
    def AddUser(user: Client):
        context = DBContext()
        cursor = context.cursor
        query = (f"""INSERT INTO Client(FirstName,LastName,Patronymic,NumberPhone,Email,PasswordProgram)
                     VALUES('{user.FirstName}','{user.LastName}','{user.Patronymic}','{user.NumberPhone}',
                     '{user.Email}','{user.Password}')""")
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

    def GetClient(self, IdClient):
        result = self.__Request(f"""SELECT * FROM Client Where ID = {IdClient}""")
        return result

    def __Request(self, query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except ProgrammingError:
            raise "Ошибка"