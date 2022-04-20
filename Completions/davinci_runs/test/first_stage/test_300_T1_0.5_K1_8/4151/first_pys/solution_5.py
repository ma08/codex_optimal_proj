

def solve(a):
    n = len(a)
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = [i]
        else:
            d[a[i]].append(i)
    # print(d)

    res = 1
    for i in d:
        res *= (2**(len(d[i])-1))
        res %= 998244353
    return res

n = int(input())
a = list(map(int, input().split()))
print(solve(a))