

N = int(input())
difficulties = list(map(int, input().split()))

arc_problems = 0
for i in range(N):
    if difficulties[i] >= N // 2:
        arc_problems += 1

if arc_problems == N // 2:
    print(1)
else:
    print(0)