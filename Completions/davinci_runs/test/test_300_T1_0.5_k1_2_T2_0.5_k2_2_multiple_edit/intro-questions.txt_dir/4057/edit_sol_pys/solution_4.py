

# n = int(input())
# a = list(map(int, input().split()))
n = 6
a = [1, 2, 4, 3, 3, 2]

# 1. Find the minimum value of all coins
# 2. Find the maximum value of all coins
# 3. If the difference between the minimum and the maximum value is less than the number of coins,
#    then the minimum number of pockets is 1.
# 4. Otherwise, the minimum number of pockets is 2.

min_a = min(a)
max_a = max(a)

if max_a - min_a < n:
    print(2)
else:


# # n = int(input())
# # a = list(map(int, input().split()))
# n = 6
# a = [1, 2, 4, 3, 3, 2]
#
# # 1. Find the minimum value of all coins
# # 2. Find the maximum value of all coins
# # 3. If the difference between the minimum and the maximum value is less than the number of coins,
# #    then the minimum number of pockets is 1.
# # 4. Otherwise, the minimum number of pockets is 2.
#
# min_a = min(a)
# max_a = max(a)
#
# if max_a - min_a < n:
#     print(2)
# else:
#     print(1)
    print(1)
