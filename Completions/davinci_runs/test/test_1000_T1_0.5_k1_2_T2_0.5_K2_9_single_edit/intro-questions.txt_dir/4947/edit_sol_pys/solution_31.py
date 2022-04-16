
from math import ceil

x = float(input('Введите число в милях: '))
print(ceil(1000 * (5280 / 4854) * x))
