

def main():
    """
    Safe order.
    """
    n = int(input())
    s = list(map(int, input().split()))
    if s[0] < sum(s[1:]):
        print("impossible")
    else:
        print("1", end=" ")
        for i in range(2, n+1):
            print(i, end=" ")

if __name__ == '__main__':
    main()