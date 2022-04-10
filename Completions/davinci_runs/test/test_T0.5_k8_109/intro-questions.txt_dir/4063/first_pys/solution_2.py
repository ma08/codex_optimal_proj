

n = int(input())
difficulties = list(map(int, input().split()))
difficulties.sort()

# The difference between the number of problems for ARCs and the number of problems for ABCs is
# the number of problems with difficulty larger than K minus the number of problems with difficulty smaller than K.
# If the difference is 0, then the number of problems for ARCs and the number of problems for ABCs are the same.
# Therefore, the problem is equivalent to finding the number of K's that make the difference 0.
#
# We can find the number of K's that make the difference 0 by adding 1 to the number of K's that make the difference 1,
# and subtracting 1 from the number of K's that make the difference -1.
# This is because we can make the difference 0 by subtracting 1 from the number of problems for ARCs and adding 1 to the number of problems for ABCs.
#
# We can find the number of K's that make the difference 1 or -1 by counting the number of problems with difficulty larger or smaller than K, respectively.
#
# We can count the number of problems with difficulty larger than K by using binary search.
# The lower bound of binary search is the smallest difficulty, and the upper bound is the largest difficulty.
# Since we want to find the number of problems with difficulty larger than K, we want to find the largest K that makes the difference 1.
# Therefore, we want to find the lower bound of the largest K that makes the difference 1.
# We can find the lower bound of the largest K that makes the difference 1 by using lower_bound function.
#
# We can count the number of problems with difficulty smaller than K by using binary search.
# The lower bound of binary search is the smallest difficulty, and the upper bound is the largest difficulty.
# Since we want to find the number of problems with difficulty smaller than K, we want to find the smallest K that makes the difference -1.
# Therefore, we want to find the upper bound of the smallest K that makes the difference -1.
# We can find the upper bound of the smallest K that makes the difference -1 by using upper_bound function.

# The number of K's that make the difference 0.
num_of_k_that_make_difference_0 = 0

# The number of K's that make the difference 1.
num_of_k_that_make_difference_1 = bisect.bisect_left(difficulties, difficulties[n // 2])

# The number of K's that make the difference -1.
num_of_k_that_make_difference_minus_1 = n - bisect.bisect_right(difficulties, difficulties[n // 2])

# Add 1 to the number of K's that make the difference 1, and subtract 1 from the number of K's that make the difference -1.
num_of_k_that_make_difference_0 += num_of_k_that_make_difference_1 + 1
num_of_k_that_make_difference_0 -= num_of_k_that_make_difference_minus_1 - 1

print(num_of_k_that_make_difference_0)