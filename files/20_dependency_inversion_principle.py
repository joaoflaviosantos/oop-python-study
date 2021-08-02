############## CLASSES CODES #################

from typing import Type
from modules_20 import Repository, MysqlRepository, MongoRepository

class User:

    def __init__(self, repository: Type[Repository]) -> None:
        self.__repository = repository

    def store_data(self, data: any) -> None:
        self.__repository.insert(data)

    def remove_data(self, data: any) -> None:
        self.__repository.delete(data)

################## TESTS ####################

print('\n############## DEPENDENCY INVERSION PRINCIPLE TEST ################\n')

user1 = User(MysqlRepository())
user2 = User(MongoRepository())

user1.store_data('Lhama')
user1.remove_data('Lhama')
print()
user2.store_data('John')
user2.remove_data('John')