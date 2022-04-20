
n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
players = [k for _ in range(n)]

for i in range(q):
    players[a[i] - 1] += 1

for i in range(n):
    if players[i] <= 0:
        print("No")
    else:
        print("Yes")
