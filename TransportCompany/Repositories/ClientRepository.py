from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Client import Client
from pyodbc import ProgrammingError


class ClientRepository:

    def AddUser(self, client: Client):
        self.__UID(f"""INSERT INTO Client(FirstName,LastName,Patronymic,NumberPhone,Email,PasswordProgram)
                     VALUES(?, ?, ?, ?, ?, ?)""", (client.FirstName, client.LastName, client.Patronymic,
                                                   client.NumberPhone, client.Email, client.Password))

    def UpdatePhone(self, IdClient, Phone):
        self.__UID(f"""UPDATE Client SET NumberPhone = ? WHERE ID = ?""", (Phone, IdClient))

    def UpdateEmail(self, IdClient, Email):
        self.__UID(f"""UPDATE Client SET Email = ? WHERE ID = ?""", (Email, IdClient))

    def UpdatePassword(self, IdClient, Password):
        self.__UID(f"""UPDATE Client SET PasswordProgram = ? WHERE ID = ?""", (Password, IdClient))

    def GetClient(self, IdClient):
        result = self.__request(f"""SELECT * FROM Client Where ID = ?""", IdClient)
        return result

    @staticmethod
    def __request(query: str, list_param: [tuple, int, str] = ()):
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