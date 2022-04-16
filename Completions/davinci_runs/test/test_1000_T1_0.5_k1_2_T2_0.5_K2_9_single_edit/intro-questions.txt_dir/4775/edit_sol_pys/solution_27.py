

a,b = input().split()

for i in range(len(b)):
    if b[i] in a:
        break

for j in range(len(b)):
    if b[j] in a and j >= i:
        print('.'*i+b[j]+'.'*(len(a)-i-1))
    else:
        print('.'*len(a))
