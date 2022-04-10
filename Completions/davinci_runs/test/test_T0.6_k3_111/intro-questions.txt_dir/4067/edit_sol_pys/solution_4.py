
n = int(input())
s = input()

if n % 3 == 0:
    cnt = s.count('0')
    z = s.replace('0', '')
    z = z.replace('1', '0')
    z = z.replace('2', '1')
    z = z.replace('0', '2', cnt)
    print(z, end='')
else:
    print(-1)
