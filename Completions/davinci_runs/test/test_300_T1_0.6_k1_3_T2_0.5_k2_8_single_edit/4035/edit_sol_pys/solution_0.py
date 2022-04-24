

a, b = map(int, input().split())

consumption_1 = a / 0.08
consumption_2 = b / 0.1
if consumption_1 > consumption_2:
    print(int(consumption_2))
elif consumption_1 < consumption_2:
    print(int(consumption_1))
else:
    print(int(consumption_1))
