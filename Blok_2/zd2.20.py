import math

e = int(input("Введите e:"))
f = int(input("Введите f:"))
g = int(input("Введите g:"))
h = int(input("Введите h:"))
a = (e + f / 2) / 3
print("a =", a)

b = abs(h ** 2 - g)
print("b =", b)

c = math.sqrt((g - h) ** 2 - 3 * math.sin(e))
print("c =", c)