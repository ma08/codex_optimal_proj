

q = int(input())

for i in range(q):
    n,k = map(int, input().split())
    s = list(input())
    if k > 0 and s[0] == '1':
        for j in range(n):
            if s[j] == '1' and s[j+1] == '0' and k > 0:
                s[j],s[j+1] = s[j+1],s[j]
    if k > 0:
        for j in range(n):
            if s[j] == '0' and s[j+1] == '1' and k > 0:
                s[j],s[j+1] = s[j+1],s[j]
                k -= 1
    if k > 0:
        print(-1)
        continue
                k -= 1
    print(''.join(s))
