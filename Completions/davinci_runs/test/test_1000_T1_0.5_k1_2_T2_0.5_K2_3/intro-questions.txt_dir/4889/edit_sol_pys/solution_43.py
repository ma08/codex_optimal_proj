

n = int(input())
l = [int(x) for x in input().split()]

l = [21,34,18,9]
n = len(l)

def max_jumping(l):
    if len(l) == 1:
        return l[0]
    else:
        l = sorted(l)
        return l[-1] + max_jumping(l[:-1]) - 1

print(max_jumping(l))
