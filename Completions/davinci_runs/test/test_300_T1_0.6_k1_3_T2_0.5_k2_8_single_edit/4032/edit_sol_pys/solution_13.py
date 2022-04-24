
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]


def solve(a, n, k):
    solved = 0
    i, j = 0, n-1
    while i <= j:
        solved += 1
        if a[i] <= k and a[j] <= k:
            if a[i] < a[j]:
                i += 1
            elif a[i] > a[j]:
                j -= 1
            else:
                i += 1
        elif a[i] > k and a[j] <= k:
            j -= 1
        elif a[i] <= k and a[j] > k:
            i += 1
        else:
            break
    print(solved)


if __name__ == '__main__':
    solve(a, n, k)
