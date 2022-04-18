

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in range(len(lst)):
    if len(lst[i]) == len(set(lst[i])):
        print("Yes")
    else: print("No")
