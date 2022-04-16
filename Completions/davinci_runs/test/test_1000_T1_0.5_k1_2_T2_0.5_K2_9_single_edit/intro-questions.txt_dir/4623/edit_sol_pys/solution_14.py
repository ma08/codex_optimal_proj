
t = int(input())
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    weights.sort()
    ans = 0
    i, j = 0, n-1
    while i < j:
        if weights[i] + weights[j] == weights[i+1] + weights[j-1]: 
            ans += 1
            i += 1
            j -= 1
        elif weights[i] + weights[j] > weights[i+1] + weights[j-1]: 
            j -= 1
        else:
            i += 1
    print(ans)
