

n = int(input())  # number of elements
l = list(map(int, input().split()))  # list of elements

c = 0  # number of positive elements
s = 0  # sum of positive elements

for i in range(n):
    if l[i] != -1:
        s += l[i]
        c += 1

print(s/c)
