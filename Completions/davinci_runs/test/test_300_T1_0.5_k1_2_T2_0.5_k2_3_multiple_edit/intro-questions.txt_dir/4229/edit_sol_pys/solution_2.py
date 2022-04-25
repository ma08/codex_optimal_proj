

n = int(input())

# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
# 1,2,0,4,0,0,7,8,0,0,11,0,13,14,0,16,0,18,0,0,22,0,23,24,0,26,0,28,29,0

cnt = [0,0,0,0,0]
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
