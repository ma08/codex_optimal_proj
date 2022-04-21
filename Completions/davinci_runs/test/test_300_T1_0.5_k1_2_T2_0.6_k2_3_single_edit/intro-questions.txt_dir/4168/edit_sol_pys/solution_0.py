
n = int(input())

if n == 0:
    print(0)
    exit()
ans = ""
while n != 0:
    if n % (-2) == 0:
        ans += "0"
        n = n // (-2)
    else:
        ans += "1"
        n = n // (-2) + 1

print(ans[::-1])
