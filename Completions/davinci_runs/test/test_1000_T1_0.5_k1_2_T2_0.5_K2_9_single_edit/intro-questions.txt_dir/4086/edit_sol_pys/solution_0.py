import re


def find(a):
    b = []
    for i in range(len(a)):
        if re.search(r'\d+', a[i]):
            b.append(a[i])
    return b

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
