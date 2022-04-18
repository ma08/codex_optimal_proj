

N = int(input())

days = [0 for i in range(365)]

for i in range(N):
    start, end = map(int, input().split()) #start and end are lists
    for j in range(start - 1, end): #start and end are indexes
        days[j] += 1

print(sum(days))
