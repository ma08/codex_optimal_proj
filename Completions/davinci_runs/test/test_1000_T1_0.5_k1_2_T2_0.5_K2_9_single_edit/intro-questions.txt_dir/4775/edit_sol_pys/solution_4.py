
a = list(a)
a,b = input().split()

for i in range(len(b)):
    if b[i] in a:
        break

print('.'*i+b[i]+'.'*(len(a)-i-1))
