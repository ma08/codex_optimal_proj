

n = int(input())
s = input()

if n % 2 == 1:
    print(0)
else:
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print(0)
            break
    else:
        print(cnt // 2)
