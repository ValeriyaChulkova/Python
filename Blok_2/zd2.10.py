import math
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
print("Среднее арифметическое: ", (a + b)/2)
geo_mean = math.sqrt(a*b)
print("Среднее геометрическое:", geo_mean)