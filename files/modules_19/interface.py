from abc import ABC, abstractmethod

class FlyingBird(ABC):

    @abstractmethod
    def eat(self) -> None:
        raise 'Should Implement eat method'
    
    @abstractmethod
    def fly(self) -> None:
        raise 'Should Implement fly method'

    @abstractmethod
    def scream(self) -> None:
        raise 'Should Implement scream method'


class UnflyingBird(ABC):

    @abstractmethod
    def eat(self) -> None:
        raise 'Should Implement eat method'
    
    @abstractmethod
    def scream(self) -> None:
        raise 'Should Implement scream method'