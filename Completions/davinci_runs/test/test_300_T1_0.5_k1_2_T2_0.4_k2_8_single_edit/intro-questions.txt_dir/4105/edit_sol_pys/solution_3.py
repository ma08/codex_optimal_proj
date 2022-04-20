

n = int(input())

a = [int(x) for x in input().split()]

a.sort(reverse=True)

print(a[0]*a[1])
