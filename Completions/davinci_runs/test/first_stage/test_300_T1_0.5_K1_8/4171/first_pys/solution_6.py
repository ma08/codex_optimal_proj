

# Solution 1:
# This is a greedy approach.
# In order to get k equal numbers, the minimum number of operations is the number of operations needed to make all the numbers equal to the minimum number in the array.
# So, we first find the minimum number in the array, and then find the number of operations needed to make all the numbers equal to the minimum number.
# The time complexity is O(n).

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
min_a = min(a)
ans = 0
for i in range(n):
    ans += a[i] - min_a
print(ans)

# Solution 2:
# This is a greedy approach.
# We first find the minimum number in the array, and then find the number of operations needed to make all the numbers equal to the minimum number.
# The time complexity is O(n).

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
min_a = min(a)
ans = 0
for i in range(n):
    ans += (a[i] - min_a) // 2
    a[i] -= (a[i] - min_a) // 2 * 2
if min(a) == min_a:
    print(ans)
else:
    print(ans + 1)

# Solution 3:
# This is a greedy approach.
# We first find the minimum number in the array, and then find the number of operations needed to make all the numbers equal to the minimum number.
# The time complexity is O(n).

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
min_a = min(a)
ans = 0
for i in range(n):
    ans += (a[i] - min_a) // 2
    a[i] -= (a[i] - min_a) // 2 * 2
print(ans + 1 if min(a) != min_a else ans)