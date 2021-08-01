############## CLASSES CODES #################

class PersonA:

    def introduce_yourself(self) -> None:
        print('Hello, I am person A.')
        print()

class PersonB(PersonA):

    def __init__(self) -> None:
        super().__init__()
    
    def introduce_yourself(self) -> None:
        print('I am changing the "introduce_yourself" method. Unlike the Liskov Principle, in Polymorphism, the "states" of objects propagate to the lower levels of class inheritance.')
        print()

class PersonC(PersonB):

    def __init__(self) -> None:
        super().__init__()


################## TESTS ####################

print('\n############## POLYMORPHISM PERSON TEST ################\n')

person1 = PersonA()
person1.introduce_yourself()

person3 = PersonC()
person3.introduce_yourself()

person2 = PersonB()
person2.introduce_yourself()

person3 = PersonC()
person3.introduce_yourself()


print('\n############## POLYMORPHISM DATABASE TEST ################\n')

from modules_16 import Repository, Inserter

class FakerRepository(Repository):

    def __init__(self) -> None:
        super().__init__()
    
    def select(self, name: str) -> None:
        return None


repo1 = Repository()
repo2 = FakerRepository()
inserter1 = Inserter(repo1)
inserter2 = Inserter(repo2)

# data1 = inserter1.data_record('Lhama', 26) Error, raises Exception
# print(data1)

data2 = inserter2.data_record('Lhama', 26)
print(data2)