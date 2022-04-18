n = int(input())
a = [int(x) for x in input().split()]

def remove_duplicates(a, n):
    b = []
    for i in range(n):
        if a[i] not in b:
            b.append(a[i])
    return b

b = remove_duplicates(a)
print(len(b))
print(*b)
