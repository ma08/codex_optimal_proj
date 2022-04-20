
n = int(input())
heights = list(map(int, input().split()))
flag = True
for i in range(1, n):
    if heights[i] < heights[i - 1]:
        heights[i] = heights[i - 1]
    if heights[i] > heights[i - 1]:
        flag = False
if flag:
    print('Yes')
else:
    print('No')
