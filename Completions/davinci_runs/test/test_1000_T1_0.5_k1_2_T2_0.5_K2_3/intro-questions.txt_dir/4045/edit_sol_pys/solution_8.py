
n = int(input())
s = input()
t = input()
for i in range(n):
    if set(s[i:i+2]) == set(t[i:i+2]):
        print("NO")
        exit()
print("YES")
