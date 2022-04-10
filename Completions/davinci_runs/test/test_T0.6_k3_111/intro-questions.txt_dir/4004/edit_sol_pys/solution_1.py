


# Problem
# You are given a sequence a1, a2, ..., aN. Find the smallest positive integer that does not occur in the sequence.

# Input
# The first line of the input contains an integer 1 ≤ N ≤ 10^6.

# The second line contains N integers a1, a2, ..., aN separated by spaces. Each of the integers is between 1 and 10^9 inclusive.

# Output
# Print the smallest positive integer that does not occur in the sequence.

# Examples
# input
# 5
# 1 2 3 4 6
# output
# 5
# input
# 4
# 1 2 3 4
# output
# 5
# input
# 4
# 2 2 2 2
# output
# 1

# Note
# In the first example, the missing integer is 5.

# In the second example, all the integers in the sequence are positive, so we print the smallest positive integer that does not occur in the sequence, which is 5.

# In the third example, the only positive integer that does not occur in the sequence is 1.

# Solution
# Solved 

import sys

n = int(input())
a = list(map(int, input().split()))

max_a = max(a)
min_a = min(a)

if n == 1:
    print(0)
    sys.exit()

if max_a == min_a:
    print(0)
    sys.exit()

if max_a - min_a > 100:
    print(-1)
    sys.exit()

for i in range(max_a - min_a + 1):
    if i == 0:
        continue

    flag = True

    for j in range(len(a)):
        if a[j] - i < min_a:
            flag = False
            break

    if flag:
        print(i)
        sys.exit()

print(-1)
