

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    min_a = min(A)
    for i in range(n):
        A[i] = A[i] - min_a
    if sum(A) % n == 0:
        print(min_a)
    else:
        print(-1)

if __name__ == "__main__":
    main()
