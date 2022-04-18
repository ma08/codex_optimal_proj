
n = int(input())
s = input()
t = input()
for i in range(n):
    if s[i:i+2] == t[i:i+2]:
        print("NO")
        exit()
print("YES")
