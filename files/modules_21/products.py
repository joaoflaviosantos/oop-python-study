class Product:

    def __init__(self, prod_name: str, prod_value: int) -> None:
        self.__prod_name = prod_name
        self.__prod_value = prod_value

    def product_info(self) -> None:
        print('Product: {} | Value: $ {}.00' . format(self.__prod_name, self.__prod_value))

    def product_value(self) -> int:
        return self.__prod_value