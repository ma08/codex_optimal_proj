

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    ans = 0
    if (a - b) % 2 == 0:
        ans = 1
    else:
        ans = 2
    print(ans)
