

n = int(input())
s = list(input())

cnt = 0
for i in range(1, n):
    if s[i-1] == '1' and s[i] == '0':
        cnt += 1
        s[i] = '1'
print(cnt)