n = int(input())
a = [int(x) for x in input().split()]

def remove_duplicates(a):
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
>>>>>>> f2f8e6a0b6e9c6d9e6c8e7b6f1b6f0c6d8a6f2e6
print(*b)
