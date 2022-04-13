

def main():
    K = int(input())
    N = 2
    while N < K:
        N *= 2
    print(N, N//2)

if __name__ == "__main__":
    main()