

a, b = map(int, input().split())

consumption = a / 0.08 * 100
if consumption > b / 0.1 * 100:
    print(int(b / 0.1 * 100))
elif consumption < a / 0.1 * 100:
    print(int(a / 0.1 * 100))
else:
    print(int(consumption))
