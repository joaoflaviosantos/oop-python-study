class House:

    def __init__(self) -> None:
        self.__address = 'Main Street'
        self.__owner = None
    
    def turn_on_lights(self) -> None:
        print("I'm lighting the lights")
    
    def get_address(self) -> str:
        return self.__address
    
    def set_owner(self, owner: any) -> None:
        self.__owner = owner

    def get_owner(self) -> any:
        return self.__owner