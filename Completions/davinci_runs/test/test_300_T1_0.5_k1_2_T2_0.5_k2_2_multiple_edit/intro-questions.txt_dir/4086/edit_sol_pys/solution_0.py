

n = int(input()) #taking input from user
a = [int(x) for x in input().split()] #taking input from user and converting it to list
def remove_duplicates(a): #defining function
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
