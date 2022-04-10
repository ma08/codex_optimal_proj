
def solve(n, a):
    disturbed = []
    for i in range(1, n - 1):
        if a[i - 1] == a[i + 1] == 1 and a[i] == 0:
            disturbed.append(i)

    if len(disturbed) == 0:
        return 0
    if len(disturbed) == 1:
        return 1
    else:
        for i in range(len(disturbed)):
            for j in range(i + 1, len(disturbed)):
                if a[disturbed[i] - 1] == a[disturbed[j] - 1] == 1 and a[disturbed[i]] == 0:
                    return 2
                if a[disturbed[i] + 1] == a[disturbed[j] + 1] == 1 and a[disturbed[i]] == 0:
                    return 2
        return 3


n = int(input())
a = list(map(int, input().split()))[:n]
print(solve(n, a))
