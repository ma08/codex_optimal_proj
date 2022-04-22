# import sys
# sys.stdin = open("input.txt")
# sys.stdout = open("output.txt", "w")

n = int(input())

a = [int(x) for x in input().split()]

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
for i in range(len(b)):
    print(b[i], end=" ")
