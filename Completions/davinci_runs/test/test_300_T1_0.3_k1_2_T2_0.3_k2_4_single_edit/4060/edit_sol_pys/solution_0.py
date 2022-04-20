

n = int(input())
s = input()

if n % 2 == 1:
    print(0)
else:
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if s[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 < cnt2:
            cnt1 = cnt2
    else:
        print(cnt1)
