

N = int(input())
times = list(map(int, input().split()))
times.sort()

totalTime = 0

for i in range(N):
    totalTime += sum(times[i:])

print(totalTime)
