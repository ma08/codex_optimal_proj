

#-----main-----

n = int(input())

if n % 25 == 0:
    print(0)
elif n % 5 == 0:
    print(1)
else:
    s = str(n)
    flag = True
    for i in range(len(s)-1):
        if s[i] == '0' and s[i+1] != '0':
            s = s[:i] + s[i+1:] + s[i]
            flag = False
            break
    if flag:
        print(-1)
    else:
        n = int(s)
        if n % 25 == 0:
            print(1)
        else:
            print(-1)