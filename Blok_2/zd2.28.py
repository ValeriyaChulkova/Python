import math

a = float(input("Введите длину меньшего основания: "))
b = float(input("Введите длину большего основания: "))
alpha = float(input("Введите угол при большем основании (в градусах): "))

# переводим угол из градусов в радианы
alpha = math.radians(alpha)

h = math.sqrt(a**2 - (b**2/4) + a*b*math.cos(alpha))
S = (a + b) * h / 2

print("Площадь трапеции: {:.2f}".format(S))