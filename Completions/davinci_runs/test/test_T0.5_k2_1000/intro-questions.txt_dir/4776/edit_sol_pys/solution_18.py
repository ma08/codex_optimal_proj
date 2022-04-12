N = int(input())

days = [list(map(int, input().split())) for _ in range(N)]

days.sort()
total_days = 0

for i in range(N):
    if i == 0:
        total_days += days[i][1] - days[i][0] + 1
    else:
        if days[i][0] <= days[i - 1][1]:
            if days[i][1] > days[i - 1][1]:
                total_days += days[i][1] - days[i - 1][1]
        else:
            total_days += days[i][1] - days[i][0] + 1

print(total_days)
