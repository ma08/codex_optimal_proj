

def check(num):
    temp = num
    while temp > 0:
        if temp % 10 == 7:
            return True
        temp //= 10
    return False

n = int(input()) % (10 ** 9 + 7)

ans = 0
for i in range(1, n+1):
    if check(i):
        ans += i

print(ans)
