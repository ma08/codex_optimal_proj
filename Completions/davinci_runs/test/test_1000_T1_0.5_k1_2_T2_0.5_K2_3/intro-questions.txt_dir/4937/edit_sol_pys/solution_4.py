

n, a = map(int, input().split())
e = list(map(int, input().split()))

e.sort()

# print(e)

i = 0
j = n-1

res = 0

while i <= j:
    if e[i] >= e[j]:
        if a >= e[i]:
            a -= e[i]
            e[i] = 0
            i += 1
        else:
            break
    else:
        if a >= e[j]:
            a -= e[j]
            e[j] = 0
            j -= 1
        else:
            break

# print(e)

for i in range(n):
    if e[i] == 0:
        res += 1

print(res)
