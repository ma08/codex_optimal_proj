

# SOLUTION:

socks, capacity, color_diff = [int(x) for x in input().split()]
colors = [int(x) for x in input().split()]

colors.sort()

count = 0

for i in range(socks):
    if i == 0 or colors[i] - colors[i - 1] > color_diff:
        count += 1

if count % capacity == 0:
    print(count // capacity)
else:
    print(count // capacity + 1)
