############## CLASSES CODES #################

class RegistrationSystem:   

    def registration(self, name: str, age: int) -> None:
        if self.__data_check(name, age):
            self.__data_save(name, age)
        else:
            self.__return_error()
            
    def __data_check(self, name: str, age: int) -> bool: # single responsability (info check)
        if isinstance(name, str) and isinstance(age, int):
            return True
        else:
            return False

    def __data_save(self, name: str, age: int) -> None: # single responsability (info save)
        print('Accessing the database...')
        print('Registering the User {}, age {}.' .format(name, age))

    def __return_error(self) -> None: # single responsability (return error)
        print('Invalid data!')


################# TESTS ####################

print('\n############## SINGLE RESPONSIBILITY TEST ################\n')

object_test = RegistrationSystem()

ruan = object_test.registration('Ruan', 27)

ruan_error = object_test.registration('Ruan', '27')