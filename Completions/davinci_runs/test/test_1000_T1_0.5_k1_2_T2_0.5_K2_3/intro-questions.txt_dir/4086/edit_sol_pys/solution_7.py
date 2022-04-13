
n = int(input("Enter the number of elements: "))
a = [int(x) for x in input("Enter the elements: ").split()]

def remove_duplicates(a):
    b = set()
    for i in a:
        b.add(i)
    return list(b)

b = remove_duplicates(a)
print(len(b))
print(*b)
