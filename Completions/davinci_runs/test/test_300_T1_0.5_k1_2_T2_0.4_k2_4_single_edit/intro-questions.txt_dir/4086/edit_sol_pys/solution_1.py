
n = int(input())
a = [int(x) for x in input().split()]


b = remove_duplicates(a)
print(len(b))
print(*b)
