############## CLASSES CODES #################

from modules_19 import Falcon, Penguin

################## TESTS ####################

print('\n############## INTERFACES SEGREGATION PRINCIPLE TEST ################\n')

falcon = Falcon()
penguin = Penguin()

falcon.fly()
print()
penguin.eat()