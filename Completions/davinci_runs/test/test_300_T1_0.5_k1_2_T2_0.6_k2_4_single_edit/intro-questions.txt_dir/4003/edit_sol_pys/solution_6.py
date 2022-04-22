

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    l = [a[0], 1]
    r = [a[n-1], 1]
    l_i = 1
    r_i = n-2
    while l_i < r_i:
        if a[l_i] > l[-2]:
            l[-1] += 1
            l_i += 1
        if a[r_i] > r[-2]:
            r[-1] += 1
            r_i -= 1
        if a[l_i] <= l[-2] and a[r_i] <= r[-2]:
            break
    if l[-1] > r[-1]:
        print(l[-1])
        print("L"*l[-1])
    else:
        print(r[-1])
        print("R"*r[-1])
