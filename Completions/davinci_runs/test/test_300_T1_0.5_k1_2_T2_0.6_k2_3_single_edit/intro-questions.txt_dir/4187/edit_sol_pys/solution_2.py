
n = int(input())
a = list(map(int, input().split()))

max_rest = -1
rest = 0

for i in a:
    if i == 0:
        if max_rest < rest:
            max_rest = rest
        rest = 0
    else:
        rest += 1

if max_rest < rest:
    max_rest = rest

print(max_rest)
