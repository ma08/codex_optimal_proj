
#this is a test file
a,b = input().split(' ')

for i in range(len(a)):
    if a[i] in b:
        print('.'*i+a[i]+'.'*(len(a)-i-1))
    else:
        print('.'*len(a))

for j in range(len(a)):
    if a[j] in b:
        print('.'*j+a[j]+'.'*(len(a)-j-1))
    else: print('.'*len(a))
