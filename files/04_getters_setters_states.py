############## CLASSES CODES #################

class Alarm:

    def __init__(self, state: bool) -> None:
        self.__state = state # private atribute

    def get_state(self) -> bool:
        return self.__state

    def set_state(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__state = value
        else:
            print("Incorrect value! '{}' isn't boolean value." .format(value))


################# TESTS ####################

print("\n############## GETTER AND SETTERS TEST ################\n")

al = Alarm(False)

print(al.get_state())
al.set_state(True)
print(al.get_state())
al.set_state(1)
print(al.get_state())