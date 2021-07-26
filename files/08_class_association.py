############## CLASSES CODES #################
from typing import Type

class Switch:

    def __init__(self, room: str) -> None:
        self.__room = room

    def turn_on(self) -> None:
        print('Turning on the {} light.' .format(self.__room))

    def turn_off(self) -> None:
        print('Turning off the {} light.' .format(self.__room))


class Person:

    def turn_on_light(self, switch: Type[Switch]) -> None:
        switch.turn_on()

    def turn_off_light(self, switch: Type [Switch]) -> None:
        switch.turn_off()
    
    def sleep(self) -> None:
        print('Sleeping... ZZZzz..')


################# TESTS ####################

print('\n############## ASSOCIATION CLASS TEST ################\n')

lhama = Person()
bedroom_switch = Switch('bedroom')
kitchen_switch = Switch('kitchen') 

bedroom_switch.turn_on() # direct method call
bedroom_switch.turn_off() # direct method call
print('\n')

lhama.turn_on_light(bedroom_switch) # associative method call
lhama.turn_on_light(kitchen_switch)  # associative method call
lhama.turn_off_light(bedroom_switch)  # associative method call
lhama.sleep()

