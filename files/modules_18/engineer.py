from typing import Type
from .shapes import InterfaceShapes

class Engineer:

    def __init__(self, name: str) -> None:
        self.name = name

    def measure_perimeter(self, land: Type[InterfaceShapes]) -> None:
        perimeter = land.get_perimeter()
        print('{} meters is the perimeter measurement. Engineer {} measured.' . format(perimeter, self.name))

    def measure_area(self, land: Type[InterfaceShapes]) -> None:
        area = land.get_area()
        print('{} square meters is the area measurement. Engineer {} measured.' . format(area, self.name))