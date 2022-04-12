
q = int(input())

for i in range(q):
    n,k = map(int, input().split())
    s = list(input())
    for j in range(n-1):
        if s[j] == '1' and s[j+1] == '0' and k > 0:
            s[j],s[j+1] = s[j+1],s[j]
            k -= 1
    if k > 0 and s[0] == '0':
        s[0] = '1'
        k -= 1
    if k > 0 and s[n-1] == '0':
        s[n-1] = '1'
        k -= 1
    if k > 0 and s[0] == '1' and s[n-1] == '1':
        for j in range(n-1):
            if s[j] == '0' and s[j+1] == '1' and k > 0:
                s[j],s[j+1] = s[j+1],s[j]
                k -= 1
    print(''.join(s))
