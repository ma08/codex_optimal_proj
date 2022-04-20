

def main():
    n = int(input())  # number of elements
    x = list(map(int, input().split()))  # elements
    m = min(x)  # minimum element
    x = [i - m for i in x]  # subtract minimum element from all elements
    x.sort()  # sort elements
    s = sum(x)  # sum of all elements
    if s % n:  # if sum is not divisible by number of elements
        print(-1)  # not possible
    else:  # if sum is divisible by number of elements
        s //= n  # average of all elements
        if x[0] == x[-1]:  # if all elements are equal
            print(0)  # no moves required
        else:  # if all elements are not equal
            c = 0  # count
            for i in x:  # iterate through all elements
                c += abs(i - s)  # count moves required to make all elements equal
            print(c//2)  # print moves required

if __name__ == '__main__':
    main()
