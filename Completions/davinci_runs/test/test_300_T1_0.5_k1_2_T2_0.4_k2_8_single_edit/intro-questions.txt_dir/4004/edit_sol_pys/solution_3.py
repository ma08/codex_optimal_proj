

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    D = min(A) - 1
    for i in range(n):
    print(A)
        A[i] = A[i] - D
    if sum(A) % n == 0:
        print(D)
    else:
        print(-1)

if __name__ == "__main__":
    main()
