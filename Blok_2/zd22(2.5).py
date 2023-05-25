import math
h = int(input("Введите высоту в метрах: "))
r = 6350
print("Растояние до горизонта: ", math.sqrt(((h + r) ** 2) - r ** 2))