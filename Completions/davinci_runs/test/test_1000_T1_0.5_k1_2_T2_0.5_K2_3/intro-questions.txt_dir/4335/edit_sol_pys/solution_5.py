

n = int(input())
s = input()

if n % 2 == 0:
    if s[:n//2] == s[(n//2):]:
        print("Yes")
    else:
        print("No")
else:
    if s[:n//2] == s[(n//2)+1:]:
        print("Yes")
    else:
        print("No")
