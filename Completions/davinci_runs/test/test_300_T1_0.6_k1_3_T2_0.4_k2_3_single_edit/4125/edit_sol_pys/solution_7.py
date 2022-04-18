

def main():
    # input
    n, x = map(int, input().split())
    xi = list(map(int, input().split()))

    # sort xi
    xi.sort()

    # find D
    D = 0
    for i in range(n):
        D = max(D, abs(x - xi[i]))

    print(D)

if __name__ == '__main__':
    main()
