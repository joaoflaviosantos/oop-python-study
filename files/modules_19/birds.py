from .interface import FlyingBird, UnflyingBird

class Falcon(FlyingBird):
            
    def eat(self) -> None:
        print('The falcon is Eating.')

    def fly(self) -> None:
        print('The falcon is Flying.')
        
    def scream(self) -> None:
        print('The falcon is Screaming.')


class Penguin(UnflyingBird):
            
    def eat(self) -> None:
        self.__hunt()
        print('The penguin is Eating the hunted fish.')
        
    def scream(self) -> None:
        print('The penguin is Screaming.')

    def __hunt(self) -> None:
        print('Now the penguin will Hunt some fish..')