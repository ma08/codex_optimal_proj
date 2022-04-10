

# cook your dish here

n = int(input())
a = list(map(int, input().split()))

yes = True

for i in range(n-1):
    if abs(a[i]-a[i+1]) >= 2:
        yes = False
        break

if yes:
    print("YES")
else:
    print("NO")