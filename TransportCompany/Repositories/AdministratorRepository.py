from TransportCompany.DBcontext.DBContext import DBContext
from pyodbc import ProgrammingError


class AdministratorRepository:

    def GetAdmin(self, IdAdmin):
        result = self.__Request(f"""SELECT * FROM Administrator WHERE ID = {IdAdmin}""")
        return result
    def __Request(self, query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except ProgrammingError:
            raise "Ошибка"