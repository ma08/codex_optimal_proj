
N = int(input())

start_dates = []  # list to store starting dates
end_dates = []  # list to store ending dates
# iterate over N

    # store start and end dates in start_dates and end_dates
for i in range(N):
    start, end = map(int, input().split())
    start_dates.append(start)
    end_dates.append(end)
# sort start_dates and end_dates

start_dates.sort()
end_dates.sort()
# counter to store number of rooms needed

count = 0
# index for start_dates and end_dates

curr_start = 0
curr_end = 0

# iterate over start_dates and end_dates
while curr_start < len(start_dates) and curr_end < len(end_dates):
    # if starting date is less than ending date, increment count
    if start_dates[curr_start] <= end_dates[curr_end]:
        count += 1
        curr_start += 1
    # else decrement count
    else:
        count -= 1
        curr_end += 1

# print count
print(count)
