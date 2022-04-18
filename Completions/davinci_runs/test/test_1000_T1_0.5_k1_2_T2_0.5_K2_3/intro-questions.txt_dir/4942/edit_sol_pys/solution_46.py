
trees = int(input())
days = list(map(int, input().split()))
days.sort()
time = 0
for i in range(trees):
    if days[i] < time:
        time += 1
    else:
        time += days[i]
print(time)
