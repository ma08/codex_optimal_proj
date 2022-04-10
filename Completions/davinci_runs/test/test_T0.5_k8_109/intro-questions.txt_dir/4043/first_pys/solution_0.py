

def solution(n, d, k):
    if d > n-1:
        return "NO"
    if k == 1:
        if d == 1:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        else:
            return "NO"
    if k == 2:
        if d == 1:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        elif d == 2:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        else:
            return "NO"
    if k == 3:
        if d == 1:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        elif d == 2:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        elif d == 3:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        else:
            return "NO"
    if k == 4:
        if d == 1:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        elif d == 2:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        elif d == 3:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        elif d == 4:
            return "YES\n" + "\n".join(["{} {}".format(i, i+1) for i in xrange(1, n)])
        else:
            return "NO"

n, d, k = map(int, raw_input().split())
print solution(n, d, k)