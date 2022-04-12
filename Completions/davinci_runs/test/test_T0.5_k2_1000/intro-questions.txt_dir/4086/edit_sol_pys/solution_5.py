n = int(input())
a = [int(x) for x in input().split()][:n]

def remove_duplicates(a):
    return list(set(a))

b = remove_duplicates(a)
print(len(b))
print(*b)
