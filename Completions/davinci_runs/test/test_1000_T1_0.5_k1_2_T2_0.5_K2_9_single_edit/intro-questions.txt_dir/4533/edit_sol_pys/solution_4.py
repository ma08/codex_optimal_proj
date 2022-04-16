"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        content_children = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                content_children += 1
                i += 1
                j += 1
            else:
                j += 1
        return content_children
