
s, t = list(input()), list(input())

if s == t:
    print("Yes")
    exit()

for i in range(len(s)):
    s.insert(0, s.pop(-1))
    if s == list(t):
        print("Yes")
        exit()

print("No")
