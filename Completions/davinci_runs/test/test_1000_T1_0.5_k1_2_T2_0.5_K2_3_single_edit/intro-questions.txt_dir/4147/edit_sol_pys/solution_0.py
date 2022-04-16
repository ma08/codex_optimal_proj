N = int(input())
A = list(map(int, input().split()))


ans = 0
for i in range(N):
    if i == 0:
        if A[i] != 0:
            ans += 1
    else:
        if A[i] > A[i-1]:
            ans += A[i] - A[i-1] + 1
        elif A[i-1] > A[i]:
            ans += A[i-1] - A[i] + 1
print(ans)




