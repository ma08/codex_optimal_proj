

s = input().rstrip()
t = input().rstrip()

if len(s) < len(t):
    print("Yes")  # s < t
elif len(s) > len(t):
    print("No")  # s > t
else:
    for i in range(len(s)):
        if s[i] < t[i]:
            print("Yes")  # s < t
            break
        elif s[i] > t[i]:
            print("No")  # s > t
            break
        else:
            if i == len(s) - 1:
                print("No")  # s == t
