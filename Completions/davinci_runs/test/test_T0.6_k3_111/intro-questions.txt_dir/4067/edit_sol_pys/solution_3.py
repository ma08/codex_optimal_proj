
n = int(input())
s = input()

if n % 3 == 0:
    cnt = s.count('0')
    z = s.replace('0', '', cnt)
    z = z.replace('1', '0', cnt)
    z = z.replace('2', '1', cnt)
    z = z.replace('0', '2')
    print(z)
else:
    print(-1)
