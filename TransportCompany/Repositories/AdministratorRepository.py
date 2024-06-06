from DBcontext.DBContext import DBContext
from pyodbc import ProgrammingError


class AdministratorRepository:

    def GetAdmin(self, IdAdmin):
        result = self.__Request(f"""SELECT * FROM Administrator WHERE ID = ?""", IdAdmin)
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