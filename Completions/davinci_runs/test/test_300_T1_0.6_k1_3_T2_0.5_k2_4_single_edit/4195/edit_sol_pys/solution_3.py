
def main():
    D, N = map(int, input().split())  # D: 0, 1, 2, N: 1

    if N == 100:
        N += 1

    if D == 0:  # D == 0
        print(N)  # N
    elif D == 1:  # D == 1
        print(100 * N)  # 100 * N
    else:  # D == 2
        print(10000 * N)  # 10000 * N

if __name__ == '__main__':
    main()
