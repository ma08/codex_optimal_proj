
# -*- coding: utf-8 -*-

def main():
    n, k = map(int, raw_input().split())
    s = raw_input()
    if k > 2**n:
        print -1
    else:
        ans = 0
        for i in xrange(n):
            if k & (1 << i):
                ans += n - i
        print ans

if __name__ == '__main__':
    main()
