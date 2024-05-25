from TransportCompany.DBcontext.DBContext import DBContext
from TransportCompany.Entities.Accountant import Accountant


class AccountantRepository:

    def RegistrationAccountant(self, accountant: Accountant):
        context = DBContext()
        cursor = context.cursor
        query = f"""INSERT INTO Accountant(Firstname,Lastname,Patronymic,NumberPhone,Email,Age,Experience)
                   VALUES('{accountant.FirstName}','{accountant.LastName}','{accountant.Patronymic}',
                   '{accountant.NumberPhone}','{accountant.Email}',{accountant.Age},{accountant.Experience})"""
        cursor.execute(query)
        context.connection.commit()
        context.connection.close()

    def GetAccountant(self, IdAccountant):
        result = self.__Demand(f"""SELECT * FROM Accountant WHERE ID = {IdAccountant}""")
        return result

    def __Demand(self, query: str):
        try:
            __context = DBContext()
            __cursor = __context.cursor
            __cursor.execute(query)
            result = __cursor.fetchall()
            __context.connection.close()
            return result
        except ProgrammingError:
            raise "проблемы с подключением"