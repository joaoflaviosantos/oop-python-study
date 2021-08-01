class Person:

    def __init__(self, name: str) -> None:
        self.__location = None
        self.__name = name

    def enter_the_location(self) -> None:
        self.__location.turn_on_lights()
    
    def present_location(self) -> None:
        address = self.__location.get_address()
        print(address)

    def introduce_yourself(self) -> None:
        print('Hello, my name is {}' .format(self.__name))
    
    def set_location(self, location: any) -> None:
        self.__location = location
    
    def get_location(self) -> any:
        return self.__location