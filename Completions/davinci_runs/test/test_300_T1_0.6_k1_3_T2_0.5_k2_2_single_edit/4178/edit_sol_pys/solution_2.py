

n = int(input())
heights = map(int, input().split())
heights = list(heights)

for i in range(1, n):
    if heights[i] < heights[i - 1]:
        heights[i] = heights[i - 1]

print('Yes')
