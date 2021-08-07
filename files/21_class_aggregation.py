############## CLASSES CODES #################

from modules_21 import Product, ShoppingCart

# This exemple not use a inteface class.

################## TESTS ####################

print('\n############## 1º DIRECT CLASS AGGREGATION TEST ################\n')

cart = ShoppingCart()

product1 = Product('Monitor', 120)
product3 = Product('CPU', 400)
product2 = Product('Beer', 2)

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)


cart.checkout()