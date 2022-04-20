

k = int(input())
a, b = map(int, input().split())

if a <= k <= b:
    print("OK")
elif b < k <= a:
    print("NG")
else:
    print("NG")
