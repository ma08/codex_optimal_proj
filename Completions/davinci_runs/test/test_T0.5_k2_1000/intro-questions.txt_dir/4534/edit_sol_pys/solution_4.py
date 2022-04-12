class Solution:
    def getRow(self, row_index: int):
        res = [1]
        for i in range(1, row_index+1):
            res = [1] + [res[j] + res[j+1] for j in range(i-1)] + [1]
        return res

    def getRow2(self, row_index):
        res = [0 for _ in range(row_index+1)]
        res[0] = 1
        for i in range(1, row_index+1):
            for j in range(i, 0, -1):
                res[j] += res[j-1]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))
    print(s.getRow2(3))
