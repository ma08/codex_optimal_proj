

L, R = map(int, input().split())

# 2019で割った数の値が小さいものを探す
if L % 2019 != 0:
    L += 1
if R % 2019 != 0:
    R -= 1

if L > R:
    print(0)
else:
    print(min(i * (i + 1) % 2019 for i in range(L, R)))