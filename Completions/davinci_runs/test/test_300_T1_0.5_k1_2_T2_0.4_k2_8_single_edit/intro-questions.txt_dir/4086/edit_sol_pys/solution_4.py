

n = int(input()) # number of elements
a = [int(x) for x in input().split()] # list of elements

def remove_duplicates(a): # function to remove duplicates
    b = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            b.append(a[i])
    return b

b = remove_duplicates(a) # list of unique elements
print(len(b)) # number of unique elements
print(*b) # list of unique elements
