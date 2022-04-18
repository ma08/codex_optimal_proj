import sys


a, b = map(int, sys.stdin.readline().split())

consumption = a / 0.08
if consumption > b / 0.1:
    print(int(b / 0.1))
elif consumption < a / 0.1:
    print(int(a / 0.1))
else:
    print(int(consumption))
