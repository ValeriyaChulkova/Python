import math

a = int(input("Введите меньшее осноавние трапеции:"))
b = int(input("Введите большее основании трапеции:"))
h = int(input("Введитте высоту трапеции:"))
#боковя сторона трапеции
c = math.sqrt(((b - a)/2) ** 2 + h ** 2)
print("Периметр трапеции:", a+b+2*c)
