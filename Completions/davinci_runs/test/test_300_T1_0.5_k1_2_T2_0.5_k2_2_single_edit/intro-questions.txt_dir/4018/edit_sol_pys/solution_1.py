
import math
# -*- coding: utf-8 -*

def main():
    n, m = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()
    if m == 0:
        print 0
    else:
        ans = a[0]
        for i in xrange(1, n):
            ans = ans + a[i] * math.ceil(1.0 * i / m)
        print int(ans)
        
if __name__ == '__main__':
    main()
