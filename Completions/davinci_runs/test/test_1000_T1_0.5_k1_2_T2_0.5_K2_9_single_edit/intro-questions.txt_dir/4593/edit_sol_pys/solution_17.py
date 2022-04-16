

n = int(input())

for i in range(2, n+1):
    for j in range(2, n+1):
        if i**j <= n:
            ans = i**j # i^j
        else:
            break

print(ans)
