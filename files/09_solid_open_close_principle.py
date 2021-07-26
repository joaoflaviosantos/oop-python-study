############## ClASSES CODES #################

class CircusClosedClass: # Class closed for changes and closed for extensions

    def exhibit(self, type: int) -> None:
        if type == 1:
            self.__exhibit_juggler()
        if type == 2:
            self.__exhibit_clown()
            
    def __exhibit_juggler(self) -> None:
        print('The juggler is presenting his show.')

    def __exhibit_clown(self) -> None:
        print('The clown is presenting his show.')


class CircusOpenedClass: # Class closed for changes, but open for extensions

    def exhibit(self, presenter: any) -> None:
        presenter.exhibit_show()

class Juggler:

    def exhibit_show(self) -> None:
        print('The juggler is presenting his show.')

class Clown:

    def exhibit_show(self) -> None:
        print('The clown is presenting his show.')
    
class Equilibrist:

    def exhibit_show(self) -> None:
        print('The equilibrist is presenting his show.')

################# TESTS ####################

print('\n############## SOLID CLOSED CLASS TEST ################\n')

circus_closed_class = CircusClosedClass()

circus_closed_class.exhibit(1)
circus_closed_class.exhibit(2)

print('\n############## SOLID OPENED CLASS TEST ################\n')

circus_opened_class = CircusOpenedClass()
jugger = Juggler()
clown = Clown()
equilibrist = Equilibrist()

circus_opened_class.exhibit(jugger)
circus_opened_class.exhibit(clown)
circus_opened_class.exhibit(equilibrist)