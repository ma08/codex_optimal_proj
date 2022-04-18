

a, b = map(float, input().split())

consumption = a / 0.08 / 1000
if consumption > b / 0.1:
    print(int(b / 0.1 / 1000))
elif consumption < a / 0.1:
    print(int(a / 0.1 / 1000))
else:
    print(int(consumption / 1000))
