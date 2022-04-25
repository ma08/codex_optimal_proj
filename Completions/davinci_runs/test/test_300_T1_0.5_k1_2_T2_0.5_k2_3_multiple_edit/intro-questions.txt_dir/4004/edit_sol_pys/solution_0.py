def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    D = min(A)
    for i in range(n):
        A[i] = A[i] - D
    if sum(A) % n == 0:
        print(D)
    else:
        print(-1)
if __name__ == "__main__":
    main()
