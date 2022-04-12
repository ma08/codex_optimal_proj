
t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    w.sort()
    ans = 0
    i = 0
    j = n-1
    while i<j:
        if w[i] + w[j] == w[i+1] + w[j-1]:
            ans += 1
            i += 1
            j -= 1
        elif w[i] + w[j] > w[i+1] + w[j-1]:
            j -= 1
        else:
            i += 1
    print(ans)
