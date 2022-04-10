

n = int(input())
a = list(map(int, input().split()))

def solve(a):
    # sort the array
    a.sort()
    # loop over the array
    # if the next value is the same as the current value, then increment the number of pockets
    # otherwise, keep the number of pockets the same
    pockets = 1
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            pockets += 1
    return pockets

print(solve(a))