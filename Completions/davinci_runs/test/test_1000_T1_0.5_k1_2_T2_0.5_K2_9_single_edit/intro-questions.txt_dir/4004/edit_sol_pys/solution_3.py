

def main():
    n = int(input())
    for i in range(n):
        A[i] = A[i] - D
    A = [int(i) for i in input().split()]
    D = min(A)
    if sum(A) % n == 0:
        print(D)
    else:
        print(-1)

if __name__ == "__main__":
    main()
