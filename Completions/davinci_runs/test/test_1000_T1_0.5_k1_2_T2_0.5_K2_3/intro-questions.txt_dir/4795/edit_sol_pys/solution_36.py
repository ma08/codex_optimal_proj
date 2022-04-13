class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2 and s[0] == s[1]:
            return 1
        if len(s) == 2 and s[0] != s[1]:
            return 2
        if len(s) > 2:
            string = s[0]
            result = 1
            i = 1
            while i < len(s):
                if s[i] not in string:
                    string += s[i]
                    result = max(result, len(string))
                else:
                    string = string[string.index(s[i]) + 1:]
                    string += s[i]
                    result = max(result, len(string))
                i += 1
            return result


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
