
a = int(input())
b = [a]

while True:
    if b[-1] % 2 == 0:
        b.append(int(b[-1]/2))
    else:
        b.append(int(3*b[-1]+1))
    if b.count(b[-1]) == 2:
        print(b.index(b[-1])+1)
        break
