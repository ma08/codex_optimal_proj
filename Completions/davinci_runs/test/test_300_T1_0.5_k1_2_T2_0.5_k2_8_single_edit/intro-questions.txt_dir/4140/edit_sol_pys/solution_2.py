
from sys import stdin

s = stdin.readline().strip()

def longest_substring_without_repeating_characters(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    l = 0
    max_len = 0
    for r in range(1, len(s)):
        for i in range(l, r):
            if s[i] == s[r]:
                l = i + 1
        max_len = max(max_len, r - l + 1)
    return max_len
 
print(longest_substring_without_repeating_characters(s))
