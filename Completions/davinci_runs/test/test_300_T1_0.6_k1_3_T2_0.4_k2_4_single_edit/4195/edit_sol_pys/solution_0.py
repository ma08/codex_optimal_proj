

def main():
    D, N = map(int, input().split())

    if D == 0:
        print(N, end="")
    elif D == 1:
        print(100 * N, end="")
    else:
        print(10000 * N, end="")

if __name__ == '__main__':
    main()
