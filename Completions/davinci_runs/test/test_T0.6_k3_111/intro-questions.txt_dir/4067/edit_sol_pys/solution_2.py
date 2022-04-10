
n = int(input())
s = input()

if n % 3 == 0:
    cnt = s.count('0')
    s = s.replace('0', '')
    s = s.replace('1', '0')
    s = s.replace('2', '1')
    s = s.replace('0', '2', cnt)
    print(s)
else:
    print(-1)
