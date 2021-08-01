class MysqlDB:

    def __init__(self) -> None:
        self.__connection = 'Mysql'

    def connect(self) -> str:
        print('Connecting to Mysql database')
        return self.__connection

    def desconnect(self) -> None:
        print('Desconnecting to Mysql database')