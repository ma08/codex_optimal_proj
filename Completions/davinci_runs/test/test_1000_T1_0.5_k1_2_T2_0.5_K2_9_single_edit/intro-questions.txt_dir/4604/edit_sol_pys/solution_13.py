

N = int(input())
A = list(map(int, input().split()))

if A[0] != 0 or len(set(A)) != N:
    ans = 0
else:
    s = []
    for i in range(N):
        if len(s) == 0:
            s.append(i+1)
            continue
        if A[i] >= len(s):
            s.append(i+1)
        else:
            s.insert(A[i], i+1)

    ans = 1
    for i in range(N):
        ans *= i+1
        ans %= 10**9+7
    print(ans)
