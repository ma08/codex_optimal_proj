

# Use the idea of sorting
# 1. If the min and max are equal, then return 0 as the answer
# 2. If the min and max are not equal, then we have to increase the min and decrease the max
# 3. The number of times we have to do this is the difference between the min and max
# 4. We keep doing this until the difference between the min and max is zero
# 5. We keep track of the number of times we do this.

# Time complexity: O(n)
# Space complexity: O(1)

n, k = map(int, input().split())
a = list(map(int, input().split()))

min_val = min(a)
max_val = max(a)

if min_val == max_val:
    print(0)
else:
    print(max_val - min_val)