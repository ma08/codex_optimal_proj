
n = int(raw_input())
s = map(int, raw_input().split())
s = sorted(s)
count = 0
for i in xrange(n):
    for j in xrange(i, n):
        if s[i] == s[j]:
            count += 1
        else:
            break
    print(count)
    count = 0
