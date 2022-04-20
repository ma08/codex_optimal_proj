
n = int(input())
heights = list(map(int, input().split()))

for i in range(n - 1):
    if heights[i] > heights[i + 1]:
        heights[i + 1] = heights[i]

print('Yes')
