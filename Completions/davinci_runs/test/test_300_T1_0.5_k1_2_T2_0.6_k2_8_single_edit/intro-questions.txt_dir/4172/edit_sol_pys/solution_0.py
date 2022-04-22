# Coder: Alka Wadhwa

# Q2. Input:
# n = 3, k = 2
# arr = [1, 4, 7]
# Output:
# 6
# Explanation:
# The minimum amount of moves required to make all elements equal is 6.
# Here's our sequence of moves:
# [1, 4, 7] => [2, 3, 6] => [1, 2, 5] => [2, 3, 4] => [1, 2, 3] => [2, 3, 4]

# Q3. Input:
# n = 5, k = 2
# arr = [1, 5, 8, 9, 11]
# Output:
# 15
# Explanation:
# The minimum amount of moves required to make all elements equal is 15.
# Here's our sequence of moves:
# [1, 5, 8, 9, 11] => [2, 4, 7, 10, 12] => [1, 3, 6, 9, 11] => [2, 4, 7, 8, 10] => [3, 5, 6, 8, 9] => [4, 5, 7, 8, 9] => [3, 4, 6, 7, 8]

# Q4. Input:
# n = 7, k = 3
# arr = [1, 2, 3, 4, 5, 6, 7]
# Output:
# 0

# Q5. Input:
# n = 5, k = 3
# arr = [1, 2, 3, 4, 5]
# Output:
# 4

# Q6. Input:
# n = 5, k = 2
# arr = [1, 2, 3, 4, 5]
# Output:
# 4

# Q7. Input:
# n = 5, k = 4
# arr = [1, 2, 3, 4, 5]
# Output:
# 0

n, k = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

moves = 0

if k == n:
    print(a[-1] - a[0])
else:
    while a[-1] != a[0]:
        a[-1] -= 1
        a[0] += 1
        moves += 1
        a.sort()
    print(moves)
