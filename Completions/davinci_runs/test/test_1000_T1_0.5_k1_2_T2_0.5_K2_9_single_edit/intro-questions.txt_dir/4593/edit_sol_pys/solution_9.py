

x = int(input())

for i in range(2, x+1):
    for j in range(2, x):
        if i**j <= x:
            ans = i**j
        else:
            break

print(ans)
