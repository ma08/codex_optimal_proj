

def main():
    # read the number of test cases
    t = int(input())

    # iterate over test cases
    for i in range(t):
        # read the input
        n = int(input())
        a = list(map(int, input().split()))

        # find the maximum number of steps
        steps = 0
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                steps += a[j] - a[j + 1]

        # print the result for the current test case
        print(steps)

if __name__ == "__main__":
    main()
