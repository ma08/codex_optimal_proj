import sys
input = sys.stdin.readline


n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort(reverse=True)

print(sum([a[i] * b[i] for i in range(n)]))
