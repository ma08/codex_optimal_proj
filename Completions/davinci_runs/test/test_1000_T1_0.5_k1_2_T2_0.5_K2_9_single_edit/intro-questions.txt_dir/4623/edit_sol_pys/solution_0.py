

# SOLUTION 
t = int(input())
for _ in range(t):
    n = int(input())
    weights = map(int, input().split())
    weights = list(weights)
    weights.sort()
    ans = 0
    i = 0
    j = n-1
    while i<j:
        if weights[i] + weights[j] == weights[i+1] + weights[j-1]:
            ans += 1
            i += 1
            j -= 1
        elif weights[i] + weights[j] > weights[i+1] + weights[j-1]:
            j -= 1
        else:
            i += 1
    print(ans)
