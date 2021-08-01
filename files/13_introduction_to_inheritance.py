############## CLASSES CODES #################

class MotherClass:

    def __init__(self, address: str) -> None:
        self.address = address
        self.last_name = 'Silva'

    def eat(self) -> None:
        print('I am eating!')

    def study(self) -> None:
        print('I am studying')


class DaughterClass(MotherClass):
    
    def __init__(self, address: str) -> None:
        super().__init__(address)

    def play(self, toy: str) -> None:
        print('I am playing with {}.' .format(toy))


class GrandDaugtherClass(DaughterClass):

    def __init__(self, address: str) -> None:
        super().__init__(address)


################## TESTS ####################

print('\n############## INHERITANCE TESTE ################\n')

ana = MotherClass('Elvira Street')
clara = DaughterClass('Cake Street')
julia = GrandDaugtherClass('Main Street')

print('Ana lives in {}.' .format(ana.address))
print('Clara lives in {}.' .format(clara.address))
print('Julia lives in {}.' .format(julia.address))

clara.eat()
clara.play('ball')
julia.play('doll')