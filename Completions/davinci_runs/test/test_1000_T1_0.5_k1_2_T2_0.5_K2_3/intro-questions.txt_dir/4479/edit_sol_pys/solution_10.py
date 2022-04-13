class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        pos = {v: i for i, v in enumerate(row)}


        ans = 0
        for i in range(0, N, 2):
            x = row[i]
            if x % 2 == 0:
                y = x + 1
            else:
                y = x - 1
            j = pos[y]

            if j - i == 1:
                continue

            ans += 1
            row[i + 1], row[j] = row[j], row[i + 1]
            pos[row[i + 1]] = i + 1
            pos[row[j]] = j
        return ans
