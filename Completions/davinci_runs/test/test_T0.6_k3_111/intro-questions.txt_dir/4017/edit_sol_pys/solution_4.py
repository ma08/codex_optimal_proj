n = int(input()) # number of elements
a = list(map(int, input().split())) # list of elements
total = sum(a) # sum of all elements

count = 0
for i in range(n):
    if a[i] == total-a[i]:
        count += 1
        print(i+1, end=' ')
if not count:
    print(count)
