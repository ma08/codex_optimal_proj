

import sys

def main():
    q = int(sys.stdin.readline())
    for i in range(q):
        s = list(sys.stdin.readline().strip())
        m = int(sys.stdin.readline())
        b = [int(x) for x in sys.stdin.readline().split()]
        print(solve(s, m, b))

def solve(s, m, b):
    n = len(s)
    count = [0] * 26
    for x in s:
        count[ord(x) - ord('a')] += 1

    #print(count)

    for i in range(m):
        for j in range(b[i]):
            count[ord(s[n - 1 - j]) - ord('a')] -= 1
        s = s[:-b[i]]
        #print(s)

    ans = [''] * 26
    for i in range(26):
        ans[i] = chr(ord('a') + i) * count[i]

    return ''.join(ans)

if __name__ == '__main__':
    main()