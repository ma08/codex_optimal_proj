

def solve(n, k, a):
    a.sort()
    a.append(a[-1] + 5) # append a dummy element to the end of the array
    #print(a)
    cnt = 0
    for i in range(n):
        if i == 0 or a[i] - a[i-1] > 5:
            cnt += 1
            if cnt == k + 1:
                return i
    return n

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
