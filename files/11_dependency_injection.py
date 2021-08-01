############## CLASSES CODES #################

from typing import Type
class House:

    def __init__(self) -> None:
        self.__address = 'Main Street'
    
    def turn_on_lights(self) -> None:
        print("I'm lighting the lights")
    
    def get_address(self) -> str:
        return self.__address

class Person:

    def __init__(self, name: str, location: Type[House]) -> None:
        self.__location = location
        self.__name = name

    def enter_the_location(self) -> None:
        self.__location.turn_on_lights()
    
    def present_location(self) -> None:
        address = self.__location.get_address()
        print(address)


################## TESTS ####################

print('\n############## DEPENDENCY INJECTION TEST ################\n')

house1 = House()
ana = Person('Ana', house1)

ana.enter_the_location()
ana.present_location()
