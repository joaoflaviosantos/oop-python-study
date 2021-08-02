from .shapes import InterfaceShapes

class QuadrateLand(InterfaceShapes):

    def __init__(self, side: int) -> None:
        self.side = side
    
    def get_perimeter(self) -> int:
        perimeter = self.side * 4
        return perimeter

    def get_area(self) -> int:
        area = self.side * self.side
        return area
