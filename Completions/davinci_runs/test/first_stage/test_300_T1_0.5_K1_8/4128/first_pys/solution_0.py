

# SOLUTION
# This is a classic example of a problem that can be solved using a binary search
# The idea is to find the smallest number a such that a^2 > n
# Then, the answer is a - 1
# This is because we know that the answer is less than a, and it is greater than a - 2
# So, we have to check a - 1 and a - 2, and then we have the answer
# The complexity is O(log n)

t = int(input())

for _ in range(t):
    n = int(input())
    
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        if mid ** 2 <= n:
            low = mid + 1
        else:
            high = mid
    print(low - 1)