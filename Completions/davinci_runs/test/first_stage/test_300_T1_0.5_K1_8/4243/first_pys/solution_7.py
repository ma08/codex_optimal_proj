

import math

x = int(input())

five_hundred_yen_coins = math.floor(x / 500)
x = x - five_hundred_yen_coins * 500
five_yen_coins = math.floor(x / 5)

print(five_hundred_yen_coins * 1000 + five_yen_coins * 5)