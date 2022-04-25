

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in lst:
    if len(i) == len(set(i)):
        print("Yes")
    else:
        print("No")

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in lst:
    a = len(i)
    b = len(set(i))
    c = ord(max(i))
    d = ord(min(i))
    e = c - d + 1
    if a == b and b == e:
        print("Yes")
    else:
        print("No")
