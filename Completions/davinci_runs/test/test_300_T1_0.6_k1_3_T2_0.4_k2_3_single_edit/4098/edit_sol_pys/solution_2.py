

def solve(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

a = list(map(int, input().split()))
print(solve(a))
