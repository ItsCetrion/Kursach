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