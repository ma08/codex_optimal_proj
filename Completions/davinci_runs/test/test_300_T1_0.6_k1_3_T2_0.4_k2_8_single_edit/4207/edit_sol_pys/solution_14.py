

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Solution:
    def solve(self, a, b):
        # Write your code here
        n = len(a)
        m = len(b)
        if n != m:
            return -1
        if n == 1:
            if a[0] == b[0]:
                return 1
            return -1
        if n == 2:
            if a[0] == b[0] and a[1] == b[1]:
                return 1
            if a[0] == b[1] and a[1] == b[0]:
                return 1
            return -1
        if n == 3:
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[2]:
                return 1
            if a[0] == b[0] and a[1] == b[2] and a[2] == b[1]:
                return 1
            if a[0] == b[1] and a[1] == b[0] and a[2] == b[2]:
                return 1
            if a[0] == b[1] and a[1] == b[2] and a[2] == b[0]:
                return 1
            if a[0] == b[2] and a[1] == b[0] and a[2] == b[1]:
                return 1
            if a[0] == b[2] and a[1] == b[1] and a[2] == b[0]:
                return 1
            return -1
        if n == 4:
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] == b[3]:
                return 1
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[3] and a[3] == b[2]:
                return 1
            if a[0] == b[0] and a[1] == b[2] and a[2] == b[1] and a[3] == b[3]:
                return 1
            if a[0] == b[0] and a[1] == b[2] and a[2] == b[3] and a[3] == b[1]:
                return 1
            if a[0] == b[0] and a[1] == b[3] and a[2] == b[1] and a[3] == b[2]:
                return 1
            if a[0] == b[0] and a[1] == b[3] and a[2] == b[2] and a[3] == b[1]:
                return 1
            if a[0] == b[1] and a[1] == b[0] and a[2] == b[2] and a[3] == b[3]:
                return 1
            if a[0] == b[1] and a[1] == b[0] and a[2] == b[3] and a[3] == b[2]:
                return 1
            if a[0] == b[1] and a[1] == b[2] and a[2] == b[0] and a[3] == b[3]:
                return 1
            if a[0] == b[1] and a[1] == b[2] and a[2] == b[3] and a[3] == b[0]:
                return 1
            if a[0] == b[1] and a[1] == b[3] and a[2] == b[0] and a[3] == b[2]:
                return 1
            if a[0] == b[1] and a[1] == b[3] and a[2] == b[2] and a[3] == b[0]:
                return 1
            if a[0] == b[2] and a[1] == b[0] and a[2] == b[1] and a[3] == b[3]:
                return 1
            if a[0] == b[2] and a[1] == b[0] and a[2] == b[3] and a[3] == b[1]:
                return 1
            if a[0] == b[2] and a[1] == b[1] and a[2] == b[0] and a[3] == b[3]:
                return 1
            if a[0] == b[2] and a[1] == b[1] and a[2] == b[3] and a[3] == b[0]:
                return 1
            if a[0] == b[2] and a[1] == b[3] and a[2] == b[0] and a[3] == b[1]:
                return 1
            if a[0] == b[2] and a[1] == b[3] and a[2] == b[1] and a[3] == b[0]:
                return 1
            if a[0] == b[3] and a[1] == b[0] and a[2] == b[1] and a[3] == b[2]:
                return 1
            if a[0] == b[3] and a[1] == b[0] and a[2] == b[2] and a[3] == b[1]:
                return 1
            if a[0] == b[3] and a[1] == b[1] and a[2] == b[0] and a[3] == b[2]:
                return 1
            if a[0] == b[3] and a[1] == b[1] and a[2] == b[2] and a[3] == b[0]:
                return 1
            if a[0] == b[3] and a[1] == b[2] and a[2] == b[0] and a[3] == b[1]:
                return 1
            if a[0] == b[3] and a[1] == b[2] and a[2] == b[1] and a[3] == b[0]:
                return 1
            return -1
        if n == 5:
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] == b[3] and a[4] == b[4]:
                return 1
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] == b[4] and a[4] == b[3]:
                return 1
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[3] and a[3] == b[2] and a[4] == b[4]:
                return 1
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[3] and a[3] == b[4] and a[4] == b[2]:
                return 1
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[4] and a[3] == b[2] and a[4] == b[3]:
                return 1
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[4] and a[3] == b[3] and a[4] == b[2]:
                return 1
            if a[0] == b[0] and a[1] == b[2] and a[2] == b[1] and a[3] == b[3] and a[4] == b[4]:
                return 1
            if a[0] == b[0] and a[1] == b[2] and a[2] == b[


s = Solution()
assert s.solve([1, 2, 3, 4, 5], [2, 4, 7, 11, 3]) == 2
assert s.solve([13, 37, 39], [1, 2, 3]) == 2
assert s.solve([0, 0, 0, 0], [1, 2, 3, 4]) == 0
assert s.solve([1, 2, -1], [-6, -12, 6]) == 3
