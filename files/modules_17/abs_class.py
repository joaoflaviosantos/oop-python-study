from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def __init__(self) -> None:
        self.attribute = 'Hello World!'

    def method(self, element: str) -> None:
        print(element)

    @abstractmethod
    def abstract_method1(self) -> None:
        pass

    @abstractmethod
    def abstract_method2(self) -> None:
        pass

    @abstractmethod
    def abstract_method3(self) -> None:
        pass