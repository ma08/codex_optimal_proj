
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


def main():
    inputs = [1, 2, 3]
    inputs = [4, 3, 2, 1]
    result = Solution().plusOne(inputs)
    print result


if __name__ == '__main__':
    main()
