
s = input().strip().split()
t = input().strip().split()

for i in range(len(s)-1):
    if s[i] != t[2*i+1]:
        print(s[i], end=' ')
print(s[-1])
