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