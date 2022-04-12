
def main():
    N, K = map(int, input().split())

    print(min(N % K, abs(N % K - K)))

if __name__ == '__main__':
    main()
