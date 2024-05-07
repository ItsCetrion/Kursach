from TransportCompany.DBContext import DBContext
from TransportCompany.Entities.User import User
class UserRepository:
    @staticmethod
    def CheckPhoneInDB(phone: str):
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
    def CheckEmailInDB(Email: str):
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

    @staticmethod
    def AddUserInDB(user: User):
        context = DBContext()
        cursor = context.cursor
        query = (f"""INSERT INTO UserProgram 
                             VALUES('{user.FirstName}','{user.LastName}','{user.Patronymic}','{user.NumberPhone}',
                             '{user.Email}','{user.Password}','{user.Role}')""")
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()