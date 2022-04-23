

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == 1 or n == 2:
        print(0)
    else:
        print(m - 1)
