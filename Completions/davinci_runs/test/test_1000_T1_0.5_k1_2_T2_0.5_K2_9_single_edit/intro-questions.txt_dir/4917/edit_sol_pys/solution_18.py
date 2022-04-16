
n = int(input())

count = 0
intervals = []
for i in range(n):
    a, b = map(int, input().split())
    intervals.append((a, b))

intervals.sort()

for i in range(n-1):
    a, b = intervals[i]
    a_next, b_next = intervals[i+1]
    if a_next > b:
        count += 1
    if count > 1:
        print("edward is right")
        exit(0)

print("gunilla has a point")
