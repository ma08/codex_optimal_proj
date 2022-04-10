

def minCost(n, k, s):
    cost = 0
    for i in range(n):
        if s[i] == '1':
            cost += i + 1
        else:
            if i - k >= 0 and s[i - k] == '1':
                cost += i + 1
            elif i + k < n and s[i + k] == '1':
                cost += i + 1
            else:
                cost += i + 1
                if i + 1 < n and s[i + 1] == '1':
                    s[i + 1] = '0'
    return cost


n, k = map(int, input().split())
s = list(input())
print(minCost(n, k, s))