
n = int(input())
a = list(map(int, input().split()))

print(sum(a[i] != i + 1 for i in range(n)))
