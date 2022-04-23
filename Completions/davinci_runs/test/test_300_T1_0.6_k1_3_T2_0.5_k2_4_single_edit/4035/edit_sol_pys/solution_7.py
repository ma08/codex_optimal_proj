

a, b = map(float, input().split())

consumption = a / 0.08
if consumption > b / 0.1:
    print(b / 0.1)
elif consumption < a / 0.1:
    print(a / 0.1)
else:
    print(consumption)
