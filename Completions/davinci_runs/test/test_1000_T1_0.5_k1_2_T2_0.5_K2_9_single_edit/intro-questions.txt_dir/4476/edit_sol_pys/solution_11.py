# coding: utf-8


T = int(input())

for _ in range(T):
    a, b = map(int, input().split())  # 入力の受け取り
    ans = 0
    if (a - b) % 2 == 0:
        ans = 2
    else:
        ans = 0
    print(ans)
