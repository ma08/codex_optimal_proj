

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    l = [a[0]]
    r = [a[-1]]
    l_i = 1
    r_i = -2
    while l_i < r_i:
        if a[l_i] > l[-1]:
            l.append(a[l_i])
            l_i += 1
        if a[r_i] > r[-1]:
            r.append(a[r_i])
            r_i -= 1
        if a[l_i] <= l[-1] and a[r_i] <= r[-1]:
            break
    if len(l) > len(r):
        print(len(l))
        print("L" * len(l))
    else:
        print(len(r))
        print("R" * len(r))
