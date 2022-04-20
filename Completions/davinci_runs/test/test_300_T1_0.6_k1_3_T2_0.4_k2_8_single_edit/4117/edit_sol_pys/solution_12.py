import sys


n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[j] + l[k] > l[i] and l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                cnt += 1

sys.stdout.write(str(cnt))
