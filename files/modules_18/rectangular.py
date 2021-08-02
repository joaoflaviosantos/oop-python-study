from .shapes import InterfaceShapes

class RectangularLand(InterfaceShapes):

    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
    
    def get_perimeter(self) -> int:
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter

    def get_area(self) -> int:
        area = self.length * self.width
        return area
