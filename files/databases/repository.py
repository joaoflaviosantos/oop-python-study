class Repository:

    def select(self, db_connection: any) -> None:
        connection = db_connection.connect()
        print('I connected to the database {}' .format(connection))
        print('Performing SELECT * FROM...')
        db_connection.desconnect()

    def insert(self, db_connection: any) -> None:
        connection = db_connection.connect()
        print('I connected to the database {}' .format(connection))
        print('Performing INSERT VALUES...')
        db_connection.desconnect()