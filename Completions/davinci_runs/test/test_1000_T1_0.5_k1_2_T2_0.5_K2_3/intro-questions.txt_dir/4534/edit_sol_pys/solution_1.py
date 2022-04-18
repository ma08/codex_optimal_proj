class Solution:
    def getRow(self, rowIndex):
        res = [1]
        for i in range(1, rowIndex+1):
            res = [1] + [res[j] + res[j+1] for j in range(i-1)] + [1]
        return res

    def getRow2(self, rowIndex):
        res = [0 for _ in range(rowIndex+1)]
        res[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                res[j] += res[j-1]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(4))
    print(s.getRow2(4))
