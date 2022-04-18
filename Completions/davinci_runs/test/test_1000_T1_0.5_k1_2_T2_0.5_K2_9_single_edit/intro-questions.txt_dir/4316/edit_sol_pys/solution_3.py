#-----main-----
N = int(input())
S = []
for i in range(N):
    S.append(input())


for s in S:
    if len(s) == 4:
        if s[0] == s[1] and s[2] == s[3]:
            if s[0] != s[2]:
                print("Yes")
            else:
                print("No")
        elif s[0] == s[2] and s[1] == s[3]:
            if s[0] != s[1]:
                print("Yes")
            else:
                print("No")
        elif s[0] == s[3] and s[1] == s[2]:
            if s[0] != s[1]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
