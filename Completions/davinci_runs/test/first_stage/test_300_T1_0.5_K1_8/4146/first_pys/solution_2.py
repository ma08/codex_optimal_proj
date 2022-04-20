

n = int(input())
v = list(map(int, input().split()))

# Count the number of occurrences of each element
counts = {}
for i in range(n):
    if v[i] in counts:
        counts[v[i]] += 1
    else:
        counts[v[i]] = 1

# If there are more than two different elements, the answer is -1
if len(counts) > 2:
    print(-1)
    exit()

# If there is only one different element, the answer is n/2
if len(counts) == 1:
    print(n//2)
    exit()

# If there are two different elements, the answer is the smaller count
counts_list = list(counts.values())
print(min(counts_list))