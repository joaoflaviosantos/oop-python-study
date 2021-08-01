from typing import Type

class Connection:

    def connect(self) -> None:
        print('Connecting to database..')
    
    def desconnect(self) -> None:
        print('Desconnecting to database..')
    

class MysqlRepo(Connection):

    def __init__(self) -> None:
        super().__init__()

    def select(self) -> None:
        self.connect()
        print('Performing SELECT * FROM table...')
        self.desconnect()

    def insert(self) -> None:
        self.connect()
        print('Performing INSERT VALUES in table...')
        self.desconnect()


class DBAcess:

    def search_data(self, db_repo: Type[MysqlRepo]) -> None:
        db_repo.select()
    
    def insert_data(self, db_repo: Type[MysqlRepo]) -> None:
        db_repo.insert()