

#Solution

t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    if n == 1:
        print(d[0]*2)
    else:
        print(-1)