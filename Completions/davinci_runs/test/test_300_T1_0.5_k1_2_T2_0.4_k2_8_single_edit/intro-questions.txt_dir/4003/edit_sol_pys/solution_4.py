

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    l = []
    r = []
    l_i = 0
    r_i = n-1
    while l_i <= r_i:
        if l_i == r_i:
            l.append(a[l_i])
        elif a[l_i] > a[l_i+1]:
            l.append(a[l_i])
            l_i += 1
        elif a[r_i] > a[r_i-1]:
            r.append(a[r_i])
            r_i -= 1
        elif a[l_i] <= a[l_i+1] and a[r_i] <= a[r_i-1]:
            break
    if len(l) >= len(r):
        print(len(l))
        print("R"*len(l))
    else:
        print(len(r))
        print("L"*len(r))
