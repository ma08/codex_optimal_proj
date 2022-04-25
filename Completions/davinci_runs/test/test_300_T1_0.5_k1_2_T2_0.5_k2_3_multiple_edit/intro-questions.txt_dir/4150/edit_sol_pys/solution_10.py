
n, k = input().split() 
a = list(map(int, input().split())) 
a = [0] + a + [n + 1] 
a.sort() 
ans = [0] * (n + 2) 
for i in range(1, n + 2): 
    left = a[i - 1] + k 
    right = a[i] - k - 1 
    if left <= right: 
        ans[left] += 1 
        ans[right + 1] -= 1 
for i in range(1, n + 1): 
    ans[i] += ans[i - 1] 
ans = ans[1:] 
print(''.join(map(str, ans))) 
