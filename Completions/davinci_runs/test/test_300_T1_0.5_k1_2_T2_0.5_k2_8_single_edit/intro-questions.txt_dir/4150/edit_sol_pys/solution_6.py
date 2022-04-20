class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall('[a-zA-Z0-9]', s)).lower()
        return s == s[::-1]

