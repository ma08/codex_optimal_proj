

def remove_duplicates(a):
    b = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            b.append(a[i])
    return len(b)

print(remove_duplicates([int(x) for x in input().split()]))
