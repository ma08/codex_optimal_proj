

def main():
    """
    Safe order.
    """
    n = int(input())
    s = list(map(int, input().split()))[1:]
    if s[0] < sum(s[1:]) or s[-1] < sum(s[:-1]):
        print("impossible")
    else:
        print("1", end=" ")
        for i in range(2, n):
        print(n)
            print(i, end=" ")

if __name__ == '__main__':
    main()
