############## CLASSES CODES #################

from modules_10 import House, Person


################## TESTS ####################

print('\n############## BILATERAL ASSOCIATION TEST ################\n')

house1 = House()
ana = Person('Ana')

ana.set_location(house1)
house1.set_owner(ana)

owner = house1.get_owner()
owner.introduce_yourself()

ana.present_location()
