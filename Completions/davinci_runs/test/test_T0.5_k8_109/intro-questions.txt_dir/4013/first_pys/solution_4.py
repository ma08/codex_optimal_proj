

n = int(input())
a = [int(i) for i in input().split()]

print(max(a) - min(a) - max([abs(a[i] - a[i+1]) for i in range(n-1)]) - min([abs(a[i] - a[i+1]) for i in range(n-1)]))