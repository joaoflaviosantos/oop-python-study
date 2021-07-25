############## ClASSES CODES #################

class MyClass:

    static = 'Lhama' # class variable / static variable / global variable

    def __init__(self, state: bool) -> None:
        self.state = state
        #self.static = 'Lhama' # class variable / static variable / global variable
    
    def print_static(self) -> None:
        print(self.static)

    def change_obj_static(self) -> None:
        self.static = "Programador Lhama Object"

    @classmethod
    def change_class_static(cls) -> None:
        cls.static = "Programador Lhama Class Method"

#------------------------------------------#

class Store:

    tax = 1.03

    def __init__(self, address: str) -> None:
        self.__address = address

    def print_address(self) -> None:
        print(self.__address)
    
    @classmethod
    def sell(cls, qtd: int) -> int:
        return qtd * cls.tax

    @classmethod
    def change_tax(cls, new_tax: int) -> None:
        cls.tax = new_tax


################# TESTS ####################

print('\n############## 1º CLASS VARIABLE TEST ################\n')

obj1 = MyClass(True)
obj2 = MyClass(False)

print(obj1.static)
print(obj2.static)
print(MyClass.static)
print('\n')

obj1.static = 'Programador'

print(obj1.static)
print(obj2.static)
print(MyClass.static)
print('\n')

MyClass.static = 'Programador'

print(obj1.static)
print(obj2.static)
print(MyClass.static)
print('\n')

obj1.static = 'Lhama'

print(obj1.static)
print(obj2.static)
print(MyClass.static)
print('\n')

obj1.change_obj_static()
print(obj1.static)
print(obj2.static)
print(MyClass.static)
print('\n')

obj2.change_class_static()
print(obj1.static)
print(obj2.static)
print(MyClass.static)
print('\n')

obj1.print_static()
obj2.print_static()
print('\n')

obj3 = MyClass(True)
obj4 = MyClass(False)

print(obj3.static)
print(obj4.static)

print('\n############## 2º EXEMPLE CLASS VARIABLE TEST ################\n')

beach_store = Store('Beach Store')
city_store = Store('City Store')

print('Variable Class "tax" is {}' .format(Store.tax))
print('\n')

beach_store.print_address()
print(beach_store.sell(20))
print('\n')

city_store.print_address()
print(city_store.sell(20))
print('\n')

beach_store.change_tax(1.5)

print('Variable Class "tax" changed to {}' .format(Store.tax))
print('\n')
beach_store.print_address()
print(beach_store.sell(20))
print('\n')

city_store.print_address()
print(city_store.sell(20))
print('\n')