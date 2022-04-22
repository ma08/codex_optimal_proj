

n, k = map(int, input().split())

a = list(map(int, input().split())) # get the array

a.sort() # sort the array

moves = 0 # initialize the moves

if k == n:
    print(a[-1] - a[0])
else:
    while a[-1] != a[0]:
        a[-1] -= 1
        a[0] += 1
        moves += 1
        a.sort()
    print(moves)
