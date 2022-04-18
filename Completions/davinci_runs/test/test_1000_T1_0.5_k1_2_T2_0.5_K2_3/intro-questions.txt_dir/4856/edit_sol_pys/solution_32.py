
# -----main-----
a, b = map(int, input().split())

if int(str(a)[::-1]) > int(str(b)[::-1]):
    print(str(a)[::-1])
else:
    print(str(b)[::-1])
