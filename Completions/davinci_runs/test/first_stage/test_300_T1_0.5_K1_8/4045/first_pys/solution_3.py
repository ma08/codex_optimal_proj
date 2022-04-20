

n = int(input())
s = input()
t = input()

if s == t:
    print("NO")
elif s[0] == t[1] and s[1] == t[0]:
    print("NO")
else:
    print("YES")
    for i in range(n):
        print(s[0], end="")
        print(s[1], end="")
        print(t[0], end="")
        print(t[1], end="")
        print(s[0], end="")
        print(s[1], end="")