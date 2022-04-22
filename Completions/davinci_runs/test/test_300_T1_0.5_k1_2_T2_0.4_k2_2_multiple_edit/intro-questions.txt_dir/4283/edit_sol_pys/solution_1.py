
def main():
    n = int(input())  # number of integers
    arr = [int(x) for x in input().split()]  # array of integers
    arr.sort()  # sort the array
    max_team = 0  # initialize max team
    for i in range(n - 1):
        if arr[i + 1] - arr[i] <= 5:
            max_team += 1  # increment max team
    print(max_team + 1)


if __name__ == '__main__':
    main()
