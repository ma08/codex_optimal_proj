

def main():
    # input number
    N = int(input())
    # input sequence
    A = list(map(int, input().split()))

    # initialize
    count = 0

    # count number of even numbers
    for i in range(N):
        if A[i] % 2 == 0:
            count += 1

    # output
    print(count)

if __name__ == '__main__':
    main()
