

from sys import stdin

s = stdin.readline()

def check(s):
    # count the number of adjacent 0's and 1's
    count = {}
    c = s[0]
    count[c] = 1
    for i in range(1, len(s)):
        if s[i] == c:
            count[c] += 1
        else:
            c = s[i]
            count[c] = 1

    return min(count.values()) * 2

print check(s)
