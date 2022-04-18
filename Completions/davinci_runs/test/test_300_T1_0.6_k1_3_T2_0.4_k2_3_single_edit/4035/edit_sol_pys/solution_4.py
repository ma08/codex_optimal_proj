

a, b = map(int, input().split())

consumption = a / 0.08
if consumption > b / 0.1:
    print(int(b / 0.1))
else:
    print(int(consumption))
