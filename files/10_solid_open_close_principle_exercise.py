############## CLASSES CODES #################

from modules_10 import PostgresDB, MysqlDB, Repository

################# TESTS ####################

print('\n############## SOLID OPENED CLASS TEST ################\n')

db_conn1 = PostgresDB()
db_conn2 = MysqlDB()
repo = Repository()

repo.insert(db_conn1)
print('\n')
repo.select(db_conn1)
print('\n')

repo.insert(db_conn2)
print('\n')
repo.select(db_conn2)
print('\n')
