

n = int(input())

cnt = [0,0,0,0,0]
for i in range(n):
    if (i+1) % 15 == 0:
        cnt[3] += 1
    elif (i+1) % 3 == 0:
        cnt[2] += 1
    elif (i+1) % 5 == 0:
        cnt[1] += 1
    else:
        cnt[0] += 1

print(cnt)

result = 0
result += cnt[0] * n
result += cnt[1] * (n-5)
result += cnt[2] * (n-2)
result += cnt[3] * (n-15)

print(result)
