from calculator import PaintCalculator
from car_parts import CAR_PARTS
from paint_color import PAINT_COLORS


def main():
    calculator = PaintCalculator()

    print("Калькулятор стоимости окраски автомобиля")
    print("=========================================")


    print("\nДоступные детали:")
    for part_name in CAR_PARTS:
        print(f"- {part_name}")

    print("\nДоступные цвета:")
    for color_name in PAINT_COLORS:
        print(f"- {color_name}")

    part = input("\nВведите название детали: ")
    color = input("Введите название цвета: ")

    price = calculator.calculate_price(part, color)

    if isinstance(price, str):
        print(price)
    else:
        print(f"\nСтоимость окраски {part} в {color} цвет: {price:.2f} рублей")


if __name__ == "__main__":
    main()