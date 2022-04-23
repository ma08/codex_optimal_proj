

def main():
    n, m = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]  # list of all the numbers
    arr.sort()  # sort the list
    if arr[0] > m:  # if the smallest number is greater than m
        print(-1)  # print -1
        return  # return
    i = 0  # index
    days = 0  # days
    while m > 0:  # while m is greater than 0
        m -= arr[i]  # subtract the number at index i from m
        i += 1  # increment i
        days += 1  # increment days
        if i == n:  # if i is equal to n
            i = 0  # reset i
    print(days)  # print days


if __name__ == "__main__":
    main()
