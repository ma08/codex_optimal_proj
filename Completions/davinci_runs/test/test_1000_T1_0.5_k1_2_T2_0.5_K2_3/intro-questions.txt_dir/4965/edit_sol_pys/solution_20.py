

import sys, time

def timeit(f):
    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result

    return timed

def rearrange(n, t):
    t = sorted(t)
    if n%2 == 0:
        t1 = t[:n//2]
        t2 = t[n//2:]
    else:
        t1 = t[:n//2]
        t2 = t[n//2+1:]
    t1.reverse()
    t1 = t1 + t2
    return t1
@timeit

n = int(input())
t = [int(x) for x in input().split()]


print(*rearrange(n, t))
