
class Solution:
    def solve(self, a, b):
        # Write your code here
        pass


s = Solution()
assert s.solve([1, 2, 3, 4, 5], [2, 4, 7, 11, 3]) == 2, "Test 1 Failed"
assert s.solve([13, 37, 39], [1, 2, 3]) == 2, "Test 2 Failed"
assert s.solve([0, 0, 0, 0], [1, 2, 3, 4]) == 0, "Test 3 Failed"
assert s.solve([1, 2, -1], [-6, -12, 6]) == 3, "Test 4 Failed"
print("All Tests Passed")
