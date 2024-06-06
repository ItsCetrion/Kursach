from TransportCompany.DBcontext.DBContext import DBContext
from pyodbc import ProgrammingError


class AllRoleRepository:
    def CheckPhone(self, phone: str):
        result = self.__Request(f"""SELECT Firstname 
                                    FROM CrossTable Where NumberPhone = ?""", phone)
        if len(result) == 0:
            return False
        else:
            return True

    def CheckEmail(self, email: str):
        result = self.__Request(f"""SELECT Firstname 
                                    FROM dbo.CrossTable Where Email = ?""", email)
        if len(result) == 0:
            return False
        else:
            return True

    def GetEntity(self, password, email) -> list:
        if password == "Null":
            result = self.__Request(f"""SELECT * FROM CrossTable
                                        Where Email = ? and PasswordProgram is NUll""", email)
        else:
            result = self.__Request(f"""SELECT * FROM CrossTable
                                        Where Email = ? and PasswordProgram = ?""", (email, password))
        return result

    @staticmethod
    def __Request(query: str, list_param: [tuple, int, str] = ()):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query, list_param)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except ProgrammingError as error:
            raise error