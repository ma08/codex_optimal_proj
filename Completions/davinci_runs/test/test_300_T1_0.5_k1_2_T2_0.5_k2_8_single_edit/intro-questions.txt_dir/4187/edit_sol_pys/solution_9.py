
n = int(input())
a = list(map(int, input().split()))

max_gap = 0
gap = 0

for i in a:
    if i == 0:
        max_gap = max(max_gap, gap)
        gap = 0
    else:
        gap += 1

max_gap = max(max_gap, gap)
print(max_gap)
