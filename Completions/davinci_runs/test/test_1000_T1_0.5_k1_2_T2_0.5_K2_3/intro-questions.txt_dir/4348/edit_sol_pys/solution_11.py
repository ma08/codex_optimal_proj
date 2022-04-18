
# 
import sys

def solve(n, k, s):
    if k == 0:
        return s

    for i in range(26):
        c = chr(ord('a') + i)
        j = s.find(c)
        if j == -1:
            continue
        if j < k:
            k -= j + 1
            s = s[j + 1:]
        else:
            return s[:j] + s[j + 1:]

    return ''

if __name__ == '__main__':
    n, k = [int(x) for x in sys.stdin.readline().split()]
    s = sys.stdin.readline().strip()
    print(solve(n, k, s))
