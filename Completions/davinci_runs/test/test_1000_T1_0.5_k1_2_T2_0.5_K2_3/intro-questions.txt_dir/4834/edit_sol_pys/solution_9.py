n = int(input())
times = list(map(int, input().split()))
times.sort()
total = 0
for i in range(n):
    total += (i + 1) * times[i]

print(total)


n = int(input())
times = list(map(int, input().split()))
times.sort()
total = 0
for i in range(n):
    total += (i + 1) * times[i]

print(total)
