a,b = input().split()
a = list(a)
b = list(b)
for i in range(len(a)):
    if a[i] == '-':
        a[i] = ' '
for i in range(len(b)):
    if b[i] == '-':
        b[i] = ' '
a = ''.join(a)
b = ''.join(b)

for i in range(len(b)):
    if b[i] in a:
        j = 0
        while j < len(a):
            if a[j] == b[i]:
                break
            j += 1
        break

for i in range(len(b)):
    if b[i] in a:
        print("."*j + b[i] + "."*(len(a) - j - 1))
    else:
        print("."*len(a))
    if i != len(b) - 1:
        print('')
