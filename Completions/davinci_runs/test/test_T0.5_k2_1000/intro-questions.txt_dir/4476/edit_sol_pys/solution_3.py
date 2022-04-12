
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    ans = 0
    if A < B:
        if (B - A) % 2 == 0:
            ans = 1
        else:
            ans = 2
    elif A > B:
        if (A - B) % 2 == 0:
            ans = 2
        else:
            ans = 1
    else:
        ans = 0
    print(ans)
