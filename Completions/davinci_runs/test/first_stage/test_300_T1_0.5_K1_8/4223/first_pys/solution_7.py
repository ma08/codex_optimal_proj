

n = int(input())
s = input()

c = 1
for i in range(n-1):
    if s[i] != s[i+1]:
        c += 1
print(c)