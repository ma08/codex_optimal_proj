
n = int(input())
s = input()

if n % 2 == 1:
    print(0)
else:
    cnt = 0
    for i in range(n // 2):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
    print(cnt // 2)
