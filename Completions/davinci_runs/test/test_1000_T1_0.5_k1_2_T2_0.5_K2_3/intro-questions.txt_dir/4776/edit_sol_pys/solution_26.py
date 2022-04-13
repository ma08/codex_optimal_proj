
N = int(input())

start_dates = []
end_dates = []

for i in range(N):
    start, end = map(int, input().split())
    start_dates.append(start)
    end_dates.append(end)

start_dates.sort()
end_dates.sort()

count = 0

curr_start = 0
curr_end = 0

while curr_start < len(start_dates) and curr_end < len(end_dates):
    if start_dates[curr_start] <= end_dates[curr_end]:
        count += 1
        curr_start += 1
    else:
        count -= 1
        curr_end += 1

print(count)
