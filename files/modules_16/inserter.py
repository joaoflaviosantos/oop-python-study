from typing import Dict, Type
from modules_16 import Repository

class Inserter:

    def __init__(self, repository: Type[Repository]) -> None: # Must receive an object/instance of RepositoryClass
        self.__repo = repository

    def data_record(self, name: str, age: int) -> Dict:
        data = self.__repo.select(name)
        if data:
            raise Exception('This data alread exist.')

        novo_registro = self.__repo.insert(name, age)
        return novo_registro
        
