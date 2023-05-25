from math import sqrt

# координаты вершин треугольника
x1, y1 = 0, 0
x2, y2 = 0, 5
x3, y3 = 3, 0

# находим длины сторон
AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
BC = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
AC = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

# находим периметр
perimeter = AB + BC + AC
print(f"Периметр треугольника: {perimeter}")

# находим площадь
p = (AB + BC + AC) / 2
area = sqrt(p * (p - AB) * (p - BC) * (p - AC))
print(f"Площадь треугольника: {area}")