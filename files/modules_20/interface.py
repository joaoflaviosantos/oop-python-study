from abc import ABC, abstractmethod

class Repository(ABC):
    
    @abstractmethod
    def insert(self, data) -> None:
        pass

    @abstractmethod
    def delete(self, data) -> None:
        pass
