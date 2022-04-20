

# Solution

n, k = map(int, input().split())
s = list(map(int, input().split()))

counts = {}
for x in s:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

sorted_counts = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)

for i in range(k):
    print(sorted_counts[i][0], end=' ')