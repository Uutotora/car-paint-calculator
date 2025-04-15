from car_parts import CAR_PARTS
from paint_color import PAINT_COLORS


class PaintCalculator:
    def __init__(self):
        self.base_price = 12000  # базовая стоимость

    def calculate_price(self, part_name, color_name):
        part_name = part_name.lower()
        color_name = color_name.lower()

        # Проверяем, есть ли такая деталь в словаре
        if part_name not in CAR_PARTS:
            return f"Ошибка: Деталь '{part_name}' не найдена"

        # Проверяем, есть ли такой цвет в словаре
        if color_name not in PAINT_COLORS:
            return f"Ошибка: Цвет '{color_name}' не найден"

        # Получаем коэффициенты
        part_coefficient = CAR_PARTS[part_name].get_coefficient()
        color_coefficient = PAINT_COLORS[color_name].get_coefficient()

        # Рассчитываем стоимость
        total_price = self.base_price * part_coefficient * color_coefficient

        return total_price