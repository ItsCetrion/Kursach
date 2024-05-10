from TransportCompany.DBcontext.DBContext import DBContext


class AllRoleRepository:
    def CheckPhone(self, phone: str):

        result = self.Request(f"""SELECT Firstname 
                                  FROM CrossTable Where NumberPhone = '{phone}'""")
        if len(result) == 0:
            return False
        else:
            return True

    def CheckEmail(self, email: str):
        result = self.Request(f"""SELECT Firstname 
                                  FROM dbo.CrossTable Where Email = '{email}'""")
        if len(result) == 0:
            return False
        else:
            return True

    def GetRole(self, password, email):
        result = self.Request(f"""SELECT RoleProgram
                                  FROM CrossTable
                                  Where Email = '{email}' and PasswordProgram = '{password}'""")
        return result[0][0] if len(result) != 0 else ''

    def Request(self, query: str):
        __context = DBContext()
        __cursor = __context.cursor
        __cursor.execute(query)
        result = __cursor.fetchall()
        __context.connection.close()
        return result