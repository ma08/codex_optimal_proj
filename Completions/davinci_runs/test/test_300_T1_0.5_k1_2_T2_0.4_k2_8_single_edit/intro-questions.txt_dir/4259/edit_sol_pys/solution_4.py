

k = int(input())  # 分割数
a, b = map(int, input().split())  # 分割前の最小値と最大値

if a % k == 0:
    print("OK")
elif b % k == 0:
    print("OK")
else:
    print("NG")
