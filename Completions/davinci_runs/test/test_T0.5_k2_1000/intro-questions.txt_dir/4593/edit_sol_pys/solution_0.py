
x = int(input())

for i in range(2, x):
    if i**2 <= x:
        ans = i**2
    else:
        break

print(ans)
