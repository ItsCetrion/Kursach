from TransportCompany.DBContext import DBContext
from TransportCompany.Entities.User import User
from TransportCompany.UserRepository.UserRepository import UserRepository
import hashlib

class Register:
    def __init__(self, user: User):
        self.User = user
        self.User.Password = hashlib.md5(self.User.Password.encode()).hexdigest()

    def UserRigistation(self):
        if not(self.__CheckUserInDB()):
            UserRepository.AddUserInDB(self.User)
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
            return False
        else:
            return True
