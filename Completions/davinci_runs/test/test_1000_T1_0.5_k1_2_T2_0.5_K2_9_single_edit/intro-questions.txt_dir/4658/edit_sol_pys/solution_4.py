
class Solution:
    def reverseBits(self, n: int) -> int:
        # n is binary string of length 32
        bin_str = bin(n)[2:]
        bin_str = bin_str.zfill(32)
        bin_str = bin_str[::-1]
        return int(bin_str, 2)

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = Solution().reverseBits(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


n = 0
solution = 0
test_case = [n, solution]
test_function(test_case)

n = 3
solution = 3221225472
test_case = [n, solution]
test_function(test_case)

n = 43261596
solution = 964176192
test_case = [n, solution]
test_function(test_case)
