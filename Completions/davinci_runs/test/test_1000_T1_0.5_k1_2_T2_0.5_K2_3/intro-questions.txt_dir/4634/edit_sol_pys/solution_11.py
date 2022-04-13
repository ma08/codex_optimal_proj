def minimum_moves(n, arr):
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(minimum_moves(n, arr))
