

n, m = [int(i) for i in input().split()]

l = [int(i) for i in input().split()]

x = [int(i) for i in input().split()]

for i in range(m):
    if x[i] in l:
        print(1)
    else:
        print(0)
