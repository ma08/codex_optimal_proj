

a, b = map(int, input().split())
if a / 0.08 > b / 0.1:
    print(int(b / 0.08))
else:
    print(int(a / 0.08))
