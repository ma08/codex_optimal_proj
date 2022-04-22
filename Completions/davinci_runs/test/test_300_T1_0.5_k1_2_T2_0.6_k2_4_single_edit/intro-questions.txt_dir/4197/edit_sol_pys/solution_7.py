

N = int(input())
a = [int(i) for i in input().split()]

for i in range(N):
    print(a.index(i+1)+1, end=' ')
