

def solve(n, a):
    disturbed_indexes = []
    for i in range(1, n - 1):
        if a[i - 1] == a[i + 1] == 1 and a[i] == 0:
            disturbed_indexes.append(i)

    if len(disturbed_indexes) == 0:
        return 0
    if len(disturbed_indexes) == 1:
        return 1
    else:
        for i in range(len(disturbed_indexes)):
            for j in range(i + 1, len(disturbed_indexes)):
                if a[disturbed_indexes[i] - 1] == a[disturbed_indexes[j] - 1] == 1 and a[disturbed_indexes[i] - 1] == 0:
                    return 2
                if a[disturbed_indexes[i] + 1] == a[disturbed_indexes[j] + 1] == 1 and a[disturbed_indexes[i]] == 0:
                    return 2
        return 3


n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
