from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.User import User
class UserRepository:
    @staticmethod
    def CheckPhone(phone: str):
        context = DBContext()
        cursor = context.cursor
        query = (f"""SELECT Firstname 
                     FROM UserProgram Where NumberPhone = '{phone}'""")
        cursor.execute(query)
        result = cursor.fetchall()
        context.connection.close()
        if len(result) == 0:
            return False
        else:
            return True

    @staticmethod
    def CheckEmail(Email: str):
        context = DBContext()
        cursor = context.cursor
        query = (f"""SELECT Firstname 
                     FROM UserProgram Where Email = '{Email}'""")
        cursor.execute(query)
        result = cursor.fetchall()
        context.connection.close()
        if len(result) == 0:
            return False
        else:
            return True

    def CheckPasswordAndEmail(self, password: str, Email: str):
        context = DBContext()
        cursor = context.cursor
        query = (f"""SELECT Firstname 
                     FROM UserProgram 
                     Where Email = '{Email}' and PasswordProgram = '{password}'""")
        cursor.execute(query)
        result = cursor.fetchall()
        context.connection.close()
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