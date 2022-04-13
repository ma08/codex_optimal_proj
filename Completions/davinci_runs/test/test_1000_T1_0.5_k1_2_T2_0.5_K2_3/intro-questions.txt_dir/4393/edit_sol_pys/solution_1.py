
n = int(input())
t = list(input())
s = ""
for i in range(n):
    if i == 0 or t[i] != t[i-1]:
        s += t[i]

print(len(s))
