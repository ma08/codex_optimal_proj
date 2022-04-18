

a, b, c = map(int, input().split())

if a >= 1 and a <= 20 and b >= 1 and b <= 20 and c >= 1 and c <= 20:
    print(a*b*c)
else:
    print(-1)
