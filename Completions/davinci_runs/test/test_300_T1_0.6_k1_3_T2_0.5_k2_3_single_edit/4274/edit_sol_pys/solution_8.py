
a = int(input())
b = int(input())
c = int(input())
x = int(input())
cnt = 0
for ai in range(a + 1):
    for bi in range(b + 1):
        for ci in range(c + 1):
            if 500 * ai + 100 * bi + 50 * ci == x:
                cnt += 1
print(cnt)
