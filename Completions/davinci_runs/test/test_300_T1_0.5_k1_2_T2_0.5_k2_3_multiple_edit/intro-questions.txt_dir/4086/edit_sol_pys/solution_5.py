
def remove_duplicates(a):
    b = []
    for i in a:
        if i in b:
            continue
        else:
            b.append(i)
    return b

b = remove_duplicates(a)
print(len(b))
print(*b)
