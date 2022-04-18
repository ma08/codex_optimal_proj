
n = int(input())

intervals = []
for i in range(n):
    a, b = map(int, input().split())
    intervals.append((a, b))

intervals.sort()

for i in range(n-1):
    a, b = intervals[i]
    a_next, b_next = intervals[i+1]
    if b_next < a or b_next < b:
        print("edward is right")
        exit(0)

print("gunilla has a point")
