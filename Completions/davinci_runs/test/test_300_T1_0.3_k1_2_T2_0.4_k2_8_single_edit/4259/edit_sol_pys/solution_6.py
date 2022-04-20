

k = int(input())
a, b = map(int, input().split())

if (b - a) % k == 0 and (b - a) >= 0:
    print("OK")
else:
    print("NG")
