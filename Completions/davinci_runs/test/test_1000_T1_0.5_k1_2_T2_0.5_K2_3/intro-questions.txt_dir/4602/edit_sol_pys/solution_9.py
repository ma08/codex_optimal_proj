

def main():
    N = int(input())
    K_list = [K] * N
    K = int(input())
    x = list(map(int, input().split()))

    x_total = x + K_list
    x_total.sort()  # x_total = [0, 0, ..., K, K, ...]

    x_sort = sorted(x)
    x_sort.append(K)

    d = 0
    for i in range(N):
        d += abs(x_sort[i] - x_total[i])

    print(d)


if __name__ == "__main__":
    main()
