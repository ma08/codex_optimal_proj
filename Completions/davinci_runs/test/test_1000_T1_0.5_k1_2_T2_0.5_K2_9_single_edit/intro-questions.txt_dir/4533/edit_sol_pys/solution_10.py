
import os
import sys


def test(g, s):
    print(f"g: {g} s: {s}")
    sol = Solution()
    print(f"result: {sol.findContentChildren(g, s)}")


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count
