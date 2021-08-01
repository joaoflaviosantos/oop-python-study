############## CLASSES CODES #################

class PersonA:

    def introduce_yourself(self) -> None:
        print('Hello, I am person A.')


class PersonB(PersonA):

    def __init__(self) -> None:
        super().__init__()
    
    def introduce_yourself(self) -> None:
        print('I am changing the "introduce_yourself" method.\nThis breaks the Liskov Substitution Principle!!\nWe need to have the same functionality for the same method!!')


################## TESTS ####################

print('\n############## LISKOV PRINCIPLE BREAK TEST ################\n')

person1 = PersonA()
person1.introduce_yourself()

person2 = PersonB()
person2.introduce_yourself()
print()


print('\n############## LISKOV PRINCIPLE ANIMAL TEST ################\n')

from modules_15 import Animal, Bird, Penguin, Person
# from modules_15 import *

robert = Person()
penguin1 = Animal('penguin 1') # MotherClass Object
penguin2 = Bird('penguin 2') # DaughterClass Object
penguin3 = Penguin('penguin 3') # GrandDaugtherClass Object

print('# Acessing the MotherClass Methods:\n')

robert.watchAnimal(penguin1) # Acessing the MotherClass Methods
robert.watchAnimal(penguin2) # Acessing the MotherClass Methods
robert.watchAnimal(penguin3) # Acessing the MotherClass Methods

print('# Acessing the DaughterClass Methods:\n')

# robert.watchBird(penguin1) penguin1 can't use the DaughterClass Methods ('Animal' object has no attribute 'sing')
robert.watchBird(penguin2) # Acessing the DaughterClass and Inheritance Methods
robert.watchBird(penguin3) # Acessing the DaughterClass and Inheritance Methods

print('# Acessing the GrandDaugtherClass Methods:\n')

# robert.watchPenguin(penguin1) penguin1 can't use the DaughterClass and GrandDaugtherClass Methods ('Animal' object has no attribute 'sing')
# robert.watchPenguin(penguin2) penguin2 can't use the GrandDaugtherClass Methods ('Bird' object has no attribute 'slip')
robert.watchPenguin(penguin3) # Acessing the GrandDaugtherClass and Inheritance Methods


print('\n############## LISKOV PRINCIPLE DATABASE TEST ################\n')

from modules_15 import Connection, MysqlRepo, DBAcess
# from modules_15 import *

db_use = DBAcess()
mysql = MysqlRepo()


db_use.search_data(mysql)
print()
db_use.insert_data(mysql)