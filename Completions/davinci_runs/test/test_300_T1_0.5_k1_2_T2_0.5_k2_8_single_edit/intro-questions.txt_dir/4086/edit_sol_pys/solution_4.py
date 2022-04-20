#n = int(input())
#a = [int(x) for x in input().split()]

n = int(input())
a = [int(x) for x in input().split()]

def remove_duplicates(a):
    b = list(set(a))
    return sorted(b)

b = remove_duplicates(a)
print(len(b))
print(*b)
