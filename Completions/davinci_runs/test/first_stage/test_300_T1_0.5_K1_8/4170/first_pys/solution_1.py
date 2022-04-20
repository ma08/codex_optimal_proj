

n = int(input())
h = list(map(int, input().split()))

count = 0
max_count = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        count += 1
    else:
        count = 0
    max_count = max(count, max_count)

print(max_count)