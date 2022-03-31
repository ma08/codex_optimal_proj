

import math

N = int(input())

# We can reach any square that is in the range [1,N] in at most 2N-1 moves.
# Thus, we can solve this problem by binary search.

# Let's first find the minimum number of moves needed to reach a square that contains N.
# We can do this by binary search.
l = 0
r = 2*N-1
while l < r:
    mid = (l + r) // 2
    if (mid**2 + 2*mid + 1) // 2 >= N:
        r = mid
    else:
        l = mid + 1

# Now, let's find the maximum number of moves needed to reach a square that contains N.
# We can do this by binary search.
l = 0
r = 2*N-1
while l < r:
    mid = (l + r + 1) // 2
    if (mid**2 + 2*mid + 1) // 2 <= N:
        l = mid
    else:
        r = mid - 1

print(r - l + 1)