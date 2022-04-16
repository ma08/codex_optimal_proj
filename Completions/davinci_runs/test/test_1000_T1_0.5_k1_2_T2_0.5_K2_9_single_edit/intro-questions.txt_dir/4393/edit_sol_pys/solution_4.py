
n = int(input())
t = input()

s = ""
for i in range(n):
    if t[i] != t[i-1]:
        s += t[i]

print(s)
