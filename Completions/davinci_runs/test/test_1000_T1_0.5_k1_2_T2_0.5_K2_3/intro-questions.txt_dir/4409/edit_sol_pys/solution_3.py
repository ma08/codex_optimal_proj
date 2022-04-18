

t = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(1, t-1):
    if a[i] < a[i-1]:
        a[i] = a[i] + abs(a[i]-a[i-1])
        print(1, i+1, i)
        c += 1
    elif a[i] < a[i+1]:
        a[i] = a[i] + abs(a[i]-a[i+1])
        print(1, i+1, i+2)
        c += 1
    elif a[i] > a[i-1]:
        a[i] = a[i] - abs(a[i]-a[i-1])
        print(2, i+1, i)
        c += 1
    elif a[i] > a[i+1]:
        a[i] = a[i] - abs(a[i]-a[i+1])
        print(2, i+1, i+2)
        c += 1
print(c) 
