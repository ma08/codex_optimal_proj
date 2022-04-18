
from collections import Counter

def solve(s):
    return len(Counter(s[:len(s)//2]) & Counter(s[len(s)//2:])) + 1

print(solve(input()))
