############## CLASSES CODES #################

from modules_18 import QuadrateLand
from modules_18 import RectangularLand
from modules_18 import Engineer


################## TESTS ####################

print('\n############## INTERFACES EXEMPLE TEST ################\n')

engineer = Engineer('Lhama')
quadrate_measure = QuadrateLand(4)
rectangular_measure = RectangularLand(4, 5)

engineer.measure_perimeter(quadrate_measure)
engineer.measure_area(quadrate_measure)
print()
engineer.measure_perimeter(rectangular_measure)
engineer.measure_area(rectangular_measure)
