# заданные значения
price_candy_per_kg = 100
price_cookie_per_kg = 150
price_apple_per_kg = 50
a = 2 # кг конфет
b = 3 # кг печенья
z = 4 # кг яблок

# подсчет стоимости каждой покупки
total_candy_price = price_candy_per_kg * a
total_cookie_price = price_cookie_per_kg * b
total_apple_price = price_apple_per_kg * z

# вычисление общей суммы покупки
total_price = total_candy_price + total_cookie_price + total_apple_price

# вывод результата
print("Стоимость всей покупки:", total_price, "рублей")