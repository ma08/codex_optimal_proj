

def main():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))

    x_a = [0] * N
    x_b = [K] * N
    x_total = x_a + x
    x_total.sort()

    x_sort = sorted(x)
    x_sort.append(K + 1)

    d = 0
    for i in range(N):
        d += abs(x_sort[i] - x_total[i])

    print(d)


if __name__ == "__main__":
    main()
