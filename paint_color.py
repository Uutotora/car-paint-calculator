class PaintColor:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

    def get_name(self):
        return self.name

    def get_coefficient(self):
        return self.coefficient


PAINT_COLORS = {
    "белый": PaintColor("Белый", 1.0),
    "синий": PaintColor("Синий", 1.0),
    "желтый": PaintColor("Желтый", 1.1),
    "красный": PaintColor("Красный", 1.0),
    "перламутровый": PaintColor("Перламутровый", 1.2),
    "серый металлик": PaintColor("Серый металлик", 1.3)
}