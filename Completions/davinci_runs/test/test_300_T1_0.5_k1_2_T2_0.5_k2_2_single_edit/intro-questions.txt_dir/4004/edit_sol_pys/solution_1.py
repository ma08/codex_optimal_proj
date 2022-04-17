
def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    B = []
    for i in range(n-1):
        B.append(A[i+1] - A[i])
    D = min(B)
    for i in range(n-1):
        A[i] = A[i] + D
    if sum(A) % n == 0:
        print(D)
    else:
        print(-1)

if __name__ == "__main__":
    main()
