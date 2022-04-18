#

# Input
N = int(input())
A = list(map(int, input().split()))

# Initialize
cnt = 0
ans = 0

# Count
for i in range(N):
    if A[i] == cnt + 1:
        cnt += 1

# Output
if cnt == 0:
    print(-1)
else:
    print(N - cnt)
