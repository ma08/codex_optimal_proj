n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
moves = 0

if k == n:
    print(a[-1] - a[0])
else:
    while a[-1] != a[0]:
        a[-1] -= 1  # вычитаем из максимального
        a[0] += 1  # прибавляем к минимальному
        moves += 1
        a.sort()
    print(moves)
