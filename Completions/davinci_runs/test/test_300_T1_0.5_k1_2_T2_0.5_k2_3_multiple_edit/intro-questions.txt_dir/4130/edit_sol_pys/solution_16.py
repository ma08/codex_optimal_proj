'''
n = int(input())
a = list(map(int, input().split()))
'''
a = [1, 2, 3, 2, 1, 2, 3]
n = len(a)

a.sort() # [1, 1, 2, 2, 2, 3, 3]

a.sort()

count = 1
for i in range(1, n):
    if a[i] != a[i-1]:
        count += 1

print(count)
