def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))


    # initialization
    ans = 0

    # loop
    for i in range(n):
        # find the number of operations
        cnt = 0
        while a[i] % 2 == 0:
            cnt += 1
            a[i] //= 2

    # count the number of characters different between s and t
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    # output
    print(count)

if __name__ == '__main__':
    main()
