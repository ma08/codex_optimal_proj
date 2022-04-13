

def main():
    """
    Safe order
    """
    n = int(input())
    lis = list(map(int, input().split()))
    if lis[0] < sum(lis[1:]):
        print("impossible")
    else:
        print("1", end=" ")
        for i in range(2, n+1):
            print(i, end=" ")

if __name__ == '__main__':
    main()
