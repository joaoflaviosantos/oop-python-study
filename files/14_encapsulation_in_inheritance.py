############## CLASSES CODES #################

class DatabaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string' # _atribute is shared in inheritance context
        self.user = 'Lhama'

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connection(self) -> None: # _method is shared in inheritance context
        print('Connection is "OK".')


class Repository(DatabaseConn):

    def __init__(self) -> None:
        super().__init__()
        print(self.user)
        print(self._conn)
        # print(self.__database) Error
    
    def select(self) -> None:
        self._testing_connection()
        print('Connecting to {}.' .format(self._conn))
        print('SELECT * FROM table')
        print(self.user)
        # print(self.__database) Error


################## TESTS ####################

print('\n############## INHERITANCE TESTE ################\n')

db = DatabaseConn()
print(db.user)
# print(db.__database) Error
print(db._conn)
db.get_database()
db._testing_connection()
print()

repo = Repository()
repo.select()


