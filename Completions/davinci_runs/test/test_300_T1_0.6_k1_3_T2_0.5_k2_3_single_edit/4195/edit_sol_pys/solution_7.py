
def main():
    D, N = map(int, input().split())

    if D == 0:
        print(N+1)
    elif D == 1:
        print(100 * (N+1))
    else:
        print(10000 * (N+1))

if __name__ == '__main__':
    main()
