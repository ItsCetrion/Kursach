import pyodbc


class DBContext:
    def __init__(self):
        try:
            self.__query = 'Driver={ODBC Driver 17 for SQL Server};'\
                    'Server=MSI;'\
                    'Database=TransportCompany;'\
                    'Trusted_Connection=yes;'
            self.connection = pyodbc.connect(self.__query)
            self.cursor = self.connection.cursor()
        except:
            raise "Не удалось подключиться к базе данных"


if __name__ == "__main__":
    context = DBContext()
    cursor = context.cursor
    query = (f"""INSERT INTO UserProgram(Firstname, Lastname, Patronymic, NumberPhone, Email, PasswordProgram, RoleProgram)
                 VALUES('Иван','Иванов','Иванович','+09876543211','test@mail.ru','123456','Пользователь')""")
    cursor.execute(query)
    context.connection.commit()
    context.connection.close()