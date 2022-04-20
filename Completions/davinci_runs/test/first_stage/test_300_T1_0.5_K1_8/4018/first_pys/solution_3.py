

import sys

input = sys.stdin.readline()
n, k = map(int, input.split())
s = sys.stdin.readline()

#print(n, k)
#print(s)

# calculate the sum of n-1, n-2, ..., n-n
# if sum is >= k, then return the sum, else return -1

# if n = 4, sum = 4 + 3 + 2 + 1 = 10
# if n = 5, sum = 5 + 4 + 3 + 2 + 1 = 15

# if n = 10, sum = 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 55

# if k >= sum(n)
# return sum(n)
# else
# return -1

sum = 0
for i in range(n, 0, -1):
    sum += i

if k >= sum:
    print(sum)
else:
    print(-1)