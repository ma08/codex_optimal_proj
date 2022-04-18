

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    d = min(A)  # d is the smallest number in the given array
    for i in range(n):
        A[i] = A[i] - d
    if sum(A) % n == 0:
        print(d)
    else:
        print(-1)

if __name__ == "__main__":
    main()
