

def main():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))

    x_a = [0] * N
    x_copy = x[:]
    x_copy.sort()

    d = 0
    for i in range(N):
        d += abs(x_copy[i] - x_a[i])

    x_copy.append(K)
    x_copy.sort()

    for i in range(N):
        d += abs(x_copy[i] - x_a[i])

    print(d)


if __name__ == "__main__":
    main()
