
#Solution 
n = int(input())
a = [int(x) for x in input().split()]
a.sort()

suma = sum(a[::2])
sumb = sum(a[1::2])

print(suma, sumb)
