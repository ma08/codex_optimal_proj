N = int(input())

startDates = []
endDates = []
for i in range(N):
    start, end = map(int, input().split())
    startDates.append(start)
    endDates.append(end)
startDates.sort()
endDates.sort()
count = 0
currStart = 0
currEnd = 0
while currStart < len(startDates) and currEnd < len(endDates):
    if startDates[currStart] <= endDates[currEnd]:
        count += 1
        currStart += 1
    else:
        count -= 1
        currEnd += 1
print(count)
