

n, k = map(int, raw_input().split())

if n == 1:
    print "YES"
    print 1, 1
else:
    print "YES"
    for i in range(1, n):
        if i % 2 == 0:
            print i, i + 1
        else:
            print i + 1, i
    print 1, 2