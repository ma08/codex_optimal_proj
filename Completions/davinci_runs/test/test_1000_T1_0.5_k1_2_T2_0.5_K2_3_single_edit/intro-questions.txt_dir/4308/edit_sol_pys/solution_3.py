

def main():
    N, K = map(int, input().split())

    if N > K:
        print(abs(N - K))
    else:
        print(0)

if __name__ == '__main__':
    main()
