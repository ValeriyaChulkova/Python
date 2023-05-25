import math

x = int(input("x = "))
y = int(input("y = "))
z = (x+(2+y)/x**2)/(y+(1/(math.sqrt(x**2+10))))
print("z = ", z)

q = 7.25 * math.sin(x) - abs(y)
print("q = ", q)