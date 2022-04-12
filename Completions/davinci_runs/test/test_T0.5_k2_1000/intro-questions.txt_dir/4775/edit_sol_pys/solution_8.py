
c = ''
a, b = input().split()

for i in range(len(b)):
    if b[i] in a:
        break

for j in range(len(b)):
    if b[j] in a:
        c += '.' * i + b[j] + '.' * (len(a) - i - 1) + '\n'
    else:
        c += '.'*len(a) + '\n'

print(c)
