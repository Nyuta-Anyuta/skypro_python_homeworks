import math

def square(side):
    # Вычисляем площадь квадрата
    area = side * side
    # Округляем результат вверх, если сторона не целое число
    if not side.is_integer():
        area = math.ceil(area)
    return area

# Пример использования функции
side_length = 5  # Можете изменить на любое значение
print(f"Площадь квадрата со стороной {side_length} равна {square(side_length)}")