
def main():
    n = int(input())  # number of elements
    a = [int(x) for x in input().split()]  # input the array
    d = [a[i] - a[i - 1] for i in range(1, n)]  # find the difference between each element
    d.sort()  # sort to find the minimum and maximum difference
    if d[0] == d[-1]:  # if the difference is same then there is no way to change the order
        print(0)  # print 0
    else:  # else
        print(2)  # print 2

if __name__ == '__main__':
    main()
