a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(a)
print(b)
for i in range(len(b)):
    if b[i] % 2 == 0:
        a.append(b[i])
    else:
        a.insert(0, b[i])
print(a)
