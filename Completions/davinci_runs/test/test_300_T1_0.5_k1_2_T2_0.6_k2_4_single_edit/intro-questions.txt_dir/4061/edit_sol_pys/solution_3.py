

def s(l):
    l.sort()
    c = 0
    for i in xrange(1,len(l)):
        if l[i] == l[i-1]:
            c += 1
    return c
print s(map(int,raw_input().split()))
