

s = input().lower()
t = input().lower()

if s == t or s == t[::-1]:
    print("Yes")
else:
    print("No")
