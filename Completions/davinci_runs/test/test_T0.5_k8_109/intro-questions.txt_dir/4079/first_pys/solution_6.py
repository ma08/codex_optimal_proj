

n = int(input())

for _ in range(n):
    s = input()
    if len(s) == 1:
        print("Yes")
    else:
        flag = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                flag = False
                break
            if ord(s[i+1]) - ord(s[i]) != 1:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")