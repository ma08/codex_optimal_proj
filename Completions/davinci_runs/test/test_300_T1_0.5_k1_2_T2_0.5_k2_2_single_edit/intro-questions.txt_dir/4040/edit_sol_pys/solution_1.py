

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def get_river(n, a, b):
    river = [0] * n
    for i in range(n):
        if b[i] != 0:
            river[i] = a[b[i]-1]
            a[b[i]-1] = 0
    return [x for x in river if x != 0]

print(*get_river(n, a, b))
