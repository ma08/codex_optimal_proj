
n, m = map(int, input().split())

a = [int(i) for i in input().split()] 
b = [int(i) for i in input().split()] 

count = 0

if m%2 == 0:
    for i in range(n):
        if a[i]%2 == 0:
            count += 1
else:
    for i in range(n):
        if a[i]%2 == 1:
            count += 1

print(count/n)
