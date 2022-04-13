import math
n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
x = arr[0]
y = arr[-1]
print(int(math.sqrt(y-x)))
