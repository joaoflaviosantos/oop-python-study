############## ClASSES CODES #################

class Person:

    def __init__(self, name, age, document):
        self.name = name
        self.age = age
        self.__document = document # private atribute
    
    def run(self): # public method
        print("\nI'm running")
    
    def drink(self, liquid):
        if liquid == 'beer':
            document_number = self.__show_document()
            print("\nMy document is {}. I'm drinking a beer!".format(document_number))
        else:
            print("\nI'm drinking {}!" .format(liquid))
            
    def __show_document(self): # private method
        return self.__document


class Calculator:

    def calculate(self, op, num1, num2):
        if op == "+":
            return self.__addition(num1, num2)
        elif op == "-":
            return self.__subtraction(num1, num2)
        else:
            print("Invalid operation.")
    
    def __addition(self, num1, num2): # private method
        return num1 + num2

    def __subtraction(self, num1, num2): # private method
        return num1 - num2


################# TESTS ####################

print("\n############## PERSON PRIVATE ATRIBUTE TEST ################\n")

ronald = Person('Ronald', 32, '000.000.000-00')

print("Hi! My name is {}. I'm {} years old.".format(ronald.name, ronald.age))

ronald.drink('beer')
ronald.drink('water')


print("\n############## CALCULATOR PRIVATE METHOD TEST ################\n")

operation = Calculator()

print(operation.calculate('+', 2, 3))
print(operation.calculate('-', 2, 3))