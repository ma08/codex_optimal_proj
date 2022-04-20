

def main():
    n, k = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    d = dict()
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    t = []
    for i in range(k):
        m = 0
        for x in d:
            if d[x] > m:
                m = d[x]
                y = x
        t.append(y)
        d[y] = 0
    print(' '.join([str(x) for x in t]))

main()