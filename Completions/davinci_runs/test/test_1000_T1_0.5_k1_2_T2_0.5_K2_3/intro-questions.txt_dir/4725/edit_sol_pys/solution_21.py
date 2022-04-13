
import sys

def min_erase(s):
    min_erase = sys.maxsize
    for i in range(len(s)-1):
        s_ = s[:i] + s[i+1:]
        min_erase = min(min_erase, min_erase(s_))
    return min_erase

print(min_erase(input()))
