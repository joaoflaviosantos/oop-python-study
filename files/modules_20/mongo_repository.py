from .interface import Repository

class MongoRepository(Repository):
    
    def insert(self, data) -> None:
        print('Inserting {} in Mongo database.' .format(data))

    def delete(self, data) -> None:
        print('Removing {} in Mongo database.' .format(data))
