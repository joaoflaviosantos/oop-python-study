############## CLASSES CODES #################

class MyClass:

    def __init__(self, state) -> None:
        self.state = state

    @staticmethod
    def static_method() ->  None:
        print("I'm in static method!")


class Error:

    @staticmethod
    def protocol() -> None:
        print('Protocol presents error.')

    @staticmethod
    def entry_error() -> None:
        print('Incorrect parameters.')

    @staticmethod
    def error_500() -> None:
        print('Internal Server Error')

    @staticmethod
    def error_404() -> None:
        print('Not Found')

################# TESTS ####################

print('\n############## 1º STATIC METHOD TEST ################\n')

obj = MyClass(True)

obj.static_method()
MyClass.static_method()


print('\n############## 2º STATIC METHOD TEST ################\n')

Error.protocol()
Error.entry_error()
Error.error_500()
Error.error_404()