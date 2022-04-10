

import sys

def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    if s == t:
        print('NO')
    elif n == 1:
        print('YES')
        print('abc'[s.index('a')])
    elif n == 2:
        print('YES')
        print(''.join([s[0], s[1], t[0], t[1], s[0], t[1]]))
    else:
        print('YES')
        print(''.join([s[0], t[1], s[0], s[1], t[0], t[1]]*(n-1) + [s[1], t[1]]))

if __name__ == '__main__':
    main()