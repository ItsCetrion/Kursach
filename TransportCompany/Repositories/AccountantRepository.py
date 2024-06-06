from DBcontext.DBContext import DBContext
from Entities.Accountant import Accountant
from pyodbc import ProgrammingError


class AccountantRepository:

    def RegistrationAccountant(self, accountant: Accountant):
        self.__UID(f"""INSERT INTO Accountant(Firstname,Lastname,Patronymic,NumberPhone,Email,Age,Experience)
                   VALUES(?, ?, ?, ?, ?, ?, ?)""", (accountant.FirstName, accountant.LastName, accountant.Patronymic,
                                                    accountant.NumberPhone, accountant.Email, accountant.Age,
                                                    accountant.Experience))

    def UpdatePhone(self, IdAccountant: int, phone: str):
        self.__UID("""Update Accountant SET NumberPhone = ? WHERE ID = ?""", (phone, IdAccountant))

    def UpdateEmail(self, IdAccountant: int, email: str):
        self.__UID("""Update Accountant SET Email = ? WHERE ID = ?""", (email, IdAccountant))

    def UpdatePassword(self, IdAccountant: int, password: str):
        self.__UID(f"""Update Accountant SET PasswordProgram = ? WHERE ID = ?""", (password, IdAccountant))

    def GetAccountant(self, IdAccountant):
        result = self.__Demand(f"""SELECT * FROM Accountant WHERE ID = ?""", IdAccountant)
        return result

    @staticmethod
    def __Demand(query: str, list_param: [tuple, int, str] = ()):
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