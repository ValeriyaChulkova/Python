import math

# Вводим координаты первой точки
x1 = float(input("Введите координату x первой точки: "))
y1 = float(input("Введите координату y первой точки: "))

# Вводим координаты второй точки
x2 = float(input("Введите координату x второй точки: "))
y2 = float(input("Введите координату y второй точки: "))

# Вычисляем расстояние между точками
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Выводим результат
print("Расстояние между точками: ", distance)




