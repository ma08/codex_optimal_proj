
n = int(input())

ans = []
while n != 0:
    if n % (-2) == 0:
        ans.append(0)
        n = n // (-2)
    else:
        ans.append(1)
        n = n // (-2) + 1

print(ans[::-1])
