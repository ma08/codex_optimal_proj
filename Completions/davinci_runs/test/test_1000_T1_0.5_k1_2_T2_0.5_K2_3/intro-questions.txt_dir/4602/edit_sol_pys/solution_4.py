

def main():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))

    x_sort = sorted(x)
    x_sort.append(K)
    x_sort.sort()

    x_a = [0] * (N + 1)
    x_b = [K] * (N + 1)
    x_total = x_a + x_b
    x_total.sort()

    d = 0
    for i in range(N):
        d += abs(x_sort[i] - x_total[i])

    print(d)


if __name__ == "__main__":
    main()
