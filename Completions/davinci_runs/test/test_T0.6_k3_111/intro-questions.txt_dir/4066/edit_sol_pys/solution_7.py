
def main():
    _ = input()
    A = list(map(int, input().split()))
    # find minimum and second minima
    min1 = A[0]
    min2 = A[1]
    if min2 < min1:
        min1, min2 = min2, min1
    for i in range(2, len(A)):
        if A[i] < min2:
            if A[i] < min1:
                min2 = min1
                min1 = A[i]
            else:
                min2 = A[i]
    print(min1, min2)


if __name__ == "__main__":
    main()
