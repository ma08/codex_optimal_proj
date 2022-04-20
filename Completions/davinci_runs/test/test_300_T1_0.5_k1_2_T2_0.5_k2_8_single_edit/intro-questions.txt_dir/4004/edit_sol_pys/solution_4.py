
def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    m = min(A)
    for i in range(n):
        A[i] = A[i] - m
    if sum(A) % n == 0:
        print(m)
    else:
        print(-1)

if __name__ == "__main__":
    main()
