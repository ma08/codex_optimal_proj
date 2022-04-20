

N = int(input())
p = list(map(int, input().split()))

if N == 2:
    if p[0] > p[1]:
        print("YES")
    else:
        print("NO")
else:
    # find the first element that is not in order
    for i in range(N-1):
        if p[i] > p[i+1]:
            break

    # find the last element that is not in order
    for j in range(N-1, i, -1):
        if p[j] < p[j-1]:
            break

    # check if the elements in between are in order
    for k in range(i, j+1):
        if p[k] > p[k+1]:
            print("NO")
            exit()

    # check if the elements before the first element are in order
    for k in range(i):
        if p[k] > p[j]:
            print("NO")
            exit()

    # check if the elements after the last element are in order
    for k in range(j+1, N):
        if p[k] < p[i]:
            print("NO")
            exit()

    print("YES")
