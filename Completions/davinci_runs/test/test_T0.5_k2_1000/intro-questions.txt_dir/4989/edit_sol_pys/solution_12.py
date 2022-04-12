
n = int(input())
a = [int(x) for x in input().split()]
a.sort()

suma = sum(a[::2]) # sum of even elements
sumb = sum(a[1::2]) # sum of odd elements

print(suma, sumb)
