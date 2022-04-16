

a,b = input().split()

for i in range(len(a)):
        print('.'*i+b[i]+'.'*(len(a)-i-1))
    else:
        print('.'*len(a))
    if b[i] in a:
        break
