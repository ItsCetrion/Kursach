from TransportCompany.DBcontext.DBContext import DBContext
from pyodbc import ProgrammingError


class AllRoleRepository:
    def CheckPhone(self, phone: str):
        result = self.__Request(f"""SELECT Firstname 
                                  FROM CrossTable Where NumberPhone = '{phone}'""")
        if len(result) == 0:
            return False
        else:
            return True

    def CheckEmail(self, email: str):
        result = self.__Request(f"""SELECT Firstname 
                                  FROM dbo.CrossTable Where Email = '{email}'""")
        if len(result) == 0:
            return False
        else:
            return True

    def GetEntity(self, password, email) -> list:
        if password == "Null":
            result = self.__Request(f"""SELECT * FROM CrossTable
                                        Where Email = '{email}' and PasswordProgram is NUll""")
        else:
            result = self.__Request(f"""SELECT * FROM CrossTable
                                        Where Email = '{email}' and PasswordProgram = '{password}'""")
        return result

    @staticmethod
    def __Request(query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except ProgrammingError:
            raise "Ошибка"