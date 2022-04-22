n = int(input())

if n == 0:
    print(0)
    exit()
ans = ""
while n:
    ans += str(n % -2)
    n //= -2
print(ans[::-1])
