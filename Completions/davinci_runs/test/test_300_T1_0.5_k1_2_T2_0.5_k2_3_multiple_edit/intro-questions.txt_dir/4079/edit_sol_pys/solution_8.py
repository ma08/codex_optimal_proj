

n = int(input())
lst = []
for i in range(n):
    lst.append(input().split())

for i in lst:
    for j in i:
        if len(j) == len(set(j)):
            print("Yes")
        else:
            print("No")
