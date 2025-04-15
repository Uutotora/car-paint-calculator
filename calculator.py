from car_parts import CAR_PARTS
from paint_color import PAINT_COLORS


class PaintCalculator:
    def __init__(self):
        self.base_price = 12000

    def calculate_price(self, part_name, color_name, discount=0):
        part_name = part_name.lower()
        color_name = color_name.lower()


        if part_name not in CAR_PARTS:
            return f"Ошибка: Деталь '{part_name}' не найдена"


        if color_name not in PAINT_COLORS:
            return f"Ошибка: Цвет '{color_name}' не найден"


        part_coefficient = CAR_PARTS[part_name].get_coefficient()
        color_coefficient = PAINT_COLORS[color_name].get_coefficient()


        total_price = self.base_price * part_coefficient * color_coefficient


        if discount > 0:
            total_price = total_price * (1 - discount / 100)

        return total_price