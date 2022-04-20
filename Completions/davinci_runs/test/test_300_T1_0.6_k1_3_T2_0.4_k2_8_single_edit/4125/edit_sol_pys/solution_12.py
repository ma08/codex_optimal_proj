

def main():
    # input
    n, x = map(int, input().split())
    xi = list(map(int, input().split()))[:n]

    # sort xi
    xi.sort()

    # find D
    D = 0
    for i in range(1, n+1):
        D = max(D, abs(x - xi[i-1]))

    print(D)

if __name__ == '__main__':
    main()
