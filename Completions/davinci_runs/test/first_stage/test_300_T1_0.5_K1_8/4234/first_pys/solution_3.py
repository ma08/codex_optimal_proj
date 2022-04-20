

n = int(input())
s = input()

good = True
k = 0

for i in range(0,n-1,2):
    if s[i] == s[i+1]:
        k += 1
        good = False

if good:
    print(0)
    print(s)
else:
    print(k)
    for i in range(0,n-1,2):
        if s[i] != s[i+1]:
            print(s[i],end='')