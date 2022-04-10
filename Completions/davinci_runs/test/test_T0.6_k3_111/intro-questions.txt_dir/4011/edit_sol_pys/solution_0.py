

#@author: K. Palmer, D. C. Denton, J. Brown

n = int(input())
a = input()
f = input().split()
f = map(int, f)

for i in range(len(a)):
    a = a[:i] + str(f[int(a[i])-1]) + a[i+1:]
#    print a
    if i == len(a)-1:
        break
    for j in range(len(a)-i-1, i, -1):
        if a[j] > a[j-1]:
            a = a[:j-1] + a[j] + a[j-1] + a[j+1:]
            break
print a
