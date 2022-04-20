

n = int(input())
s = input()

if n % 2 == 1:
    print(0)
else:
    cnt = 0
    for i in range(n // 2):
        if s[i] == '(':
            cnt += 2
        else:
            cnt -= 2
        if cnt < 0:
            print(0)
            break
    else:
        print(cnt)
