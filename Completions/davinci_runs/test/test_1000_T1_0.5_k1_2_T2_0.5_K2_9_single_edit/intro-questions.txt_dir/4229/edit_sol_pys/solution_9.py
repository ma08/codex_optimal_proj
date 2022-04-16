

n = int(input())

cnt = [0]*4
for i in range(n):
    if i % 15 == 0:
        cnt[3] += 1
    elif i % 3 == 0:
        cnt[2] += 1
    elif i % 5 == 0:
        cnt[1] += 1
    else:
        cnt[0] += 1

print(cnt)

result = 0
result += cnt[0] * i
result += cnt[1] * (i-5)
result += cnt[2] * (i-2)
result += cnt[3] * (i-15)

print(result)
