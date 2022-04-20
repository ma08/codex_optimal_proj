
def main():
    n = int(input())  # input number of integers
    a = list(map(int, input().split()))  # input numbers
    a.sort()  # sort numbers
    if n % 2 == 0:  # if n is even
        if a[0] == a[-1]:  # if the first and last number is equal
            print(0)  # print 0
        else:  # if the first and last number is not equal
            print(-1)  # print -1
    else:
        if a[0] == a[-1]:
            print(0)
        else:
            if a[0] + 1 == a[-1]:
                print(1)
            else:
                print(-1)

if __name__ == '__main__':
    main()
