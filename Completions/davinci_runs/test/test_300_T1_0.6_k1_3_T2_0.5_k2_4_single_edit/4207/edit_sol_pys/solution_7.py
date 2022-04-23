

class Solution:
    def solve(self, a, b):
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    return 1
        return 0


s = Solution()
assert s.solve([1, 2, 3, 4, 5], [2, 4, 7, 11, 3]) == 2
assert s.solve([13, 37, 39], [1, 2, 3]) == 2
assert s.solve([0, 0, 0, 0], [1, 2, 3, 4]) == 0
assert s.solve([1, 2, -1], [-6, -12, 6]) == 3
