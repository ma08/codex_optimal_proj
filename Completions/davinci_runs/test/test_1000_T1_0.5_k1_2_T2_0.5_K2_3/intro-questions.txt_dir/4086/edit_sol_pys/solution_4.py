

n = int(input())
a = [int(x) for x in input().split()] #this line will take input and store it in the list a

def remove_duplicates(a): #this function will remove duplicates from the list
    b = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            b.append(a[i])
    return b

b = remove_duplicates(a)
print(len(b),*b)
