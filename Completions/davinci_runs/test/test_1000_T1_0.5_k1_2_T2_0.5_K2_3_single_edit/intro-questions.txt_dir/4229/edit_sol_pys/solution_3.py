

n = int(input())

# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# 1,2,0,4,0,0,7,8,0,0,11,0,13,14,0,16,0,18,0,0

cnt = [0,0,0,0]
for i in range(n):
    if i % 3 == 0:
        cnt[0] += 1
    if i % 5 == 0:
        cnt[1] += 1
    if i % 7 == 0:
        cnt[2] += 1
    if i % 15 == 0:
        cnt[3] += 1    

print(cnt)

result = 0
result += cnt[0] * (i-2)
result += cnt[1] * (i-5) + cnt[3] * (i-15)
result += cnt[2] * (i-7)

print(result)
