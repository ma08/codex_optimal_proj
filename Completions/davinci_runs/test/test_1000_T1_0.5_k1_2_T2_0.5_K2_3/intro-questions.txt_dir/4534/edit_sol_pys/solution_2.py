

class Solution:  # Time: O(n^2), Space: O(n)
    def getRow(self, rowIndex: int) -> List[int]:  # Time: O(n^2), Space: O(n)
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [1, 1]
        for i in range(2, rowIndex + 1):
            temp = [1] * (i + 1)
            for j in range(1, i):
                temp[j] = result[j - 1] + result[j]
            result = temp
        return result
