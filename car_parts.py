class CarPart:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

    def get_name(self):
        return self.name

    def get_coefficient(self):
        return self.coefficient


CAR_PARTS = {
    "капот": CarPart("Капот", 1.0),
    "передняя дверь": CarPart("Передняя дверь", 1.2),
    "задняя дверь": CarPart("Задняя дверь", 1.1),
    "передний бампер": CarPart("Передний бампер", 1.0),
    "задний бампер": CarPart("Задний бампер", 1.0),
    "крыша": CarPart("Крыша", 1.1)
}