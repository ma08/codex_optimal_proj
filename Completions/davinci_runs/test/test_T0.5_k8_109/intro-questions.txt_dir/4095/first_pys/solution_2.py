

def main(N, M, P):
    # sort the array
    P = sorted(P)
    # get the median
    median = P[(N-1)//2]
    # count the number of instances of the median
    count = P.count(median)
    # get the number of pairs
    pairs = count*(count-1)//2
    print(pairs)


if __name__ == '__main__':
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    main(N, M, P)