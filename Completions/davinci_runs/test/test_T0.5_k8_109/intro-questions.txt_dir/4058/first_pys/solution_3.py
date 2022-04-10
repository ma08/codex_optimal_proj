

n, r = list(map(int, input().split()))
a = list(map(int, input().split()))

def heaters(n, r, a):
    if sum(a) == 0:
        return -1

    count = 0
    i = 0
    while i < n:
        if a[i] == 1:
            i += 2*r - 1
        else:
            count += 1
            i += 2*r - 1
    return count

print(heaters(n, r, a))