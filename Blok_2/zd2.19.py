import math

a = int(input("a = "))
b = int(input("b = "))
x = ((2/(a ** 2) + 25) + b)/(math.sqrt(b) + ((a + b)/2))
print(x)

y = (abs(a) + 2 * math.sin(b))/5.5 * a
print(y)