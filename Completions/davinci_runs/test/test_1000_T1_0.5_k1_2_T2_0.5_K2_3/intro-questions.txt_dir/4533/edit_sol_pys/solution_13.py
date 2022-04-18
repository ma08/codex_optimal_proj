

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int: 
        g.sort() # sort the greed list
        s.sort() # sort the size list
        count = 0
        i = 0 # index for greed list
        j = 0 # index for size list
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count
