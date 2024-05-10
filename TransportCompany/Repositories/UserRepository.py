from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.User import User


class UserRepository:
    def CheckPhone(self, phone: str):

        result = self.Request(f"""SELECT Firstname 
                                  FROM CrossTable Where NumberPhone = '{phone}'""")
        if len(result) == 0:
            return False
        else:
            return True

    def CheckEmail(self, email: str):
        result = self.Request(f"""SELECT Firstname 
                                  FROM dbo.CrossTable Where Email = '{email}'""")
        if len(result) == 0:
            return False
        else:
            return True

    @staticmethod
    def AddUser(user: User):
        context = DBContext()
        cursor = context.cursor
        query = (f"""INSERT INTO Client(FirstName,LastName,Patronymic,NumberPhone,Email,PasswordProgram)
                     VALUES('{user.FirstName}','{user.LastName}','{user.Patronymic}','{user.NumberPhone}',
                     '{user.Email}','{user.Password}')""")
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

    def GetRole(self, password, email):
        result = self.Request(f"""SELECT RoleProgram
                                  FROM CrossTable
                                  Where Email = '{email}' and PasswordProgram = '{password}'""")
        return result[0][0] if len(result) != 0 else ''

    def Request(self, query: str):
        __context = DBContext()
        __cursor = __context.cursor
        __cursor.execute(query)
        result = __cursor.fetchall()
        __context.connection.close()
        return result