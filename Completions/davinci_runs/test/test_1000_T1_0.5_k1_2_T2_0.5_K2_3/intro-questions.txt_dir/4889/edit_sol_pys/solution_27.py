

n = int(input())
l = [int(x) for x in input().split()]

l = [21,34,18,9]
n = len(l)

def max_javelin(l, n):
    if len(l) == 1:
        return l[0]
    else:
        l = sorted(l)
        return l[-1] + max_javelin(l[:-1], n-1) - 1

print(max_javelin(l))
