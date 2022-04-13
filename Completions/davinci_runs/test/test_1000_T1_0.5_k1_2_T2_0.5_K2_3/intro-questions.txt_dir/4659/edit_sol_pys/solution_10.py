
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1] + res[i-1][j]) 
        return res
