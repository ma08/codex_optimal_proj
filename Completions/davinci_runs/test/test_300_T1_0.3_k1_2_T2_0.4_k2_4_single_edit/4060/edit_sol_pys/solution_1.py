
n = int(input())
s = input()

if n % 2 == 1:
    print(0)
else:
    cnt = 0
    for i in range(n):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print(0)
            break
    else:
        if cnt == 0:
            print(1)
        else:
            print(0)
