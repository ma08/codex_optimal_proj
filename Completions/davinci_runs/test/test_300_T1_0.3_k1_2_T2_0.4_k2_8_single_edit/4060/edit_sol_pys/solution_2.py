

n = int(input())
s = input()
cnt = 0
if n % 2 == 1:
    print(0)
else:
    for i in range(n):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print(0)
            break
    else:
        print(cnt // 2)
