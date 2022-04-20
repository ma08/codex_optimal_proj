

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    D = max(A)
    for i in range(n):
        A[i] = D - A[i]
    print(sum(A))

if __name__ == "__main__":
    main()
