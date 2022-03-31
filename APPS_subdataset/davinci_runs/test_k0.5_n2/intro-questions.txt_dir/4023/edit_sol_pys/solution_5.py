n = int(input())
a = [int(i) for i in input().split()]

def is_complete(a):
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            return False
    return True

def solve(a):
    if is_complete(a):
        return "YES"
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            a[i] += 1
            a[i + 1] += 1
            if is_complete(a):
                return "YES"
            else:
                a[i] -= 1
                a[i + 1] -= 1
    return "NO"

print(solve(a))
