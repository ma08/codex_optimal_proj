
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y = str(x)
            if y == y[::-1]:
                return True
            else:
                return False
