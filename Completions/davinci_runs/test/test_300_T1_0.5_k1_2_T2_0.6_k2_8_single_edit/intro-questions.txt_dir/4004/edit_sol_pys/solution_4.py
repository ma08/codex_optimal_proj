

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    D = min(A) - 1
    for i in range(n):
        A[i] = A[i] - D*(i+1)
    if sum(A) % n == 0:
        print(D*(n+1))
    else:
        print(-1)

if __name__ == "__main__":
    main()
