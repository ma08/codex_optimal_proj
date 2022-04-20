

n = int(input())

s = input()

if sorted(s) == list(s):
    print("YES")
    print("0" * n)
else:
    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] != s[0]:
            a = i
            break
    for i in range(len(s) - 1, -1, -1):
        if s[i] != s[-1]:
            b = i
            break
    if a == 0 and b == len(s) - 1:
        print("NO")
    else:
        print("YES")
        if a == 0:
            print("0" * (b + 1) + "1" * (len(s) - b - 1))
        elif b == len(s) - 1:
            print("1" * a + "0" * (len(s) - a))
        else:
            print("1" * (a) + "0" * (b - a + 1) + "1" * (len(s) - b - 1))