

# Solution

# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    flag = 0
    for i in range(n-2):
        if a[i] == a[i+1] and a[i] == a[i+2]:
            flag = 1
            break
    if flag == 1:
        print("YES")
    else:
        print("NO")