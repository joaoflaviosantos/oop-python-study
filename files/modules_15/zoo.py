from typing import Type

class Animal: # MotherClass

    def __init__(self, animal: str) -> None:
        self.__animal = animal
            
    def eat(self) -> None:
        print('The {} is Eating.' .format(self.__animal))

    def walk(self) -> None:
        print('The {} is Walking.' .format(self.__animal))
        
    def sleep(self) -> None:
        print('The {} is Sleeping.' .format(self.__animal))
    

class Bird(Animal): # DaughterClass

    def __init__(self, animal: str) -> None:
        super().__init__(animal)
        self.__animal = animal

    def sing(self) -> None:
        print('The {} is Singing..' .format(self.__animal))
    

class Penguin(Bird): # GrandDaugtherClass

    def __init__(self, animal: str) -> None:
        super().__init__(animal)
        self.__animal = animal
    
    def slip(self) -> None:
        print('The {} is Slipping on the ice.'  .format(self.__animal))


class Person: # Instance Object to acess Classes Atributes and Methods

    def watchAnimal(self, animal: Type[Animal]) -> None:
        animal.eat()
        animal.walk()
        animal.sleep()
        print()
    
    def watchBird(self, bird: Type[Bird]) -> None:
        bird.eat()
        bird.walk()
        bird.sleep()
        bird.sing()
        print()
    
    def watchPenguin(self, penguin: Type[Penguin]) -> None:
        penguin.eat()
        penguin.walk()
        penguin.sleep()
        penguin.sing()
        penguin.slip()
        print()