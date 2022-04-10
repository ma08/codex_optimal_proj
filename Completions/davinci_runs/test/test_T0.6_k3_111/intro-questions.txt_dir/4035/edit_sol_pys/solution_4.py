

a, b = map(int, input().split())  # a, b = (int(x) for x in input().split()) これでもOK

if a * 9 == b * 8:
    print(a * 9 // 8 + 1)
elif a * 9 < b * 8:
    print(-1)
else:
    print((a * 9 // 8 // 10 + 1) * 10)
