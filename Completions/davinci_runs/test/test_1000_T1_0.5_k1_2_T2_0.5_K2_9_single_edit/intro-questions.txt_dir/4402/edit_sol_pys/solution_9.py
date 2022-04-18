
n = int(input())
if n == 0:
    print(0)
    exit()
ans = ''
while n != 0:
    ans = str(n % 2) + ans
    n = -(-n // 2)
print(ans)
