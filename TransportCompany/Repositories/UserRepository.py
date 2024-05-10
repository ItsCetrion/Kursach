from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.User import User


class UserRepository:

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

    def Request(self, query: str):
        __context = DBContext()
        __cursor = __context.cursor
        __cursor.execute(query)
        result = __cursor.fetchall()
        __context.connection.close()
        return result