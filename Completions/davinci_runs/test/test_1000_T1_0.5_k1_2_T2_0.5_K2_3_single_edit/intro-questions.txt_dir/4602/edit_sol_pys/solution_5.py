

def main():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))

    x_total = [0] * N + [K] * N
    x_total.sort()

    x_sort = sorted(x)


    d = abs(x_sort[0] - x_total[0])
    for i in range(N):
        d += abs(x_sort[i] - x_total[i])

    print(d)


if __name__ == "__main__":
    main()
