

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    D = max(A)
    for i in range(n):
        A[i] = D - A[i]
    if sum(A) % n == 0:
        print(D)
    else:
        print(-1)

if __name__ == "__main__":
    main()
