

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

result = 0
result += cnt[0] * (i+1)
result += cnt[1] * (i+1-5)
result += cnt[2] * (i+1-2)
result += cnt[3] * (i+1-15)

print(result)
