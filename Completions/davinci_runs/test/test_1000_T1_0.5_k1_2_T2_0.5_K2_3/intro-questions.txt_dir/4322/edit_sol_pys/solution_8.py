
# SOLUTION

n = int(input())
a = [int(i) for i in input().split()]

if n == 1:
    print(1, end='\n')
    print(a[0], end=' ')
else:
    d = {}
    for i in a:
        d[i] = d.get(i, 0) + 1
    max_val = max(d.values())
    if max_val == 1:
        print(1, end='\n')
        print(a[0], end=' ')
    else:
        res = []
        for i in d:
            if d[i] == max_val:
                res.append(i)
        res.sort()
        print(len(res), end='\n')
        for i in res:
            print(i, end=' ')
