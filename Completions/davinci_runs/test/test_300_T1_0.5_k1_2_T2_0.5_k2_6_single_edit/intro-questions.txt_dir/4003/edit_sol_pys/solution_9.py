

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    l = [a[0]]
    r = [a[n-1]]
    i = 1
    j = n-2
    while i < j:
        if a[i] > l[-1]:
            l.append(a[i])
            i += 1
        if a[j] > r[-1]:
            r.append(a[j])
            j -= 1
        if a[i] <= l[-1] and a[j] <= r[-1]:
            break
    if len(l) > len(r):
        print(len(l))
        print("L"*len(l))
    else:
        print(len(r))
        print("R"*len(r))
