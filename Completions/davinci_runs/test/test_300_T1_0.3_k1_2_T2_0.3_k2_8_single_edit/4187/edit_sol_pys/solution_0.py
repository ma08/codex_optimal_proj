
n = int(input())
a = [int(i) for i in input().split()]

max_rest = 1
rest = 1

for i in range(n):
    if a[i] == 1:
        rest = rest + 1
    else:
        if rest > max_rest:
            max_rest = rest
        rest = 1

if rest > max_rest:
    max_rest = rest

print(max_rest)
