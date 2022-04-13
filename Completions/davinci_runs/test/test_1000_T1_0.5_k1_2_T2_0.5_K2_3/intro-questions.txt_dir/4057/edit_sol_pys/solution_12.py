

# n = int(input())
# a = list(map(int, input().split()))
n = 6
a = [1, 2, 4, 3, 3, 2]

# 1. Find the minimum value of all numbers
# 2. Find the maximum value of all numbers
# 3. If the difference between the minimum and the maximum value is less than the number of numbers,
#    then the minimum number of pockets is 1.
# 4. Otherwise, the minimum number of pockets is 1.

min_a = min(a)
max_a = max(a)

if max_a - min_a < n:
    print(0)
else:
    print(1)
