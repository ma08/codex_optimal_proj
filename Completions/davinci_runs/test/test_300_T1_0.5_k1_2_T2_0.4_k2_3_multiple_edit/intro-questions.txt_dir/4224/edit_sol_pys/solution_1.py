
n = int(input())
a = list(map(int, input().split()))

count = 0 

for i in range(n):
    while a[i] % 2 == 0:
        a[i] //= 2
        count += 1 

print(count)
