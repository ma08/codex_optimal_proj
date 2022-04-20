
n = int(input())
a = [int(x) for x in input().split()]  # a = list(map(int, input().split()))


def remove_duplicates(a):  # a = list(set(a))
    b = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            b.append(a[i])
    return b

b = remove_duplicates(a)
print(len(b))
print(*b)
