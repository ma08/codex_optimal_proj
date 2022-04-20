

#N = int(input())
#A = list(map(int, input().split()))
N = 3
A = [5, 2, 4]

ans = 0
for i in range(N):
    if A[i] % 2 == 0:
        A[i] /= 2
        ans += 1

print(ans)