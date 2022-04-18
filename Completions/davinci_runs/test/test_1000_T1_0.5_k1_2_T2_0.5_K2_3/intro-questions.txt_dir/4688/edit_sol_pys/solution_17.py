n = int(input())
a = [int(i) for i in input().split()]
for i in range(1, n - 1): 
    if a[i - 1] < a[i] > a[i + 1]:
        print(i + 1) 
        break 
else: 
    print(-1) 
