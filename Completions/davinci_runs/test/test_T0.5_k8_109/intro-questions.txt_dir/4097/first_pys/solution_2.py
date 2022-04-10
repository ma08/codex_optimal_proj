

n = int(input())
lst = [int(x) for x in input().split()]

def solve(n, lst):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    else:
        d = lst[1] - lst[0]
        for i in range(1, n-1):
            if d != lst[i+1] - lst[i]:
                return -1
        return 0


print(solve(n, lst))