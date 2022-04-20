

# SOLUTION

n = int(input())
a = list(map(int, input().split()))

if 1 not in a:
    print(0)
else:
    m = 0
    c = 0
    for i in a:
        if i == 1:
            c += 1
            m = max(m, c)
        else:
            c = 0
    print(m)