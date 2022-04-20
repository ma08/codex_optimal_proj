

n = int(input())
h = list(map(int, input().split()))

# Fill in the gaps
for i in range(n - 1):
    if h[i] == h[i + 1]:
        h[i + 1] += 1

# Check if all equal
if len(set(h)) == 1:
    print('YES')
else:
    print('NO')