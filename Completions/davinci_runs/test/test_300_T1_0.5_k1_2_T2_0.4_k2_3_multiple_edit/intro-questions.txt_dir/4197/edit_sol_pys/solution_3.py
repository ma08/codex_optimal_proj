
n = int(input())
a = [int(i) for i in input().split()]

for i in range(n):
    print(a.index(i+1)+1, end=' ')
