
def rearrange(t):
    t = sorted(t, reverse=True)
    return t[::2] + t[1::2]

n = int(input())
t = [int(x) for x in input().split()]

print(*rearrange(t))
