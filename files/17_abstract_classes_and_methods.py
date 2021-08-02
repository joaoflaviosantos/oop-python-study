############## CLASSES CODES #################

from modules_17 import AbstractClass

class DaughterClass(AbstractClass):

    def present_method(self) -> None:
        print(self.attribute)

    def abstract_method1(self) -> None:
        print('Implementing abstract method 1..')
        print('This is part of an interface..')
        print()
        return super().abstract_method1()

    def abstract_method2(self) -> None:
        print('Implementing abstract method 2..')
        print('This is part of an interface..')
        print()
        return super().abstract_method2()

    def abstract_method3(self) -> None:
        print('Implementing abstract method 2..')
        print('This is part of an interface..')
        print()
        return super().abstract_method3()


################## TESTS ####################

print('\n############## ABSTRACT CLASS AND METHODS TEST ################\n')

daughter = DaughterClass() # objetc instancing | Without abstract_method -> (Can't instantiate abstract class DaughterClass with abstract methods abstract_method)

daughter.present_method()
daughter.method('I am here!')
print()
daughter.abstract_method1()
daughter.abstract_method2()
daughter.abstract_method3()


# abstractClass = AbstractClass() Error after @abstractmethod decorator inserted in AbstractClass
# abstractClass.method('Doing something...') Error after @abstractmethod decorator inserted in AbstractClass