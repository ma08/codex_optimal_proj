

n = int(input())

s = 0

for i in range(n):
    s += int(input())
 
if s % n == 0:
    print('YES')
else:
    print('NO')
