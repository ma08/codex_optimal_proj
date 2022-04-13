


def adjacent_replacement_algorithm(n, a, k):
    b = []
    for i in range(n):
        if a[i] % k == 0:
            b.append(a[i] - 1)
        else:
            b.append(a[i])
    return b


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    print(*adjacent_replacement_algorithm(n, a, k))
