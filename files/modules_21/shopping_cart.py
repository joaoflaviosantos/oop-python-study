from .products import Product
from typing import Type

class ShoppingCart:

    def __init__(self) -> None:
        self.__products = []
        self.__total_purchase = 0

    def add_product(self, product: Type[Product]) -> None:
        self.__products.append(product)
        self.__total_purchase =+ product.product_value()

    def checkout(self) -> None:

        print('Completed purchases!\n')
        
        for product in self.__products:
            product.product_info()
         
        print('\nThe purchase total is {}.\n' .format(self.__total_purchase))

        print(self.__products)
                      
        self.__products = []