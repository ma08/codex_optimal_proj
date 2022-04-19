

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    l = [a[0]]  # left
    r = [a[n-1]]  # right
    l_i = 1  # left index
    r_i = n-2  # right index
    while l_i < r_i:
            # if the number is bigger than the biggest number in left, append the number to left
        if a[l_i] > l[-1]:
            l.append(a[l_i])
            l_i += 1
            # if the number is bigger than the biggest number in right, append the number to right
        if a[r_i] > r[-1]:
            r.append(a[r_i])
            r_i -= 1
        # if both numbers are smaller than the biggest numbers in left and right, break the loop
        if a[l_i] <= l[-1] and a[r_i] <= r[-1]:
            break
    # if left has more elements, print left
    if len(l) > len(r):
        print(len(l))
        print("L"*len(l))
    else:
        # if right has more elements, print right
        print(len(r))
        print("R"*len(r))
