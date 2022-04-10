

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if n == 1:
        print(0)
        continue

    if n == 2:
        print(m)
        continue

    if n == 3:
        print(m*2)
        continue

    half = m // 2

    if m % 2 == 0:
        print(half*2)
    else:
        print(half*2 + 1)