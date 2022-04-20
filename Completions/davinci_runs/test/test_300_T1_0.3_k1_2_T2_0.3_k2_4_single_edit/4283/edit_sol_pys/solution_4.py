

def main():
    n = int(input())
    a = [int(x) for x in input().split()]  # list comprehension
    a.sort()  # sort in place
    ans = 1  # initialize
    for i in range(1, n):  # loop
        if a[i] - a[i-1] <= 5:  # condition
            ans += 1  # update
    print(ans)  # output


if __name__ == "__main__":
    main()
