

# n = int(input())
# a = list(map(int, input().split()))
n = 6
a = [1, 2, 4, 3, 3, 2]

# 1. Find the minimum value of all coins
# 2. If the difference between the minimum and the maximum value is less than the number of coins,
#    then the minimum number of pockets is 1.
# 3. Otherwise, the minimum number of pockets is 2.

min_a = min(a)

if max(a) - min_a < n:
    print(1)
else:
    print(2)
