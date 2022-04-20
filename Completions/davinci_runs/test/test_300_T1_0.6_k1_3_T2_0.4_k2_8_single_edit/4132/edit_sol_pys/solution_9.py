

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))

    # sort
    A.sort()

    # compute
    while len(A) > 1:
        A = A[:-2] + [A[-1] - A[-2]]

    # output
    print(A[0])


if __name__ == '__main__':
    main()
