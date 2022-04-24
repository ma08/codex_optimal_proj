

n = int(input())
a = list(map(int, input().split()))

disturbed = [0]

for i in range(n):
    if a[i - 1] == a[i + 1] == 1 and a[i] == 0 and i > 1 and i < n - 1:
        disturbed.append(disturbed[-1] + 1)
    else:
        disturbed.append(disturbed[-1])
 
print(disturbed[-1])
