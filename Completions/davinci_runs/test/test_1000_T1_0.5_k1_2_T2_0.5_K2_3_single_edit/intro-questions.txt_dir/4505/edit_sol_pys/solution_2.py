

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    while True:
        if A[i] % 2 == 0:
            A[i] //= 2
            ans += 1
        else:
            break

print(ans)
