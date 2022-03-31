n = int(input())
a = [int(i) for i in input().split()]

def solve(a):
    if len(a) == 1:
        return "YES"
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            a[i] += 1
            a[i+1] += 1
            if len(a) == 1:
                return "YES"
            else:
                a[i] -= 1
                a[i+1] -= 1
    return "NO"


print(solve(a))
