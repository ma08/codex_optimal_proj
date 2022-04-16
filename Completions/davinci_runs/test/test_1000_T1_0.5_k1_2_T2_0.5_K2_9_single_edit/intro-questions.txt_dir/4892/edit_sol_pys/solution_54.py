


class Solution:
    def __init__(self):
        self.cache = {}

    def isMatch(self, s: str, p: str) -> bool:
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            self.cache[(s, p)] = (self.isMatch(s, p[2:]) or
                                  first_match and self.isMatch(s[1:], p))
        else:
            self.cache[(s, p)] = first_match and self.isMatch(s[1:], p[1:])
        return self.cache[(s, p)]
