

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    l = [a[0]]
    r = [a[n-1]]
    l_idx = 1
    r_idx = n-2
    while l_idx < r_idx:
        if a[l_idx] > l[-1]:
            l.append(a[l_idx])
            l_idx += 1
        if a[r_idx] > r[-1]:
            r.append(a[r_idx])
            r_idx -= 1
        if a[l_idx] <= l[-1] and a[r_idx] <= r[-1]:
            break
    if len(l) > len(r):
        print(len(l))
        print("L"*len(l))
    else:
        print(len(r))
        print("R"*len(r))
