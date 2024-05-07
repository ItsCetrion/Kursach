from TransportCompany.DBContext import DBContext
from TransportCompany.User import User


class Register:
    def __init__(self, user: User):
        self.User = user

    def UserRigistation(self):
        if self.__CheckUserInDB():
            context = DBContext()
            cursor = context.cursor
            query = (f"""INSERT INTO UserProgram 
                     VALUES('{self.User.FirstName}','{self.User.LastName}','{self.User.Patronymic}','{self.User.NumberPhone}',
                     '{self.User.Email}','{self.User.Password}','{self.User.Role}')""")
            cursor.execute(query)
            context.connection.commit()
            context.connection.close()
        else:
            raise "Пользователь с таким номером телефона или Email уже есть"

    def __CheckUserInDB(self) -> bool:
        context = DBContext()
        cursor = context.cursor
        query = (f"""SELECT Firstname 
                     FROM UserProgram Where NumberPhone = '{self.User.NumberPhone}' or Email = '{self.User.Email}'""")
        cursor.execute(query)
        result = cursor.fetchall()
        context.connection.close()
        if len(result) == 0:
            return True
        else:
            return False
