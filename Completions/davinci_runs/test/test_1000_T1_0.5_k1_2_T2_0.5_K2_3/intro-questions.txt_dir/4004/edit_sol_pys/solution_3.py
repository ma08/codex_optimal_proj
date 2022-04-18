
def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    D = min(A)
    for i in range(n):
        A[i] = A[i] - D  # subtract the smallest number from each element of the array
    if sum(A) % n == 0:
        print(D)  # if the sum of the array is divisible by n, print D
    else:
        print(-1)  # else print -1

if __name__ == "__main__":
    main()
