

N = int(input())
p = list(map(int, input().split()))

# Check if p is already sorted
p_sorted = p.copy()
p_sorted.sort()
if p == p_sorted:
    print('NO')
    exit()

# Check if p can be sorted by swapping one pair of numbers
i = 0
while i < N-1 and p[i] < p[i+1]:
    i += 1
j = i+1
while j < N-1 and p[j] < p[j+1]:
    j += 1
if i == j:
    print('NO')
    exit()
p[i], p[j] = p[j], p[i]
if p == p_sorted:
    print('YES')
    exit()
else:
    print('NO')
    exit()