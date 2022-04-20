

n = int(input())
heights = list(map(int, input().split()))

for i in range(1, n - 1):
    if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
        print('No')
        exit()

print('Yes')
