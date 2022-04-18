

# The smallest k for which s is k-periodic is the largest integer k' such that s[i] == s[i+k'] for all i in the range [0, len(s)-k'].

# To find this k', we can use a sliding window of size k' and check that all the characters are the same.

# If a window of size k' satisfies the property, then any window of size > k' will also satisfy the property.
# Thus, we can use binary search to find the largest k' that satisfies the property.
s = input()

def is_periodic(k):
    for i in range(0, len(s)-k):
        if s[i] != s[i+k]:
            return False
    return True

lo = 1
hi = len(s)
while lo < hi:
    mid = (lo + hi) // 2
    if is_periodic(mid):
        lo = mid + 1
    else:
        hi = mid
print(lo-1)
