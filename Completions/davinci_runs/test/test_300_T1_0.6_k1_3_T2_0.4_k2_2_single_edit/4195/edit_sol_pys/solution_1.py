

def main():
    D, N = map(int, input().split())

    if D == 0:
        print(N * 1)
    elif D == 1:
        print(N * 100)
    else:
        print(N * 10000)

if __name__ == '__main__':
    main()
