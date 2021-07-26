class PostgresDB:

    def __init__(self) -> None:
        self.__connection = 'Postgres'

    def connect(self) -> str:
        print('Connecting to Postgres database')
        return self.__connection

    def desconnect(self) -> None:
        print('Desconnecting to Postgres database')