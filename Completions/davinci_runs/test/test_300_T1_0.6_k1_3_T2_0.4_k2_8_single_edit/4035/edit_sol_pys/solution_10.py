

a, b = map(int, input().split())

consumption = a / 0.08  # 燃費8km/L
if consumption > b / 0.1:  # 燃費10km/L
    print(int(b / 0.1))  # 燃費10km/Lで走行可能距離
elif consumption < a / 0.1:  # 燃費10km/L
    print(int(a / 0.1))  # 燃費10km/Lで走行可能距離
else:
    print(int(consumption))  # 燃費8km/Lで走行可能距離
