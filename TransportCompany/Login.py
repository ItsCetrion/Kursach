from TransportCompany.DBContext import DBContext

class Login:
    def __init__(self, Email, password):
        self.__Email = Email
        self.__password = password

    def CheckUserInDB(self) -> bool:
        context = DBContext()
        cursor = context.cursor
        query = (f"""SELECT Firstname From UserProgram 
                 Where Email = '{self.__Email}' and PasswordProgram = '{self.__password}'""")
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 0:
            return False
        elif len(result) == 1:
            return True