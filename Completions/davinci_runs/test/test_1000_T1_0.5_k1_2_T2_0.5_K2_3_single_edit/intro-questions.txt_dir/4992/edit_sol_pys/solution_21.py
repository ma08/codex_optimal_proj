

def main():
    """
    Safe order.
    """
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] < sum(a[1:]):
        print("impossible")
    else:
        print("1", end=" ")
        for i in range(2, n+1):
            print(i, end=" ")

if __name__ == '__main__':
    main()
