

#Solution

n = int(input())
s = input()

assert(n%3 == 0)

cnt = [0]*3
for i in range(n):
    cnt[int(s[i])] += 1

for i in range(n):
    if cnt[int(s[i])] == n//3:
        continue
    for j in range(3):
        if cnt[j] < n//3:
            s = s[:i] + str(j) + s[i+1:]
            cnt[int(s[i])] += 1
            cnt[j] -= 1
            break

print(s)