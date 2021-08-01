############## CLASSES CODES #################

class PersonA:

    def introduce_yourself(self) -> None:
        print('Hello, I am person A.')

class PersonB(PersonA):

    def __init__(self) -> None:
        super().__init__()
    
    def introduce_yourself(self) -> None:
        print('I am changing the "introduce_yourself" method.\nThis breaks the Liskov Substitution Principle!!\nWe need to have the same functionality for the same method!!')


################# LISKOV PRINCIPLE BREAK TESTS ####################

person1 = PersonA()
person1.introduce_yourself()

person2 = PersonB()
person2.introduce_yourself()