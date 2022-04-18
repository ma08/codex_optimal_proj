

def main():
    N, K = list(map(int, input().split()))

    ans = (N % K)
    print(ans)

if __name__ == '__main__':
    main()
