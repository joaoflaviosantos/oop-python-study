class MysqlRepository:
    
    def insert(self, data) -> None:
        print('Inserting {} in MySql database.' .format(data))

    def delete(self, data) -> None:
        print('Removing {} in MySql database.' .format(data))
