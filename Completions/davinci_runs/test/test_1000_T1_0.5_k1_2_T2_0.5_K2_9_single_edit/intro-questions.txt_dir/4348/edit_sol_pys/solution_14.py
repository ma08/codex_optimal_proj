
# SOLUTION

n, k = map(int, input().split())
s = input()
x = 'abcdefghijklmnopqrstuvwxyz'


for i in range(k):
    for j in x:
        if j in s:
            s = s[s.find(j)+1:]
print(s)
