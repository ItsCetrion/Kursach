Use [TransportCompany]

IF EXISTS (SELECT * FROM sys.procedures WHERE name = 'Delete_all_connection')
	exec('DROP PROCEDURE Delete_all_connection')
	GO
	CREATE PROCEDURE Delete_all_connection
	AS
		DECLARE @name_connection NVARCHAR(100), @name_table NVARCHAR(100), @parent_object_id INT
		DECLARE my_cursor CURSOR FOR
			SELECT name, parent_object_id
			FROM sys.foreign_keys
		OPEN my_cursor
		FETCH NEXT FROM my_cursor INTO @name_connection, @parent_object_id
		WHILE @@FETCH_STATUS = 0
		BEGIN
			SET @name_table = (SELECT name FROM sys.tables WHERE object_id = @parent_object_id)
			EXEC('ALTER TABLE '+ @name_table + ' DROP CONSTRAINT ' + @name_connection)
			FETCH NEXT FROM my_cursor INTO @name_connection, @parent_object_id
		END

		CLOSE my_cursor
			DEALLOCATE my_cursor
			GO

IF EXISTS (SELECT * FROM sys.procedures WHERE name = 'Delele_all_table')
	exec('DROP PROCEDURE Delele_all_table')
	GO
	CREATE PROCEDURE Delele_all_table
		as
		DECLARE @NameTable nvarchar(100)
		DECLARE my_cursor CURSOR FOR 
			SELECT Name
			FROM sys.tables

		OPEN my_cursor
		FETCH NEXT FROM my_cursor INTO @NameTable
		WHILE @@FETCH_STATUS = 0
		BEGIN
			exec (N'DROP TABLE ' + @NameTable)
			FETCH NEXT FROM my_cursor INTO  @NameTable
		END

		CLOSE my_cursor
		DEALLOCATE my_cursor
		GO
		
EXEC Delete_all_connection
EXEC Delele_all_table

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'UserProgram')
	CREATE TABLE Client(ID INT IDENTITY(1	,1) NOT NULL PRIMARY KEY,
							 Firstname NVARCHAR(30) NOT NULL,
							 Lastname NVARCHAR(30) NOT NULL,
							 Patronymic NVARCHAR(30) NULL,
							 NumberPhone NVARCHAR(12) UNIQUE NOT NULL,
							 Email NVARCHAR(320) UNIQUE NOT NULL,
							 PasswordProgram NVARCHAR(35) NOT NULL,
							 RoleProgram NVARCHAR(20) NOT NULL DEFAULT('Клиент'))

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Request')
	CREATE TABLE Request(ID INT IDENTITY(1	,1) NOT NULL PRIMARY KEY,
						 FirstName NVARCHAR(30) NOT NULL,
						 LastName NVARCHAR(30) NOT NULL,
						 Email NVARCHAR(320) NOT NULL,
						 NumberPhone NVARCHAR(12) NOT NULL,
						 PlaceDeparture VARCHAR(100) NOT NULL,
						 PlaceDelivery VARCHAR(100) NOT NULL,
							 CargoWeight INT NOT NULL,
						 CargoDescription VARCHAR(100) NOT NULL,
						 Position VARCHAR(30) NOT NULL DEFAULT('На рассмотрении'),
						 IdClient INT CONSTRAINT FK_IdClient FOREIGN KEY(IdClient) REFERENCES Client(ID) ON DELETE CASCADE,
						 DateRequest DATE NOT NULL DEFAULT(GETDATE()))

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Administrator')
	Create Table Administrator(ID INT IDENTITY(1	,1) NOT NULL PRIMARY KEY,
							 Firstname NVARCHAR(30) NOT NULL,
							 Lastname NVARCHAR(30) NOT NULL,
							 Patronymic NVARCHAR(30) NULL,
							 NumberPhone NVARCHAR(12) UNIQUE NOT NULL,
							 Email NVARCHAR(320) UNIQUE NOT NULL,
							 PasswordProgram NVARCHAR(35) NOT NULL,
							 RoleProgram NVARCHAR(20) NOT NULL DEFAULT('Администратор'))

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'AcceptRequest')
	CREATE TABLE AcceptRequest(ID INT NOT NULL PRIMARY KEY,
						 FirstName NVARCHAR(30) NOT NULL,
						 LastName NVARCHAR(30) NOT NULL,
						 Email NVARCHAR(320) NOT NULL,
						 NumberPhone NVARCHAR(12) NOT NULL,
						 PlaceDeparture VARCHAR(100) NOT NULL,
						 PlaceDelivery VARCHAR(100) NOT NULL,
						 CargoWeight INT NOT NULL,
						 CargoDescription VARCHAR(100) NOT NULL,
						 Position VARCHAR(30) NOT NULL DEFAULT('В пути'),
						 IdClient INT CONSTRAINT FK__IdClient FOREIGN KEY(IdClient) REFERENCES Client(ID) ON DELETE CASCADE,
						 DateAccept DATE NOT NULL DEFAULT(GETDATE()))

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Driver')
	Create Table Driver(ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
							 Firstname NVARCHAR(30) NOT NULL,
							 Lastname NVARCHAR(30) NOT NULL,
							 Patronymic NVARCHAR(30) NULL,
							 NumberPhone NVARCHAR(12) UNIQUE NOT NULL,
							 Email NVARCHAR(320) UNIQUE NOT NULL,
							 PasswordProgram NVARCHAR(35) NULL,
							 Age INT NOT NULL,
							 Experience INT NUll,
							 IdOrderClient INT CONSTRAINT FK_IdOrderClient FOREIGN KEY(IdOrderClient) REFERENCES AcceptRequest(ID) ON DELETE CASCADE,
							 Condition NVARCHAR(20)NOT NULL DEFAULT('Свободен'),
							 RoleProgram NVARCHAR(20) NOT NULL DEFAULT('Водитель'))

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DeliveredRequest')
	CREATE TABLE DeliveredRequest(ID INT NOT NULL PRIMARY KEY,
						 FirstName NVARCHAR(30) NOT NULL,
						 LastName NVARCHAR(30) NOT NULL,
						 Email NVARCHAR(320) NOT NULL,
						 NumberPhone NVARCHAR(12) NOT NULL,
						 PlaceDeparture VARCHAR(100) NOT NULL,
						 PlaceDelivery VARCHAR(100) NOT NULL,
						 CargoWeight INT NOT NULL,
						 CargoDescription VARCHAR(100) NOT NULL,
						 Position VARCHAR(30) NOT NULL DEFAULT('Доставлено'),
						 IdClient INT CONSTRAINT FK____IdClient FOREIGN KEY(IdClient) REFERENCES Client(ID) ON DELETE CASCADE,
						 IdDriver INT CONSTRAINT FK_IdDriver FOREIGN KEY(IdDriver) REFERENCES Driver(ID) ON DELETE NO ACTION,
						 Revenue Money NULL,
						 DateDelivered DATE NOT NULL DEFAULT(GETDATE()))

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Accountant')
	Create Table Accountant(ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
							 Firstname NVARCHAR(30) NOT NULL,
							 Lastname NVARCHAR(30) NOT NULL,
							 Patronymic NVARCHAR(30) NULL,
							 NumberPhone NVARCHAR(12) UNIQUE NOT NULL,
							 Email NVARCHAR(320) UNIQUE NOT NULL,
							 PasswordProgram NVARCHAR(35) NULL,
							 Age INT NOT NULL,
							 Experience INT NUll,
							 RoleProgram NVARCHAR(20) NOT NULL DEFAULT('Бухгалтер'))

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DenyRequest')
	CREATE TABLE DenyRequest(ID INT NOT NULL PRIMARY KEY,
						 FirstName NVARCHAR(30) NOT NULL,
						 LastName NVARCHAR(30) NOT NULL,
						 Email NVARCHAR(320) NOT NULL,
						 NumberPhone NVARCHAR(12) NOT NULL,
						 PlaceDeparture VARCHAR(100) NOT NULL,
						 PlaceDelivery VARCHAR(100) NOT NULL,
						 CargoWeight INT NOT NULL,
						 CargoDescription VARCHAR(100) NOT NULL,
						 Position VARCHAR(30) NOT NULL DEFAULT('Отказано'),
						 IdClient INT CONSTRAINT FK___IdClient FOREIGN KEY(IdClient) REFERENCES Client(ID) ON DELETE CASCADE,
						 DateDeny DATE NOT NULL DEFAULT(GETDATE()))

IF EXISTS (SELECT * FROM sys.views WHERE name = 'CrossTable')
	EXEC('DROP VIEW CrossTable')
	GO
	CREATE VIEW CrossTable
	AS SELECT ID, Firstname, Lastname, Patronymic, Email, NumberPhone, PasswordProgram, RoleProgram FROM Driver
		UNION
		SELECT ID, Firstname, Lastname, Patronymic, Email, NumberPhone, PasswordProgram, RoleProgram FROM Client
		UNION
		SELECT ID, Firstname, Lastname, Patronymic, Email, NumberPhone, PasswordProgram, RoleProgram FROM Accountant
		UNION
		SELECT ID, Firstname, Lastname, Patronymic, Email, NumberPhone, PasswordProgram, RoleProgram FROM Administrator
	GO

INSERT INTO Administrator(Firstname,Lastname,Patronymic,NumberPhone,Email, PasswordProgram)
VALUES('Евгений','Озеров','Алексеевич', '89951632863', 'zhenyaoz777piratship@list.ru', '6fb42da0e32e07b61c9f0251fe627a9c')

SELECT ID, FirstName, LastName, Email, NumberPhone, 
                                         PlaceDeparture, PlaceDelivery, CargoWeight, CargoDescription, DateAccept
                                            FROM AcceptRequest Where Position = 'В пути' and IdClient = 1
                                            Order By DateAccept Desc, ID DESC
                                                            OFFSET 0 ROWS
                                                            FETCH NEXT 11 ROWS ONLY

