
# n = int(input())
# a = list(map(int, input().split()))

n = 10
a = [1, 1, 0, 1, 1, 0, 1, 0, 1, 0]

def if_disturbed(i, a):
    if i == 0:
        return (a[i] == 0 and a[i+1] == 1)
    elif i == n-1:
        return (a[i] == 0 and a[i-1] == 1)
    else:
        return (a[i-1] == 1 and a[i+1] == 1 and a[i] == 0)

def solve(n, a):
    count = 0
    for i in range(n):
        count += if_disturbed(i, a)
    return count

print(solve(n,a))