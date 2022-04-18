from sys import stdin

s = stdin.readline().rstrip()
t = stdin.readline().rstrip()

for _ in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        print("Yes")
        exit()

print("No")
