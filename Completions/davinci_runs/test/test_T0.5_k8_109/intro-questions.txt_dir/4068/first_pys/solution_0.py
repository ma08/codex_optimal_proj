

N, M = input().split()
N = int(N)
M = int(M)

broken_steps = []
for i in range(M):
    broken_steps.append(int(input()))
broken_steps.sort()

ways = [0] * (N + 1)
ways[0] = 1
ways[1] = 1

for i in range(2, N + 1):
    if i in broken_steps:
        ways[i] = 0
    else:
        ways[i] = (ways[i - 1] + ways[i - 2]) % 1000000007

print(ways[N])