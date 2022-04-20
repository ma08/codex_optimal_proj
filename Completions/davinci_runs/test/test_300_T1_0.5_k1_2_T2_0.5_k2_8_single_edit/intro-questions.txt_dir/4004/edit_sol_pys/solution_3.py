

    """
    n = int(input())
    A = [int(i) for i in input().split()]
    D = min(A)
    for i in range(n):
        A[i] = A[i] - D
    if sum(A) % n == 0:
        print(D)
    else:
        print(-1)
    """
    # another way
def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    if sum(A) % n == 0: # if sum(A) can be divided by n
        print(A[0])
    else: # if sum(A) can not be divided by n
        print(-1) # print -1

if __name__ == "__main__":
    main()
