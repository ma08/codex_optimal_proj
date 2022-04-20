

def main():
    """
    Solution
    """
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        if a[0] == a[1]:
            print(1)
            print(2)
        else:
            print(0)
            print()
    else:
        s = sum(a)
        k = 0
        for i in range(n):
            if a[i] == s - a[i]:
                k += 1
        print(k)
        for i in range(n):
            if a[i] == s - a[i]:
                print(i + 1, end=' ')
        print()


if __name__ == '__main__':
    main()