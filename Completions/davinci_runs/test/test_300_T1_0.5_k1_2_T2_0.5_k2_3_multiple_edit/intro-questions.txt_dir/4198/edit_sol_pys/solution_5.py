
def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % K == 0:
                count += 1

    print(count)

if __name__ == "__main__":
    main()
