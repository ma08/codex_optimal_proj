
n = int(input())
a = list(map(int, input().split()))
a.sort()

i = 0
j = 0

count = 0
while j < n:
    while j < n and a[j] - a[i] <= 5:
        j += 1 
    count = max(count, j - i)    
    i += 1

print(count)
