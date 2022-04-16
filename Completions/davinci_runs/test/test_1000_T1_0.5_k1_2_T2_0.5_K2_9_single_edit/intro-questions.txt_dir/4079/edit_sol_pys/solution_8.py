

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in lst:  # i is a string
    if len(i) == len(set(i)):
        print("Yes")
    else:
        print("No")
