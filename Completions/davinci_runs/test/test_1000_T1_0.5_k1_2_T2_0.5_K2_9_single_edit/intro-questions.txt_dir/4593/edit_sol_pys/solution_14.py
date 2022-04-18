

x = int(input())

for i in range(2, x+1):
    if i**2 <= x:
        ans = i**2
    else:
        break

print(ans)
