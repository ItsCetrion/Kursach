from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.User import User


class UserRepository:
    def __init__(self):
        self.__context = DBContext()
        self.__cursor = self.__context.cursor

    def CheckPhone(self, phone: str):
        result = self.Request(f"""SELECT Firstname 
                                  FROM UserProgram Where NumberPhone = '{phone}'""")
        if len(result) == 0:
            return False
        else:
            return True

    def CheckEmail(self, email: str):
        result = self.Request(f"""SELECT Firstname 
                                  FROM UserProgram Where Email = '{email}'""")
        if len(result) == 0:
            return False
        else:
            return True

    @staticmethod
    def AddUser(user: User):
        context = DBContext()
        cursor = context.cursor
        query = (f"""INSERT INTO UserProgram 
                     VALUES('{user.FirstName}','{user.LastName}','{user.Patronymic}','{user.NumberPhone}',
                     '{user.Email}','{user.Password}','{user.Role}')""")
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

    def GetUserRole(self, password, email):
        result = self.Request(f"""SELECT RoleProgram
                                  FROM UserProgram 
                                  Where Email = '{email}' and PasswordProgram = '{password}'""")
        return result[0][0] if len(result) != 0 else ''

    def Request(self, query: str):
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__context.connection.close()
        return result