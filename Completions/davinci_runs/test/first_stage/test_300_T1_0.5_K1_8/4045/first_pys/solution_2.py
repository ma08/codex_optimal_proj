

import sys

def main():
    #f = sys.stdin
    f = open('input.txt')
    n = int(f.readline().strip())
    s = f.readline().strip()
    t = f.readline().strip()
    f.close()
    if n == 1:
        print('YES')
        print('abc')
        return
    if s[0] == s[1]:
        print('NO')
        return
    if t[0] == t[1]:
        print('NO')
        return
    if (s[0] == t[0] and s[1] == t[1]) or (s[0] == t[1] and s[1] == t[0]):
        print('NO')
        return
    print('YES')
    if s[0] == t[0]:
        print(s[1]*n + t[1]*n + s[0]*n)
    else:
        print(s[0]*n + t[0]*n + s[1]*n)
    return

main()