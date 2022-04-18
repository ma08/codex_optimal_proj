

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        elif num < 4:
            return False
        else:
            return (num % 4 == 0) and self.isPowerOfFour(num / 4)
